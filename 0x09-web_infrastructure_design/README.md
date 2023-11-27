# Web Infrastructure Design

This directory contains a series of whiteboard exercises where we'll be designing web infrastructures for the website www.foobar.com, each with increasing complexity and security considerations. These exercises are intended to enhance your understanding of web infrastructure design concepts and their real-world applications.

## 0. Simple Web Stack

### Overview

In this exercise, we will design a basic web infrastructure using a single server to host www.foobar.com. The infrastructure includes a web server, an application server, a MySQL database, and a domain name configuration. 

### Requirements

- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application code base
- 1 database (MySQL)
- 1 domain name (foobar.com) configured with a www record pointing to server IP (e.g., 8.8.8.8)

### Key Concepts

- **Server**: The hardware or virtual machine that hosts our web infrastructure.
- **Domain Name**: A human-readable address (www.foobar.com) that translates to an IP address, allowing users to access the website.
- **DNS Record**: The www in www.foobar.com is a DNS record that specifies the subdomain for the website.
- **Web Server (Nginx)**: Responsible for handling HTTP requests and serving static content.
- **Application Server**: Executes dynamic content and communicates with the database.
- **Database (MySQL)**: Stores website data like user information, articles, and more.
- **User Communication**: The server communicates with the user's computer through HTTP requests and responses.

### Issues

- **Single Point of Failure (SPOF)**: If the server goes down, the website becomes unavailable.
- **Downtime During Maintenance**: Deploying new code requires restarting the web server, causing downtime.
- **Limited Scalability**: Unable to handle high traffic volumes without additional servers.

## 1. Distributed Web Infrastructure

### Overview

This exercise involves designing a more robust infrastructure for www.foobar.com, using three servers for improved redundancy and scalability.

### Requirements

- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load balancer (HAproxy)
- 1 set of application code base
- 1 database (MySQL)

### Key Concepts

- **Redundancy**: Multiple servers provide failover in case one server fails.
- **Load Balancer (HAproxy)**: Distributes incoming traffic across multiple application servers for load balancing.
- **Distribution Algorithm**: The load balancer uses a distribution algorithm to decide how to route traffic.
- **Active-Active vs. Active-Passive**: Understanding the difference between these configurations for redundancy.
- **Database Primary-Replica (Master-Slave)**: A setup where the primary database replicates data to replica databases.
- **Primary vs. Replica**: The roles and responsibilities of the primary and replica database nodes in the application.

### Issues

- **Single Points of Failure (SPOF)**: Identifying potential SPOFs in the new infrastructure.
- **Security**: Lacking a firewall and HTTPS can expose the infrastructure to security risks.
- **Monitoring**: Absence of monitoring for system health and performance.

## 2. Secured and Monitored Web Infrastructure

### Overview

In this exercise, we take the distributed infrastructure from the previous step and add security measures and monitoring.

### Requirements

- 3 firewalls
- 1 SSL certificate for HTTPS
- 3 monitoring clients
- Secure encrypted traffic and monitoring for the infrastructure.

### Key Concepts

- **Firewalls**: Protective barriers that control incoming and outgoing network traffic.
- **HTTPS**: Secure, encrypted communication protocol for website traffic.
- **Monitoring**: Continuous tracking of system performance and health for proactive issue detection.
- **Data Collection**: How monitoring tools collect data for analysis.
- **Web Server QPS (Queries Per Second)**: Measuring and monitoring web server request rates.

### Issues

- **SSL Termination**: Discussing the challenges of terminating SSL at the load balancer level.
- **Single MySQL Write Server**: Risks associated with having only one MySQL server capable of accepting writes.
- **Uniform Server Components**: Potential issues in having servers with identical components.

Please ensure that all explanations are provided in English to enhance your technical understanding in various settings. These exercises aim to develop your knowledge and skills in web infrastructure design.
