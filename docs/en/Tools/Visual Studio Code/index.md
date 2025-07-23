# :material-microsoft-visual-studio-code: Visual Studio Code

Containerlab has an official extension for **Visual Studio Code**, which significantly facilitates the creation, editing, visualization, and management of topologies in YAML format. This guide shows how to install the extension, explore its features, and use it even in remote environments.

---

## :material-tools: 1. Extension Installation

### :octicons-tools-16: Prerequisites

* Visual Studio Code installed.
* Containerlab installed (<a href="https://containerlab.dev/install/" target="_blank">official documentation</a>).
* Docker installed and running on the system.

### :material-package-variant: Installation

1. Access the Visual Studio Code marketplace.
2. Search for: `Containerlab`.
3. Or access directly: <a href="https://marketplace.visualstudio.com/items?itemName=srl-labs.vscode-containerlab" target="_blank">Containerlab Extension</a>.
4. After installing, you will see a **Containerlab icon** in the left sidebar.

---

## :simple-rocket: 2. Basic Usage

#### :octicons-tools-16: Creating and Editing Topologies

* Create files with the `.clab.yml` extension to define your topology.
* Click on the **Containerlab** icon in the sidebar and select **"Create Topology"**.
* A new file will open with a basic structure for defining nodes and links.

#### :octicons-gear-16: Quick Actions via Explorer

In the side view:

* Topologies are listed automatically.
* **Right-click** on a topology to access:

  * `Deploy`
  * `Destroy`
  * `Redeploy`
  * `Graph`
* Lab states are displayed with **colored icons**:

  * 🟠 Creating containers
  * 🟢 Lab running
  * 🔴 Error creating

---

### :fontawesome-solid-display: 2.1 Nodes Tab

When expanding a topology:

* Each **node** will be listed with its name and status.
* **Right-click** on the node to:

  * Connect via SSH/Telnet.
  * Open terminal (docker exec).
  * Copy information: IP, MAC, vendor, name.
  * Start/stop/restart the node.
  * Save node configurations.
  * View logs.
  * Open node web port (if applicable).
  * Access the *Link Impairments* panel.

#### :material-ethernet: Interfaces

* Left-click on the node to expand its interfaces.
* For each interface:

  * Interface status is displayed.
  * Right-click → **"Open with Wireshark"** (requires the [Edgeshark](../Edgeshark) plugin installed).

---

### :material-vector-polyline-remove: 2.2 Visualizing Topologies with TopoViewer

* In the side view, **right-click** on a topology.
* Select **"Graph Topo View"**.
* A graphical view (TopoViewer) will open showing:

  * Nodes with customizable icons via `labels`.
  * Connections.
  * Grouping and geolocation (optional via `geo-lat`, `geo-long`).

---

## :material-cloud-key: 3. Remote Access via SSH

The Containerlab extension can be used in conjunction with **Remote - SSH** from VS Code, enabling complete remote usage.

### :octicons-gear-16: Step by Step

1. Install the <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh" target="_blank">Remote - SSH</a> extension.
2. Click on the **green SSH icon** in the lower left corner.
3. Select **"Connect to Remote Host..."**.
4. Fill in the connection information (host, user, etc.).
5. After connecting:

   * Install the `Containerlab` extension on the remote host (via VS Code).
   * Use the extension normally with the remote topologies.

---

## :material-book-search-outline: Official Documentation

* <a href="https://containerlab.dev/" target="_blank">Official Containerlab documentation</a>
* <a href="https://marketplace.visualstudio.com/items?itemName=srl-labs.vscode-containerlab" target="_blank">Extension documentation on the Marketplace</a>