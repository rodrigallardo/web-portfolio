"""
Improved processor v5 - Combined white+black mask approach.

Strategy:
1. White mask at threshold 140 (captures painting + white wall including shadows)
2. Black mask at threshold 30 (captures only darkest blacks - the mantle)
3. ADD both masks together to get complete boundary
4. Find contour and approximate to 4 corners
"""

import cv2
import numpy as np
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class ProcessingParams:
    """Tunable parameters for the correction algorithm."""
    white_threshold: int = 140
    black_threshold: int = 30
    morph_kernel_size: int = 15
    morph_iterations: int = 3
    epsilon_factor: float = 0.02
    min_contour_area_pct: float = 1.0


class PaintingCorrector:
    """
    Perspective correction using combined white+black mask approach.
    """

    def __init__(self, params: Optional[ProcessingParams] = None):
        self.params = params or ProcessingParams()

    def process(self, image: np.ndarray) -> Tuple[Optional[np.ndarray], str]:
        """Process an image to correct perspective distortion."""
        if image is None or image.size == 0:
            return None, "Error: Invalid input image"

        try:
            corners = self._find_painting_corners(image)

            if corners is None:
                return None, "Error: Could not detect painting borders. Try adjusting parameters."

            ordered_corners = self._order_corners(corners)
            width, height = self._calculate_output_dimensions(ordered_corners)
            corrected = self._warp_perspective(image, ordered_corners, width, height)

            return corrected, "Success: Perspective corrected"

        except Exception as e:
            return None, f"Error during processing: {str(e)}"

    def _find_painting_corners(self, image: np.ndarray) -> Optional[np.ndarray]:
        """
        Detect painting corners using combined mask approach with filtering.

        Strategy:
        1. Create white mask (threshold 140) - captures painting boundary + white wall
        2. Create black mask (threshold 30) - captures only darkest blacks (mantle)
        3. ADD both masks together and INVERT (painting becomes white)
        4. Light morphology + erosion to disconnect edge artifacts
        5. Filter contours: not touching edges, centered, large enough
        6. Approximate to 4 corners
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        h, w = image.shape[:2]

        # Create white mask (threshold 140)
        _, white_mask = cv2.threshold(gray, self.params.white_threshold, 255, cv2.THRESH_BINARY)

        # Create black mask (threshold 30 - only darkest blacks)
        _, black_mask = cv2.threshold(gray, self.params.black_threshold, 255, cv2.THRESH_BINARY_INV)

        # ADD both masks together and normalize
        combined_mask = cv2.add(white_mask, black_mask)
        combined_mask = cv2.threshold(combined_mask, 128, 255, cv2.THRESH_BINARY)[1]

        # INVERT - now painting is white, background is black
        inverted_mask = cv2.bitwise_not(combined_mask)

        # Light morphology to clean noise
        kernel_light = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        inverted_clean = cv2.morphologyEx(inverted_mask, cv2.MORPH_CLOSE, kernel_light, iterations=1)

        # Erode to disconnect edge artifacts
        kernel_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        inverted_eroded = cv2.erode(inverted_clean, kernel_erode, iterations=3)

        # Find contours
        contours, _ = cv2.findContours(inverted_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            return None

        # Filter contours
        image_area = h * w
        margin = 50  # Pixels from edge
        center_x = w / 2
        center_y = h / 2
        max_dist = min(w, h) / 2

        valid_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            pct = (area / image_area) * 100

            # Must be at least 5% of image
            if pct < 5.0:
                continue

            # Get bounding box
            x, y, w_box, h_box = cv2.boundingRect(cnt)

            # Check if touching edges
            touches_edge = (x <= margin or y <= margin or
                           (x + w_box) >= (w - margin) or
                           (y + h_box) >= (h - margin))

            if touches_edge:
                continue

            # Check if centered
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                dist_from_center = np.sqrt((cx - center_x)**2 + (cy - center_y)**2)
                is_centered = dist_from_center < max_dist * 0.8
            else:
                is_centered = False

            if is_centered:
                valid_contours.append((cnt, area))

        if len(valid_contours) == 0:
            return None

        # Get largest valid contour
        valid_contours.sort(key=lambda x: x[1], reverse=True)
        painting_contour = valid_contours[0][0]

        # Approximate to polygon with 4 corners
        peri = cv2.arcLength(painting_contour, True)

        # Try different epsilon values to get exactly 4 corners
        for epsilon_mult in [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05, 0.08]:
            epsilon = epsilon_mult * peri
            approx = cv2.approxPolyDP(painting_contour, epsilon, True)

            if len(approx) == 4:
                return approx.reshape(4, 2).astype(np.float32)

        # Fallback: use minimum area rectangle
        rect = cv2.minAreaRect(painting_contour)
        box = cv2.boxPoints(rect)

        # Clip to image bounds
        box[:, 0] = np.clip(box[:, 0], 0, w - 1)
        box[:, 1] = np.clip(box[:, 1], 0, h - 1)

        return np.array(box, dtype=np.float32)

    def _order_corners(self, corners: np.ndarray) -> np.ndarray:
        """Order corners as: [top-left, top-right, bottom-right, bottom-left]."""
        ordered = np.zeros((4, 2), dtype=np.float32)

        s = corners.sum(axis=1)
        diff = np.diff(corners, axis=1)

        ordered[0] = corners[np.argmin(s)]      # top-left
        ordered[2] = corners[np.argmax(s)]      # bottom-right
        ordered[1] = corners[np.argmin(diff)]   # top-right
        ordered[3] = corners[np.argmax(diff)]   # bottom-left

        return ordered

    def _calculate_output_dimensions(self, corners: np.ndarray) -> Tuple[int, int]:
        """Calculate output dimensions preserving aspect ratio."""
        (tl, tr, br, bl) = corners

        width_top = np.linalg.norm(tr - tl)
        width_bottom = np.linalg.norm(br - bl)
        max_width = max(int(width_top), int(width_bottom))

        height_left = np.linalg.norm(bl - tl)
        height_right = np.linalg.norm(br - tr)
        max_height = max(int(height_left), int(height_right))

        return max_width, max_height

    def _warp_perspective(
        self,
        image: np.ndarray,
        corners: np.ndarray,
        width: int,
        height: int
    ) -> np.ndarray:
        """Apply perspective transformation with maximum quality."""
        dst = np.array([
            [0, 0],
            [width - 1, 0],
            [width - 1, height - 1],
            [0, height - 1]
        ], dtype=np.float32)

        M = cv2.getPerspectiveTransform(corners, dst)

        warped = cv2.warpPerspective(
            image,
            M,
            (width, height),
            flags=cv2.INTER_LANCZOS4,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0)
        )

        return warped

    def visualize_detection(self, image: np.ndarray) -> Tuple[Optional[np.ndarray], str]:
        """Visualize the detected corners."""
        corners = self._find_painting_corners(image)

        if corners is None:
            return None, "No corners detected"

        vis = image.copy()
        cv2.drawContours(vis, [corners.astype(np.int32)], -1, (0, 255, 0), 10)

        for i, corner in enumerate(corners):
            cv2.circle(vis, tuple(corner.astype(int)), 20, (0, 0, 255), -1)
            cv2.putText(vis, str(i), tuple(corner.astype(int)),
                       cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

        return vis, "Corners detected"
