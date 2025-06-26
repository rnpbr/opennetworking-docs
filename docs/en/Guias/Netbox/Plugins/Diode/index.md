# :material-power-plug-outline: Diode Plugin

The Diode plugin for NetBox is a powerful solution for those who want to automate the discovery and ingestion of network device data. With it, NetBox dynamically receives information through agents or custom scripts that collect, process, and insert the data directly into the system. This functionality facilitates integration with complex environments and promotes continuous and automated documentation of the network infrastructure.

## :simple-git: **Plugin Repository**
Copy the link below or click to access the [Github Repository](https://github.com/netboxlabs/diode/tree/develop)

```
https://github.com/netboxlabs/diode/tree/develop
```

---

## :material-receipt-text-edit-outline: **1. Components**
Diode is composed of three main components that work together to perform automated data ingestion into NetBox:

1. **Diode Plugin for NetBox:** Responsible for integrating with the NetBox ORM and managing API keys, allowing NetBox to accept external data securely and in a structured manner. [Installing the Diode Plugin](./Instalando%20o%20Diode%20Plugin.md)

2. **Diode Server:** Acts as the core of the service, processing received data and performing reconciliation with existing information in NetBox. See here how to install [Installing the Diode Server](./Instalando%20o%20Diode%20Server.md)

3. **Diode Client:** Implemented as a Python SDK, this component collects data from devices and sends it to the server via gRPC/protobuf. It can be easily incorporated into custom scripts or existing integrations. See here how to install [Installing the Diode Client](./Instalando%20o%20Diode%20Client.md)

!!! tip "Tip" 
    The component numbers indicate the **installation order**, follow them for a better experience and understanding of the subject.

---

## :fontawesome-solid-building-columns: **2. Architecture**
To facilitate understanding how Diode works, the diagram below illustrates the architecture of its main components and how they communicate with each other:

[foto do diagrama](../../../../../img/netbox_imgs/diodeDiagram.svg)