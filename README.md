# dPIR: dnsmasq Python Installer and Runner

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

dPIR is a Python-based utility that simplifies the installation, configuration, and running of dnsmasq. It's designed to help developers quickly set up `.test` domains for local development environments.

> [!IMPORTANT]\
> dnsmasq is not typically used on Windows. Consider using WSL for a Linux environment.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated installation of dnsmasq on Linux and macOS.
- Configuration of `.test`, `.local`, and `.localhost` domains.
- Starting dnsmasq service.

## Requirements

- Python 2 or 3.
- For macOS users: [Homebrew](https://brew.sh/)
- For Linux users: `apt-get`

## Installation

1. Clone this repository or download `main.py`.
2. Ensure you have the necessary system requirements: Python, and either Homebrew (macOS) or `apt-get` (Linux).

## Usage

Run the script using Python:

```bash
python main.py  # Python 2
# or
python3 main.py  # Python 3
```

Follow the prompts to enter your desired domain name and IP adress.

## Contributing

We welcome contributions to dPIR! If you'd like to contribute, follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes, ensuring they are well-tested.
4. Submit a pull request, detailing your changes and their benifits.
5. Adhere to the project's coding style and conventions.
6. Be respectful and considerate of other contributors. Everyone must be treated equally.

## License

dPIR is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.
