"""
FastAPI server for painting perspective correction.
Provides REST API for image upload, processing, and download.
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from pathlib import Path
import uuid
import shutil
from typing import Optional
import rawpy

from processor import PaintingCorrector, ProcessingParams

# Initialize FastAPI app
app = FastAPI(
    title="Painting Perspective Corrector",
    description="Automatic perspective correction for painting photographs",
    version="1.0.0"
)

# Enable CORS for localhost development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Localhost only - fine for local tool
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (frontend)
frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

# Create temp directory for uploaded/processed images
TEMP_DIR = Path("/tmp/painting-corrector")
TEMP_DIR.mkdir(exist_ok=True)

# RAW file extensions
RAW_EXTENSIONS = {'.cr2', '.cr3', '.nef', '.arw', '.raf', '.orf', '.rw2', '.dng', '.raw', '.nrw'}


def read_image(file_path: Path) -> Optional[np.ndarray]:
    """
    Read an image file, supporting both standard formats (JPEG, PNG) and RAW formats.

    Returns:
        numpy array in BGR format (OpenCV standard), or None if reading fails
    """
    file_ext = file_path.suffix.lower()

    if file_ext in RAW_EXTENSIONS:
        # Read RAW file
        try:
            with rawpy.imread(str(file_path)) as raw:
                # Post-process to RGB (use default settings for quality)
                rgb = raw.postprocess(
                    use_camera_wb=True,  # Use camera white balance
                    no_auto_bright=True,  # Don't auto-brighten
                    output_bps=8         # 8-bit output
                )
                # Convert RGB to BGR for OpenCV
                bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
                return bgr
        except Exception as e:
            print(f"Error reading RAW file {file_path}: {e}")
            return None
    else:
        # Read standard image formats with OpenCV
        return cv2.imread(str(file_path), cv2.IMREAD_UNCHANGED)


@app.get("/")
async def root():
    """Redirect to frontend."""
    return FileResponse(str(frontend_path / "index.html"))


@app.post("/api/process")
async def process_image(
    file: UploadFile = File(...),
    white_threshold: Optional[int] = Form(140),
    black_threshold: Optional[int] = Form(30),
    morph_kernel_size: Optional[int] = Form(15),
    morph_iterations: Optional[int] = Form(3),
    erosion_iterations: Optional[int] = Form(3),
    epsilon_factor: Optional[float] = Form(0.005),
):
    """
    Process an uploaded image to correct perspective.

    Parameters are optional - defaults work well for most cases.
    """
    # Validate file
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")

    try:
        # Generate unique filenames
        upload_id = str(uuid.uuid4())
        input_path = TEMP_DIR / f"{upload_id}_input{Path(file.filename).suffix}"
        output_path = TEMP_DIR / f"{upload_id}_output.png"  # PNG for lossless quality

        # Save uploaded file
        with input_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Read image (supports RAW, JPEG, PNG)
        image = read_image(input_path)
        if image is None:
            raise HTTPException(400, "Could not read image file. Ensure it's a valid RAW, JPEG, or PNG file.")

        # Create processing parameters
        params = ProcessingParams(
            white_threshold=white_threshold,
            black_threshold=black_threshold,
            morph_kernel_size=morph_kernel_size if morph_kernel_size % 2 == 1 else morph_kernel_size + 1,  # Must be odd
            morph_iterations=morph_iterations,
            epsilon_factor=epsilon_factor,
        )

        # Process image
        corrector = PaintingCorrector(params)
        corrected, message = corrector.process(image)

        if corrected is None:
            return JSONResponse({
                "success": False,
                "message": message,
                "output_url": None
            })

        # Save corrected image with maximum quality
        cv2.imwrite(str(output_path), corrected, [cv2.IMWRITE_PNG_COMPRESSION, 9])

        return JSONResponse({
            "success": True,
            "message": message,
            "output_url": f"/api/download/{upload_id}",
            "dimensions": {
                "width": corrected.shape[1],
                "height": corrected.shape[0]
            }
        })

    except Exception as e:
        raise HTTPException(500, f"Processing error: {str(e)}")
    finally:
        # Clean up input file
        if input_path.exists():
            input_path.unlink()


@app.post("/api/visualize")
async def visualize_detection(
    file: UploadFile = File(...),
    white_threshold: Optional[int] = Form(140),
    black_threshold: Optional[int] = Form(30),
    morph_kernel_size: Optional[int] = Form(15),
    morph_iterations: Optional[int] = Form(3),
    erosion_iterations: Optional[int] = Form(3),
    epsilon_factor: Optional[float] = Form(0.005),
):
    """
    Visualize detected corners on the original image.
    Useful for debugging parameter settings.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")

    try:
        # Generate unique filename
        upload_id = str(uuid.uuid4())
        input_path = TEMP_DIR / f"{upload_id}_vis_input{Path(file.filename).suffix}"
        output_path = TEMP_DIR / f"{upload_id}_visualization.png"

        # Save uploaded file
        with input_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Read image (supports RAW, JPEG, PNG)
        image = read_image(input_path)
        if image is None:
            raise HTTPException(400, "Could not read image file. Ensure it's a valid RAW, JPEG, or PNG file.")

        # Create processing parameters
        params = ProcessingParams(
            white_threshold=white_threshold,
            black_threshold=black_threshold,
            morph_kernel_size=morph_kernel_size if morph_kernel_size % 2 == 1 else morph_kernel_size + 1,
            morph_iterations=morph_iterations,
            epsilon_factor=epsilon_factor,
        )

        # Visualize detection
        corrector = PaintingCorrector(params)
        visualization, message = corrector.visualize_detection(image)

        if visualization is None:
            return JSONResponse({
                "success": False,
                "message": message,
                "visualization_url": None
            })

        # Save visualization
        cv2.imwrite(str(output_path), visualization)

        return JSONResponse({
            "success": True,
            "message": message,
            "visualization_url": f"/api/download/{upload_id}_visualization"
        })

    except Exception as e:
        raise HTTPException(500, f"Visualization error: {str(e)}")
    finally:
        # Clean up input file
        if input_path.exists():
            input_path.unlink()


