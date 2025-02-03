import os
import subprocess

def install_texlive():
    """Detect Linux distribution and install texlive-scheme-full using the appropriate package manager."""
    
    try:
        # Detect the Linux distribution
        with open("/etc/os-release", "r") as f:
            os_info = f.read().lower()

        if "fedora" in os_info or "rhel" in os_info or "centos" in os_info:
            cmd = "sudo dnf install -y texlive-scheme-full"
        elif "debian" in os_info or "ubuntu" in os_info or "pop!_os" in os_info:
            cmd = "sudo apt update && sudo apt install -y texlive-full"
        elif "arch" in os_info or "manjaro" in os_info:
            cmd = "sudo pacman -Syu --noconfirm texlive-most"
        elif "opensuse" in os_info:
            cmd = "sudo zypper install -y texlive-scheme-full"
        else:
            print("Unsupported Linux distribution. Please install texlive manually.")
            return
        
        # Run the installation command
        subprocess.run(cmd, shell=True, check=True)
        print("Installation completed successfully!")

    except Exception as e:
        print(f"Error during installation: {e}")

# Run the function
install_texlive()

