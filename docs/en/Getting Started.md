# Getting Started

This comprehensive guide will walk you through setting up a network simulation environment, utilizing the tools Netbox, Containerlab, and Netreplica.

## Prerequisites:

- **Basic knowledge in:**
    - Linux and SSH (Course Recommendation: <a href="https://www.youtube.com/watch?v=aW4Owxgcvq4&list=PLnDvRpP8BnezDTtL8lm6C-UOJZn-xzALH" target="_blanck">Introduction to Linux</a>)
    - Basic Docker (Course Recommendation: <a href="https://www.youtube.com/watch?v=c2y_yz9B6_M&list=PLg7nVxv7fa6dxsV1ftKI8FAm4YD6iZuI4&index=1" target="_blanck">Docker for Beginners</a>)


## Steps:

### 1. Installing Netbox:

Netbox is a centralized platform for network infrastructure management, providing detailed documentation of devices, IP addresses, and physical connections. It allows the creation of configuration templates using Jinja2, facilitating automation and standardization in the configuration of devices such as routers and switches. This capability is essential for maintaining organized network simulation environments that are ready to scale as needed.

- **Official Documentation:** <a href="http://netboxlabs.com/docs/netbox/en/stable/installation/" target="_blanck">NetboxLabs</a>
- **Installation Guide:** [NetBox Installation and Imports](Guias/Netbox/index.md)
- **Summary:**
    - Make sure you have Docker installed on your machine
    - Download the official Netbox repository to your machine
    - Configure Netbox by accessing the .env
    - Run the compose

### 2. Installing Containerlab:

Containerlab is responsible for simplifying the creation and management of complex network topologies using Docker containers. It allows you to efficiently define and interconnect virtualized network devices, facilitating the configuration of network simulation and testing environments. This Docker-based approach simplifies the replication of real-world environments in virtual labs, providing flexibility and scalability in network infrastructure configuration.

- **Official Documentation:** <a href="https://containerlab.dev/install/" target="_blanck">Containerlab</a>
- **Summary:**
    - Install Docker and Docker Compose.
    - Download the Containerlab binary and add it to your PATH.

### 3. Installing Netreplica:

Netreplica synchronizes data from Netbox into simulation environments using Docker containers. It allows you to test configurations without affecting the production environment, ensuring data and configuration consistency across different network scenarios.

- **Official Documentation:** <a href="https://github.com/netreplica/nrx?tab=readme-ov-file#how-to-install" target="_blanck">Netreplica</a>
- **Installation Guide:** [NetReplica Installation via Docker](Guias/Netreplica/index.md)
- **Summary:**
    - Use Docker Compose to start Netreplica in a Docker container.
    - Configure Netreplica to synchronize with Netbox.

### 4. Configuring and Running NetReplica with Netbox:

Now let's detail the configuration process to integrate Netreplica with Netbox. This step is crucial to ensure that Netbox data and configurations are replicated correctly in simulation or testing environments, using Netreplica.

- **Official Documentation:** <a href="https://github.com/netreplica/nrx?tab=readme-ov-file#how-to-use" target="_blanck">Netreplica how to use</a>
- **Configuration Guide:** [NetReplica Configuration Guide](Guias/Netreplica/NetReplica Guia Configuração e Execução com NetBox.md)
- **Summary:**
    - Create an API token in Netbox for Netreplica.
    - Configure Netreplica to use the API token and the Netbox URL.
    - Start Netreplica and verify that it is synchronizing with Netbox.

### 5. Creating and Configuring Templates in Netbox:

Device configuration templates are essential for providing the necessary configurations to Netreplica, which will later be applied in network simulations.

- **Official Documentation:** <a href="http://netboxlabs.com/docs/netbox/en/stable/features/configuration-rendering/" target="_blanck">Netbox Configuration Rendering</a>
- **Configuration Guide:** [Creating Configuration Templates](Guias/Netbox/Render_Templates/index.md)
- **Summary:**
    - Create configuration templates for network devices such as routers and switches.
    - Use Jinja2 to create dynamic templates that adapt to your topologies.