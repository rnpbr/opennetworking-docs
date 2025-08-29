# :material-bookmark: Multivendor Logs Telegraf

This lab simulates, via Containerlab, the interconnection between three Juniper, Huawei, and Cisco routers, with dynamic routing via OSPF, log exporting via Syslog using Telegraf, InfluxDB, Chronograf, and Grafana.

---

## :material-bookmark: 1. Description

### :octicons-goal-16: 1.1 Lab Objective

The objective of the lab is to simulate the export of logs from three routers from different manufacturers (Juniper, Huawei, and Cisco) to a centralized monitoring server, using the Syslog protocol. The monitoring system is composed of Telegraf, InfluxDB, Chronograf, and Grafana, allowing the collection, storage, and visualization of network metrics in real time.

### :material-lan: 1.2 Lab Topology

![Lab Topology](../../../../../../../img/labs_imgs/Topologia_Logs_Telegraf.svg)

**Topology Description**

*   Three routers (Juniper, Cisco, Huawei) interconnected in a linear topology with point-to-point /31 links.
*   Dynamic routing via OSPF between the routers.
*   Log collection via Syslog udp (514).
*   Observability with the TICK stack (Telegraf, InfluxDB, Chronograf) and Grafana.
*   External network `br-lab` connects the nodes to the monitoring infrastructure.

---

## :octicons-search-16: 2. Applications

### Application Examples

This lab can be explored in various academic and applied research scenarios, serving as a basis for experimentation in monitoring and visualizing traffic in networks with multiple routers.

#### Possible Applications:

*   **NOC team training in a multivendor environment**: Simulates real operations with Juniper, Huawei, and Cisco routers, using OSPF and log exporting via Syslog, allowing connectivity analysis and troubleshooting.
*   **Validation and testing of log collection via Syslog**: Allows verification of the compatibility and behavior of different vendors in sending logs to Telegraf.
*   **Real-time metrics visualization and analysis**: Validate and test ways to grafana templates to work with logs.
*   **Centralized monitoring with Telegraf**: Evaluates Telegraf's ability to receive and process logs from heterogeneous devices, ensuring data integrity and consistency.
*   **Teaching monitoring system integration**: Provides practical learning on Syslog configuration, metric collection, and visualization in TICK and Grafana stacks in a multivendor scenario.

---

## :material-tools: 3. Requirements

Below are the minimum hardware and software requirements needed to run the lab. Be sure to include essential tools such as **Containerlab** and **Docker**, in addition to the previously created `br-lab` network.
To learn more about these items, access:

- [br-lab Network Creation](../../../../Ferramentas/Primeiros passos - preparando o ambiente.md)
- <a target="_blank" href="https://www.docker.com/get-started/">Docker Installation</a>
- <a target="_blank" href="https://containerlab.dev/install/">Containerlab Installation</a>

And have the telegraf stack previously installed, to learn more about zabbix installation access: [Telegraf Installation](../../../../Ferramentas/Telegraf/index.md)

### :material-alert: Minimum Requirements Table:

| Requirement           | Details                       |
| --------------------- | ----------------------------- |
| **CPUs**              | 4 vCPUs                       |
| **RAM Memory**        | 8 GB                          |
| **Disk Space**        | 10 GB (recommended)           |
| **Containerlab**      | 0.45.0 or higher              |
| **Docker Engine**     | 23.0.3 or higher              |
| **Images**            | `vr-vjunos:23.2R1.14`, `vrnetlab/huawei_vrp:ne40e-8.180`, `xrd-control-plane:7.10.2` |
| **Docker Network**    | `br-lab`                      |

!!! warning "Attention"
    Check if your processor has **hardware virtualization support** and if this feature is **enabled in the BIOS/UEFI**.
    - In **Intel** processors, this technology is called **VT-x** (Intel Virtualization Technology).
    - In **AMD** processors, it is known as **AMD-V** (AMD Virtualization).

    Without this feature enabled, images such as **vJunos-router** will not work correctly.

---

## :fontawesome-solid-prescription-bottle: 4. Deploying the Lab

You can perform the deployment using a ready-made script or manually configure the lab files.

### :material-git: 4.1 Ready Deployment

This method allows the user to **download a pre-assembled version** of the laboratory, with the topology and configurations already defined. Simply download the repository and proceed to the start of execution.

!!! tip "Tip"
    Ready deployment is useful for those who want to get started quickly with a configured environment.

#### :octicons-download-16: Downloading the Lab

Execute the script below to download and configure the lab automatically:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/logs-telegraf-multvendor/get.sh" && sh get.sh && cd logs-telegraf-multvendor
    ```

=== "Windows"

    ```bat
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/logs-telegraf-multvendor/get.bat" && call get.bat && cd logs-telegraf-multvendor
    ```

!!! tip "Tip"
    In Linux/Mac, use `chmod +x get.sh` before running the script if it does not have execute permission.

---

## :octicons-play-16: 5. Initializing the Lab

After downloading or customizing, follow the steps below to **start the lab**.
Run the command below inside the downloaded directory.

```bash
sudo containerlab deploy
```

This command will create the router containers, configure the links, and start the monitoring services.

!!! tip "Debugging"
    Use `docker logs -f <container_name>` to check the status of the services if something doesn't work.

---

## :material-access-point: 6. Accessing the Devices

### :material-table: 6.1 Service IPs and Ports

| Device          | Access IP      | Port(s) | Service             |
| --------------- | -------------- |-------| ------------------- |
| **node1**       | 172.10.10.201  | 22    | SSH                 |
| **node2**       | 172.10.10.202  | 22    | SSH                 |
| **node3**       | 172.10.10.203  | 22    | SSH                 |
| **Telegraf**    | 172.10.10.114  | 161   | Metric Collection   |
| **InfluxDB**    | 172.10.10.112  | 8086  | Time Series Database|
| **Chronograf**  | 172.10.10.113  | 8888  | Analysis UI         |
| **Grafana**     | 172.10.10.111  | 3000  | Web Dashboard       |
| **Graphite**    | 172.10.10.119  | 8080  | Web UI (Graphite)   |

### :material-key-link: 6.2 Access Passwords

| Service          | User    | Password          |
| ---------------- | ------- | ----------------- |
| **node1 (SSH)**  | `admin` | `admin@123`       |
| **node2 (SSH)**  | `clab`  | `clab@123`        |
| **node3 (SSH)**  | `admin` | `admin`           |
| Grafana          | `admin` | `admin`           |
| InfluxDB         | `admin` | `influxpassword`  |

!!! warning "Startup Verification"
    Before accessing the services, use `docker ps` and check the containers' logs to ensure they are working correctly.

---

## :octicons-browser-16: 7. Observability and Visualization

### 7.1 Telegraf

Telegraf is configured to collect metrics via:

*   **syslog**: log exporting
*   **IPFIX**: traffic flow exporting.

### 7.2 InfluxDB

Time series database where Telegraf's metrics are stored. Can be accessed on port 8086.

### 7.3 Chronograf

Web interface for analyzing metrics stored in InfluxDB. Accessible at `http://172.10.10.113:8888`.

### 7.4 Grafana

Interactive visualization platform where data is presented in custom dashboards.