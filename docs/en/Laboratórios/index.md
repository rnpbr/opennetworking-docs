# Containerlab

**Containerlab** is a powerful tool for creating and managing virtualized network labs. With it, you can simulate complex network topologies using Docker containers. Below, you will find information about the prerequisites, recommended tools, and how to document your labs.

---

## Prerequisites

Before you start using Containerlab, make sure you have the following prerequisites installed:

### Docker

- Docker is used by Containerlab to create and run the containers that make up the virtualized network.
- **Link**: [Official Docker Documentation](https://www.docker.com/get-started/).

### Containerlab

- Install Containerlab according to the instructions provided in the official documentation.
- **Link**: [Official Containerlab Documentation](https://containerlab.dev/install/).

---

## Available Labs

Here is an example of a lab configured to simulate OSPF using Junos:

### OSPF (Junos)

- Simulation of OSPF with Junos, one of the most used routing technologies.
- **Link**: [OSPF (Junos) Lab](ospf-lab/index.md).

### Discovery (Junos)

- Router importing with scripts, using Zabbix and Netbox.
- **Link**: [Discovery (Junos) Lab](discovery-lab/index.md).

---

## Recommended Analysis Tools

In addition to Containerlab, you can use the following analysis tools to monitor and debug your virtualized network:

### LibreNMS

- A web-based network monitoring platform that provides insights into network performance and health. Ideal for continuous real-time network monitoring.

### Wireshark

- Packet capture and analysis tool that allows you to examine network traffic in detail. Essential for debugging and network protocol analysis.

Besides these mentioned tools, there are others that can be configured according to your needs. To learn more, access: [Analysis Tools](../Ferramentas/index.md).

---

## Documenting Your Labs

To ensure that your labs are well-documented and easy to understand, refer to the **Lab Documentation** section. There, you will find best practices and examples for creating clear and useful documentation for your simulated environments.

- **Link**: [Lab Documentation](Contribua/index.md).