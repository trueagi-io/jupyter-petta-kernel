# Testing Checklist for PeTTa Jupyter Kernel

Follow these steps to verify the kernel is working correctly:

## 1. Quick Verification

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

✅ **Pass Criteria:** All checks pass with ✓ marks.

## 2. Test with Example Notebook

The recommended way to test the kernel is to run the example notebook:

1. Launch JupyterLab:
   ```bash
   jupyter lab
   ```

2. Open `examples/basic_usage.ipynb`

3. Run all cells: **Run → Run All Cells**

The notebook tests:
- Basic arithmetic operations
- Function definitions
- Pattern matching
- Recursive functions with guards
- Error handling (syntax and type errors)
- State persistence across cells

✅ **Pass Criteria:** All cells execute successfully with expected outputs.

## 3. Manual Testing (Optional)

If you prefer to test manually:

1. Create a new notebook in JupyterLab
2. Select "PeTTa (MeTTa)" as the kernel
3. Test basic execution:
   ```metta
   !(+ 1 2)
   ```
   **Expected:** `3`

4. Test function definition:
   ```metta
   (= (double $x) (* $x 2))
   !(double 5)
   ```
   **Expected:** `10`

## Final Checklist

- [ ] Verification script passes all checks
- [ ] `examples/basic_usage.ipynb` runs successfully
- [ ] Can create new notebooks with PeTTa kernel
- [ ] Kernel restarts cleanly (Kernel → Restart Kernel)

## Troubleshooting

### Verification script fails

If `verify_kernel.py` reports any failures, follow the fix suggestions it provides. Common issues:

- **PETTA_PATH not set:** Add `export PETTA_PATH=/path/to/PeTTa` to your shell config
- **SWI-Prolog not in PATH:** Install SWI-Prolog >= 9.3.x and add to PATH
- **janus-swi errors:** Reinstall with `pip uninstall janus-swi -y && pip install janus-swi`

### Kernel won't start

- Check janus-swi is installed: `pip list | grep janus`
- Check SWI-Prolog is installed: `which swipl`
- Verify PETTA_PATH: `echo $PETTA_PATH`
- Look at JupyterLab terminal output for error messages

### Example notebook cells fail

- Make sure you're running cells in order (top to bottom)
- Try restarting kernel: **Kernel → Restart Kernel**
- Re-run all cells after restart

### Import errors

- Ensure PETTA_PATH is set in your shell config (`~/.bashrc` or `~/.zshrc`)
- Restart your terminal and JupyterLab after setting environment variables
- Run verification script to diagnose: `python3 verify_kernel.py`

## Advanced Testing

For developers working on the kernel:

1. **Test kernel modifications:**
   ```bash
   pip install -e .
   # Restart kernel in notebooks to pick up changes
   ```

2. **Test with different MeTTa code:**
   - Create notebooks in `examples/` directory
   - Test edge cases and error conditions
   - Verify error messages are clear and helpful

3. **Test installation script:**
   ```bash
   ./install.sh
   # Follow prompts and verify all checks pass
   ```

## Success!

If all tests pass, the kernel is working correctly! 🎉

For more information:
- See [README.md](README.md) for usage documentation
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Review [examples/basic_usage.ipynb](examples/basic_usage.ipynb) for MeTTa examples
