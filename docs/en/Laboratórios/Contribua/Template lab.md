# Lab Template (Lab Name)

This template serves as an **example** for creating implementation guides for laboratories in Containerlab. It is structured to serve as a model for all laboratories in the project, with information that should be followed consistently in each documentation. Each laboratory may have its specificities, but the general structure and the following sections remain the same for all labs.

---

## 1. Description

### **Lab Objective**

Clearly describe the objective of the laboratory, explaining what will be demonstrated or tested. Be brief, but include the main functionalities that the user will explore.

This part should contain an image containing the lab topology
[Lab Topology](../../../img/labs_imgs/Topologia_ospf_lab.png)

**Example: The "ospf-lab" laboratory demonstrates the configuration and testing of OSPF (Open Shortest Path First) routing in a network composed of multiple routers. The main focus is to verify the establishment of OSPF adjacency and routing between the network devices.**

!!! tip "Tip"
    Keep the description clear and concise, highlighting what is essential for the user to quickly understand what the laboratory will provide.

**Lab Topology**
Here, include the diagram or a detailed textual description of the topology, mentioning the devices and how they are interconnected.

---

Sure! Below is a **general template of the "Application Example" section**, with a **guidance description** for the user to understand what to include in this part of the guide, followed by a **practical example** that can be adapted in any similar laboratory:

---

### **Application Example**

**Description:**
Use this section to present practical and objective scenarios in which the laboratory can be applied. The focus should be on the possible uses, such as training, performance testing, configuration validation, or protocol study. Avoid technical details of the implementation and focus on **what** the laboratory can be used for in real or academic environments.

**Application Example:**

This laboratory is ideal for simulating real network scenarios, especially in the context of dynamic routing and monitoring. It can be applied in:

* **Technical training**: Training professionals in routing protocols (such as OSPF) and monitoring with SNMP, using tools like Zabbix.
* **Monitored environment testing**: Evaluating how routers behave under continuous monitoring and automatic device discovery.
* **Teaching in networking courses**: Support environment for practical computer networking classes, focusing on point-to-point topologies and integration with network management systems.
* **Tool integration validation**: Used to validate the communication between routers and monitoring platforms in virtualized environments.

---

## 3. Requirements

This topic should list **the minimum hardware and software requirements** needed to run the lab. Be sure to include the essential tools, such as **Containerlab** and **Docker**, in addition to the `br-lab` network.

### Example Requirements Table:

| Requirement           | Details |
|---------------------| --- |
| **CPUs**            | [x] CPUs (specify) |
| **RAM Memory**     | [x] GB |
| **Disk Space** | [x] GB |
| **Containerlab**    | [Containerlab Version] |
| **Created Network**     | [ br-lab] |

!!! tip "Tip"
    Check if the Docker and Containerlab versions are compatible to avoid errors during deployment.

---

## 4. Deploying the Lab

This topic describes the **laboratory deployment** process, with detailed instructions for the user to download and start the environment.

### 4.1 Ready Deployment

This method allows the user to **download a pre-assembled version** of the laboratory, with the topology and configurations already defined. Simply download the repository and proceed to the start of execution.

!!! tip "Tip"
    Ready deployment is useful for those who want to get started quickly with a configured environment but does not allow modifications to the initial topology.

### Downloading the Lab

To download the laboratory, execute the command corresponding to your operating system.

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "<https://git.rnp.br/redes-abertas/labs/-/raw/main/><lab-name>/get.sh?inline=false" && sh get.sh && cd <lab-name>

    ```

=== "Windows"

    ```bash
    curl -L -o get.bat "<https://git.rnp.br/redes-abertas/labs/-/raw/main/<lab-name>/get.bat?inline=false" && call get.bat && cd <lab-name>

    ```

This command will download the installation script and direct you to the laboratory directory.

!!! tip "Tip"
    Before running the scripts, check if the execution permissions are correct (use `chmod +x get.sh` on Linux/Mac).

---

### 4.2 Custom Deployment (Under Development)

If you want a **customized version** of the laboratory, you can start the modification using tools like **NetBox** and **NetReplica**. **This step is under development**, but we will have more information soon.

!!! tip "Tip"
    Advanced customization can be useful for adjusting the topology to your specific needs, such as including more devices or testing different scenarios.

---

## 5. Starting the Lab

After downloading or customizing, follow the steps below to **start the laboratory**.

### 5.1 Bringing Up the Lab

Execute the command below within the directory where the laboratory was downloaded or customized:

```bash
sudo containerlab deploy

```

This command will start the topology defined in the laboratory and create all the necessary containers.

!!! tip "Tip"
    If any error occurs, check the command output for possible error messages. Use `docker logs <container_name>` to debug.

---

## 6. Access

After the laboratory is started, you can access the devices and services configured in the network.

### 6.1 Table of IPs and Service Ports

Here is an example of a table of devices, IPs, and service ports available in the laboratory.

| Device | Access IP | Port | Service |
| --- | --- | --- | --- |
| **Router 1** | 192.168.1.1 | 22 | SSH |
| **Router 2** | 192.168.1.2 | 22 | SSH |
| **Monitoring Server** | 192.168.1.3 | 8080 | Web (Graphite) |
| **DB Server** | 192.168.1.4 | 3306 | MySQL |

### 6.2 Access Passwords

Here is an example of a table with the access passwords for the services configured in the laboratory.

| Service | User | Password |
| --- | --- | --- |
| **Router 1 (SSH)** | admin | admin@123 |
| **Router 2 (SSH)** | admin | admin@123 |
| **Graphite (Web)** | admin | admin@123 |
| **MySQL Database** | root | mysql@123 |

!!! warning "Attention"
    before accessing, access the log of a device to verify that it has been started and configured correctly.
---

## 7. :octicons-rocket-24: Next Steps

this part is intended for what to do after starting the laboratory. You can add other guides here, such as
using some tool or operation of the laboratory
---

### Conclusion (Delete later)

This template is designed to serve as the **standard structure** for documenting all project laboratories. It should be followed consistently to ensure clarity and standardization in the creation of new laboratories. The sections described are essential and applicable to any laboratory within Containerlab, aiming to provide a smooth experience for both developers and users, without changing the structure of the documentation and without adding anything and not changing the links or references.