@app.post("/api/debug")
async def debug_visualization(
    file: UploadFile = File(...),
    white_threshold: Optional[int] = Form(140),
    black_threshold: Optional[int] = Form(30),
    erosion_iterations: Optional[int] = Form(3),
):
    """
    Generate debug visualization showing all intermediate processing steps.
    Returns URLs for: white mask, black mask, combined mask, inverted mask, corner detection.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")

    try:
        # Generate unique ID
        upload_id = str(uuid.uuid4())
        input_path = TEMP_DIR / f"{upload_id}_debug_input{Path(file.filename).suffix}"

        # Save uploaded file
        with input_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Read image (supports RAW, JPEG, PNG)
        image = read_image(input_path)
        if image is None:
            raise HTTPException(400, "Could not read image file. Ensure it's a valid RAW, JPEG, or PNG file.")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        h, w = image.shape[:2]

        # Generate all intermediate images
        # 1. White mask
        _, white_mask = cv2.threshold(gray, white_threshold, 255, cv2.THRESH_BINARY)
        white_path = TEMP_DIR / f"{upload_id}_white.png"
        cv2.imwrite(str(white_path), white_mask)

        # 2. Black mask
        _, black_mask = cv2.threshold(gray, black_threshold, 255, cv2.THRESH_BINARY_INV)
        black_path = TEMP_DIR / f"{upload_id}_black.png"
        cv2.imwrite(str(black_path), black_mask)

        # 3. Combined mask (add)
        combined = cv2.add(white_mask, black_mask)
        combined_mask = cv2.threshold(combined, 128, 255, cv2.THRESH_BINARY)[1]
        combined_path = TEMP_DIR / f"{upload_id}_combined.png"
        cv2.imwrite(str(combined_path), combined_mask)

        # 4. Inverted mask (painting region)
        inverted_mask = cv2.bitwise_not(combined_mask)
        inverted_path = TEMP_DIR / f"{upload_id}_inverted.png"
        cv2.imwrite(str(inverted_path), inverted_mask)

        # 5. After morphology
        kernel_light = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        inverted_clean = cv2.morphologyEx(inverted_mask, cv2.MORPH_CLOSE, kernel_light, iterations=1)
        clean_path = TEMP_DIR / f"{upload_id}_clean.png"
        cv2.imwrite(str(clean_path), inverted_clean)

        # 6. After erosion
        kernel_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        inverted_eroded = cv2.erode(inverted_clean, kernel_erode, iterations=erosion_iterations)
        eroded_path = TEMP_DIR / f"{upload_id}_eroded.png"
        cv2.imwrite(str(eroded_path), inverted_eroded)

        # 7. Final detection
        params = ProcessingParams(
            white_threshold=white_threshold,
            black_threshold=black_threshold,
            epsilon_factor=0.005
        )
        corrector = PaintingCorrector(params)
        visualization, message = corrector.visualize_detection(image)

        detection_path = TEMP_DIR / f"{upload_id}_detection.png"
        if visualization is not None:
            cv2.imwrite(str(detection_path), visualization)

        return JSONResponse({
            "success": True,
            "upload_id": upload_id,
            "images": {
                "white_mask": f"/api/debug-image/{upload_id}_white.png",
                "black_mask": f"/api/debug-image/{upload_id}_black.png",
                "combined_mask": f"/api/debug-image/{upload_id}_combined.png",
                "inverted_mask": f"/api/debug-image/{upload_id}_inverted.png",
                "clean_mask": f"/api/debug-image/{upload_id}_clean.png",
                "eroded_mask": f"/api/debug-image/{upload_id}_eroded.png",
                "detection": f"/api/debug-image/{upload_id}_detection.png" if visualization is not None else None,
            },
            "message": message if visualization is not None else "Could not detect corners"
        })

    except Exception as e:
        raise HTTPException(500, f"Debug visualization error: {str(e)}")
    finally:
        # Clean up input file
        if input_path.exists():
            input_path.unlink()


@app.get("/api/debug-image/{filename}")
async def get_debug_image(filename: str):
    """Serve a debug image."""
    file_path = TEMP_DIR / filename
    if not file_path.exists():
        raise HTTPException(404, "Debug image not found")
    return FileResponse(file_path, media_type="image/png")


@app.get("/api/download/{upload_id}")
async def download_image(upload_id: str):
    """Download a processed image."""
    # Support both regular output and visualization
    if upload_id.endswith("_visualization"):
        file_path = TEMP_DIR / f"{upload_id}.png"
    else:
        file_path = TEMP_DIR / f"{upload_id}_output.png"

    if not file_path.exists():
        raise HTTPException(404, "File not found or expired")

    return FileResponse(
        file_path,
        media_type="image/png",
        filename=f"corrected_painting.png",
        headers={"Content-Disposition": "attachment; filename=corrected_painting.png"}
    )


@app.delete("/api/cleanup/{upload_id}")
async def cleanup_files(upload_id: str):
    """Clean up temporary files after download."""
    output_path = TEMP_DIR / f"{upload_id}_output.png"

    if output_path.exists():
        output_path.unlink()

    return {"message": "Cleanup successful"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "painting-corrector"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")
