# VMware Module Installer Automation

This repository provides an automated solution to resolve compatibility issues with VMware Workstation Pro kernel modules (`vmmon` and `vmnet`) on Linux systems. The script simplifies the process of downloading, modifying, and installing patched modules from [mkubecek's vmware-host-modules repository](https://github.com/mkubecek/vmware-host-modules).

## Features
- Automatically downloads the required `vmware-host-modules` patch for VMware Workstation 17.5.1.
- Applies necessary modifications to `vmnetInt.h` and `bridge.c` files to bypass compatibility issues.
- Builds and installs the patched kernel modules.
- Saves time and reduces errors by automating manual steps.

This script is particularly useful for users who encounter issues with VMware Workstation on Linux, where kernel updates break compatibility with `vmmon` and `vmnet` modules. By automating the process, it ensures seamless integration and reduces the burden of troubleshooting.

## Prerequisites
1. **Linux Distribution**:
   - Tested on Fedora Workstation 41.
   - Known to work on other distributions like Ubuntu and Pop!_OS with similar kernel versions.
2. **Dependencies**:
   - `Python 3`
   - `requests` module (install using `pip install requests` if not already installed).
   - Essential build tools (e.g., `gcc`, `make`, `kernel-devel`).

## Installation and Usage

### Step 1: Download and Run the Script
Save the `vmware_module_installer.py` script to your `~/Downloads` directory. Then run:
```bash
cd ~/Downloads
python3 vmware_module_installer.py
```

### Step 2: Complete VMware Setup
Once the script completes successfully:
1. Launch VMware Workstation Pro.
2. Follow the on-screen prompts to complete the installation process.

## Technical Details

The script performs the following tasks:
1. **Downloads the patch**:
   - From [mkubecek's GitHub repository](https://github.com/mkubecek/vmware-host-modules).
   - Retrieves the `workstation-17.5.1.zip` patch.
   - Note: This patch corresponds to VMware Workstation version **17.5.2**, as the `workstation-17.5.1` branch in mkubecek's repository ensures compatibility with the latest updates of VMware Workstation installers.
2. **Extracts the patch**:
   - Unzips the file to `~/Downloads/vmware-host-modules-workstation-17.5.1`.
3. **Modifies source files**:
   - Applies comments to `#define dev_lock_list` and `#define dev_unlock_list` macros in `vmnetInt.h`.
   - Comments out all instances of `dev_lock_list()` and `dev_unlock_list()` in `bridge.c`.
4. **Builds and installs the modules**:
   - Runs `make` to build the modules.
   - Runs `sudo make install` to install the modules.

This automation eliminates the need for manual intervention in editing and building kernel modules, ensuring consistency and reliability.

## Acknowledgments
This solution is built entirely on the outstanding work by [mkubecek](https://github.com/mkubecek) and his `vmware-host-modules` repository. His repository provides the essential patches and updates needed to resolve kernel compatibility issues with VMware Workstation. This script merely automates the steps outlined in his work, adding convenience and accessibility for users.

## Notes
- The script is designed to work with `~/Downloads` as the working directory and does not use placeholder paths.
- Tested extensively on Fedora Workstation 41. Results may vary on other distributions.

## Contributing
If you encounter issues or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

