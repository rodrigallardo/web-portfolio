# Findings & Technical Documentation

## Portfolio Website (Production)

**Live:** https://rodrigallardo.art
**Version:** v1.5.0
**Last Updated:** 2026-03-06

---

### Multi-Size Prints Feature (v1.5.0)

**Implemented:** 2026-03-06
**Status:** ✅ Production

#### Overview
Prints can now have multiple size options with different prices. Users select a size from a dropdown, and the price/dimensions update dynamically.

#### Data Schema

**Print Size Object:**
```typescript
{
  name: string;           // "A3", "A2", "A1", etc.
  dimensionsCm: string;   // "29.7 x 42"
  price: string;          // "$1000 UYU"
  available: boolean;     // Per-size availability
}
```

**Print Schema:**
```typescript
{
  titleEs: string;
  titleEn: string;
  descriptionEs: string;
  descriptionEn: string;
  price?: string;          // Legacy field (optional)
  dimensionsCm?: string;   // Legacy field (optional)
  year: number;
  image: string;
  available: boolean;
  order?: number;
  orientation: 'landscape' | 'portrait';
  sizes?: Array<PrintSize>;  // Multi-size support
}
```

**Backward Compatibility:**
- Prints without `sizes` array use legacy `price` and `dimensionsCm`
- Both formats work simultaneously
- No breaking changes to existing prints

#### Component Architecture

**PrintSizeSelector.astro:**
- Location: `src/components/PrintSizeSelector.astro`
- Props: `{ sizes: Size[], lang: 'es' | 'en' }`
- Features:
  - Dropdown with all available sizes
  - Disabled state for sold-out sizes
  - Dynamic price display
  - Dynamic dimensions display (cm for ES, inches for EN)
  - Fires `print-size-changed` custom event
- JavaScript: ~30 lines for dropdown interaction

**Event Flow:**
1. User selects size from dropdown
2. Component updates displayed price and dimensions
3. Fires `print-size-changed` event with size details
4. Detail page script listens for event
5. Updates WhatsApp URL with new size in message

#### Gallery Price Display Logic

**Function:** `getPriceDisplay(artwork)`

**Logic:**
```typescript
if (artwork has sizes array) {
  if (only 1 available size) → return single price
  if (multiple available sizes) → return "Desde {first price}" / "From {first price}"
  if (no available sizes) → return null
} else {
  return legacy price field
}
```

**Examples:**
- 1 size (A3 $1000): Shows "$1000 UYU"
- 2 sizes (A3 $1000, A2 $2000): Shows "Desde $1000 UYU" (ES) / "From $1000 UYU" (EN)

#### WhatsApp Integration

**Message Format:**
- Legacy: `"Hola, estoy interesado en la obra "{title}". Me gustaría obtener más información."`
- Multi-size: `"Hola, estoy interesado en la impresión "{title}" ({sizeName}). Me gustaría obtener más información."`

**Implementation:**
- Initial URL includes default size
- Event listener updates URL when size changes
- Button has data attributes: `data-artwork-title`, `data-phone-number`, `data-has-sizes`

#### Files Modified

**Schema & Components:**
- `src/content/config.ts` - Print schema with sizes array
- `src/components/PrintSizeSelector.astro` - New component
- `src/components/ArtworkSchema.astro` - Multi-size support

**Detail Pages:**
- `src/pages/prints/[id].astro` - Spanish detail
- `src/pages/en/prints/[id].astro` - English detail

**Gallery Pages:**
- `src/pages/prints.astro` - Spanish gallery with price range
- `src/pages/en/prints.astro` - English gallery with price range

**Translations:**
- `src/i18n/es.json` - Added `size`, `from`, `soldOut`
- `src/i18n/en.json` - Added `size`, `from`, `soldOut`

**Content:**
- `src/content/prints/terrazas_palermo.json` - Migrated to multi-size

---

### Orientation Attribute (v1.5.0)

**Implemented:** 2026-03-06
**Status:** ✅ Production

#### Problem Solved
Print sizes can be different orientations than the original artwork (e.g., landscape painting with portrait-oriented A3 print). Computing orientation from print dimensions caused layout issues.

#### Solution
Added explicit `orientation` field to all artwork schemas:

```typescript
orientation: 'landscape' | 'portrait';  // Required field
```

