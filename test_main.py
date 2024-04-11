import unittest
from main import configure_dnsmasq

class TestConfigureDnsmasq(unittest.TestCase):
    def test_linux_configuration(self):
        # Test Linux configuration
        domain = "example"
        tld = "com"
        ip = "192.168.0.1"
        system = "Linux"
        expected_config_path = "/etc/dnsmasq.conf"
        expected_config = f"address=/{domain}.{tld}/127.0.0.1:{ip}\n"

        # Call the function
        configure_dnsmasq(domain, tld, ip, system)

        # Assert the configuration file is updated correctly
        with open(expected_config_path, "r") as file:
            config_content = file.read()
            self.assertIn(expected_config, config_content)

    def test_macos_configuration(self):
        # Test macOS configuration
        domain = "example"
        tld = "com"
        ip = "192.168.0.1"
        system = "macOS"
        expected_config_path = "/usr/local/etc/dnsmasq.conf"
        expected_config = f"address=/{domain}.{tld}/127.0.0.1:{ip}\n"

        # Call the function
        configure_dnsmasq(domain, tld, ip, system)

        # Assert the configuration file is updated correctly
        with open(expected_config_path, "r") as file:
            config_content = file.read()
            self.assertIn(expected_config, config_content)

if __name__ == "__main__":
    unittest.main()