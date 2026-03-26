import os

def main():
    print("Checking for GPU...")
    os.system("nvidia-smi")

if __name__ == "__main__":
    main()