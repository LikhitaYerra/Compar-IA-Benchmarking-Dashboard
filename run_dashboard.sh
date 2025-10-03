#!/bin/bash

# Compar'IA Benchmarking Dashboard Launcher
# This script sets up and runs the Streamlit dashboard

echo "🤖 Compar'IA Benchmarking Dashboard"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ Python and pip are available"
echo ""

# Install requirements if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🚀 Starting dashboard..."
echo "The dashboard will open in your default browser at http://localhost:8501"
echo "Press Ctrl+C to stop the dashboard"
echo ""

# Run the dashboard
streamlit run dashboard.py