**Layout Logic:**
```typescript
// Old (computed from dimensions)
const [width, height] = dimensionsCm.split('x').map(d => parseInt(d));
const isLandscape = width > height;

// New (explicit attribute)
const isLandscape = artwork.data.orientation === 'landscape';
```

**Benefits:**
- Artwork orientation independent of print size dimensions
- More accurate layout rendering
- Clearer intent in data model
- No computation needed

**Files Updated:**
- All schema definitions (3 schemas)
- All detail pages (6 pages)
- All content files (9 JSON files)

---

### About Page Updates (v1.5.0)

**Implemented:** 2026-03-06

**Changes:**
1. Removed `rounded-lg` class from profile picture
2. Fixed mobile centering by moving `mx-auto` to image element

**Files Modified:**
- `src/pages/about.astro`
- `src/pages/en/about.astro`

---

## Painting Perspective Correction Tool

## Current Project: Painting Perspective Correction Tool

**Status:** Research phase
**Branch:** feature/painting-perspective-correction
**Purpose:** Experimental image processing tool for correcting distorted painting photographs

---

## Project Context

This is a standalone utility tool, **separate from the main web portfolio project**. The web portfolio is production-ready and deployed at https://rodrigallardo.art. This new tool is for internal use to speed up photo post-processing before uploading artwork images to the website.

**Problem being solved:**
- Painting photos often have perspective distortion (trapezoid shape, curved edges)
- Manual correction is slow and inconsistent
- Need automated solution to speed up workflow

---

## Research Notes

### Computer Vision Approaches for Perspective Correction

**Research completed:** 2026-03-04

The problem of perspective correction (transforming trapezoids to rectangles) is well-solved in the document scanning domain. Multiple existing implementations can be adapted for painting photographs.

#### 1. Edge Detection Algorithms

**Canny vs Sobel Comparison:**

**Canny Edge Detection (RECOMMENDED):**
- Multi-stage algorithm: Gaussian smoothing → gradient calculation → non-maximum suppression → hysteresis thresholding
- Produces thin, well-defined edges (1-pixel width)
- Excellent noise reduction
- Best for accuracy-critical applications
- OpenCV implementation: `cv2.Canny()`
- **When to use:** For paintings with complex backgrounds or noisy images

**Sobel Edge Detection:**
- Simpler gradient-based approach
- Faster, suitable for real-time applications
- Provides directional information (horizontal/vertical)
- Less robust to noise
- **When to use:** When speed is critical or images are clean

**Recommendation:** Use Canny for painting border detection due to superior noise handling and edge quality.

