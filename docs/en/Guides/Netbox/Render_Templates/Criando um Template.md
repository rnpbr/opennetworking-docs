# Configuration Template Creation

## How Does Render Template Work in NetBox?

"Render Template" in NetBox is a powerful feature that allows network administrators to automate the generation of network device configurations based on predefined configuration templates. It simplifies the device deployment and maintenance process, making it more efficient and less prone to human errors. Here's how it works:

1. **Configuration Template Creation:** First, administrators create configuration templates using the Jinja2 template language. These templates serve as structures for the desired device configurations.
2. **Variable Incorporation:** Configuration templates can incorporate J2 variables, which are placeholders for dynamic information. These variables are replaced with device-specific data when the template is rendered.
3. **Association with Devices:** Each configuration template is associated with a specific device type. This allows NetBox to know which configuration templates to use for each device based on its type.
4. **Automated Rendering:** When an administrator creates or updates a device in NetBox, the "Render Template" comes into action. NetBox identifies the device type and the corresponding configuration template.
5. **Filling with Real Data:** The J2 variables in the configuration template are filled with real data from the device, such as its name, location, IP address, among others.
6. **Configuration Generation:** NetBox automatically generates a complete configuration for the device, applying the J2 variable values to the configuration template. This creates a customized and ready-to-use configuration.
7. **Configuration Application:** The generated configuration can be deployed to the device via traditional methods, such as SSH/SCP file transfer, or integrated with configuration management tools for further automation.

In summary, "Render Template" in NetBox simplifies the network device configuration process by allowing the creation of flexible templates and automating the generation of configurations based on device information. This saves time, reduces errors, and facilitates network infrastructure maintenance.

- **{{ }} - J2 Variables:** Expressions enclosed in double curly braces, such as `{{ device.name }}`, are J2 variables. They are replaced by the real values of the devices during template rendering. For example, `{{ device.name }}` will be replaced by the name of the specific device.
- **Control Blocks:** Control blocks, such as `{% if condition %} ... {% endif %}`, allow conditional logic and loops. They are used to check if a condition is true (`if`) or to iterate over a list of items (`for`). This is useful for handling cases where information may or may not be available.
- **Python Underneath:** J2 templates use the Jinja2 template language, which is based on Python. Therefore, you can use Python syntax to create custom logic within your templates. This includes the use of conditionals, loops, and custom functions.

Now that we have explained how it works, here are the available variables for devices registered in NetBox.

## Variables and Usage

| Name | Command | Description | Return Example |
| --- | --- | --- | --- |
| Device Name | {{ <http://device.name/> }} | Device name | Device name |
| Device Type | {{ device.device_type.name if device.device_type else 'N/A' }} | Device type | Device type (or 'N/A' if no type) |
| Site | {{ <http://device.site.name/> if device.site else 'N/A' }} | Site name | Site name (or 'N/A' if no site) |
| Status | {{ device.status if device.status else 'N/A' }} | Device status | Device status (or 'N/A' if no status) |
| Serial Number | {{ device.serial if device.serial else 'N/A' }} | Device serial number | Device serial number (or 'N/A' if no serial number) |
| Primary IP | {{ device.primary_ip.address if device.primary_ip.address else 'N/A' }} | Device primary IP address | Device primary IP address (or 'N/A' if no primary IP) |
| Platform | {{ device.platform if device.platform else 'N/A' }} | Device platform | Device platform (or 'N/A' if no platform) |
| Rack | {{ <http://device.rack.name/> if device.rack else 'N/A' }} | Rack name | Rack name (or 'N/A' if no rack) |
| Asset Tag | {{ device.asset_tag if device.asset_tag else 'N/A' }} | Device asset tag | Device asset tag (or 'N/A' if no asset tag) |
| Comments | {{ device.comments }} | Device comments | Device comments (or blank) |
| Interface Name | {{ <http://interface.name/> if <http://interface.name/> else 'N/A' }} | Interface name | Interface name (or 'N/A' if no name) |
| Type | {{ interface.type if interface.type else 'N/A' }} | Interface type | Interface type (or 'N/A' if no type) |
| MAC Address | {{ interface.mac_address if interface.mac_address else 'N/A' }} | Interface MAC address | Interface MAC address (or 'N/A' if no MAC address) |
| IP Addresses | {{ ip.address }} | Interface IP addresses (multiple may be present) | List of interface IP addresses |
| Operational Status | {{ interface.enabled if interface.enabled else 'N/A' }} | Interface operational status | Interface operational status (or 'N/A' if no operational status) |
| Admin Status | {{ interface.enabled if interface.enabled is defined else 'N/A' }} | Interface administrative status | Interface administrative status (or 'N/A' if no administrative status) |
| VLANs | {% for vlan in interface.untagged_vlan.all() %}{{ vlan.vid }} {% endfor %} | Interface VLANs | List of interface VLANs (if any) |

## Example

This rendering template is designed to generate interface configurations in the appropriate format for a Juniper router. It iterates over all the device interfaces in NetBox that have associated IP addresses and generates configurations for those interfaces.

Here's how the template works:

```
{%- for interface in device.interfaces.all() -%}
    {%- if interface.ip_addresses.all() %}
    {{ interface.name.split('.')[0].split(':')[0] }} {
        unit 0 {
            family inet {
                {%- for ip in interface.ip_addresses.all() %}
                address {{ ip }};
                {%- endfor %}
            }
        }
    }
    {%- endif %}
{%- endfor %}

```

The generated output after rendering this template will be something like the following:

```
ge-0/0/0 {
    unit 0 {
        family inet {
            address 192.168.1.1/24;
            address 10.0.0.1/30;
        }
    }
}
ge-0/0/1 {
    unit 0 {
        family inet {
            address 172.16.0.1/24;
        }
    }
}

```

In this example:

- The loop `{%- for interface in device.interfaces.all() -%}` iterates through all the device's interfaces in NetBox.
- The condition `{%- if interface.ip_addresses.all() %}` checks if the interface has IP addresses associated with it.
- `{{ interface.name.split('.')[0].split(':')[0] }}` is used to extract the interface name in the desired format. For example, if the interface name is "ge-0/0/0.0:1", it will be converted to "ge-0/0/0".
- The template then generates the configurations for each interface, including the IP address (obtained from the loop `{%- for ip in interface.ip_addresses.all() %}`).

The resulting output is a series of interface configurations formatted correctly for a Juniper device. Each interface has its own configuration, including its name and IP address, if applicable.