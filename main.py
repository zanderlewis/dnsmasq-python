import subprocess
import platform
import sys


class OSError(Exception):
    """Exception raised for errors in the input operating system.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Unsupported operating system"):
        self.message = message
        super().__init__(self.message)


class TLDError(Exception):
    """Exception raised for errors in the input operating system.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self, message="Invalid top-level domain. Please use test, local, or localhost."
    ):
        self.message = message
        super().__init__(self.message)


tlds = ["test", "local", "localhost"]

domain = input("Enter the domain you want to use (e.g. myapp): ")

tld = input(
    "Enter the top-level domain you want to use (test, local, or localhost): "
).lower()

if not tld in tlds:
    raise TLDError()

ip = input("Enter the IP address you want to use (e.g. 8000): ")

os_type = platform.system()
if os_type == "Linux":
    system = "Linux"
elif os_type == "Darwin":  # macOS
    system = "macOS"
elif os_type == "Windows":
    print(
        "dnsmasq is not typically used on Windows. Consider using WSL for a Linux environment."
    )
    sys.exit(1)
else:
    raise OSError(f"Unsupported operating system: {os_type}")


def install_dnsmasq():
    """
    Installs dnsmasq on the current operating system.
    """
    try:
        if system == "Linux":
            subprocess.run(["sudo", "apt-get", "install", "-y", "dnsmasq"], check=True)
        elif system == "macOS":
            subprocess.run(["brew", "install", "dnsmasq"], check=True)
    except subprocess.CalledProcessError:
        print(
            "Failed to install dnsmasq. Please check your permissions or install manually."
        )
        sys.exit(1)


def configure_dnsmasq():
    """
    Configures dnsmasq on Linux by appending a DNS address to the dnsmasq configuration file.
    """
    config = f"address=/{domain}.{tld}/127.0.0.1:{ip}\n"
    if system == "Linux":
        config_path = "/etc/dnsmasq.conf"
    elif system == "macOS":
        config_path = "/usr/local/etc/dnsmasq.conf"
    print(f"Configuring dnsmasq in {config_path}...")
    try:
        with open(config_path, "a") as file:
            if config not in file.read():
                file.write(config)
    except IOError:
        print(
            f"Failed to open {config_path}. Please check your permissions or configure manually."
        )
        sys.exit(1)


def start_dnsmasq():
    """
    Starts the dnsmasq service on Linux using the systemctl command.
    """
    print("Starting dnsmasq...")
    try:
        if system == "Linux":
            subprocess.run(["sudo", "systemctl", "start", "dnsmasq"], check=True)
        elif system == "macOS":
            subprocess.run(["sudo", "brew", "services", "start", "dnsmasq"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to start dnsmasq. Please check your permissions")
        sys.exit(1)


install_dnsmasq()
configure_dnsmasq()
start_dnsmasq()
print("dnsmasq setup complete.")
