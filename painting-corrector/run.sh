#!/bin/bash

# Painting Perspective Corrector - Start Script

echo "🖼️  Painting Perspective Corrector"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📚 Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

# Create temp directory if it doesn't exist
mkdir -p /tmp/painting-corrector

# Start the server
echo ""
echo "✨ Starting server..."
echo ""
echo "🌐 Open in browser: http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
python main.py
