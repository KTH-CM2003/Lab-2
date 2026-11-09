"""Compile the Cython extension cm2003/im2col_cython (fast convolution layers).

Needed for the "fast layers" part of ConvolutionalNetworks.ipynb. Run it with the Python of
your environment, from the repository folder or from a notebook (%run build_cython.py).
It needs a C compiler: built in on MAIA and most Linux systems; on macOS run
`xcode-select --install` once; on Windows install "Microsoft C++ Build Tools".
"""
import subprocess
import sys
from pathlib import Path

CM2003 = Path(__file__).resolve().parent / "cm2003"

subprocess.run(
    [sys.executable, "setup.py", "build_ext", "--inplace"], cwd=CM2003, check=True
)
print("Cython extension compiled successfully.")
