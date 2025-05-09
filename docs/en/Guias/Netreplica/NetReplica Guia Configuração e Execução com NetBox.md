# :material-content-duplicate: NetReplica Guide: Configuration and Execution with NetBox

This guide describes the necessary configurations to integrate NetReplica with NetBox. NetReplica is a tool used for replicating and analyzing networks, while NetBox is a network asset management platform.

## :octicons-tools-24: Step 1: Direct Execution with NRX

---

!!! tip "Note"
    Before proceeding, verify that NetReplica is installed and that NetBox is installed. You can find more information here: [Netreplica Installation](index.md)

`nrx` is the command-line interface for NetReplica that allows you to configure and execute tasks directly without needing to create a configuration file. The following are the main commands you can use:

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

This command allows exporting using parameters directly on the command line, such as the NetBox API URL, tags, site, and output format.

3 **Using Authentication Tokens**:

To pass the authentication token without using a configuration file:

   ```bash
   export NB_API_TOKEN='your_token_here'
   nrx -a http://<netbox_ip>:<port> -t '<tags>' -s '<site>' -o clab
   ```

4 **Specify Output Directory**:

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

The `.conf` configuration file provides a structured way to define the variables needed for topology export. It is particularly useful when you want to reuse the same settings or when there are many options to be defined.

Of course, here is the configuration file with a detailed explanation for each field:

---

## Complete Configuration File

```bash
# NetBox API URL. Alternatively, use the --api argument or the NB_API_URL environment variable
NB_API_URL           = 'https://demo.netbox.dev'
# NetBox API Token. Alternatively, use the NB_API_TOKEN environment variable
NB_API_TOKEN         = ''
# Perform TLS certificate validation
TLS_VALIDATE         = true
# Timeout for API requests, in seconds
API_TIMEOUT          = 10
# Optimization of bulk queries to the NetBox API
[NB_API_PARAMS]
interfaces_block_size = 4
cables_block_size =     64

# Topology name, optional. Alternatively, use the --name argument
TOPOLOGY_NAME        = 'DemoSite'
# Output format to use for export: 'gml' | 'cyjs' | 'clab'. Alternatively, use the --output argument
OUTPUT_FORMAT        = 'clab'
# Overwrite output directory. By default, a subdirectory corresponding to the topology name will be created. Alternatively, use the --dir argument. Environment variables are supported
OUTPUT_DIR           = '$HOME/nrx'
# Path for template searching. The default path is ['./templates','$HOME/.nr/templates']. Environment variables are supported
TEMPLATES_PATH       = ['./templates','$HOME/.nr/custom','$HOME/.nr/templates']
# Path to the platform map. If not provided, 'platform_map.yaml' in the current directory is checked first, and then in the TEMPLATES_PATH folders. Environment variables are supported
PLATFORM_MAP         = '$HOME/.nr/platform_map.yaml'

# List of NetBox Device Roles to be exported
EXPORT_DEVICE_ROLES  = ['router', 'core-switch', 'distribution-switch', 'access-switch', 'tor-switch', 'server']
# NetBox Site to be exported. Alternatively, use the --sites argument
EXPORT_SITES          = ['DM-Akron']
# NetBox Tags to be exported. Alternatively, use the --tags argument
EXPORT_TAGS          = []
# Export device configurations, when available
EXPORT_CONFIGS       = true

# Levels of device roles for visualization
[DEVICE_ROLE_LEVELS]
unknown =              0
server =               0
tor-switch =           1
access-switch =        1
leaf =                 1
distribution-switch =  2
spine =                2
core-switch =          3
super-spine =          3
router =               4
```

## Field Explanation

### NetBox API Settings

1. **NB_API_URL**
    - **Description**: NetBox API URL.
    - **Example**: `'https://demo.netbox.dev'`
    - **Usage**: Defines the URL to which NetReplica should send API requests. If you are using a local NetBox instance, change to `'http://localhost:8000'`.

2. **NB_API_TOKEN**
    - **Description**: NetBox API authentication token.
    - **Example**: `'my_api_token'`
    - **Usage**: This token is required to authenticate requests to the NetBox API. It must be obtained from the NetBox administration panel.

