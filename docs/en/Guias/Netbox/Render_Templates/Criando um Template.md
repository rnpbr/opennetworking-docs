# Configuration Template Creation

## How Does Render Template Work in NetBox?

"Render Template" in NetBox is a powerful feature that allows network administrators to automate the generation of network device configurations based on predefined configuration templates. It simplifies the process of device deployment and maintenance, making it more efficient and less prone to human error. Here's how it works:

1. **Configuration Template Creation:** First, administrators create configuration templates using the Jinja2 templating language. These templates serve as structures for the desired device configurations.
2. **Incorporating Variables:** Configuration templates can incorporate J2 variables, which are placeholders for dynamic information. These variables are replaced with device-specific data when the template is rendered.
3. **Association to Devices:** Each configuration template is associated with a specific device type. This allows NetBox to know which configuration templates to use for each device based on its type.
4. **Automated Rendering:** When an administrator creates or updates a device in NetBox, the "Render Template" comes into action. NetBox identifies the device type and the corresponding configuration template.
5. **Populating with Real Data:** The J2 variables in the configuration template are populated with real device data, such as its name, location, IP address, and more.
6. **Configuration Generation:** NetBox automatically generates a complete configuration for the device, applying the values of the J2 variables to the configuration template. This creates a custom, ready-to-use configuration.
7. **Configuration Application:** The generated configuration can be deployed to the device via traditional methods, such as SSH/SCP file transfer, or integrated with configuration management tools for further automation.

In summary, "Render Template" in NetBox simplifies the process of configuring network devices by allowing the creation of flexible templates and automating the generation of configurations based on device information. This saves time, reduces errors, and facilitates network infrastructure maintenance.

- **{{ }} - J2 Variables:** Expressions within double curly braces, like `{{ device.name }}`, are J2 variables. They are replaced with the actual values of the devices during template rendering. For example, `{{ device.name }}` will be replaced by the specific device's name.
- **Control Blocks:** Control blocks, such as `{% if condition %} ... {% endif %}`, allow conditional logic and loops. They are used to check if a condition is true (`if`) or to iterate over a list of items (`for`). This is useful for handling cases where information may or may not be available.
- **Python Underneath:** J2 templates use the Jinja2 templating language, which is based on Python. Therefore, you can use Python syntax to create custom logic within your templates. This includes using conditionals, loops, and custom functions.

Now that we have explained how it works, here are the available variables for devices registered in NetBox.

## Variables and Usage

| Name | Command | Description | Example Return |
| --- | --- | --- | --- |
| Device Name | {{ <http://device.name/> }} | Device Name | Device Name |
| Device Type | {{ device.device_type.name if device.device_type else 'N/A' }} | Device Type | Device Type (or 'N/A' if no type) |
| Site | {{ <http://device.site.name/> if device.site else 'N/A' }} | Site Name | Site Name (or 'N/A' if no site) |
| Status | {{ device.status if device.status else 'N/A' }} | Device Status | Device Status (or 'N/A' if no status) |
| Serial Number | {{ device.serial if device.serial else 'N/A' }} | Device Serial Number | Device Serial Number (or 'N/A' if no serial number) |
| Primary IP | {{ device.primary_ip.address if device.primary_ip.address else 'N/A' }} | Device Primary IP Address | Device Primary IP Address (or 'N/A' if no primary IP) |
| Platform | {{ device.platform if device.platform else 'N/A' }} | Device Platform | Device Platform (or 'N/A' if no platform) |
| Rack | {{ <http://device.rack.name/> if device.rack else 'N/A' }} | Rack Name | Rack Name (or 'N/A' if no rack) |
| Asset Tag | {{ device.asset_tag if device.asset_tag else 'N/A' }} | Device Asset Tag | Device Asset Tag (or 'N/A' if no asset tag) |
| Comments | {{ device.comments }} | Device Comments | Device Comments (or blank) |
| Interface Name | {{ <http://interface.name/> if <http://interface.name/> else 'N/A' }} | Interface Name | Interface Name (or 'N/A' if no name) |
| Type | {{ interface.type if interface.type else 'N/A' }} | Interface Type | Interface Type (or 'N/A' if no type) |
| MAC Address | {{ interface.mac_address if interface.mac_address else 'N/A' }} | Interface MAC Address | Interface MAC Address (or 'N/A' if no MAC address) |
| IP Addresses | {{ ip.address }} | Interface IP Addresses (multiple may be present) | List of Interface IP Addresses |
| Operational Status | {{ interface.enabled if interface.enabled else 'N/A' }} | Interface Operational Status | Interface Operational Status (or 'N/A' if no operational status) |
| Admin Status | {{ interface.enabled if interface.enabled is defined else 'N/A' }} | Interface Administrative Status | Interface Administrative Status (or 'N/A' if no administrative status) |
| VLANs | {% for vlan in interface.untagged_vlan.all() %}{{ vlan.vid }} {% endfor %} | Interface VLANs | List of Interface VLANs (if any) |

## Example

This rendering template is designed to generate interface configurations in the appropriate format for a Juniper router. It iterates through all the device's interfaces in NetBox that have associated IP addresses and generates configurations for those interfaces.

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

The output generated after rendering this template will be similar to the following:

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