# :material-content-duplicate: NetReplica Guide: Configuration and Execution with NetBox

This guide outlines the necessary configurations to integrate NetReplica with NetBox. NetReplica is a tool used for replicating and analyzing networks, while NetBox is a network asset management platform.

## :octicons-tools-24: Step 1: Direct Execution with NRX

---

!!! tip "Note"
    Before proceeding, verify that NetReplica and NetBox are installed. You can find more information here: [Netreplica Installation](index.md)

`nrx` is the NetReplica command-line interface that allows you to configure and execute tasks directly without the need to create a configuration file. The following are the main commands you can use:

### :octicons-command-palette-24: Basic Commands

1 **Command to Export a Topology**:

   ```bash
   nrx -c conf/<Topology_Name>.conf
   ```

This command uses the `.conf` configuration file to export the specified topology.

2 **Export from a NetBox API URL**:

   ```bash
   nrx -a http://<netbox_ip>:<port> -t '<tags>' -s '<site>' -o clab
   ```

This command allows exporting using parameters directly on the command line, such as NetBox API URL, tags, site, and output format.

3 **Use Authentication Tokens**:

To pass the authentication token without using a configuration file:

   ```bash
   export NB_API_TOKEN='your_token_here'
   nrx -a http://<netbox_ip>:<port> -t '<tags>' -s '<site>' -o clab
   ```

4 **Specify the Output Directory**:

   ```bash
   nrx -c conf/<Topology_Name>.conf -D /path/to/output
   ```

This command allows you to define a specific directory for the output of the exported files.

5 **Ignore TLS Certificate**:

   ```bash
   nrx -c conf/<Topology_Name>.conf --insecure
   ```

This command disables TLS certificate verification.

### :material-text-box-search-outline: Common `nrx` Arguments

- `-c, --config CONFIG`: Defines the configuration file to be used.
- `-a, --api API`: Defines the NetBox API URL.
- `-s, --site SITE`: Specifies the NetBox site to be exported.
- `-t, --tags TAGS`: Defines the NetBox tags to be exported.
- `-o, --output OUTPUT`: Defines the output format (e.g., 'clab', 'cyjs').
- `-D, --dir DIR`: Defines the output directory.
- `--insecure`: Disables TLS certificate verification.

---

## :material-file-document: Step 2: `.conf` File Configuration

---

The `.conf` configuration file provides a structured way to define the variables necessary for topology export. It is particularly useful when you want to reuse the same configurations or when there are many options to define.

Of course, here is the configuration file with a detailed explanation for each field:

---

## Summarized Configuration File

```bash
NB_API_URL           = 'http://localhost:8000'    # NetBox API URL or NB_API_URL env var
NB_API_TOKEN         = ''                         # API Token or NB_API_TOKEN env var
TLS_VALIDATE         = false                      # TLS certificate validation
API_TIMEOUT          = 10                         # API timeout (s)

TOPOLOGY_NAME        = 'lab'         # Topology name
OUTPUT_FORMAT        = 'clab'        # Output format: gml | cyjs | clab
OUTPUT_DIR           = 'conf/lab'    # Output directory (default: ./<topology>)
TEMPLATES_PATH       = ['templates']
PLATFORM_MAP         = 'templates/platform_map.yaml'   # Platform mapping file
EXPORT_CONFIGS       = true           # Export configs if available

EXPORT_DEVICE_ROLES  = []             # Device roles to export
EXPORT_SITES         = ['DM-Akron']   # Sites to export
EXPORT_TAGS          = []             # Tags to export
```

---


### NetBox API Settings

### 1. **NB\_API\_URL**
 
  * **Description**: NetBox API URL.
  * **Usage**: Defines the address of the NetBox instance to be queried by NetReplica.
  * **Example**: `'http://localhost:8000'`.

### 2. **NB\_API\_TOKEN**

   * **Description**: NetBox API authentication token.
   * **Usage**: Required to authenticate requests to the API.
   * **Example**: `''` (must be filled in with the actual token).

### 3. **TLS\_VALIDATE**
  * **Description**: Controls TLS certificate validation.
  * **Usage**: `true` enables validation (recommended in production); `false` disables (useful in testing).
  * **Example**: `false`.

### 4. **API\_TIMEOUT**

   * **Description**: Timeout for API requests, in seconds.
   * **Usage**: Defines how long NetReplica waits for a response before considering the request failed.
   * **Example**: `10`.

---

### Export Settings

### 5. **TOPOLOGY\_NAME**

   * **Description**: Name of the exported topology.
   * **Usage**: Identifies the exported files and groups the topology.
   * **Example**: `'lab'`.

### 6. **OUTPUT\_FORMAT**

   * **Description**: Format of the exported data.
   * **Usage**: Can be `'gml'`, `'cyjs'` or `'clab'`.
   * **Example**: `'clab'`.

### 7. **OUTPUT\_DIR**

   * **Description**: Destination directory for the exported files.
   * **Usage**: Replaces the default export directory.
   * **Example**: `'conf/lab'`.

### 8. **TEMPLATES\_PATH**

   * **Description**: List of template directories used in the export.
   * **Usage**: Allows locating custom templates.
   * **Example**: `['templates']`.

### 9. **PLATFORM\_MAP**

   * **Description**: Platform mapping file.
   * **Usage**: Defines how each device platform will be represented in the exported files.
   * **Example**: `'templates/platform_map.yaml'`.

### 10. **EXPORT\_CONFIGS**

   * **Description**: Defines whether device configurations should be exported.
   * **Usage**: `true` includes the configs, `false` ignores them.
   * **Example**: `true`.

---

### Device Filter Settings

### 11. **EXPORT\_DEVICE\_ROLES**

   * **Description**: List of device roles to be exported.
   * **Usage**: Filters which devices will be included.
   * **Example**: `[]` (exports all if empty).

### 12. **EXPORT\_SITES**

   * **Description**: List of NetBox sites to be exported.
   * **Usage**: Filters devices by site.
   * **Example**: `['DM-Akron']`.

### 13. **EXPORT\_TAGS**

   * **Description**: List of tags used as a filter for export.
   * **Usage**: Only devices with these tags will be exported.
   * **Example**: `[]` (exports all if empty).

---

This configuration file allows detailed customization of how NetReplica interacts with NetBox and exports data,
helping to meet specific visualization and export needs.


### :fontawesome-solid-arrow-right-to-bracket: **Next Steps**

Now to delve deeper you can check out the next guide that shows how to create and configure new Templates and add new images to netreplica. check it out here [NetReplica Creating Templates](NetReplica%20Criando%20Templates.md).

### :fontawesome-solid-link: References

- <a target="_blank" href="https://github.com/netreplica/nrx?tab=readme-ov-files">NetReplica GitHub Repository</a>