# PeTTa Jupyter Kernel

A Jupyter kernel for executing MeTTa code using PeTTa.

## Features

- Execute MeTTa code in Jupyter notebooks
- Clean output formatting
- Graceful error handling with readable error messages
- State persistence across notebook cells
- Support for syntax errors, type errors, and runtime errors

## Prerequisites

This kernel requires PeTTa to be installed separately. PeTTa provides the core MeTTa execution engine.

**Install PeTTa first:**
```bash
git clone https://github.com/patham9/PeTTa.git
cd PeTTa
# Follow PeTTa installation instructions
```

## Requirements

- Python 3.8+
- SWI-Prolog >= 9.3.x
- PeTTa (installed separately - see Prerequisites above)
- janus-swi (Python package)
- ipykernel (Python package)
- jupyterlab or jupyter notebook

## Installation

### Step 0: Create a Virtual Environment (Recommended)

It's recommended to install the Jupyter kernel in a Python virtual environment. You can use any virtual environment tool (venv, virtualenv, conda, etc.).

**Example using venv:**

```bash
# Create a virtual environment
python3 -m venv ~/jupyter-env

# Activate it
source ~/jupyter-env/bin/activate  # On Windows: ~/jupyter-env/Scripts/activate
```

### Step 1: Set PETTA_PATH Environment Variable

The kernel needs to know where PeTTa is installed. Set the `PETTA_PATH` environment variable:

```bash
export PETTA_PATH=/path/to/PeTTa
```

To make this permanent, add it to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
echo 'export PETTA_PATH=/path/to/PeTTa' >> ~/.bashrc
source ~/.bashrc
```

### Step 2: Install the Kernel

#### Quick Install (Recommended)

```bash
cd /path/to/jupyter-petta-kernel
./install.sh
```

The install script will:

- Check if you're in a virtual environment (recommended)
- Install the kernel package
- Check for JupyterLab and offer to install it if needed
- Register the kernel with Jupyter

#### Manual Installation

```bash
# Install the package
export PETTA_PATH=/path/to/PeTTa
pip install -e /path/to/jupyter-petta-kernel

# Register the kernel
jupyter kernelspec install --user /path/to/jupyter-petta-kernel/resources --name petta
```

### Verify Installation

Run the verification script to check all requirements:

```bash
cd /path/to/jupyter-petta-kernel
python3 verify_kernel.py
```

This will check:

- PETTA_PATH environment variable is set
- SWI-Prolog is installed and in PATH
- janus-swi Python package is installed
- petta_jupyter kernel can import successfully
- Kernel is registered with Jupyter

Alternatively, check manually:

```bash
jupyter kernelspec list
```

You should see `petta` in the list.

## Usage

1. Launch JupyterLab or Jupyter Notebook:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

2. Create a new notebook and select "PeTTa (MeTTa)" as the kernel

3. Write MeTTa code in cells and execute them:
   ```metta
   !(+ 1 2)
   ```

   Output: `3`

4. Define functions:
   ```metta
   (= (factorial 0) 1)
   (= (factorial $n) (* $n (factorial (- $n 1))))
   ```

5. Use defined functions:
   ```metta
   !(factorial 5)
   ```

   Output: `120`

## Examples

### Basic arithmetic
```metta
!(+ 1 2)         # Returns: 3
!(* 3 4)         # Returns: 12
!(- 10 5)        # Returns: 5
```

### Function definition
```metta
(= (double $x) (* $x 2))
!(double 5)      # Returns: 10
```

### Error handling
```metta
!(+ 1           # Error: Parse error: missing ')'
!(+ abc def)    # Error: Type error: Expected evaluable, got def/0
```

## Implementation Details

### Architecture

- **kernel.py**: Main kernel implementation, handles code execution
- **output_formatter.py**: Formats results and error messages
- **resources/kernel.json**: Kernel specification for Jupyter

### Technical Decisions

- Uses temporary files to pass code to PeTTa (avoids Prolog string escaping issues)
- Integrates with PeTTa's Python API via janus_swi
- Extracts clean error messages from Prolog error terms
- Displays errors in red (stderr) and normal output in black (stdout)

## Troubleshooting

### Quick Diagnosis

Run the verification script to identify issues:

```bash
cd /path/to/jupyter-petta-kernel
python3 verify_kernel.py
```

### "Cannot find petta module" error

Make sure the `PETTA_PATH` environment variable is set and persists across sessions:

```bash
export PETTA_PATH=/path/to/PeTTa
```

Add it to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) to make it permanent, then restart your terminal and JupyterLab.

### "Library not loaded" or janus-swi errors

If you see errors about missing SWI-Prolog libraries, this means janus-swi was compiled against a different SWI-Prolog installation than the one currently in your PATH.

Fix by reinstalling janus-swi:

```bash
# Ensure SWI-Prolog is in your PATH first
which swipl  # Should show the path to your SWI-Prolog installation

# Reinstall janus-swi
pip uninstall janus-swi -y
pip install janus-swi --no-cache-dir
```

**Important**: Make sure SWI-Prolog remains in your PATH when you start JupyterLab. Add the appropriate export to your shell configuration file.

### Kernel crashes on startup

Make sure janus-swi is installed:

```bash
pip install janus-swi
```

### Kernel not found in Jupyter

Re-register the kernel:

```bash
jupyter kernelspec install --user /path/to/jupyter-petta-kernel/resources --replace
```

## Development

To modify the kernel:

1. Edit the source files in `python/petta_jupyter/`
2. Reinstall: `pip install -e .`
3. Restart the kernel in your notebook

## License

[Add appropriate license information]
