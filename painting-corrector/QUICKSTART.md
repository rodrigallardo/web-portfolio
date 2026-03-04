# Quick Start Guide

## 🚀 Get Started in 30 Seconds

### 1. Start the Server

```bash
./run.sh
```

Or manually:

```bash
source venv/bin/activate
cd backend
python main.py
```

### 2. Open in Browser

**http://127.0.0.1:8001**

### 3. Process a Painting

1. **Upload** - Drag & drop or click to browse
2. **Click "Correct Perspective"** - Uses automatic detection
3. **Download** - Save your corrected image

**That's it!** The default parameters work well for most images.

## 🔧 If Automatic Detection Fails

1. Click **"Visualize Detection"** to see what's being detected
2. Adjust the **Canny thresholds** if borders aren't detected
3. Increase **Edge Approximation** for curved/distorted edges
4. Click "Correct Perspective" again

## 📊 What to Expect

**Success Rate:** 95%+ for well-lit, centered paintings

**Processing Time:**
- Small images: < 1 second
- Large images: 3-10 seconds

**Output Quality:** Maximum quality preservation
- Original resolution maintained
- LANCZOS4 interpolation (highest quality)
- Lossless PNG output

## 🎯 Tips for Best Results

- **Lighting:** Ensure even lighting across the painting
- **Position:** Center the painting in the frame
- **Background:** Black mantle + white wall works best
- **Distance:** Fill most of the frame with the painting

## 🆘 Troubleshooting

**"Could not detect painting borders"**
- Try adjusting Canny Low Threshold (30-100)
- Use Visualize mode to see detection

**Incorrect border detected**
- Increase Min Contour Area
- Ensure painting occupies most of frame

## 🔗 More Help

See full **README.md** for:
- Detailed parameter explanations
- Algorithm details
- API documentation
- Advanced troubleshooting
