# Discovery

## :material-bookmark: **Introduction**

This lab simulates a network with 2 routers configured with OSPF and SNMP, integrating Zabbix and Netbox for automated device import and management.

---

## :fontawesome-solid-prescription-bottle: 1. **Description**

### :octicons-goal-16: 1.1 **Lab Objective**

The objective of this lab is to import network devices and their configurations into Netbox from Zabbix, as well as demonstrate the basic operation of OSPF routing between two routers connected in a ring and monitored via SNMP.

### :material-lan: 1.2 **Lab Topology**
Below is the topology in image format, representing the routers, servers, and their connections.

![Topologia.svg](../../../img/labs_imgs/Topologia_discovery_lab.svg)

The routers are configured with the following technologies:

- **OSPF (Open Shortest Path First)**: Used for dynamic routing in the network, allowing routers to exchange information about routes and topology updates.
- **SNMP (Simple Network Management Protocol)**: Used for network monitoring and management, allowing access to telemetry information from devices.
---

## :octicons-search-16: **2. Applications**

### Application Examples

This lab is focused on practical experimentation with automatic discovery of devices in IP networks, integrating monitoring (Zabbix) and documentation (Netbox) tools. It is ideal for studies and training involving inventory automation, topology discovery, and network data integration.

#### Possible Applications:

- **Network discovery automation:** Demonstrates how to automatically identify active devices in a network using Zabbix and how to import this data into Netbox, reducing manual effort in asset mapping.

- **NetDevOps and inventory management training:** Excellent for training professionals in modern network operations practices, focusing on tool integration via API and automation of infrastructure documentation.

- **Creation of a centralized device repository:** Enables building a reliable database of network information in real-time, based on information discovered via SNMP and documented in Netbox.

- **Study of Zabbix + Netbox integration via API:** Allows exploring the use of RESTful APIs to synchronize information between monitoring and network asset management tools.

- **Teaching SNMP discovery and centralized management:** Provides a practical experience for students and professionals to understand how network data collection (interfaces, IPs, manufacturers, etc.) occurs and how this data is processed by management tools.

---

## :material-tools: **3. Requirements**
### :material-alert: 3.1 Prerequisites

To start the lab, the following components need to be installed and configured:

- Netbox
- Containerlab
- Docker
- Python

If your environment is not configured, follow the steps in the [Configuration Guide](../../Getting%20Started.md)

### :material-alert: 3.2 Computational Requirements Table

| Requirement           | Details |
|---------------------| --- |
| **CPUs**            | 4 vCPUs (minimum recommended) |
| **RAM Memory**     | 12 GB |
| **Disk Space** | 10 GB |
| **Containerlab**    | 0.64.0 |
| **Network Created**     | br-lab |

!!! tip "Tip"
    Check if the Docker and Containerlab versions are compatible to avoid errors during deployment.

!!! warning "Attention"
    Verify that your processor has **hardware virtualization support** and that this feature is **enabled in the BIOS/UEFI**.
    - On **Intel** processors, this technology is called **VT-x** (Intel Virtualization Technology).
    - On **AMD** processors, it is known as **AMD-V** (AMD Virtualization).

    Without this feature enabled, images like **vJunos-router** will not function correctly.
---

## :octicons-tools-16: 4. Installation

### :material-network-strength-4-cog: 4.1 Configuring the Docker Network

Before starting the containers, create the bridge network that will interconnect the devices:

```bash
docker network create \
  --driver=bridge \
  --opt com.docker.network.bridge.name=br-lab \
  --subnet=172.10.10.0/24 \
  br-lab
```

### :material-git: 4.2 Cloning the Lab Repository

