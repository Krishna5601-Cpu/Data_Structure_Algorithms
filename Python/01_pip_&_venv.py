"""
TODAY'S LEARNING SUMMARY: PIP & PYTHON VIRTUAL ENVIRONMENTS

1. WHAT IS PIP?
   - The standard package manager for Python.
   - Downloads and manages open-source packages from PyPI.
   - Handles automatic dependency resolution.

2. WHAT IS A VIRTUAL ENVIRONMENT (venv)?
   - An isolated environment containing its own Python binary and libraries.
   - Prevents dependency/version conflicts across different projects.

3. CORE COMMAND WORKFLOW:
   - Create environment:     python -m venv .venv
   - Activate (macOS/Linux): source .venv/bin/activate
   - Activate (Windows CMD): .venv\Scripts\activate.bat
   - Install package:        pip install <package_name>
   - Export dependencies:    pip freeze > requirements.txt
   - Deactivate env:         deactivate
"""
