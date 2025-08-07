# Containerlab

**Containerlab** is a powerful tool for creating and managing virtualized network labs. With it, you can simulate complex network topologies using Docker containers. Below, you will find information about the prerequisites, recommended tools, and how to document your labs.

---

## Prerequisites

Before you start using Containerlab, make sure you have the following prerequisites installed:

### Docker

- Docker is used by Containerlab to create and run the containers that make up the virtualized network.
- **Link**: [Docker official documentation](https://www.docker.com/get-started/).

### Containerlab

- Install Containerlab according to the instructions provided in the official documentation.
- **Link**: [Containerlab official documentation](https://containerlab.dev/install/).

---

## Available Labs

Here is an example of a lab configured to simulate OSPF using Junos:

### OSPF Routing (Junos)

- OSPF simulation with Junos, one of the most used routing technologies.
- **Link**: [OSPF Routing (Junos) Lab](Juniper/vMX/Roteamento-OSPF/index.md).

### Discovery (Junos)

- Importing routers with scripts, using Zabbix and Netbox.
- **Link**: [Discovery (Junos) Lab](Juniper/vJunos/Descoberta/index.md).

### ELK Monitoring (Junos)

- Exporting IPFIX flows to Elasticsearch with Elastic Agent.
- Real-time flow visualization with dashboards in Kibana.
- **Link**: [ELK Monitoring (Junos)](Juniper/vJunos/Monitoramento-ELK/index.md).

### Telegraf Monitoring (Junos)
- Exporting traffic flows via Telegraf/IPFIX to InfluxDB.
- Ready-made dashboards in Grafana for traffic analysis by interface and protocol.
- **Link**: [Telegraf Monitoring (Junos)](Juniper/vJunos/Monitoramento-Telegraf/index.md).

### Zabbix Monitoring (Junos)
- Monitoring routers via SNMP with centralized collection by the Zabbix Server.
- Allows viewing metrics and alerts in real-time on the Zabbix frontend.
- **Link**: [Zabbix Monitoring (Junos)](Juniper/vJunos/Monitoramento-Zabbix/index.md).

---

## Recommended Analysis Tools

In addition to Containerlab, you can use the following analysis tools to monitor and debug your virtualized network:

### LibreNMS

- A web-based network monitoring platform that provides insights into network performance and health. Ideal for continuous real-time network monitoring.

### Wireshark

- Packet capture and analysis tool that allows you to examine network traffic in detail. Essential for debugging and analyzing network protocols.

Besides these mentioned tools, there are others that can be configured according to your needs, to know more access: [Analysis Tools](../Ferramentas/index.md).

---

## Documenting Your Labs

To ensure that your labs are well-documented and easy to understand, see the section on **Lab Documentation**. There, you will find best practices and examples for creating clear and useful documentation for your simulated environments.

- **Link**: [Lab Documentation](Contribua/index.md).