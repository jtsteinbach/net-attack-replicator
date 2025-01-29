# Network Attack Replicator

![GitHub](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)

The **Network Attack Replicator** is a Python script designed to replicate network attacks captured in `.pcap` files to a specified destination IP address and port. This tool is intended for educational, testing, and research purposes to help security professionals understand and analyze network attack patterns.

## Features

- **PCAP File Parsing**: Reads and parses `.pcap` files containing network attack traffic.
- **Attack Replication**: Replicates the attack traffic to a specified destination IP and port.
- **Customizable**: Allows customization of the destination IP, port, and other parameters.
- **Supports Common Protocols**: Works with TCP, UDP, and other common network protocols.

## Prerequisites

- Python 3.7 or higher
- `scapy` library (`pip install scapy`)

## Usage

```bash
python network_attack_replicator.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Always ensure you have proper authorization before using this tool in any network environment. Unauthorized use of this tool may violate laws and regulations.
