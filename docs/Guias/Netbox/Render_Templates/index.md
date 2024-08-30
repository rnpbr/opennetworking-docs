
# :octicons-rocket-24: Render Templates

Os Render Templates no NetBox são uma poderosa ferramenta que permite gerar configurações de rede de maneira dinâmica e personalizada para cada dispositivo. 
Esses templates utilizam a linguagem de marcação Jinja2 para processar variáveis e renderizar arquivos de configuração com base nas informações armazenadas no banco de dados do NetBox.
## :material-folder-cog: 1. Adicionando Templates

### :material-remote-desktop: 1.1 Templates Remotos

Os templates remotos ficam disponíveis online em um repositório Git. Para adicionar o nosso repositório de templates, siga os passos abaixo:

#### :material-git: Adicionando o Repositório

1. Acesse o NetBox e vá em **Personalização > Fonte de Dados > Adicionar**.
2. Defina um nome de sua escolha e selecione o tipo como **Git**.
3. Na URL, adicione o seguinte link para usar o template:

   ```bash
   https://git.rnp.br/redes-abertas/config-templates-data-source.git
   ```

!!! warning "Atenção"
    Caso o repositório seja privado, adicione o seu método de autenticação nos parâmetros de back-end.

4. Clique em **Criar**.
5. Clique no data source que foi criado e, em seguida, clique em **Sync** para realizar a análise do repositório.

   Se a sincronização for bem-sucedida, aparecerá uma mensagem de "Concluído" na parte de Status.

6. Agora, você poderá visualizar os templates na aba **Provisionamento > Modelos de Configuração**.

### :material-monitor: 1.2 Templates Locais

Para adicionar templates locais, siga estes passos:

1. Acesse o NetBox e vá para **Provisionamento > Modelos de Configuração > Adicionar**.
2. Adicione um nome, uma descrição e, em **Dados**, insira o código Jinja2 do template que deseja adicionar. Preencha as demais atribuições conforme necessário.

Aqui está um exemplo de template Jinja2 genérico:

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

3. Após inserir todas as informações, clique em **Criar**.

## :octicons-link-24: 2. Associando Templates aos Dispositivos

Para associar um template a um dispositivo específico:

1. Selecione o dispositivo em **Dispositivos > Dispositivos**.
2. Clique em **Editar** ou no ícone de lápis no canto direito.
3. Procure pela seção **Gestão > Modelo de Configuração**.

   Nessa aba, você verá todas as configurações disponíveis.

!!! info "Observação"
    Atente-se ao sistema do dispositivo, pois os templates de configuração são criados de forma diferente para sistemas distintos.

4. Após selecionar o template desejado, clique em **Salvar**.
5. Para visualizar o template, acesse o dispositivo e clique em **Render Config**. Isso renderizará a configuração específica para o dispositivo de forma dinâmica.

## :material-skip-next: Próximos Passos

Caso queira criar outros templates e aprender mais sobre o funcionamento da base de templates, clique [aqui](Criando um Template.md).



