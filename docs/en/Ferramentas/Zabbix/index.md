# Zabbix Installation Guide

## :octicons-book-24: 1. Introduction

This guide outlines the installation of **Zabbix**, an open-source monitoring tool to be used for collecting and analyzing metrics in the **br-lab** laboratory. Zabbix provides real-time monitoring of devices, servers, and applications, assisting in the identification and resolution of problems. The installation utilizes Docker Compose to provision services quickly and pre-configured, ensuring a practical and efficient implementation in the laboratory environment.

---

## :material-network-pos: 2. What is Zabbix?

**Zabbix** is an open-source monitoring platform that collects, processes, and displays performance metrics for servers, applications, and network devices. It offers an intuitive graphical interface, alert notifications, and reports to identify issues and help administrators proactively manage their infrastructures.

### Key components:
- **Zabbix Server**: Processes monitoring data, stores it in the database, and sends alerts.
- **Web Interface (Frontend)**: Allows the visualization, configuration, and analysis of metrics.
- **Zabbix Agent**: Collects metrics from the host where it is installed.
- **Database**: Stores historical data, configurations, and performance statistics.

---

## :octicons-checklist-24: 3. Prerequisites

Ensure that you meet the following prerequisites before installation:

1. **br-lab network configured**:
    - The **br-lab** network is required to isolate services in the environment. For more details on this configuration, consult the [**Getting Started: Preparing the Environment**](../Primeiros passos - preparando o ambiente.md) guide.

2. **Required Packages**:
    - `docker`, `docker-compose`, `curl`.

---

## :octicons-tools-24: 4. Preparing the Environment

To quickly initialize the Zabbix environment on the **br-lab** network, we will use Docker Compose with an automated script.

## :fontawesome-brands-docker: 5. Downloading Docker Compose

To download Docker Compose, execute the following command:

=== "Linux/ Mac"

    ```bash
        curl -L -o get.sh "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/Zabbix/get.sh?inline=false" && sh get.sh && cd Zabbix
    ```

=== "Windows"

    ```bash
        curl -L -o get.bat "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/Zabbix/get.bat?inline=false" && call get.bat && cd Zabbix
    ```

This command downloads the installation script and then navigates to the **Zabbix** directory.

---

## :octicons-container-24: 5. Starting the containers

To start the Zabbix services, use the command below:

```bash
docker compose up -d
```

This command will start the following containers:

1. **PostgreSQL**: Database that stores Zabbix metrics.
    - **IP**: `172.10.10.118`
    - **Access credentials**:
        - **User**: `zabbix`
        - **Password**: `zabbixdatabase`
    - **Default Port**: `5432` (exposed only within the **br-lab** network).

2. **Zabbix Server**: Main component that processes data and sends alerts.
    - **IP**: `172.10.10.115`
    - **Default Port**: `10051` (for connection with agents).
   - **Documentation**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>    

3. **Zabbix Frontend**: Web interface for configuration and visualization.
    - **IP**: `172.10.10.116`
    - **Default Port**: `880` (accessible externally).
   - **Documentation**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>
   
4. **Zabbix Agent**: Responsible for collecting metrics from the main host.
    - **IP**: `172.10.10.117`
    - **Default Port**: `10050`.
   - **Documentation**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>

To verify that all containers are running, use:

```bash
docker compose ps
```

## :fontawesome-solid-display: 6. Accessing the Zabbix Frontend

After the services are initialized, the Zabbix Web interface will be available at:

```bash
  http://<SERVER_IP>:880
```

### 6.1. Access Credentials

The default credentials for logging into the Zabbix Frontend are:

- **User**: `Admin`
- **Password**: `zabbix`

### 6.2. Changing the Default Password

For security reasons, change the administrator user password after the first login:

- Navigate to **Administration > Users**.
- Select the **Admin** user and click on **Change Password**.

## :octicons-rocket-24: 8. Next Steps

With the Zabbix environment configured, you can:

- Add custom templates for monitoring specific services.
- Integrate Zabbix with other automation and monitoring tools.

Consult the <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a> to explore more features and best practices.