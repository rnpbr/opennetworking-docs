# Telegraf Lab

This lab simulates, via Containerlab, the interconnection between three routers representing the GO–MS–MT connection in the RNP backbone, with dynamic routing via OSPF, flow export via IPFIX, and monitoring via SNMP/Telemetry using Telegraf, InfluxDB, Chronograf, and Grafana.

---

## 1. Description

### Lab Objective

The `telegraf-lab` lab aims to simulate traffic monitoring of a topology with three interconnected routers (GO, MS, and MT), using dynamic routing protocols (OSPF), flow export (IPFIX), and monitoring with SNMP. The collection and visualization of network metrics are performed with modern observability tools: **Telegraf**, **InfluxDB**, **Chronograf**, and **Grafana**.

**Lab Topology**
[Lab Topology](../../../img/labs_imgs/Topologia_Telegraf.svg)

**Topology Description**

* Three routers (GO, MS, MT) interconnected in a linear topology with point-to-point /31 links.
* Dynamic routing via OSPF between routers.
* Collection of traffic metrics via IPFIX and SNMP.
* Observability with the TICK stack (Telegraf, InfluxDB, Chronograf) and Grafana.
* External network `br-lab` connects the nodes to the monitoring infrastructure.

---

## 2. Applications

### Application Examples

This lab can be explored in various academic and applied research scenarios, serving as a basis for experimenting with monitoring and visualizing traffic in networks with multiple routers.

#### Possible Applications:

* **Training network and NOC teams**: Simulates real operations with OSPF, IPFIX, and SNMP, facilitating the analysis of traffic behavior.
* **Traffic analysis with IPFIX**: Allows exporting flows and studying traffic patterns between domains.
* **Metrics visualization with Grafana**: Supports performance studies, bottlenecks, and network utilization peaks.
* **Distributed monitoring with Telegraf**: Evaluates the simultaneous collection of data from multiple routers with different protocols.
* **Teaching routing and telemetry protocols**: Ideal environment for advanced network practical classes.

---

## 3. Requirements

Below are listed the minimum hardware and software requirements to run the lab. Make sure to include essential tools such as **Containerlab** and **Docker**, in addition to the `br-lab` network.
To learn more about these items, access: [First Steps - preparing the environment](../../Ferramentas/Primeiros passos - preparando o ambiente.md).

And have the telegraf stack previously installed, to learn more about zabbix installation access: [Telegraf Installation](../../Ferramentas/Telegraf/index.md)

### 🖥️ Requirements Table

| Requirement           | Details              |
| ------------------- |-----------------------|
| **CPUs**            | 6 vCPUs               |
| **RAM**     | 12 GB                 |
| **Disk Space** | 10 GB (recommended)   |
| **Containerlab**    | 0.45.0 or higher    |
| **Docker Engine**   | 23.0.3 or higher    |
| **Images**         | `vr-vjunos:23.2R1.14` |
| **Docker Network**     | `br-lab`              |

!!! warning "Attention"
    Check if your processor has **hardware virtualization support** and if this feature is **enabled in the BIOS/UEFI**.
    - On **Intel** processors, this technology is called **VT-x** (Intel Virtualization Technology).
    - On **AMD** processors, it is known as **AMD-V** (AMD Virtualization).

    Without this feature enabled, images like **vJunos-router** will not work correctly, as they require execution in containers in `--privileged` mode with extended permissions (such as `SYS_ADMIN`) and hardware emulation support.

---

## 4. Deploying the Lab

You can perform the deployment through a ready-made script or manually configure the lab files.

### 4.1 Ready Deployment

Run the script below to download and configure the lab automatically:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/telegraf-lab/get.sh?ref_type=heads&inline=false" && sh get.sh && cd telegraf-lab
    ```

=== "Windows"

    ```bat
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/telegraf-lab/get.bat?ref_type=heads&inline=false" && call get.bat && cd telegraf-lab
    ```

!!! tip "Tip"
    On Linux/Mac, use `chmod +x get.sh` before running the script if it does not have execute permission.

---

## 5. Initializing the Lab

Inside the downloaded directory, start the lab with:

```bash
sudo containerlab deploy
```

This command will create the router containers, configure the links, and start the monitoring services.

!!! tip "Debugging"
    Use `docker logs -f <container_name>` to check the status of the services if something doesn't work.

---

## 6. Accessing the Devices

### 6.1 IPs and Ports of Services

| Device     | Access IP  | Port(s) | Service            |
| --------------- | ------------- |-----| ------------------ |
| **Router GO** | 172.10.10.6   | 22  | SSH                |
| **Router MS** | 172.10.10.7   | 22  | SSH                |
| **Router MT** | 172.10.10.8   | 22  | SSH                |
| **Telegraf**    | 172.10.10.114 | 161 | Metrics collection |
| **InfluxDB**    | 172.10.10.112 | 8086 | Time series database    |
| **Chronograf**  | 172.10.10.113 | 8888 | Analysis UI      |
| **Grafana**     | 172.10.10.111 | 3000 | Web Dashboard      |
| **Graphite** | 172.10.10.119 | 8080    | Web UI (Graphite) |

### 6.2 Access Passwords

| Service          | User | Password             |
| ---------------- | ------- |-------------------|
| Routers (SSH) | `admin` | `admin@123`       |
| Grafana          | `admin` | `admin`           |
| InfluxDB         | `admin` | `influxpassword`  |

!!! warning "Initialization Verification"
    Before accessing the services, use `docker ps` and check the container logs to ensure they are working correctly.

---

## 7. Observability and Visualization

### 7.1 Telegraf

Telegraf is configured to collect metrics via:

* **SNMP**: periodic reading of the routers.
* **IPFIX**: export of traffic flows.
* **Docker and system**: collection of local container metrics.

### 7.2 InfluxDB

Time series database where Telegraf metrics are stored. It can be accessed through port 8086.

### 7.3 Chronograf

Web interface for analyzing metrics stored in InfluxDB. Accessible at `http://172.10.10.113:8888`.

### 7.4 Grafana

Interactive visualization platform where data is presented in custom dashboards.