"""Get the datasets for Lab 2 into cm2003/datasets/ (works on Linux, macOS and Windows).

- CIFAR-10 (about 170 MB): on MAIA copied from the course's shared folder (~/shared/datasets),
  elsewhere downloaded from the official CIFAR-10 website.
- PneumoniaMNIST (about 4 MB, used in PyTorch.ipynb): downloaded from Zenodo (MedMNIST).

Usage:  python download_data.py
"""
import shutil
import tarfile
import urllib.request
from pathlib import Path

CIFAR_URL = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
PNEUMONIA_URL = "https://zenodo.org/records/10519652/files/pneumoniamnist.npz?download=1"
SHARED = Path.home() / "shared" / "datasets"
DATASETS = Path(__file__).resolve().parent / "cm2003" / "datasets"
CIFAR = DATASETS / "cifar-10-batches-py"
PNEUMONIA = DATASETS / "pneumoniamnist.npz"


def get_cifar10():
    if (CIFAR / "data_batch_1").exists():
        print(f"CIFAR-10 is already there: {CIFAR}")
        return
    if (SHARED / "cifar-10-batches-py" / "data_batch_1").exists():
        print(f"Copying CIFAR-10 from {SHARED / 'cifar-10-batches-py'} ...")
        shutil.copytree(SHARED / "cifar-10-batches-py", CIFAR)
    else:
        archive = DATASETS / "cifar-10-python.tar.gz"
        print(f"Downloading CIFAR-10 (about 170 MB) from {CIFAR_URL} ...")
        print("This can take a while if the server is busy.")
        urllib.request.urlretrieve(CIFAR_URL, archive)
        print("Extracting ...")
        with tarfile.open(archive) as tar:
            if hasattr(tarfile, "data_filter"):  # Python 3.12+: safe extraction
                tar.extractall(DATASETS, filter="data")
            else:
                tar.extractall(DATASETS)
        archive.unlink()
    print(f"Done: {CIFAR}")


def get_pneumoniamnist():
    if PNEUMONIA.exists():
        print(f"PneumoniaMNIST is already there: {PNEUMONIA}")
        return
    if (SHARED / PNEUMONIA.name).exists():
        print(f"Copying PneumoniaMNIST from {SHARED} ...")
        shutil.copy(SHARED / PNEUMONIA.name, PNEUMONIA)
    else:
        print(f"Downloading PneumoniaMNIST (about 4 MB) from {PNEUMONIA_URL} ...")
        tmp = PNEUMONIA.with_suffix(".part")
        urllib.request.urlretrieve(PNEUMONIA_URL, tmp)
        tmp.rename(PNEUMONIA)
    print(f"Done: {PNEUMONIA}")


if __name__ == "__main__":
    DATASETS.mkdir(parents=True, exist_ok=True)
    get_cifar10()
    get_pneumoniamnist()
