# 0x10-https_ssl

## 0. World Wide Web

### Mandatory

#### Configure Domain Zone and Subdomains

**Score: 0.0% (Checks completed: 0.0%)**

Configure your domain zone to meet the following requirements:

1. Add the subdomain www to your domain and point it to your lb-01 IP.
2. Add the subdomain lb-01 to your domain and point it to your lb-01 IP.
3. Add the subdomain web-01 to your domain and point it to your web-01 IP.
4. Add the subdomain web-02 to your domain and point it to your web-02 IP.

Additionally, create a Bash script that accepts two arguments:

- `domain` (mandatory): The domain name to audit.
- `subdomain` (optional): The specific subdomain to audit.

**Bash Script Requirements:**

- The script must display information about subdomains.
- Output format: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`.
- When only the `domain` parameter is provided, display information for subdomains www, lb-01, web-01, and web-02 in that order.
- When passing both `domain` and `subdomain` parameters, display information for the specified subdomain.
- Ignore shellcheck case SC2086.
- Must use `awk`.
- Include at least one Bash function.

**Note:** You do not need to handle edge cases such as empty parameters or nonexistent domain names/subdomains.

## 1. HAproxy SSL Termination

### Mandatory

#### Terminate SSL on HAproxy

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for the subdomain www.

**Requirements:**

1. HAproxy must listen on port TCP 443.
2. HAproxy must accept SSL traffic.
3. HAproxy must serve encrypted traffic that returns the root (/) of your web server.
4. When querying the root of your domain name, the page returned must contain "Holberton School."

**Configuration:**

- Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`).
- The file `1-haproxy_ssl_termination` must be your HAproxy configuration file.

**Additional Notes:**

- Make sure to install HAproxy 1.5 or higher, as SSL termination is not available before v1.5.
- Remove occurrences of "Score: 0.0% (Checks completed: 0.0%)" from your submission.
