# :octicons-rocket-24: Render Templates

Render Templates in NetBox are a powerful tool that allows you to generate network configurations dynamically and customized for each device. These templates use the Jinja2 markup language to process variables and render configuration files based on the information stored in the NetBox database.

## :material-folder-cog: 1. Adding Templates

### :material-remote-desktop: 1.1 Remote Templates

Remote templates are available online in a Git repository. To add our template repository, follow the steps below:

#### :material-git: Adding the Repository

1.  Access NetBox and go to **Customization > Data Sources > Add**.
2.  Define a name of your choice and select the type as **Git**.
3.  In the URL, add the following link to use the template:

    ```bash
    https://git.rnp.br/redes-abertas/config-templates-data-source.git
    ```

!!! warning "Attention"
    If the repository is private, add your authentication method in the backend parameters.

4.  Click **Create**.
5.  Click on the data source that was created and then click **Sync** to perform the repository analysis.

    If the synchronization is successful, a "Completed" message will appear in the Status section.

6.  Now, you can view the templates in the **Provisioning > Configuration Templates** tab.

### :material-monitor: 1.2 Local Templates

To add local templates, follow these steps:

1.  Access NetBox and go to **Provisioning > Configuration Templates > Add**.
2.  Add a name, a description, and, in **Data**, enter the Jinja2 code of the template you want to add. Fill in the other attributes as needed.

Here is an example of a generic Jinja2 template:

```jinja
Device Information:
------------------------------------------
Device Name: {{ device.name }}
Device Type: {{ device.device_type.name if device.device_type else 'N/A' }}
Site: {{ device.site.name if device.site else 'N/A' }}
Status: {{ device.status if device.status else 'N/A' }}
Serial Number: {{ device.serial if device.serial else 'N/A' }}
{% if device.primary_ip %}
Primary IP: {{ device.primary_ip.address if device.primary_ip.address else 'N/A' }}
{% endif %}
Platform: {{ device.platform if device.platform else 'N/A' }}
Rack: {{ device.rack.name if device.rack else 'N/A' }}
Asset Tag: {{ device.asset_tag if device.asset_tag else 'N/A' }}
{% if device.comments %}
Comments: {{ device.comments }}
{% endif %}

Interfaces Information:
----------------------------------------------
{% for interface in device.interfaces.all() %}
Interface Name: {{ interface.name if interface.name else 'N/A' }}
Type: {{ interface.type if interface.type else 'N/A' }}
MAC Address: {{ interface.mac_address if interface.mac_address else 'N/A' }}
{% if interface.ip_addresses %}
IP Addresses: {% for ip in interface.ip_addresses.all() %}
              {{ ip.address }}
              {% endfor %}
{% endif %}
Operational Status: {{ interface.enabled if interface.enabled else 'N/A' }}
Admin Status: {{ interface.enabled if interface.enabled is defined else 'N/A' }}
{% if interface.untagged_vlan %}
VLANs: {% for vlan in interface.untagged_vlan.all() %}
       {{ vlan.vid }}
       {% endfor %}
{% endif %}
----------------------------------------------
{% endfor %}
```

3.  After entering all the information, click **Create**.

## :octicons-link-24: 2. Associating Templates to Devices

To associate a template to a specific device:

1.  Select the device in **Devices > Devices**.
2.  Click **Edit** or the pencil icon in the right corner.
3.  Look for the **Management > Configuration Template** section.

    In this tab, you will see all available configurations.

!!! info "Note"
    Pay attention to the device's system, as configuration templates are created differently for different systems.

4.  After selecting the desired template, click **Save**.
5.  To view the template, access the device and click **Render Config**. This will render the specific configuration for the device dynamically.

## :material-skip-next: Next Steps

If you want to create other templates and learn more about how the template base works, click [here](Criando um Template.md).