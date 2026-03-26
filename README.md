# Kaggle API GPU Demo

This is a minimal demonstration of using the Kaggle Python API to run GPU workloads (like `nvidia-smi`) on Kaggle directly from a Python script, avoiding manual web UI interactions.

## Prerequisites

1.  A [Kaggle](https://www.kaggle.com) Account
2.  An API Token:
    *   Go to your Kaggle Account Settings (`kaggle.com/<username>/account`).
    *   Click **"Create New API Token"** to download `kaggle.json`.
3.  Python 3.7+ installed.

## Setup

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Configure your Kaggle Credentials:
    
    **Option 1 (Environment Variables)**:
    ```bash
    export KAGGLE_USERNAME="your_kaggle_username"
    export KAGGLE_KEY="your_kaggle_key"
    ```

    **Option 2 (JSON Config)**:
    Place the downloaded `kaggle.json` into `~/.kaggle/kaggle.json` (Linux/Mac) or `C:\Users\<Windows-username>\.kaggle\kaggle.json` (Windows). Let it have restricted permissions (`chmod 600 ~/.kaggle/kaggle.json`).

## Running the Demo

The workspace contains:
1. `train.py`: A simple python script that checks for the GPU runtime.
2. `kernel-metadata.json`: The kernel config which specifies `"enable_gpu": "true"` and `"code_file": "train.py"`.

**Before running:** open `kernel-metadata.json` and change `YOUR_KAGGLE_USERNAME` to your actual Kaggle username.

Then use the Kaggle CLI to push, monitor, and pull the outputs of your kernel:

```bash
# Push to Kaggle (triggers a new run)
kaggle kernels push -p ./

# Check run status
kaggle kernels status your-username/my-gpu-kernel

# Pull output/logs when done
kaggle kernels output your-username/my-gpu-kernel -p ./output
```