#!/bin/bash

# Installation script for PeTTa Jupyter kernel

set -e

echo "Installing PeTTa Jupyter kernel..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found. Please install Python 3.8 or later."
    exit 1
fi

# Check if pip is available
if ! command -v pip &> /dev/null && ! python3 -m pip --version &> /dev/null; then
    echo "Error: pip not found. Please install pip."
    exit 1
fi

# Check if we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ] && [ -z "$CONDA_DEFAULT_ENV" ]; then
    echo ""
    echo "WARNING: You are not in a Python virtual environment!"
    echo ""
    echo "It is recommended to install the Jupyter kernel in a virtual environment."
    echo "To create and activate a virtual environment:"
    echo ""
    echo "  python3 -m venv ~/jupyter-env"
    echo "  source ~/jupyter-env/bin/activate  # On Windows: ~/jupyter-env/Scripts/activate"
    echo "  cd ${SCRIPT_DIR}"
    echo "  ./install.sh"
    echo ""
    read -p "Continue with system-wide installation anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 1
    fi
fi

# Check if PETTA_PATH is set
if [ -z "$PETTA_PATH" ]; then
    echo ""
    echo "WARNING: PETTA_PATH environment variable is not set!"
    echo ""
    echo "The kernel needs to know where PeTTa is installed."
    echo "Please set PETTA_PATH to your PeTTa installation directory:"
    echo ""
    echo "  export PETTA_PATH=/path/to/PeTTa"
    echo ""
    echo "To make this permanent, add it to your ~/.bashrc or ~/.zshrc:"
    echo "  echo 'export PETTA_PATH=/path/to/PeTTa' >> ~/.bashrc"
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 1
    fi
fi

# Install the kernel package
echo "Installing PeTTa Jupyter kernel package..."
python3 -m pip install -e "${SCRIPT_DIR}"

# Check if JupyterLab is installed
if ! python3 -m jupyter --version &> /dev/null; then
    echo ""
    echo "JupyterLab is not installed."
    read -p "Install JupyterLab now? (Y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
        echo "Installing JupyterLab..."
        python3 -m pip install jupyterlab
    else
        echo "Warning: JupyterLab is required to use this kernel."
        echo "Install it later with: pip install jupyterlab"
    fi
fi

# Install the kernel spec
echo "Registering Jupyter kernel..."
python3 -m jupyter kernelspec install --user "${SCRIPT_DIR}/resources" --name petta --replace

echo ""
echo "✓ Installation complete!"
echo ""
echo "To use the kernel:"
echo "  1. Start JupyterLab: jupyter lab"
echo "  2. Create a new notebook"
echo "  3. Select 'PeTTa (MeTTa)' as the kernel"
echo ""
echo "To verify installation:"
echo "  python3 -m jupyter kernelspec list"