Run the script below to automatically download and configure the lab:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/discovery-lab/get.sh?ref_type=heads&inline=false" && sh get.sh && cd discovery-lab
    ```

=== "Windows"

    ```bat
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/discovery-lab/get.bat?ref_type=heads&inline=false" && call get.bat && cd discovery-lab
    ```

!!! tip "Tip"
    On Linux/Mac, use `chmod +x get.sh` before running the script if it does not have execute permission.

---

## :fontawesome-solid-house-chimney: 5. Environment Deployment

### :material-router-wireless: 5.1 Starting the Routers with Containerlab

Start the topology with the command:

```bash
sudo clab deploy -t clab/discovery-lab.clab.yaml
```

!!! warning "Debug"
    The devices may take about 10 minutes to be fully operational.
    If any errors occur, check the command output for possible error messages. Use `docker logs <container_name>` to debug.

### :material-server: 5.2 Launching Zabbix
!!! tip "Tip"
    If you already have a configured Zabbix environment, just skip this step.

To bring up the container with Zabbix:

```bash
docker compose -f zabbix-docker/docker-compose.yml up -d
```
The Zabbix web interface will be available on port 81.

---
## :material-relation-one-to-one: 6. Integration with Zabbix and Netbox
In this step, you need to create an API token in both Zabbix and Netbox to add the token to the .env file.

### :material-import: 6.1 Importing Routers into Zabbix

1. Access the scripts folder:
```bash
cd scripts/
```
2. Create and activate the Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Python dependencies:
```bash
pip install -r requirements.txt
```
4. Configure the environment with your credentials:
```bash
mv .env.example .env
nano .env
```
Example .env:
```bash
 # Zabbix
ZABBIX_TOKEN=zabbix_token                     # API Token
ZABBIX_URL=http://yourdomain/api_jsonrpc.php  # API access URL
ZABBIX_USER=Admin                             # Default User
ZABBIX_PASSWORD=zabbix                        # Default Password
ZABBIX_GROUP=Juniper                          # Group to add the routers
ZABBIX_TEMPLATE="Juniper by SNMP"             # Monitoring template for Juniper routers

# Netbox
NETBOX_URL=http://yourdomain/api              # API access URL
NETBOX_TOKEN=netbox_token                     # API Token

# Devices
DEVICE_USERNAME=admin                         # Default access username to routers
DEVICE_PASSWORD=admin@123                     # Default access password to routers
```
5. Now, to import the routers into Zabbix, run the command:
```bash
python3 import_zabbix.py
```

### :octicons-key-16: 6.2 Generating API Tokens
Creating an API Token in Zabbix.

1. Access the Zabbix interface.
2. Go to **Users** > **API Tokens**.
3. Click **Create**, fill it out, and copy the generated token.
4. Update the `ZABBIX_TOKEN` field in `.env`.

Creating an API Token in Netbox.

1. Access the Netbox interface.
2. Navigate to **Admin** > **API Tokens**.
3. Click **Add**, associate it with a user and copy the token.
4. Update the `NETBOX_TOKEN` field in `.env`.

### :material-import: 6.3 Importing Routers into Netbox
Now with the environment fully configured, you can import the routers into Netbox with the command:
```bash
python3 import_netbox.py
```

With the script successful, you can view the routers inside Netbox with their respective information!
___

## :material-access-point: 7. Access

After the lab is started, you will be able to access the devices and services configured on the network.

### :material-table: 7.1 IP and Service Port Table

Here is the table of devices, IPs, and service ports available in the lab.

| Device | Access IP | Port | Service |
| --- | --- | --- | --- |
| **RO** | 172.10.10.101 | 22 | SSH |
| **AC** | 172.10.10.102 | 22 | SSH |
| **Monitoring Server** | 172.20.20.1 | 8080 | Web (Graphite) |
| **Zabbix Server** | 172.10.10.115 | 81 | Zabbix |

### :material-key-link: 7.2 Access Passwords

Here is the table with the access passwords for the services configured in the lab.

| Service | User | Password |
| --- | --- | --- |
| **AC (SSH)** | admin | admin@123 |
| **RO (SSH)** | admin | admin@123 |
| **Graphite (Web)** | admin | admin@123 |
| **Zabbix Server(Web)** | Admin | zabbix |

!!! warning "Attention"
    Before accessing, check the log of a device to verify that it has been started and configured correctly.
---

## :octicons-rocket-24: 8. Next Steps
With the lab finished, you can follow some steps below as **extra**.

- Monitor the routers via SNMP in the Zabbix interface.
- Explore Netbox to view and manage the network inventory.
- Modify the topology as needed (in future customized versions).
- Consult the OSPF guide to validate dynamic communication between routers.
---

### :fontawesome-solid-paintbrush: 9. Conclusion

✅ Done! Your environment is now configured, monitored, and documented in Netbox. Feel free to customize or expand the topology according to the objectives of your study or project, without altering the structure of the documentation, adding anything, or changing the links or references.