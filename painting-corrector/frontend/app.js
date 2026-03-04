// Painting Perspective Corrector - Frontend Logic

// State
let uploadedFile = null;
let currentUploadId = null;

// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const parametersSection = document.getElementById('parametersSection');
const previewSection = document.getElementById('previewSection');
const originalImage = document.getElementById('originalImage');
const correctedImage = document.getElementById('correctedImage');
const loadingSpinner = document.getElementById('loadingSpinner');
const statusBar = document.getElementById('statusBar');
const statusText = document.getElementById('statusText');
const resultInfo = document.getElementById('resultInfo');
const statusMessage = document.getElementById('statusMessage');
const dimensions = document.getElementById('dimensions');
const downloadBtn = document.getElementById('downloadBtn');
const resetBtn = document.getElementById('resetBtn');
const processBtn = document.getElementById('processBtn');
const visualizeBtn = document.getElementById('visualizeBtn');

// Parameter inputs
const whiteThreshold = document.getElementById('whiteThreshold');
const whiteThresholdValue = document.getElementById('whiteThresholdValue');
const blackThreshold = document.getElementById('blackThreshold');
const blackThresholdValue = document.getElementById('blackThresholdValue');
const morphKernel = document.getElementById('morphKernel');
const morphKernelValue = document.getElementById('morphKernelValue');
const morphIterations = document.getElementById('morphIterations');
const morphIterationsValue = document.getElementById('morphIterationsValue');
const erosion = document.getElementById('erosion');
const erosionValue = document.getElementById('erosionValue');
const epsilon = document.getElementById('epsilon');
const epsilonValue = document.getElementById('epsilonValue');

// Debug section elements
const debugSection = document.getElementById('debugSection');
const debugBtn = document.getElementById('debugBtn');
const whiteMask = document.getElementById('whiteMask');
const blackMask = document.getElementById('blackMask');
const combinedMask = document.getElementById('combinedMask');
const invertedMask = document.getElementById('invertedMask');
const cleanMask = document.getElementById('cleanMask');
const erodedMask = document.getElementById('erodedMask');
const detectionMask = document.getElementById('detectionMask');
const whiteDebug = document.getElementById('whiteDebug');
const blackDebug = document.getElementById('blackDebug');
const erosionDebug = document.getElementById('erosionDebug');

// Debounce timer for real-time updates
let debugUpdateTimer = null;

// Event Listeners

// File upload area
uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFileSelect(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFileSelect(e.target.files[0]);
    }
});

// Parameter sliders - update display values and trigger debug updates
whiteThreshold.addEventListener('input', (e) => {
    whiteThresholdValue.textContent = e.target.value;
    whiteDebug.textContent = e.target.value;
    if (debugSection.style.display !== 'none') {
        scheduleDebugUpdate();
    }
});

blackThreshold.addEventListener('input', (e) => {
    blackThresholdValue.textContent = e.target.value;
    blackDebug.textContent = e.target.value;
    if (debugSection.style.display !== 'none') {
        scheduleDebugUpdate();
    }
});

morphKernel.addEventListener('input', (e) => {
    morphKernelValue.textContent = e.target.value;
});

morphIterations.addEventListener('input', (e) => {
    morphIterationsValue.textContent = e.target.value;
});

erosion.addEventListener('input', (e) => {
    erosionValue.textContent = e.target.value;
    erosionDebug.textContent = e.target.value;
    if (debugSection.style.display !== 'none') {
        scheduleDebugUpdate();
    }
});

epsilon.addEventListener('input', (e) => {
    epsilonValue.textContent = e.target.value;
});

// Buttons
processBtn.addEventListener('click', processImage);
visualizeBtn.addEventListener('click', visualizeDetection);
debugBtn.addEventListener('click', toggleDebugMode);
downloadBtn.addEventListener('click', downloadImage);
resetBtn.addEventListener('click', reset);

// Functions

function handleFileSelect(file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
        showStatus('Please select an image file', 'error');
        return;
    }

    uploadedFile = file;

    // Show preview of original image
    const reader = new FileReader();
    reader.onload = (e) => {
        originalImage.src = e.target.result;
        parametersSection.style.display = 'block';
        previewSection.style.display = 'block';
        correctedImage.style.display = 'none';
        loadingSpinner.style.display = 'none';
        resultInfo.style.display = 'none';
        downloadBtn.style.display = 'none';
    };
    reader.readAsDataURL(file);

    showStatus('Image loaded. Adjust parameters if needed, then click "Correct Perspective"', 'success');
}

async function processImage() {
    if (!uploadedFile) {
        showStatus('Please upload an image first', 'error');
        return;
    }

    // Show loading state
    loadingSpinner.style.display = 'flex';
    correctedImage.style.display = 'none';
    resultInfo.style.display = 'none';
    downloadBtn.style.display = 'none';
    processBtn.disabled = true;
    visualizeBtn.disabled = true;

    // Create form data
    const formData = new FormData();
    formData.append('file', uploadedFile);
    formData.append('white_threshold', whiteThreshold.value);
    formData.append('black_threshold', blackThreshold.value);
    formData.append('morph_kernel_size', morphKernel.value);
    formData.append('morph_iterations', morphIterations.value);
    formData.append('erosion_iterations', erosion.value);
    formData.append('epsilon_factor', epsilon.value);

    try {
        const response = await fetch('/api/process', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            // Show corrected image
            correctedImage.src = result.output_url;
            correctedImage.style.display = 'block';
            currentUploadId = result.output_url.split('/').pop();

            // Show result info
            resultInfo.style.display = 'block';
            statusMessage.textContent = result.message;
            statusMessage.classList.remove('error');
            dimensions.textContent = `Output: ${result.dimensions.width} × ${result.dimensions.height} pixels`;

            // Show download button
            downloadBtn.style.display = 'inline-flex';

            showStatus('Success! Perspective corrected with maximum quality preservation.', 'success');
        } else {
            showStatus(result.message, 'error');
            statusMessage.textContent = result.message;
            statusMessage.classList.add('error');
            resultInfo.style.display = 'block';
        }
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
    } finally {
        loadingSpinner.style.display = 'none';
        processBtn.disabled = false;
        visualizeBtn.disabled = false;
    }
}

