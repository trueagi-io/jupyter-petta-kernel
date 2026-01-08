#!/usr/bin/env python3
"""
Quick verification script to test if the PeTTa Jupyter kernel is working.
Run this before starting JupyterLab to ensure everything is configured correctly.
"""

import sys
import os

def check_env_vars():
    """Check required environment variables."""
    print("1. Checking environment variables...")
    petta_path = os.environ.get('PETTA_PATH')
    if petta_path:
        print(f"   ✓ PETTA_PATH is set: {petta_path}")
    else:
        print("   ✗ PETTA_PATH is not set!")
        print("     Add to ~/.zshrc: export PETTA_PATH=/opt/snet/PeTTa")
        return False
    return True

def check_swipl():
    """Check if SWI-Prolog is in PATH."""
    print("\n2. Checking SWI-Prolog...")
    import shutil
    swipl = shutil.which('swipl')
    if swipl:
        print(f"   ✓ swipl found: {swipl}")
        import subprocess
        result = subprocess.run([swipl, '--version'], capture_output=True, text=True)
        version = result.stdout.strip().split('\n')[0]
        print(f"   {version}")
        return True
    else:
        print("   ✗ swipl not found in PATH!")
        print("     Add to ~/.zshrc: export PATH=\"/Applications/SWI-Prolog.app/Contents/MacOS:$PATH\"")
        return False

def check_janus():
    """Check if janus-swi can import."""
    print("\n3. Checking janus-swi...")
    try:
        import janus_swi
        print(f"   ✓ janus-swi imported successfully")
        return True
    except ImportError as e:
        print(f"   ✗ Failed to import janus-swi: {e}")
        print("     Install with: pip install janus-swi")
        return False

def check_petta_jupyter():
    """Check if petta_jupyter kernel can import."""
    print("\n4. Checking petta_jupyter kernel...")
    # Add PeTTa python directory to path
    petta_path = os.environ.get('PETTA_PATH')
    if petta_path:
        sys.path.insert(0, os.path.join(petta_path, 'python'))

    try:
        import petta_jupyter
        print(f"   ✓ petta_jupyter imported successfully")
        print(f"   Kernel class: {petta_jupyter.PeTTaKernel}")
        return True
    except ImportError as e:
        print(f"   ✗ Failed to import petta_jupyter: {e}")
        return False

def check_jupyter_kernelspec():
    """Check if kernel is registered with Jupyter."""
    print("\n5. Checking Jupyter kernel registration...")
    import subprocess
    result = subprocess.run(['jupyter', 'kernelspec', 'list'], capture_output=True, text=True)
    if 'petta' in result.stdout:
        print("   ✓ petta kernel is registered with Jupyter")
        # Extract the kernel path
        for line in result.stdout.split('\n'):
            if 'petta' in line:
                print(f"   {line.strip()}")
        return True
    else:
        print("   ✗ petta kernel is not registered!")
        print("     Register with: jupyter kernelspec install --user /path/to/jupyter-petta-kernel/resources --name petta")
        return False

def main():
    print("=" * 60)
    print("PeTTa Jupyter Kernel Verification")
    print("=" * 60)

    checks = [
        check_env_vars(),
        check_swipl(),
        check_janus(),
        check_petta_jupyter(),
        check_jupyter_kernelspec()
    ]

    print("\n" + "=" * 60)
    if all(checks):
        print("✓ All checks passed!")
        print("\nYou can now start JupyterLab:")
        print("  jupyter lab")
        print("\nCreate a new notebook and select 'PeTTa (MeTTa)' as the kernel.")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
