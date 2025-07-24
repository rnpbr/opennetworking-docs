# Configuring IPFIX on ELK

## :octicons-book-24: Introduction

IPFIX (Internet Protocol Flow Information Export) is a standard for exporting network flow information, which allows you to monitor and analyze traffic in real time. This guide is aimed at configuring IPFIX in the ELK stack (Elasticsearch, Logstash, Kibana). Before you begin, make sure you have the following prerequisites:

- **ELK Stack Installation**: See the "Getting Started" guide to install ELK.
- **Fleet Access**: Make sure Fleet is configured in your ELK environment.


## :material-cursor-default-click: 1. Access the Fleet Sub-tab of Management

### What are Fleet Server and Fleet Agent?

- **Fleet Server**: A component that manages the configuration and communication between agents and the ELK server. It allows centralized agent management.
- **Fleet Agent**: A tool that collects data from systems and sends it to the ELK server, facilitating data analysis and monitoring.

!!! tip "More Information"
    For more information, access the official Fleet Server documentation: <a href="https://www.elastic.co/guide/en/fleet/current/fleet-server.html" target="_blank">Elastic Documentation - Fleet</a>

## :material-tools: 2. Modifying the Fleet Policy

### What are Fleet Server Policies?

Fleet Server policies define how agents behave, which integrations are applied, and what data should be collected. These policies are essential for customizing data collection according to the needs of your environment.

!!! tip "More Information"
    For more information, access the official Fleet policies documentation: <a href="https://www.elastic.co/guide/en/fleet/current/agent-policy.html" target="_blank">Elastic Documentation - Policies</a>

## :material-cursor-default-click: 3. Access the Fleet Server Policy

1. In the **Agent Policy** column, click on the policy called **Fleet Server Policy**.
2. In this tab, you will see a list of integrations available for the agent.

### What are Integrations?

Integrations are packages that define how to collect data from different sources. They facilitate agent configuration, allowing you to add features and functionalities as needed.

!!! tip "More Information"
    For more information, access the official Integrations documentation: <a href="https://www.elastic.co/guide/en/fleet/current/integrations.html" target="_blank">Elastic Documentation - Integrations</a>

## :octicons-plus-16: 4. Adding the NetFlow Integration

1. Click on **Add Integration** and search for **NetFlow**.
2. Select the **NetFlow Records** option.

### :material-text-box: Integration Summary

After selecting the integration, a short summary explaining what this integration does will be displayed. Click on **Add NetFlow Records** to proceed.


## :octicons-gear-24: 5. Integration Configuration

In the configuration tab, you will see the following options:

- **Listen IP**: The IP address where the agent will listen for IPFIX packets.
- **Reception Portal**: The portal on which data will be received.

!!! warning "Note"
    You do not need to modify these settings, as they are set to work with the default configuration. For more information, access the official documentation: <a href="https://www.elastic.co/docs/current/integrations/netflow" target="_blank">Elastic Documentation - NetFlow Integrations</a>


## :octicons-check-16: 6. Finalizing the Configuration

1. Click on **Save and Continue**.
2. Then, click on **Save and Deploy Changes** to apply the changes.