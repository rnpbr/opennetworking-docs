# Lab Template (Lab Name)

This template serves as an **example** for creating lab implementation guides in Containerlab. It is structured to serve as a model for all labs in the project, with information that must be followed consistently in each documentation. Each lab may have its specificities, but the general structure and the following sections remain the same for all labs.

---

## 1. Description

### **Lab Objective**

Describe the objective of the lab clearly, explaining what will be demonstrated or tested. Be brief, but include the main functionalities that the user will explore.

This part should contain an image containing the lab topology.
[Lab Topology](../../../img/labs_imgs/<Topology.svg>)

**Example: The "ospf-lab" lab demonstrates the configuration and testing of OSPF (Open Shortest Path First) routing in a network composed of multiple routers. The main focus is to verify the establishment of the OSPF adjacency and routing between the devices in the network.**

!!! tip "Tip"
    Keep the description clear and concise, highlighting what is essential for the user to quickly understand what the lab will provide.

**Lab Topology**
Here, include a diagram or a detailed textual description of the topology, mentioning the devices and how they are interconnected.

---

## 2. Use Cases

### **Application Example**

Here, provide a basic example of the application or functionality of the lab, with clear steps and example commands. Use a simple scenario so that the user can replicate the configuration.

**Application Example:**

1. **OSPF Configuration**:
    - On Router 1: Enable OSPF and add the `192.168.1.0/24` network to the OSPF area.
    - On Router 2: Configure OSPF to include the `192.168.2.0/24` network in the same area.
2. **Expected Result**:
    - After configuration, the routers should form an OSPF adjacency, and network traffic between the two networks should be routed correctly.

!!! tip "Tip"
    Verify that the networks are being advertised correctly between the routers after configuration.

---

## 3. Requirements

This topic should list the **minimum hardware and software requirements** needed to run the lab. Be sure to include essential tools such as **Containerlab** and **Docker**, as well as the `br-lab` network.

### Example Requirements Table:

| Requirement           | Details |
|---------------------| --- |
| **CPUs**            | [x] CPUs (specify) |
| **RAM Memory**     | [x] GB |
| **Disk Space** | [x] GB |
| **Containerlab**    | [Containerlab Version] |
| **Created Network**     | [ br-lab] |

!!! tip "Tip"
    Check that the Docker and Containerlab versions are compatible to avoid errors during deployment.

---

## 4. Deploying the Lab

This topic describes the **lab deployment process**, with detailed instructions for the user to download and start the environment.

### 4.1 Ready-Made Deployment

This method allows the user to **download a pre-built version** of the lab, with the topology and configurations already defined. Simply download the repository and proceed to start execution.

!!! tip "Tip"
    Ready-made deployment is useful for those who want to get started quickly with a configured environment but does not allow modifications to the initial topology.

### Downloading the Lab

To download the lab, execute the command corresponding to your operating system.

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
    Before running the scripts, verify that the execution permissions are correct (use `chmod +x get.sh` on Linux/Mac).

---

### 4.2 Custom Deployment (Under Development)

If you want a **customized version** of the lab, you can start modifying it using tools such as **NetBox** and **NetReplica**. **This step is under development**, but we will have more information soon.

!!! tip "Tip"
    Advanced customization can be useful for adjusting the topology to your specific needs, such as including more devices or testing different scenarios.

---

## 5. Starting the Lab

After downloading or customizing, follow the steps below to **start the lab**.

### 5.1 Spinning up the Lab

Execute the command below within the directory where the lab was downloaded or customized:

```bash
sudo containerlab deploy

```

This command will start the topology defined in the lab and create all the necessary containers.

!!! tip "Tip"
    If an error occurs, check the command output for possible error messages. Use `docker logs <container_name>` to debug.

---

## 6. Access

After the lab is started, you can access the devices and services configured on the network.

### 6.1 Table of IPs and Service Ports

Here is an example table of devices, IPs, and service ports available in the lab.

| Device | Access IP | Port | Service |
| --- | --- | --- | --- |
| **Router 1** | 192.168.1.1 | 22 | SSH |
| **Router 2** | 192.168.1.2 | 22 | SSH |
| **Monitoring Server** | 192.168.1.3 | 8080 | Web (Graphite) |
| **DB Server** | 192.168.1.4 | 3306 | MySQL |

### 6.2 Access Passwords

Here is an example table with the access passwords for the services configured in the lab.

| Service | User | Password |
| --- | --- | --- |
| **Router 1 (SSH)** | admin | admin@123 |
| **Router 2 (SSH)** | admin | admin@123 |
| **Graphite (Web)** | admin | admin@123 |
| **MySQL Database** | root | mysql@123 |

!!! warning "Attention"
    Before accessing, access the log of a device to verify that it was started and configured correctly.
---

## 7. :octicons-rocket-24: Next Steps

This part is intended for what to do after starting the lab. You can add other guides here, such as how to
use some tool or operation of the laboratory.
---

### Conclusion (Delete Later)

This template is designed to serve as the **standard structure** for documentation of all project labs. It must be followed consistently to ensure clarity and standardization in the creation of new labs. The sections described are essential and applicable to any lab within Containerlab, with the aim of providing a smooth experience for both developers and users, without changing the structure of the documentation, and without adding anything.