3. **TLS_VALIDATE**
    - **Description**: Whether to perform TLS certificate validation.
    - **Example**: `true`
    - **Usage**: `true` enables TLS certificate validation to ensure communication security. `false` disables validation, which can be useful in test environments but is not recommended for production.

4. **API_TIMEOUT**
    - **Description**: Timeout for API requests, in seconds.
    - **Example**: `10`
    - **Usage**: Defines the maximum time NetReplica should wait for an API response before considering the request failed.

### API Optimization Settings

5. **[NB_API_PARAMS]**
    - **Description**: Parameters to optimize bulk queries in the NetBox API.
    - **Example**:
      ```bash
      interfaces_block_size = 4
      cables_block_size = 64
      ```
    - **Usage**: Controls the number of interfaces and cables processed in each bulk query. Adjusting these values can improve performance depending on the size of your database.

### Export Settings

6. **TOPOLOGY_NAME**
    - **Description**: Name of the topology for export.
    - **Example**: `'DemoSite'`
    - **Usage**: Defines the name used to identify the exported topology. It is useful for organizing and identifying exported files.

7. **OUTPUT_FORMAT**
    - **Description**: Output format for exporting data.
    - **Example**: `'clab'`
    - **Usage**: Defines the format of the exported data. Can be `'gml'`, `'cyjs'`, `'clab'`, among other compatible formats.

8. **OUTPUT_DIR**
    - **Description**: Directory where the exported files will be saved.
    - **Example**: `'$HOME/nrx'`
    - **Usage**: Defines the path where the exported files will be stored. Can override the default directory if specified.

9. **TEMPLATES_PATH**
    - **Description**: Path to the templates used during export.
    - **Example**: `'./templates'`
    - **Usage**: Defines where to look for templates for export. Can include multiple directories for greater flexibility.

10. **PLATFORM_MAP**
    - **Description**: Path to the platform mapping file.
    - **Example**: `'$HOME/.nr/platform_map.yaml'`
    - **Usage**: File that defines how platforms are mapped to node parameters. It is used to customize the visualization of devices in the export.

### Device Export Settings

11. **EXPORT_DEVICE_ROLES**
    - **Description**: List of NetBox device roles to be exported.
    - **Example**: `['router', 'core-switch']`
    - **Usage**: Defines which types of devices (e.g., routers, switches) should be included in the export.

12. **EXPORT_SITES**
    - **Description**: List of NetBox sites to be exported.
    - **Example**: `['DM-Akron']`
    - **Usage**: Defines which specific sites should be exported. Can include multiple sites.

13. **EXPORT_TAGS**
    - **Description**: List of NetBox tags to be exported.
    - **Example**: `['production', 'datacenter']`
    - **Usage**: Defines which tags should be used to filter devices during export.

14. **EXPORT_CONFIGS**
    - **Description**: Whether device configurations should be exported, when available.
    - **Example**: `true`
    - **Usage**: If `true`, device configurations will be included in the export.

### Device Role Levels

15. **[DEVICE_ROLE_LEVELS]**
    - **Description**: Defines the visualization levels for different device roles.
    - **Example**:
      ```bash
      unknown =              0
      server =               0
      tor-switch =           1
      access-switch =        1
      leaf =                 1
      distribution-switch =  2
      spine =                2
      core-switch =          3
      super-spine =          3
      router =               4
      ```
    - **Usage**: Defines the order of visualization of devices in the export. Devices with higher levels are displayed more prominently.

---

This configuration file allows detailed customization of how NetReplica interacts with NetBox and exports data, helping to meet specific visualization and export needs.

### :fontawesome-solid-arrow-right-to-bracket: **Next Steps**

Now, to delve deeper, you can check out the next guide that shows how to create and configure new Templates and add new images to netreplica. Check it out here [NetReplica Creating Templates](NetReplica%20Creating%20Templates.md).

### :fontawesome-solid-link: References

- <a target="_blank" href="https://github.com/netreplica/nrx?tab=readme-ov-files">NetReplica GitHub Repository</a>