**Sources:**
- [Edge Detection Using OpenCV (LearnOpenCV)](https://learnopencv.com/edge-detection-using-opencv/)
- [Mastering Edge Detection with OpenCV (Medium)](https://medium.com/@noel.benji/a-guide-to-robust-edge-detection-with-opencv-1d703506e014)
- [Sobel vs Canny Edge Detection (GeeksforGeeks)](https://www.geeksforgeeks.org/computer-vision/sobel-edge-detection-vs-canny-edge-detection-in-computer-vision/)

#### 2. Contour Detection and Analysis

After edge detection, OpenCV's contour finding identifies closed shapes:
- `cv2.findContours()` - Finds all contours in binary image
- `cv2.approxPolyDP()` - Approximates contours to polygons
- Select largest quadrilateral contour (painting border)

#### 3. Perspective Transformation (Homography)

Two main Python libraries provide perspective transformation:

**OpenCV Approach:**
```python
M = cv2.getPerspectiveTransform(src_points, dst_points)
warped = cv2.warpPerspective(image, M, (width, height))
```
- Uses 4-point homography
- Fast and widely used
- Industry standard

**scikit-image Approach:**
```python
from skimage.transform import ProjectiveTransform, warp
transform = ProjectiveTransform()
transform.estimate(src, dst)
warped = warp(image, transform.inverse)
```
- More flexible API
- Scientific computing focus
- Better for custom transformations

**Recommendation:** Use OpenCV for this project (faster, more documentation for document scanning use case).

**Sources:**
- [4 Point OpenCV getPerspective Transform (PyImageSearch)](https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/)
- [skimage.transform Documentation](https://scikit-image.org/docs/stable/api/skimage.transform.html)
- [Using geometric transformations (scikit-image)](https://scikit-image.org/docs/stable/auto_examples/transform/plot_geometric.html)

#### 4. Existing Document Scanner Implementations

**Multiple open-source projects exist that solve this exact problem:**

**GitHub Repositories:**
1. **[andrewdcampbell/OpenCV-Document-Scanner](https://github.com/andrewdcampbell/OpenCV-Document-Scanner)**
   - Interactive scanner with automatic corner detection
   - Image sharpening and color thresholding
   - Well-documented, production-ready

2. **[ArashNasrEsfahani/Python-Document-Scanner-OpenCV](https://github.com/ArashNasrEsfahani/Python-Document-Scanner-OpenCV)**
   - Perspective correction + image enhancement
   - Clean pipeline architecture
   - Recent updates

3. **[joyeecheung/perspective-correction](https://github.com/joyeecheung/perspective-correction)**
   - Uses Canny detector + Hough transform
   - Automatic A4 paper detection
   - Good for understanding algorithm steps

**Commercial SDK:**
- **[document-scanner-sdk](https://pypi.org/project/document-scanner-sdk/)**
  - Python wrapper for professional-grade detection
  - Edge detection, perspective correction, brightness adjustment
  - Cross-platform (Windows, Linux, macOS)
  - Paid solution but very robust

**Tutorials:**
- [How to Build a Document Scanner in 5 Minutes (PyImageSearch)](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
  - ~200 lines of Python code
  - Complete working implementation
  - Step-by-step explanation

- [Automatic Document Scanner using OpenCV (LearnOpenCV)](https://learnopencv.com/automatic-document-scanner-using-opencv/)
  - Multi-stage pipeline
  - GrabCut background removal
  - Professional-quality results

- [Scanning Documents with Perspective Transformation (Medium)](https://medium.com/@ahamrouni/scanning-documents-with-perspective-transformation-using-opencv-65be79fd774c)
  - Recent tutorial (2026)
  - Modern Python practices

**Sources:**
- [PyImageSearch Document Scanner](https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [LearnOpenCV Automatic Scanner](https://learnopencv.com/automatic-document-scanner-using-opencv/)
- [Document Scanner in Python (Medium, Feb 2026)](https://medium.com/@coders.stop/document-scanner-in-python-perspective-correction-and-enhancement-1a5c5ac9bf6c)

#### 5. Frame vs Painting Edge Differentiation

**Strategy for handling framed paintings:**
1. Find all contours in image
2. Sort by contour area (largest first)
3. Select largest quadrilateral contour = outer frame
4. Alternative: Use hierarchy to find outermost parent contour

**OpenCV provides contour hierarchy:**
```python
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
- `RETR_TREE` mode captures parent-child relationships
- Outermost contour = frame edge (if present)

### Tech Stack Options

**RECOMMENDATION: Python + OpenCV + Flask/FastAPI**

**Backend: Python + OpenCV (CHOSEN)**

**Rationale:**
- Most mature computer vision library
- Extensive documentation and tutorials
- Large community (document scanner implementations readily available)
- Can adapt existing code significantly reducing development time
- Native Python bindings are fast and stable
- Rich ecosystem: numpy, PIL, scikit-image for additional processing

**Alternatives considered:**
- Node.js + opencv4nodejs: Less documentation, harder to debug
- Node.js + sharp: No perspective transformation support
- Python + scikit-image alone: Slower than OpenCV, less complete for this use case

**Frontend: Vanilla HTML/CSS/JS (CHOSEN)**

**Rationale:**
- Simple upload/preview/download workflow doesn't need framework overhead
- Faster development for basic UI
- No build step complexity
- Easy to add parameter sliders with vanilla JS

**Alternatives considered:**
- React: Overkill for simple UI
- Vue: Same issue, adds complexity

**Server: FastAPI (CHOSEN)**

**Rationale:**
- Modern Python web framework
- Automatic API documentation (OpenAPI/Swagger)
- Fast development with type hints
- Built-in file upload handling
- WebSocket support (for real-time progress updates if needed)
- Easy CORS configuration for localhost

**Alternatives considered:**
- Flask: Simpler but less modern, no automatic docs
- Express (Node.js): Would require opencv4nodejs (less mature)

### Required Libraries

**Core dependencies:**
```
opencv-python==4.9.0.80  # Computer vision
numpy==1.26.4            # Array operations
fastapi==0.110.0         # Web framework
uvicorn==0.27.1          # ASGI server
python-multipart==0.0.9  # File upload support
pillow==10.2.0           # Image I/O
```

**Optional (for enhancements):**
```
scikit-image==0.22.0     # Additional image processing
imutils==0.5.4           # Convenience functions for OpenCV
```

---

## Algorithm Design

**Based on document scanner best practices, adapted for paintings**

### Complete Pipeline

```
Input Image
    ↓
1. Preprocessing
   - Convert to grayscale
   - Gaussian blur (reduce noise)
   - Resize for processing (if very large)
    ↓
2. Edge Detection
   - Canny edge detection
   - Parameters: low_threshold, high_threshold
    ↓
3. Contour Detection
   - Find all contours
   - Sort by area (largest first)
    ↓
4. Quadrilateral Detection
   - Approximate contours to polygons
   - Filter for 4-sided shapes
   - Select largest quadrilateral (painting border)
    ↓
5. Corner Ordering
   - Order corners: top-left, top-right, bottom-right, bottom-left
   - Critical for correct transformation
    ↓
6. Perspective Transformation
   - Calculate destination rectangle size (aspect ratio preserving)
   - Compute homography matrix
   - Warp image to rectangle
    ↓
7. Post-processing (optional)
   - Brightness/contrast adjustment
   - Sharpening
   - Color correction
    ↓
Output Image
```

### Key Tunable Parameters

**For UI exposure:**

1. **Canny Edge Detection:**
   - `low_threshold` (default: 50)
   - `high_threshold` (default: 150)
   - `aperture_size` (default: 3)

2. **Gaussian Blur:**
   - `kernel_size` (default: 5)
   - Reduces noise before edge detection

3. **Contour Selection:**
   - `min_contour_area` (default: 10% of image area)
   - Filters out small noise contours

4. **Polygon Approximation:**
   - `epsilon_factor` (default: 0.02)
   - Controls how strictly contours must match quadrilaterals

5. **Output Size:**
   - `max_width` or `max_height` (optional)
   - Resize output if needed

### Handling Edge Cases

**Framed paintings:**
- Use `cv2.RETR_TREE` contour mode
- Select outermost quadrilateral
- Alternative: Find largest quadrilateral (usually outer frame)

**Poor lighting:**
- Adaptive thresholding before edge detection
- Histogram equalization to improve contrast

**Curved edges:**
- Increase `epsilon_factor` in polygon approximation
- Forces curve to approximate to straight lines

**Multiple paintings in frame:**
- Sort contours by area
- Allow user to select which contour to use (UI enhancement)

### Code Structure (Proposed)

```
painting_corrector/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── processor.py         # Image processing pipeline
│   ├── utils.py             # Helper functions
│   └── config.py            # Default parameters
├── frontend/
│   ├── index.html           # Main UI
│   ├── styles.css           # Styling
│   └── app.js               # Upload/preview/download logic
└── requirements.txt         # Python dependencies
```

### Adaptation from Document Scanners

**What works identically:**
- Edge detection (Canny)
- Contour finding
- 4-point perspective transformation
- Corner ordering algorithms

**What needs adjustment:**
- Background assumptions (black mantle + white wall vs white paper + dark desk)
- Color preservation (paintings need accurate colors vs documents can be B&W)
- Edge types (paintings may have frames with distinct edges)
- Quality requirements (paintings need high-res output, documents can be compressed)

### Expected Performance

**Processing time (estimated):**
- Small image (< 2MP): < 1 second
- Medium image (2-8MP): 1-3 seconds
- Large image (> 8MP): 3-10 seconds

**Accuracy expectations:**
- Well-lit, centered paintings: 95%+ success rate
- Poor lighting or extreme angles: 60-80% success rate
- Manual parameter adjustment can improve failed cases

---

## Implementation Details

*To be filled in as we build*

---

## Testing & Validation

*Test results will be documented here*

---

## Performance Considerations

*Processing speed metrics and optimizations*

---

## Known Limitations

*Edge cases and known issues*

---

## Future Improvements

*Ideas for enhancements*

---

**Note:** This findings.md file is dedicated to the painting perspective correction tool. The previous web portfolio findings have been archived in the git history.
