# Containerlab

**Containerlab** is a powerful tool for creating and managing virtualized network labs. With it, you can simulate complex network topologies using Docker containers. Below, you will find information about prerequisites, recommended tools, and how to document your labs.

---

## Prerequisites

Before you start using Containerlab, make sure you have the following prerequisites installed:

### Docker

- Docker is used by Containerlab to create and run the containers that make up the virtualized network.
- **Link**: [Official Docker documentation](https://www.docker.com/get-started/).

### Containerlab

- Install Containerlab according to the instructions provided in the official documentation.
- **Link**: [Official Containerlab documentation](https://containerlab.dev/install/).

---

## Available Labs

Here is an example of a lab configured to simulate OSPF using Junos:

### OSPF Routing (Junos)

- OSPF simulation with Junos, one of the most used routing technologies.
- **Link**: [OSPF Routing (Junos) Lab](Juniper/VMX/Roteamento-OSPF/index.md).

### Discovery (Junos)

- Importing routers with scripts, using Zabbix and Netbox.
- **Link**: [Discovery (Junos) Lab](Juniper/Vjunos/Descoberta/index.md).

### ELK Monitoring (Junos)
- Exporting IPFIX flows to Elasticsearch with Elastic Agent.
- Viewing flows in real-time with dashboards in Kibana.
- **Link**: [ELK Monitoring (Junos)](Juniper/Vjunos/Monitoramento-ELK/index.md).

### Telegraf Monitoring (Junos)
- Exporting traffic flows via Telegraf/IPFIX to InfluxDB.
- Ready-made dashboards in Grafana for traffic analysis by interface and protocol.
- **Link**: [Telegraf Monitoring (Junos)](Juniper/Vjunos/Monitoramento-Telegraf/index.md).

### Zabbix Monitoring (Junos)
- Monitoring routers via SNMP with centralized collection by the Zabbix Server.
- Allows viewing metrics and alerts in real-time in the Zabbix frontend.
- **Link**: [Zabbix Monitoring (Junos)](Juniper/Vjunos/Monitoramento-Zabbix/index.md).
---

## Recommended Analysis Tools

In addition to Containerlab, you can use the following analysis tools to monitor and debug your virtualized network:

### LibreNMS

- A web-based network monitoring platform that provides insights into network performance and health. Ideal for continuous real-time network monitoring.

### Wireshark

- Packet capture and analysis tool that allows you to examine network traffic in detail. Essential for debugging and analyzing network protocols.

Besides these tools mentioned there are others that can be configured according to your needs, to know more access: [Analysis Tools](../Ferramentas/index.md).

---

## Documenting Your Labs

To ensure that your labs are well documented and easy to understand, refer to the section on **Lab Documentation**. There, you will find best practices and examples for creating clear and useful documentation for your simulated environments.

- **Link**: [Lab Documentation](Contribua/index.md).