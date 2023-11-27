# 0x08 Networking Basics 2

This directory contains Bash scripts related to advanced networking topics. Below, you'll find a description of each script along with its requirements and usage instructions.

## Table of Contents

1. [Change Your Home IP](#change-your-home-ip)
2. [Show Attached IPs](#show-attached-ips)
3. [Port Listening on localhost](#port-listening-on-localhost)

---

## Change Your Home IP

### Mandatory

This Bash script is designed to configure an Ubuntu server with specific IP resolution requirements. Please make sure to read the following requirements before using the script:

**Requirements:**

- `localhost` should resolve to `127.0.0.2`.
- `facebook.com` should resolve to `8.8.8.8`.

**Note:** The checker is running on Docker, so ensure that you consider this while configuring the server.

---

## Show Attached IPs

### Mandatory

This Bash script is responsible for displaying all active IPv4 IPs on the machine where it's executed. It provides a straightforward way to view the IP addresses associated with the local system.

---

## Port Listening on localhost

### Advanced

This Bash script goes beyond the basics and involves setting up a port listener on port 98 for the localhost. This can be useful for various networking and testing purposes, such as checking for open ports or experimenting with network services.

---

Please refer to each script's individual documentation and comments within the script files for detailed usage instructions. Ensure that you have the necessary permissions and understand the implications of running these scripts on your system, especially those marked as "advanced."

**Note:** Always exercise caution when making network configuration changes or listening on ports, and only do so in environments where you have appropriate permissions and authorization.

Feel free to explore and use these scripts to expand your knowledge of networking basics and advanced concepts.
