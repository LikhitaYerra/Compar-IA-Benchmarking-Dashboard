#!/usr/bin/env python3
"""
Compar'IA Benchmarking Dashboard Launcher
Simple launcher script for the Streamlit dashboard
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pandas', 'plotly', 'numpy', 'openpyxl']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
        print("✅ All packages installed successfully!")
    else:
        print("✅ All required packages are available")

def launch_dashboard():
    """Launch the Streamlit dashboard"""
    print("🚀 Launching Compar'IA Benchmarking Dashboard...")
    print("📊 Dashboard will open at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the dashboard")
    print("=" * 50)
    
    try:
        subprocess.run(['streamlit', 'run', 'dashboard.py'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching dashboard: {e}")
        sys.exit(1)

def main():
    """Main launcher function"""
    print("🤖 Compar'IA Benchmarking Dashboard Launcher")
    print("=" * 45)
    
    # Check if we're in the right directory
    if not os.path.exists('dashboard.py'):
        print("❌ dashboard.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check and install dependencies
    check_dependencies()
    
    # Launch dashboard
    launch_dashboard()

if __name__ == "__main__":
    main()
