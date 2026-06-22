"""Streamlit Cloud entry point.

Imports dashboard.main safely (dashboard.py has no Streamlit calls at import time).
"""

from dashboard import main

main()
