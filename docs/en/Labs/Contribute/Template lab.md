# Lab Template (Lab Name)

This template serves as an **example** for creating lab implementation guides in Containerlab. It is structured to serve as a model for all project labs, with information that should be followed consistently in each documentation. Each lab may have its specificities, but the general structure and the following sections remain the same for all labs.

---

## 1. Description

### **Lab Objective**

Clearly describe the lab's objective, explaining what will be demonstrated or tested. Be brief, but include the main functionalities that the user will explore.

This part should contain an image with the lab topology.
[Lab Topology](../../../img/labs_imgs/Topologia_ospf_lab.png)

**Example: The "ospf-lab" lab demonstrates the configuration and testing of OSPF (Open Shortest Path First) routing in a network composed of multiple routers. The main focus is to verify the establishment of OSPF adjacency and routing between the network devices.**

!!! tip "Tip"
    Keep the description clear and concise, highlighting what is essential for the user to quickly understand what the lab will provide.

**Lab Topology**
Here, include the diagram or a detailed textual description of the topology, mentioning the devices and how they are interconnected.

---

Sure! Below is a **general template for the "Application Example" section**, with an **orientative description** for the user to understand what to include in this part of the guide, followed by a **practical example** that can be adapted in any similar lab:

---

### **Application Example**

**Description:**
Use this section to present practical and objective scenarios in which the lab can be applied. The focus should be on the possible uses, such as training, performance testing, configuration validation, or protocol study. Avoid technical implementation details and focus on **what** the lab can be used for in real or academic environments.

**Application Example:**

This lab is ideal for simulating real network scenarios, especially in the context of dynamic routing and monitoring. It can be applied in:

*   **Technical training**: Training professionals in routing protocols (such as OSPF) and monitoring with SNMP, using tools like Zabbix.
*   **Monitored environment testing**: Evaluating how routers behave under continuous monitoring and automatic device discovery.
*   **Network course education**: Supporting practical computer network classes, focusing on point-to-point topologies and integration with network management systems.
*   **Tool integration validation**: Used to validate communication between routers and monitoring platforms in virtualized environments.

---

## 3. Requirements

This topic should list **the minimum hardware and software requirements** needed to run the lab. Make sure to include essential tools such as **Containerlab** and **Docker**, in addition to the `br-lab` network.

### Example Requirements Table:

| Requirement           | Details |
|---------------------| --- |
| **CPUs**            | [x] CPUs (specify) |
| **RAM**             | [x] GB |
| **Disk Space**      | [x] GB |
| **Containerlab**    | [Containerlab Version] |
| **Created Network** | [ br-lab] |

!!! tip "Tip"
    Check that the Docker and Containerlab versions are compatible to avoid errors during deployment.

---

## 4. Deploying the Lab

This topic describes the process of **deploying the lab**, with detailed instructions for the user to download and start the environment.

### 4.1 Ready-made Deployment

This method allows the user to **download a pre-assembled version** of the lab, with the topology and configurations already defined. Simply download the repository and proceed to the start of execution.

!!! tip "Tip"
    The ready-made deployment is useful for those who want to start quickly with a configured environment, but does not allow modifications to the initial topology.

### Downloading the Lab

To download the lab, run the command corresponding to your operating system.

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "<https://git.rnp.br/redes-abertas/labs/-/raw/main/><lab-name>/get.sh?inline=false" && sh get.sh && cd <lab-name>
    
    ```

=== "Windows"

    ```bash
    curl -L -o get.bat "<https://git.rnp.br/redes-abertas/labs/-/raw/main/><lab-name>/get.bat?inline=false" && call get.bat && cd <lab-name>
    
    ```

This command will download the installation script and direct you to the lab directory.

!!! tip "Tip"
    Before running the scripts, check that the execution permissions are correct (use `chmod +x get.sh` on Linux/Mac).

---

### 4.2 Customized Deployment (Under Development)

If you want a **customized version** of the lab, you can start modifying it using tools like **NetBox** and **NetReplica**. **This step is under development**, but we will have more information soon.

!!! tip "Tip"
    Advanced customization can be useful for adjusting the topology to your specific needs, such as including more devices or testing different scenarios.

---

## 5. Starting the Lab

After downloading or customizing, follow the steps below to **start the lab**.

### 5.1 Spinning Up the Lab

Run the command below inside the directory where the lab was downloaded or customized:

```bash
sudo containerlab deploy

```

This command will start the topology defined in the lab and create all necessary containers.

!!! tip "Tip"
    If any errors occur, check the command output for possible error messages. Use `docker logs <container_name>` to debug.

---

## 6. Access

After the lab is started, you can access the devices and services configured in the network.

### 6.1 Table of IPs and Service Ports

Here is an example of a table of devices, IPs, and service ports available in the lab.

| Device                   | Access IP       | Port | Service       |
| ---                      | ---             | ---  | ---           |
| **Router 1**             | 192.168.1.1     | 22   | SSH           |
| **Router 2**             | 192.168.1.2     | 22   | SSH           |
| **Monitoring Server**    | 192.168.1.3     | 8080 | Web (Graphite)|
| **DB Server**          | 192.168.1.4     | 3306 | MySQL         |

### 6.2 Access Passwords

Here is an example table with the access passwords for the services configured in the lab.

| Service             | User  | Password   |
| ---                 | ---   | ---        |
| **Router 1 (SSH)**    | admin | admin@123  |
| **Router 2 (SSH)**    | admin | admin@123  |
| **Graphite (Web)**    | admin | admin@123  |
| **MySQL Database** | root  | mysql@123  |

!!! warning "Attention"
    Before accessing, check the log of a device to verify that it has been started and configured correctly.
---

## 7. :octicons-rocket-24: Next Steps

This part is intended for what to do after starting the lab. You can add other guides here such as
how to use a tool or operation of the lab.
---

### Conclusion (Delete later)

This template is designed to serve as the **standard structure** for documenting all project labs. It should be followed consistently to ensure clarity and standardization in the creation of new labs. The sections described are essential and applicable to any lab within Containerlab, with the aim of providing a smooth experience for both developers and users. without changing the structure of the documentation. and do not add anything and do not change the links or references.