# Network Scanner

## Overview
This network scanning tool is a Python-based utility that leverages the Scapy library to detect devices on a network. Designed for network administrators and cybersecurity enthusiasts, it simplifies the task of identifying devices connected to a LAN. The tool scans the specified IP range, extracts MAC addresses, and optionally retrieves the vendor information for each detected device.

## Features
- **IP Range Scanning**: Users can specify an IP range to scan for connected devices.
- **MAC Address Detection**: The tool captures the MAC addresses of all devices within the specified range.
- **Vendor Information Retrieval**: Incorporates an API call to `macvendors.com` to fetch vendor details for each MAC address.

## Getting Started

To begin using the network scanner, you'll need to clone the repository to your local machine.

```sh
git clone https://github.com/SAMi-Rn/Network_Scanner.git
cd Network_Scanner
```
## Installation
Before running the scanner, ensure you have Python installed on your system, along with the following dependencies:
- Scapy
- Requests

You can install the necessary libraries using pip:

```sh
pip install scapy requests
```
## Usage
To use the network scanner, run the script from the command line with the desired IP range:
```sh
python network_scanner.py -t <target_ip_range>
```
### Arguments
`-t` or `--target`: Target IP or IP range to scan (e.g., `192.168.1.1/24`).

## How It Works
The script performs the following steps:

1. Sends an ARP request over the network to the specified IP range.
2. Captures the ARP responses to identify active devices.
3. Extracts the IP and MAC addresses from the responses.
4. Queries an external API for vendor information based on the MAC addresses.
5. Prints a summary of all detected devices along with their IP addresses, MAC addresses, and vendor names.

## Example Output
```sh
IP Address          MAC Address                        Vendor
---------------------------------------------------
192.168.1.1         aa:bb:cc:dd:ee:ff                  ExampleCorp
192.168.1.2         ff:ee:dd:cc:bb:aa                  DeviceMaker Inc.
```
## Troubleshooting
Ensure that you have the proper permissions to execute network scans and that your firewall settings allow for ARP requests to be broadcasted and responses to be received.

## Disclaimer
This tool is intended for educational purposes and should be used only on networks where you have authorization to perform network scans.
