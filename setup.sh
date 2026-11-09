#!/bin/bash
# Sets up everything needed for Lab 2:
#   1. the conda environment "cm2003-lab2" (see environment.yml)
#   2. a Jupyter kernel with the same name
#   3. the compiled Cython extension for the fast convolution layers (build_cython.py)
#   4. the datasets in cm2003/datasets/ (download_data.py)
set -e
cd "$(dirname "${BASH_SOURCE[0]}")"
ENV_NAME=cm2003-lab2

source "$(conda info --base)/etc/profile.d/conda.sh"

# Packages listed in environment.yml. The conda ones are installed with conda-forge only
# (--override-channels), so Anaconda's "defaults" channel and its Terms of Service prompt are not
# used; the ones under "pip:" (PyTorch, MedMNIST) are installed with pip.
CONDA_PACKAGES=$(sed -n '/^dependencies:/,$p' environment.yml | grep -E '^  - ' | grep -v 'pip:' | sed -E 's/^  - //')
PIP_PACKAGES=$(sed -n '/^ *- pip:/,$p' environment.yml | grep -E '^      - ' | sed -E 's/^ +- //')

if conda env list | grep -qE "^${ENV_NAME} |/${ENV_NAME}$"; then
  echo "Environment ${ENV_NAME} already exists, making sure all packages are installed"
  conda install -y -n "$ENV_NAME" --override-channels -c conda-forge $CONDA_PACKAGES
else
  conda create -y -n "$ENV_NAME" --override-channels -c conda-forge $CONDA_PACKAGES
fi

conda activate "$ENV_NAME"
python -m pip install $PIP_PACKAGES
python -m ipykernel install --user --name="$ENV_NAME" --display-name "CM2003 Lab 2"

python build_cython.py
python download_data.py

echo
echo "Setup complete! In Jupyter, select the kernel \"CM2003 Lab 2\" (Kernel > Change kernel)."
