# **Home**

**Welcome to the Redes Abertas project!**

This project aims to provide a solid foundation for configuring and simulating networks using modern and efficient tools: **Netbox**, **Containerlab**, and **Netreplica**.

The **Redes Abertas** project was developed for networking professionals and enthusiasts who want to:

- **Explore**: Test different network configurations in a controlled environment.
- **Automate**: Use templates to standardize and automate network device configurations.
- **Replicate**: Reproduce real network environments in virtual labs for testing and validation.
- **Manage**: Centralize the documentation and management of network infrastructures efficiently.

With these tools, the project aims to simplify the creation, management, and documentation of complex network topologies, providing flexibility and scalability.

---

## Containerlab Capabilities

**Containerlab** is a powerful tool for creating and managing virtualized network labs using Docker containers. With it, you can test and simulate complex network topologies in a controlled environment. The tool supports various network devices, allowing the configuration of **multivendor** networks, which is ideal for testing interactions between different vendors in the same lab.
Below is a list of the main vendors supported by Containerlab:
![Vendors](../img/vendors.svg)

---

## Lab Flowchart

The flowchart illustrates the workflow of **Netreplica** in the context of a network simulation environment, integrated with **Containerlab**:

![../img/tools_imgs/workflow-netreplica.png](../img/tools_imgs/workflow-netreplica.png)

---

## Workflow Structure

### 1. **Topology**

The network topology defines the structure and interconnection of network devices.

### 2. **Netbox**

The topology is documented and managed in **Netbox**, a centralized platform for network infrastructure management. Netbox stores detailed information about devices, IP addresses, and physical connections.

### 3. **Netreplica**

**Netreplica** synchronizes configuration information from Netbox and prepares the data for simulation. It obtains data via API and generates YAML configuration files required for the simulation.

### 4. **Configurations**

**Netreplica** generates detailed YAML configuration files that describe how network devices should be configured.

### 5. **Containerlab**

**Containerlab** uses the generated configuration files to create and manage complex network topologies in Docker containers.

### 6. **Laboratory (Docker Stack)**

The simulation is executed in a lab environment using a Docker stack. The defined topology is reproduced, allowing for testing and validation.

### 7. **Graphite**

To monitor and visualize metrics and performance of the simulation, **Graphite** is integrated into the lab. It collects and displays relevant data for analysis.

---

## Workflow Summary

1. **Topology Definition**: The structure and interconnection of network devices are defined.
2. **Documentation in Netbox**: The topology is documented and managed in **Netbox**.
3. **Synchronization with Netreplica**: **Netreplica** synchronizes information from **Netbox** via API and generates YAML configurations.
4. **Topology Creation with Containerlab**: **Containerlab** uses the YAML configurations to create the network topology in Docker containers.
5. **Simulation Execution**: The topology is executed in a Docker lab environment.
6. **Monitoring with Graphite**: The performance and metrics of the simulation are monitored and visualized with **Graphite**.

---

## Project Status

Project in progress.

---

## Getting Started
To get started, read the [Configuration Guide](./Getting%20Started.md) to learn how to use the Netbox, Containerlab, and Netreplica tools together.

---

## Available Labs

- [OSPF Lab](Laborat%C3%B3rios/ospf-lab/index.md) - OSPF Configuration Laboratory based on the Juniper MX platform in a ring topology.

---

## Tools

- [Netbox](Getting Started.md): Tool for network infrastructure management
- [Containerlab](Getting Started.md): Tool for simulating complex network topologies
- [Netreplica](Getting Started.md): Tool for replicating network environments from Netbox to Containerlab
- [ELK](Ferramentas/Elasticsearch/index.md): Stack for monitoring logs and data flows in real-time
- [Edgeshark](Ferramentas/Edgeshark/index.md): Tool for capturing and visualizing network traffic
- [LibreNMS](Ferramentas/LibreNMS/index.md): Tool for monitoring network devices

---

## Contribute

Contribute to the project by clicking [here](Contribua.md).