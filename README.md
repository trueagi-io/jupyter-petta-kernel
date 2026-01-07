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

This will install the Python package and register the kernel with Jupyter.

#### Manual Installation

```bash
# Install the package
export PETTA_PATH=/path/to/PeTTa
pip install -e /path/to/jupyter-petta-kernel

# Register the kernel
jupyter kernelspec install --user /path/to/jupyter-petta-kernel/resources --name petta
```

### Verify Installation

Check that the kernel is installed:

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

### "Cannot find petta module" error

Make sure the `PETTA_PATH` environment variable is set:

```bash
export PETTA_PATH=/path/to/PeTTa
```

Then restart JupyterLab/Jupyter Notebook.

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
