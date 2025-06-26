## Introduction

This lab provides a hands-on approach to configuring network devices using the NETCONF protocol and YANG data models.

### Prerequisites

- containerlab
- `uv` (if you want to create the virtual environment manually, use Python 3.12)

To get started, clone the repository containing scripts and examples from:
```
https://git.rnp.br/redes-abertas/schema-driven-cfg
```
## Building the Test Environment with `containerlab`

In this section, we will use `containerlab` to deploy a simple network topology defined in the `simple-lab.yaml` file.

1.  **Image Generation (if needed):**
    The virtual router images (vSRX for Juniper and NE40E for Huawei) must be available locally. Use `vrnetlab` to build these images. See the [`vrnetlab` documentation](https://containerlab.dev/manual/vrnetlab/#vrnetlab) for detailed instructions on how to generate the `VSRX 20.1R1.13` and `Huawei NE40E V800R011C00SPC607B607` images.

2.  **Topology Deployment:**
    With the images ready, execute the following command to start the lab:

    ```bash
    sudo containerlab deploy -t simple-lab.yaml
    ```
    `containerlab` will provision the containers and display a table with the IP addresses for each device. Note these IPs, as they will be used in subsequent steps.

## Installing Python Dependencies

The Python scripts used in this lab have external dependencies. Follow one of the methods below to install them:

#### Using `uv` (Recommended)

If you have `uv` installed, run the command below in the root of the cloned repository to create a virtual environment and install the dependencies:

```bash
uv sync
```
Then, activate the virtual environment:
```bash
source .venv/bin/activate
```

#### Using `pip` with a Manual Virtual Environment

If you prefer to manage the virtual environment manually with Python 3.12+ and `pip`:

1.  Create a virtual environment:
    ```bash
    python3 -m venv .venv
    ```
2.  Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Testing NETCONF Operations

With the environment configured, we can test NETCONF operations using the `netconf_test.py` script. This script uses YAML configuration files to define device connection parameters and XML payloads for NETCONF operations.

1.  **Update the Device Configuration Files:**
    Modify the `huawei_device_config.yaml` and `junos_device_config.yaml` files with the correct IP addresses of your devices (provided by `containerlab`) and the corresponding credentials.

    Example (`huawei_device_config.yaml`):
    ```yaml
    # filepath: huawei_device_config.yaml
    device:
    hostname: "172.20.20.5"
    username: "admin"
    password: "admin"
    port: 830
    type: "huaweiyang"
    ```

2.  **Execute the `netconf_test.py` Script:**

    **Script Usage:**
    ```bash
    python netconf_test.py -c <config_yaml_file> -p <payload_xml_file>
    ```

    **Arguments:**
    -   `-c CONFIG`, `--config CONFIG`: Path to the YAML configuration file of the device (e.g., `huawei_device_config.yaml`).
    -   `-p PAYLOAD`, `--payload PAYLOAD`: Path to the XML file containing the NETCONF payload (e.g., `xml/huawei-native-interface-ip.xml`).

    **Example of Applying Interface Configuration on a Huawei Device:**
    ```bash
    python netconf_test.py -c huawei_device_config.yaml -p xml/huawei-native-interface-ip.xml
    ```
    Access the device and verify that the IP `10.1.1.2/24` has been configured on the `Ethernet1/0/1` interface.

    To remove the configuration, use the deletion payload:
    ```bash
    python netconf_test.py -c huawei_device_config.yaml -p xml/huawei-native-interface-ip-delete.xml
    ```

    **Example of Applying Interface Configuration on a Juniper Device:**
    ```bash
    python netconf_test.py -c junos_device_config.yaml -p xml/junos-native-interface-ip.xml
    ```
    Access the device and verify that the IP `10.1.1.2/24` has been configured on the `ge-0/0/0` interface.

    To remove the configuration, use the deletion payload:
    ```bash
    python netconf_test.py -c junos_device_config.yaml -p xml/junos-native-interface-ip-delete.xml
    ```

    **Example Using OpenConfig Models:**

    Now try performing the same operation using OpenConfig model payloads:
    ```bash
    #Huawei
    python netconf_test.py -c huawei_device_config.yaml -p xml/openconfig-huawei-interface-ip.xml
    #Juniper
    python netconf_test.py -c junos_device_config.yaml -p xml/openconfig-junos-interface-ip.xml
    ```

## Obtaining YANG Models from Devices

YANG models define the structure of configuration and state data for network devices, serving as the basis for automation and interoperability via NETCONF. Understanding and exploring these models is essential for creating correct NETCONF payloads.

Below, we present methods for obtaining YANG models from the Huawei and Juniper devices in this example.

### Obtaining YANG Models from Huawei Devices

In the case of Huawei devices, we can obtain the YANG models via NETCONF, without needing to change the initial device configuration done by containerlab. Use the `huawei_get_schema.py` script to download the models to a local folder.

**Script Usage:**

```bash
python huawei_get_schema.py <host> <username> <password> [output_dir]
```

**Arguments:**

-   `host`: IP address or hostname of the Huawei device (obtained from `containerlab`).
-   `username`: Username for NETCONF authentication.
-   `password`: Password for NETCONF authentication.
-   `output_dir` (Optional): Directory to save the YANG files. Default: `huawei-schema`.

### Obtaining YANG Models from Juniper Devices

For Juniper devices (Junos OS), it is recommended to obtain the YANG models directly from the equipment's CLI and transfer them to your local machine.

Refer to the [official Juniper documentation](https://www.juniper.net/documentation/us/en/software/junos/netconf/topics/task/netconf-yang-module-obtaining-and-importing.html) for detailed guidance.