# Project: 0x0F-load_balancer

## Overview

This project involves setting up a load balancer using HAproxy and configuring two web servers (web-01 and web-02) to handle HTTP requests behind the load balancer. The primary goal is to distribute incoming traffic evenly between the two web servers using the round-robin algorithm. Additionally, a custom Nginx response header, named X-Served-By, must be added to help track which web server is handling the HTTP requests.

## Tasks

### 1. Double the number of webservers

In this task, the focus is on configuring web-02 to be identical to web-01. A Bash script named `0-custom_http_response_header` will be created to automate the configuration process. The script will ensure that Nginx on both web servers includes a custom HTTP response header (X-Served-By) containing the hostname of the server.

#### Requirements:

- Configure Nginx on web-01 and web-02 to include a custom HTTP header (X-Served-By).
- The custom header's name must be `X-Served-By`.
- The value of the custom header must be the hostname of the server running Nginx.
- Write a Bash script (`0-custom_http_response_header`) to configure a new Ubuntu machine to meet the specified requirements.
- Ignore SC2154 for shellcheck.

### 2. Install your load balancer

This task involves the installation and configuration of HAproxy on the lb-01 server. The load balancer should distribute traffic using the round-robin algorithm across web-01 and web-02.

#### Requirements:

- Install and configure HAproxy on lb-01.
- Configure HAproxy to send traffic to web-01 and web-02.
- Distribute requests using a round-robin algorithm.
- Ensure HAproxy can be managed via an init script.
- Make sure the servers (web-01 and web-02) have the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. Follow the provided tutorial if needed.
- Write a Bash script for configuring a new Ubuntu machine to meet the specified requirements.

## Instructions

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/0x0F-load_balancer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x0F-load_balancer
   ```

3. Follow the instructions for each task mentioned in the corresponding subdirectories (`1-web_server` and `2-haproxy`).

4. Execute the provided scripts to automate the configuration process.

## Notes

- Ensure that you have the necessary permissions to execute the scripts.
- Refer to the individual task directories for detailed instructions and additional resources.

Good luck with your load balancer project!
