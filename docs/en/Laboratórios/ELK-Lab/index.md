# ELK-Lab

This lab simulates, via Containerlab, the interconnection between three routers representing the GO–MS–MT connection in the RNP backbone, with dynamic routing via OSPF, flow export via IPFIX, and analysis/visualization via Elastic Stack (Elasticsearch, Kibana, Fleet Server, and Elastic Agent).

---

## 1. Description

### Lab Objective

The primary objective of the `elk-lab` is to simulate the sending and analysis of IPFIX traffic flows in a topology of three interconnected routers (GO, MS, and MT), using OSPF for dynamic routing and Elastic Stack tools for observability and real-time traffic analysis.

**Lab Topology**
[Lab Topology](../../../img/labs_imgs/Topologia_ELK.svg)

**Topology Description**

*   Three routers (GO, MS, MT) interconnected in a linear topology with point-to-point /31 links.
*   Dynamic routing via OSPF.
*   IPFIX flow export to the **Fleet Server**.
*   Elastic Agent installed to receive flows and send them to Elasticsearch.
*   Data visualization and analysis via Kibana.
*   The external `br-lab` network connects the network elements to the ELK stack.

---

## 2. Applications

### Application Examples

The `elk-lab` can be applied to different educational and research contexts, allowing the simulation of real-world scenarios for traffic export and analysis with Elastic Stack.

#### Possible Applications:

*   **Teaching IPFIX in real environments**: Practical application of flow export to analysis tools.
*   **Elastic Stack training for networks**: Demonstrates IPFIX integration with Elastic Agent and the use of dashboards in Kibana.
*   **Network traffic and forensic analysis**: Support for studies on traffic patterns, anomalies, and threats.
*   **Integration with Elasticsearch-based SIEMs**: Evaluation of data pipelines for use with network security.
*   **Traffic flow visualization**: Composition of dynamic dashboards in real time.

---

## 3. Requirements

Below are the minimum hardware and software requirements to run the lab. Make sure to include essential tools such as **Containerlab** and **Docker**, as well as the `br-lab` network.
To learn more about these items, visit: [Getting Started - Preparing the Environment](../../Ferramentas/Primeiros passos - preparando o ambiente.md).

And have the ELK stack pre-installed, to learn more about the zabbix installation, visit: [ELK Installation](../../Ferramentas/Elasticsearch/index.md)

### 🖥️ Requirements Table

| Requirement           | Details               |
| --------------------- | --------------------- |
| **CPUs**              | 6 vCPUs               |
| **RAM Memory**        | 16 GB                 |
| **Disk Space**        | 15 GB (recommended)    |
| **Containerlab**      | 0.45.0 or higher      |
| **Docker Engine**     | 23.0.3 or higher      |
| **Images**            | `vr-vjunos:23.2R1.14` |
| **Docker Network**    | `br-lab`              |

!!! warning "Attention"
    Check if your processor has **hardware virtualization support** and if this feature is **enabled in the BIOS/UEFI**.
    - In **Intel** processors, this technology is called **VT-x** (Intel Virtualization Technology).
    - In **AMD** processors, it is known as **AMD-V** (AMD Virtualization).

    Without this feature enabled, images like the **vJunos-router** will not work correctly, as they require execution in containers in `--privileged` mode with extended permissions (such as `SYS_ADMIN`) and hardware emulation support.

---

## 4. Lab Deployment

### 4.1 Download and Preparation

Execute the script below to download the lab files:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/elk-lab/get.sh?ref_type=heads&inline=false" && sh get.sh && cd elk-lab
    ```

=== "Windows"

    ```bash
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/elk-lab/get.bat?ref_type=heads&inline=false" && call get.bat && cd elk-lab
    ```

---

## 5. Accessing the Devices

### 5.1 IPs and Ports

| Device            | Access IP     | Port(s) | Service           |
| ----------------- | ------------- | ------- | ----------------- |
| **GO Router**     | 172.10.10.6   | 22      | SSH               |
| **MS Router**     | 172.10.10.7   | 22      | SSH               |
| **MT Router**     | 172.10.10.8   | 22      | SSH               |
| **Fleet Server**  | 172.10.10.110 | 8220    | Data Ingestion    |
| **Elasticsearch** | 172.10.10.108 | 9200    | Database          |
| **Kibana**        | 172.10.10.109 | 5601    | Web Interface     |

### 5.2 Access Credentials

| Service         | User                                                | Password      |
| --------------- | --------------------------------------------------- | ------------- |
| SSH Routers     | `admin`                                             | `admin@123`   |
| Kibana          | `elastic`                                           | `admin@123`   |

---

## 6. Flow Collection and Export
To configure data collection using IPFIX, with our [IPFIX configuration guide](../../Ferramentas/Elasticsearch/Configurando IPFIX no ELK.md).