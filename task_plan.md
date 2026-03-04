# Task Plan: Painting Perspective Correction Tool

## Current Status
Planning phase - Experimental image processing tool (separate from web portfolio)

## Project Overview

**Goal:** Build a web-based tool to automatically correct perspective distortions in painting photographs

**Context:** This is an experimental feature unrelated to the main web portfolio. It's a standalone utility to speed up photo post-processing for artwork images before uploading to the website.

**Branch:** `feature/painting-perspective-correction` (isolated from main portfolio)

## Problem Statement

### Photography Challenges
- Camera not perfectly perpendicular to painting center
- Lens distortion effects
- Resulting image distortions:
  - Straight lines appear curved
  - Trapezoidal shapes instead of rectangles
  - Warped dimensions

### Current Workflow Pain Points
- Manual correction is time-consuming
- Inconsistent results
- Need faster, automated solution

## Technical Requirements

### 1. Image Processing Algorithm
- **Automatic border detection**
  - Detect painting edges (may be curved due to distortion)
  - Assumptions:
    - Paintings on black mantle
    - White wall background
    - Centered in frame
- **Perspective correction**
  - Transform borders to perfect rectangle
  - Minimize transformation to avoid corrupting painting
  - Preserve texture and detail quality
- **Smart cropping**
  - Crop to corrected rectangle
  - Remove background
- **Frame handling**
  - Detect multiple border sets (framed paintings)
  - Select outermost border to preserve frame

### 2. User Interface Requirements
- **Deployment:** Local web server (localhost only)
- **Core workflow:**
  1. Upload image from local files
  2. Process with algorithm (automatic)
  3. Preview corrected result
  4. Save to local files if satisfactory
- **Tuneable parameters:**
  - Expose algorithm parameters for fine-tuning
  - UI controls to adjust if automatic detection fails
  - Real-time preview of parameter changes

## Phases

### Phase 1: Research & Planning ⏳
**Status:** In Progress
**Started:** 2026-03-04

**Tasks:**
- [ ] Research classical computer vision algorithms for edge detection
- [ ] Research perspective transformation techniques (OpenCV, scikit-image, etc.)
- [ ] Evaluate Python vs Node.js for image processing
- [ ] Research border detection algorithms (Canny, Hough, contour detection)
- [ ] Design algorithm pipeline architecture
- [ ] Choose tech stack (backend + frontend)
- [ ] Document findings in findings.md

**Key Questions:**
- Which library provides best edge detection for paintings?
- How to handle curved edges vs straight edges?
- What parameters need to be tunable?
- Best approach for frame detection?

### Phase 2: Tech Stack Selection 📋
**Status:** Pending

**Tasks:**
- [ ] Choose backend language/framework
- [ ] Choose computer vision library
- [ ] Choose frontend framework (React, Vue, vanilla JS?)
- [ ] Choose build/bundling tools
- [ ] Document rationale for each choice

**Candidates:**
- Backend: Python (OpenCV, scikit-image, PIL) vs Node.js (sharp, opencv4nodejs)
- Frontend: React/Vue vs Vanilla HTML/JS
- Local server: Flask/FastAPI vs Express

### Phase 3: Core Algorithm Implementation 🔧
**Status:** Pending

**Tasks:**
- [ ] Implement border detection
- [ ] Implement perspective transformation
- [ ] Implement cropping
- [ ] Implement frame detection (outermost border selection)
- [ ] Test with sample painting photos
- [ ] Tune default parameters
- [ ] Handle edge cases (poor lighting, angled photos, etc.)

**Success Criteria:**
- Algorithm successfully detects borders in 80%+ of test images
- Perspective correction produces rectangular output
- No visible warping or corruption of painting details

### Phase 4: Web UI Development 🎨
**Status:** Pending

**Tasks:**
- [ ] Create file upload interface
- [ ] Implement image preview (before/after)
- [ ] Add parameter adjustment controls
- [ ] Add save/download functionality
- [ ] Style UI (minimal, functional)
- [ ] Handle errors gracefully
- [ ] Add loading states

**UI Components:**
- File input (drag-drop + browse)
- Before/after image display (side-by-side or toggle)
- Parameter sliders/inputs
- Save button
- Status/error messages

### Phase 5: Integration & Testing 🧪
**Status:** Pending

**Tasks:**
- [ ] Connect frontend to backend API
- [ ] Test full workflow end-to-end
- [ ] Test with various painting photos
- [ ] Test with framed vs unframed paintings
- [ ] Test edge cases (poor quality, extreme angles)
- [ ] Optimize processing speed
- [ ] Document usage instructions

**Test Cases:**
- Portrait orientation paintings
- Landscape orientation paintings
- Framed paintings (multiple borders)
- Unframed paintings
- Various lighting conditions
- Different camera angles

### Phase 6: Documentation & Deployment 📚
**Status:** Pending

**Tasks:**
- [ ] Write README for the tool
- [ ] Document algorithm parameters
- [ ] Create usage guide with screenshots
- [ ] Add troubleshooting section
- [ ] Setup instructions for localhost deployment
- [ ] Future improvements list

## Design Decisions

### To Be Decided:
- [ ] Python vs Node.js backend?
- [ ] Which edge detection algorithm? (Canny, Sobel, etc.)
- [ ] How to distinguish frame from painting edge?
- [ ] Parameter exposure strategy (which to expose, which to hardcode)
- [ ] Image format handling (JPEG, PNG, TIFF, etc.)

## Constraints & Considerations

### Technical Constraints:
- Local deployment only (no cloud/hosting needed)
- Must handle high-resolution images (artwork photos)
- Processing time should be reasonable (<10 seconds)
- Output quality must preserve painting details

### User Experience:
- Simple, intuitive interface
- Fast feedback (preview quickly)
- Easy to iterate (adjust parameters, re-process)
- Clear error messages

### Future Extensibility:
- Batch processing multiple images?
- Save preset parameter configurations?
- Export processing history/settings?

## Success Criteria

**Minimum Viable Product (MVP):**
- ✅ Automatically detects painting borders
- ✅ Corrects perspective to rectangle
- ✅ Crops to final image
- ✅ Simple web UI for upload/preview/save
- ✅ Works on localhost

**Nice to Have:**
- Parameter tuning UI
- Batch processing
- Preset configurations
- Processing history

## Notes

- Keep isolated in feature branch (unrelated to main portfolio)
- Experimental - okay if not perfect
- Primary goal: speed up workflow, not production-ready tool
- Can iterate based on real-world usage

## Errors Encountered

| Error | Attempt | Resolution |
|-------|---------|------------|
| (none yet) | - | - |

---

**Next Step:** Begin Phase 1 research on computer vision algorithms and tech stack options
