Okay, here's the English translation of the provided ELK installation guide, keeping the structure and content consistent:

# ELK (Elasticsearch) Installation Guide

## :octicons-book-24: 1. Introduction

In this guide, we will cover the setup of the **ELK** stack (Elasticsearch, Logstash, and Kibana) for data monitoring and analysis in laboratory environments. ELK is a powerful combination of tools that allows for the collection, storage, analysis, and visualization of data in real-time, being widely used for log management and systems monitoring.

## :simple-elastic: 2. What is ELK?

![Flow_Fleet_Elasticsearch.png](../../../img/tools_imgs/flow_fleet_elasticsearch.png)
Source: [Elastic Documentation](https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html)

The image above illustrates the data flow and integration of ELK Stack components for centralized monitoring and real-time analysis.

- **Elasticsearch**: Responsible for storing and indexing data received from the Fleet Server. With real-time search and analysis capabilities, Elasticsearch is the core of the ELK Stack, enabling efficient queries across large volumes of data and facilitating detailed analysis.

- **Kibana**: Kibana offers a graphical interface where data in Elasticsearch can be visualized and analyzed. Kibana also manages the packages and integrations available for agents, which can be loaded from the Package Registry. With it, you can create dashboards, reports, and graphs, transforming raw data into visual insights.

- **Elastic Agent**: Located on the devices to be monitored, Elastic Agents collect log data, metrics, and events and send them to the Fleet Server Cluster. These agents are configured and managed by policies that control what data is collected and where it is sent.

- **Fleet Server Cluster**: Utilizing a load balancer for high availability, the Fleet Server Cluster centralizes the management of Elastic Agents. It distributes policies to agents, ensuring consistent data collection, and then forwards them to Elasticsearch for storage and analysis.

This flow ensures that network data is collected in a unified manner, stored optimally, and made available for visualization and analysis, offering a complete and robust solution for monitoring and analyzing complex and distributed networks.

!!! warning "Note"
    In this installation, we will not use **Logstash**, but rather the more modern data collection approach, which are **Fleet Server** and **Fleet Agent**.
    To learn more, access the official Fleet documentation: <a href="https://www.elastic.co/guide/en/fleet/current/fleet-overview.html" target="_blank">Elastic Documentation - Fleet</a>

---

## :octicons-checklist-24: 4. Prerequisites

Before proceeding with the ELK configuration, it is necessary to configure the **br-lab** network. For details on this configuration, consult the guide [**First Steps: Preparing the Environment**](../Primeiros passos - preparando o ambiente.md).

---

## :octicons-tools-24: 5. Preparing the Environment

After ensuring that the **br-lab** network is configured, follow the steps below to prepare the working environment.

## :fontawesome-brands-docker: 6. Downloading Docker Compose

To download Docker Compose, execute the following command:

=== "Linux/ Mac"

    ```bash
        curl -L -o get.sh "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/ELK-Stack/get.sh?inline=false" && sh get.sh && cd ELK-Stack
    ```

=== "Windows"
```bash
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/ELK-Stack/get.bat?inline=false" && call get.bat && cd ELK-Stack
```

This command downloads the installation script and then navigates to the **ELK-Stack** directory.

## :octicons-container-24: 7. Starting the Containers

After downloading Docker Compose, execute the command below to start the ELK services:

```bash
docker compose up -d
```

This command will start three essential containers for the ELK stack to function:

1. **Elasticsearch**
    - **Description**: Search engine and data storage. It allows storing documents in JSON format and provides a RESTful API for searching and analyzing. Ideal for searching large volumes of data.
    - **IP**: `172.10.10.201`
    - **Default Port**: `9200`
    - **Documentation**: <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html" target="_blanck">Elasticsearch Documentation</a>
2. **Kibana**
    - **Description**: Graphical interface for visualizing data stored in Elasticsearch. Kibana allows users to create interactive dashboards and real-time data visualizations, facilitating data analysis and interpretation.
    - **IP**: `172.10.10.202`
    - **Default Port**: `5601`
    - **Documentation**: <a href="https://www.elastic.co/guide/en/kibana/current/index.html" target="_blanck">Kibana Documentation</a>
3. **Fleet Server**
    - **Description**: Agent responsible for collecting metrics and logs from different sources and sending them to Elasticsearch. The Fleet Server facilitates the centralized management of collection agents, such as the Elastic Agent, enabling efficient data collection and delivery.
    - **IP**: `172.10.10.203`
    - **Documentation**: <a href="https://www.elastic.co/guide/en/fleet/current/index.html" target="_blanck">Fleet Server Documentation</a>
!!! info "Access"
    :material-access-point: Default username and password
    - **Default Username**: `elastic`
    - **Default Password**: `admin@123`

!!! tip "Configuration"
    To change the password or the Elasticsearch version, edit the **.env** file.

## :simple-kibana: 8. Accessing the Kibana Interface

To access the Kibana interface, use the following link:

```
https://<your-ip>:5601
```

Log in with the default username and password.

## :material-skip-next-outline: Next Steps

- **Configure IPFIX Collection**: After configuring ELK, the next step will be to configure data collection using IPFIX, with our [IPFIX configuration guide](Configurando IPFIX no ELK.md).