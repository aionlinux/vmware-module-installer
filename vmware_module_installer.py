import os
import zipfile
import requests
import re
import subprocess

# Define URLs and paths
DOWNLOAD_URL = "https://github.com/mkubecek/vmware-host-modules/archive/refs/heads/workstation-17.5.1.zip"
DOWNLOAD_DIR = os.path.expanduser("~/Downloads")
ZIP_FILE = os.path.join(DOWNLOAD_DIR, "workstation-17.5.1.zip")
EXTRACTED_DIR = os.path.join(DOWNLOAD_DIR, "vmware-host-modules-workstation-17.5.1")

def download_file(url, output_path):
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f"Downloaded to {output_path}")

def unzip_file(zip_path, extract_to):
    print(f"Unzipping {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Unzipped to {extract_to}")

def comment_out_instances(file_path, patterns):
    print(f"Modifying {file_path}...")
    with open(file_path, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if any(re.search(pattern, line) for pattern in patterns):
            modified_lines.append("// " + line)
        else:
            modified_lines.append(line)

    with open(file_path, "w") as file:
        file.writelines(modified_lines)
    print(f"Modified {file_path}")

def run_make_commands():
    print("Running `make` and `sudo make install`...")
    try:
        subprocess.run(["make"], cwd=EXTRACTED_DIR, check=True)
        subprocess.run(["sudo", "make", "install"], cwd=EXTRACTED_DIR, check=True)
        print("Kernel modules built and installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during `make` or `make install`: {e}")

def main():
    # Step 1: Set working directory
    os.chdir(DOWNLOAD_DIR)
    print(f"Working directory set to {DOWNLOAD_DIR}")

    # Step 2: Download the zip file
    download_file(DOWNLOAD_URL, ZIP_FILE)

    # Step 3: Unzip the file
    unzip_file(ZIP_FILE, DOWNLOAD_DIR)

    # Step 4: Modify vmnetInt.h
    vmnetint_h_path = os.path.join(EXTRACTED_DIR, "vmnet-only", "vmnetInt.h")
    comment_out_instances(vmnetint_h_path, [r"dev_lock_list", r"dev_unlock_list"])

    # Step 5: Modify bridge.c
    bridge_c_path = os.path.join(EXTRACTED_DIR, "vmnet-only", "bridge.c")
    comment_out_instances(bridge_c_path, [r"dev_lock_list", r"dev_unlock_list"])

    # Step 6: Build and install kernel modules
    run_make_commands()

    print("Automation script completed successfully.")

if __name__ == "__main__":
    main()