async function visualizeDetection() {
    if (!uploadedFile) {
        showStatus('Please upload an image first', 'error');
        return;
    }

    // Show loading state
    loadingSpinner.style.display = 'flex';
    correctedImage.style.display = 'none';
    visualizeBtn.disabled = true;
    processBtn.disabled = true;

    // Create form data
    const formData = new FormData();
    formData.append('file', uploadedFile);
    formData.append('white_threshold', whiteThreshold.value);
    formData.append('black_threshold', blackThreshold.value);
    formData.append('morph_kernel_size', morphKernel.value);
    formData.append('morph_iterations', morphIterations.value);
    formData.append('erosion_iterations', erosion.value);
    formData.append('epsilon_factor', epsilon.value);

    try {
        const response = await fetch('/api/visualize', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            // Show visualization in corrected image area
            correctedImage.src = result.visualization_url;
            correctedImage.style.display = 'block';

            showStatus('Visualization shown. Green outline = detected border. Adjust parameters if detection is incorrect.', 'success');
        } else {
            showStatus(result.message, 'error');
        }
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
    } finally {
        loadingSpinner.style.display = 'none';
        visualizeBtn.disabled = false;
        processBtn.disabled = false;
    }
}

function downloadImage() {
    if (!currentUploadId) {
        showStatus('No processed image available', 'error');
        return;
    }

    // Trigger download
    const link = document.createElement('a');
    link.href = `/api/download/${currentUploadId}`;
    link.download = 'corrected_painting.png';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showStatus('Download started', 'success');
}

function reset() {
    uploadedFile = null;
    currentUploadId = null;

    parametersSection.style.display = 'none';
    previewSection.style.display = 'none';
    resultInfo.style.display = 'none';
    downloadBtn.style.display = 'none';

    fileInput.value = '';

    // Reset parameters to defaults
    whiteThreshold.value = 140;
    whiteThresholdValue.textContent = '140';
    blackThreshold.value = 30;
    blackThresholdValue.textContent = '30';
    morphKernel.value = 15;
    morphKernelValue.textContent = '15';
    morphIterations.value = 3;
    morphIterationsValue.textContent = '3';
    erosion.value = 3;
    erosionValue.textContent = '3';
    epsilon.value = 0.005;
    epsilonValue.textContent = '0.005';

    // Hide debug section
    debugSection.style.display = 'none';
    debugBtn.textContent = '🔍 Show Debug Masks';

    showStatus('Ready for a new image', 'success');
}

function showStatus(message, type = 'info') {
    statusBar.style.display = 'block';
    statusText.textContent = message;

    // Remove all type classes
    statusBar.classList.remove('success', 'error');

    // Add appropriate class
    if (type === 'success') {
        statusBar.classList.add('success');
    } else if (type === 'error') {
        statusBar.classList.add('error');
    }

    // Auto-hide after 5 seconds for success messages
    if (type === 'success') {
        setTimeout(() => {
            statusBar.style.display = 'none';
        }, 5000);
    }
}

async function toggleDebugMode() {
    if (!uploadedFile) {
        showStatus('Please upload an image first', 'error');
        return;
    }

    if (debugSection.style.display === 'none') {
        // Show debug mode
        debugSection.style.display = 'block';
        debugBtn.textContent = '🔍 Hide Debug Masks';
        await updateDebugVisualization();
    } else {
        // Hide debug mode
        debugSection.style.display = 'none';
        debugBtn.textContent = '🔍 Show Debug Masks';
    }
}

function scheduleDebugUpdate() {
    // Debounce: wait 300ms after last change before updating
    clearTimeout(debugUpdateTimer);
    debugUpdateTimer = setTimeout(() => {
        updateDebugVisualization();
    }, 300);
}

async function updateDebugVisualization() {
    if (!uploadedFile) return;

    try {
        const formData = new FormData();
        formData.append('file', uploadedFile);
        formData.append('white_threshold', whiteThreshold.value);
        formData.append('black_threshold', blackThreshold.value);
        formData.append('erosion_iterations', erosion.value);

        const response = await fetch('/api/debug', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            // Update all debug images with cache-busting timestamp
            const timestamp = Date.now();
            whiteMask.src = result.images.white_mask + '?t=' + timestamp;
            blackMask.src = result.images.black_mask + '?t=' + timestamp;
            combinedMask.src = result.images.combined_mask + '?t=' + timestamp;
            invertedMask.src = result.images.inverted_mask + '?t=' + timestamp;
            cleanMask.src = result.images.clean_mask + '?t=' + timestamp;
            erodedMask.src = result.images.eroded_mask + '?t=' + timestamp;
            if (result.images.detection) {
                detectionMask.src = result.images.detection + '?t=' + timestamp;
            }
        } else {
            console.error('Debug visualization failed:', result.message);
        }
    } catch (error) {
        console.error('Error updating debug visualization:', error);
    }
}

// Initialize
showStatus('Ready to process painting photographs', 'success');
