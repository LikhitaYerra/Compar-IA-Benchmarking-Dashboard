#!/usr/bin/env python3
"""
ComparAI Dashboard Launcher
Launches the dashboard with your ComparAI template data
"""

import subprocess
import sys
import os

def check_comparai_template():
    """Check if ComparAI template exists"""
    template_file = "ComparAI_Benchmark_Template_v2-2.xlsx"
    if os.path.exists(template_file):
        print(f"✅ Found ComparAI template: {template_file}")
        return True
    else:
        print(f"❌ ComparAI template not found: {template_file}")
        print("Please ensure the template is in the current directory")
        return False

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

def launch_comparai_dashboard():
    """Launch the ComparAI dashboard"""
    print("🚀 Launching ComparAI Benchmarking Dashboard...")
    print("📊 Dashboard will open at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the dashboard")
    print("=" * 50)
    
    try:
        subprocess.run(['streamlit', 'run', 'dashboard_comparai.py'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching dashboard: {e}")
        sys.exit(1)

def main():
    """Main launcher function"""
    print("🤖 ComparAI Benchmarking Dashboard Launcher")
    print("=" * 45)
    
    # Check if we're in the right directory
    if not os.path.exists('dashboard_comparai.py'):
        print("❌ dashboard_comparai.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check for ComparAI template
    if not check_comparai_template():
        print("\n⚠️  Dashboard will run with sample data instead")
        print("To use your ComparAI data, place the template in this directory")
    
    # Check and install dependencies
    check_dependencies()
    
    # Launch dashboard
    launch_comparai_dashboard()

if __name__ == "__main__":
    main()
