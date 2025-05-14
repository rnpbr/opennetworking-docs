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

### OSPF Routing (Junos)

- Simulation of OSPF with Junos, one of the most widely used routing technologies.
- **Link**: [OSPF Routing (Junos) Lab](Roteamento-OSPF/index.md).

### Discovery (Junos)

- Importing routers with scripts, using Zabbix and Netbox.
- **Link**: [Discovery (Junos) Lab](Descoberta/index.md).

### ELK Monitoring (Junos)
- Exporting IPFIX flows to Elasticsearch with Elastic Agent.
- Real-time flow visualization with dashboards in Kibana.
- **Link**: [ELK Monitoring (Junos)](Monitoramento-ELK/index.md).

### Telegraf Monitoring (junos)
- Exporting traffic flows via Telegraf/IPFIX to InfluxDB.
- Ready-made dashboards in Grafana for traffic analysis by interface and protocol.
- **Link**: [Telegraf Monitoring (Junos)](Monitoramento-Telegraf/index.md).

### Zabbix Monitoring (junos)
- Monitoring routers via SNMP with centralized collection by the Zabbix Server.
- Allows visualization of metrics and real-time alerts in the Zabbix frontend.
- **Link**: [Zabbix Monitoring (Junos)](Monitoramento-Zabbix/index.md).
---

## Recommended Analysis Tools

In addition to Containerlab, you can use the following analysis tools to monitor and debug your virtualized network:

### LibreNMS

- A web-based network monitoring platform that provides insights into network performance and health. Ideal for continuous real-time network monitoring.

### Wireshark

- Packet capture and analysis tool that allows you to examine network traffic in detail. Essential for debugging and analyzing network protocols.

Besides these mentioned tools there are others that can be configured according to your needs, to learn more access: [Analysis Tools](../Ferramentas/index.md).

---

## Documenting Your Labs

To ensure your labs are well documented and easy to understand, refer to the section on **Lab Documentation**. There, you will find best practices and examples for creating clear and useful documentation for your simulated environments.

- **Link**: [Lab Documentation](Contribua/index.md).