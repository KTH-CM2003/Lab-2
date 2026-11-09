# CM2003 Lab 2: Neural Networks and Convolutional Neural Networks

## Setting up the environment

This lab uses NumPy, PyTorch and a few scientific Python packages. You need two things:

1. **A Python environment** with the packages in `requirements.txt` / `environment.yml`.
2. **The datasets** in `cm2003/datasets/`: CIFAR-10 (about 170 MB) and PneumoniaMNIST (about 4 MB,
   for `PyTorch.ipynb`). They are not included in the repository; `python download_data.py` gets
   them for you (on MAIA, CIFAR-10 is copied from the course's shared folder).

Pick **one** of the options below.

### Option 1: On MAIA

Your MAIA workspace already has a ready-made environment called **`DL_labs_GPU`**, so there is
nothing to install.

1. Open a terminal in JupyterLab (*File > New > Terminal*) and clone your repository:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```
2. Activate the environment and get the datasets:
   ```bash
   conda activate DL_labs_GPU
   python download_data.py
   ```
3. Open a notebook (start with `FullyConnectedNets.ipynb`) and select the kernel **DL_labs_GPU**
   (*Kernel > Change Kernel...*). If it is not in the list, refresh the browser tab.

Working over SSH or in VS Code instead? Activate the environment in the terminal with
`conda activate DL_labs_GPU`, and select `DL_labs_GPU` as the Python interpreter/kernel in VS Code.

### Option 2: On your own computer with conda

1. Install [Miniforge](https://github.com/conda-forge/miniforge) (a minimal conda that uses the
   free conda-forge channel). Any existing Anaconda/Miniconda installation also works.
2. In a terminal (on Windows: the *Miniforge Prompt*), go to the repository folder.
3. **macOS / Linux:** run the setup script. It creates the conda environment `cm2003-lab2`,
   registers it as a Jupyter kernel called *CM2003 Lab 2* and downloads the datasets:
   ```bash
   ./setup.sh
   ```
   **Windows:** run the same steps by hand:
   ```bash
   conda env create -f environment.yml
   conda activate cm2003-lab2
   python -m ipykernel install --user --name=cm2003-lab2 --display-name "CM2003 Lab 2"
   python download_data.py
   ```
4. Start Jupyter (or VS Code), open a notebook and select the kernel **CM2003 Lab 2**.

Next time, activate the environment with `conda activate cm2003-lab2`.

> If `conda env create` stops with a *Terms of Service* error (newer Anaconda/Miniconda
> installations), create the environment from conda-forge only and install the rest with pip:
> ```bash
> conda create -n cm2003-lab2 --override-channels -c conda-forge python=3.13 pip
> conda activate cm2003-lab2
> pip install -r requirements.txt
> ```
> Then continue with the `ipykernel install` line above.

### Option 3: On your own computer with uv

[uv](https://docs.astral.sh/uv/) is a fast alternative to conda/pip. Install it by following
[the uv installation guide](https://docs.astral.sh/uv/getting-started/installation/), then, in the
repository folder:

```bash
uv venv --python 3.13                 # creates the environment in .venv/ (uv downloads Python 3.13 if needed)
uv pip install -r requirements.txt    # installs the lab packages into .venv/
uv run python -m ipykernel install --user --name=cm2003-lab2 --display-name "CM2003 Lab 2"
uv run python download_data.py
```

`uv run <command>` runs a command inside the `.venv` environment without activating it. To
activate it in your terminal instead: `source .venv/bin/activate` (macOS / Linux) or
`.venv\Scripts\activate` (Windows). Then open a notebook and select the kernel **CM2003 Lab 2**.
In VS Code, you can also pick `.venv` directly as the Python interpreter.

### GPU or CPU?

The NumPy notebooks (Q1 to Q4) run on the CPU. `PyTorch.ipynb` uses a GPU when one is available
(it prints `using device: cuda`) and otherwise runs on the CPU, which is slower but works. On
MAIA, `DL_labs_GPU` already has a PyTorch build that matches the GPUs. On your own computer,
`pip`/`uv` install the default PyTorch build for your system (Apple-silicon Macs can use
`device = torch.device('mps')`); for an NVIDIA GPU on Windows, see
[pytorch.org](https://pytorch.org/get-started/locally/) for the CUDA build.

### Check that it works

Run the setup cells at the top of `FullyConnectedNets.ipynb` (loads CIFAR-10) and of
`PyTorch.ipynb` (loads PneumoniaMNIST). If both run without errors, you are ready.

### Troubleshooting

- **The kernel does not show up in Jupyter:** refresh the browser tab. For your own environment,
  re-run the `ipykernel install` command from your option above.
- **`FileNotFoundError` mentioning `cifar-10-batches-py`:** the dataset is missing. Run
  `python download_data.py` (with your environment's Python) from the repository folder.
- **`ModuleNotFoundError`:** the notebook is using the wrong kernel. Check the kernel name in the
  top-right corner of the notebook (*DL_labs_GPU* on MAIA, *CM2003 Lab 2* on your own computer).

## Goals

In this assignment, you will practice writing backpropagation code and training Neural Networks and Convolutional Neural Networks. The goals of this assignment are as follows:

1. Understand Neural Networks and how they are arranged in layered architectures.
2. Understand and be able to implement (vectorized) backpropagation.
3. Implement Batch Normalization for training deep networks.
4. Implement Dropout to regularize networks.
5. Understand the architecture of Convolutional Neural Networks and get practice with training them.
6. Gain experience with a major deep learning framework, PyTorch.

## Assignment Structure

### Q1: Multi-Layer Fully Connected Neural Networks
In the notebook `FullyConnectedNets.ipynb`, you will implement fully connected networks of arbitrary depth. To optimize these models, you will implement several popular update rules.

### Q2: Batch Normalization - **Optional**
The notebook `BatchNormalization.ipynb` will guide you through implementing batch normalization and using it to train deep fully connected networks. This notebook is optional to complete. Simply skip the parts including batchnorm in the other labs if you do not have time to complete this one.

### Q3: Dropout
In `Dropout.ipynb`, you will implement dropout and explore its effects on model generalization.

### Q4: Convolutional Neural Networks
The notebook `ConvolutionalNetworks.ipynb` will have you implement several new layers that are commonly used in convolutional networks.

### Q5: PyTorch on PneumoniaMNIST
For this part, you will work with PyTorch, a popular and powerful deep learning framework. Open `PyTorch.ipynb` to learn how the framework works, culminating in training a convolutional network of your own design on PneumoniaMNIST to achieve the best performance you can.

## Submitting Your Work

Submit your lab on Github
