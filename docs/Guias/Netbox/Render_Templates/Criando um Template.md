# Criação de Templates de configurações

## Como Funciona o Render Template no NetBox?

O "Render Template" no NetBox é uma poderosa funcionalidade que permite aos administradores de rede automatizar a geração de configurações de dispositivos de rede com base em modelos de configuração predefinidos. Ele simplifica o processo de implementação e manutenção de dispositivos, tornando-o mais eficiente e menos propenso a erros humanos. Aqui está como ele funciona:

1. **Criação de Modelos de Configuração:** Primeiro, os administradores criam modelos de configuração usando a linguagem de template Jinja2. Esses modelos servem como estruturas para as configurações desejadas dos dispositivos.
2. **Incorporação de Variáveis:** Os modelos de configuração podem incorporar variáveis J2, que são espaços reservados para informações dinâmicas. Essas variáveis são substituídas por dados específicos de dispositivos quando o template é renderizado.
3. **Associação a Dispositivos:** Cada modelo de configuração é associado a um tipo de dispositivo específico. Isso permite que o NetBox saiba quais modelos de configuração usar para cada dispositivo com base em seu tipo.
4. **Renderização Automatizada:** Quando um administrador cria ou atualiza um dispositivo no NetBox, o "Render Template" entra em ação. O NetBox identifica o tipo de dispositivo e o modelo de configuração correspondente.
5. **Preenchimento com Dados Reais:** As variáveis J2 no modelo de configuração são preenchidas com dados reais do dispositivo, como seu nome, localização, endereço IP, entre outros.
6. **Geração de Configuração:** O NetBox gera automaticamente uma configuração completa para o dispositivo, aplicando os valores das variáveis J2 ao modelo de configuração. Isso cria uma configuração personalizada e pronta para uso.
7. **Aplicação da Configuração:** A configuração gerada pode ser implantada no dispositivo por meio de métodos tradicionais, como transferência de arquivos SSH/SCP, ou integrada a ferramentas de gerenciamento de configuração para automação adicional.

Em resumo, o "Render Template" no NetBox simplifica o processo de configuração de dispositivos de rede, permitindo a criação de modelos flexíveis e automatizando a geração de configurações com base nas informações dos dispositivos. Isso economiza tempo, reduz erros e facilita a manutenção da infraestrutura de rede.

- **{{ }} - Variáveis J2:** As expressões entre chaves duplas, como `{{ device.name }}`, são variáveis J2. Elas são substituídas pelos valores reais dos dispositivos durante a renderização do template. Por exemplo, `{{ device.name }}` será substituído pelo nome do dispositivo específico.
- **Blocos de Controle:** Os blocos de controle, como `{% if condition %} ... {% endif %}`, permitem a lógica condicional e os loops. Eles são usados para verificar se uma condição é verdadeira (`if`) ou para iterar sobre uma lista de itens (`for`). Isso é útil para lidar com casos em que as informações podem ou não estar disponíveis.
- **Python por Baixo:** Os templates J2 usam a linguagem de template Jinja2, que é baseada em Python. Portanto, você pode usar a sintaxe do Python para criar lógica personalizada dentro de seus templates. Isso inclui o uso de condicionais, loops e funções personalizadas.

Agora que explicamos o funcionamento, aqui estão as variáveis disponíveis dos devices cadastrados no netbox

## Variáveis e Uso

| Nome | Comando | Descrição | Exemplo de Retorno |
| --- | --- | --- | --- |
| Device Name | {{ <http://device.name/> }} | Nome do dispositivo | Nome do dispositivo |
| Device Type | {{ device.device_type.name if device.device_type else 'N/A' }} | Tipo do dispositivo | Tipo do dispositivo (ou 'N/A' se não houver tipo) |
| Site | {{ <http://device.site.name/> if device.site else 'N/A' }} | Nome do site | Nome do site (ou 'N/A' se não houver site) |
| Status | {{ device.status if device.status else 'N/A' }} | Status do dispositivo | Status do dispositivo (ou 'N/A' se não houver status) |
| Serial Number | {{ device.serial if device.serial else 'N/A' }} | Número de série do dispositivo | Número de série do dispositivo (ou 'N/A' se não houver número de série) |
| Primary IP | {{ device.primary_ip.address if device.primary_ip.address else 'N/A' }} | Endereço IP primário do dispositivo | Endereço IP primário do dispositivo (ou 'N/A' se não houver IP primário) |
| Platform | {{ device.platform if device.platform else 'N/A' }} | Plataforma do dispositivo | Plataforma do dispositivo (ou 'N/A' se não houver plataforma) |
| Rack | {{ <http://device.rack.name/> if device.rack else 'N/A' }} | Nome do rack | Nome do rack (ou 'N/A' se não houver rack) |
| Asset Tag | {{ device.asset_tag if device.asset_tag else 'N/A' }} | Tag de ativo do dispositivo | Tag de ativo do dispositivo (ou 'N/A' se não houver tag de ativo) |
| Comments | {{ device.comments }} | Comentários do dispositivo | Comentários do dispositivo (ou em branco) |
| Interface Name | {{ <http://interface.name/> if <http://interface.name/> else 'N/A' }} | Nome da interface | Nome da interface (ou 'N/A' se não houver nome) |
| Type | {{ interface.type if interface.type else 'N/A' }} | Tipo da interface | Tipo da interface (ou 'N/A' se não houver tipo) |
| MAC Address | {{ interface.mac_address if interface.mac_address else 'N/A' }} | Endereço MAC da interface | Endereço MAC da interface (ou 'N/A' se não houver endereço MAC) |
| IP Addresses | {{ ip.address }} | Endereços IP da interface (vários podem estar presentes) | Lista de endereços IP da interface |
| Operational Status | {{ interface.enabled if interface.enabled else 'N/A' }} | Status operacional da interface | Status operacional da interface (ou 'N/A' se não houver status operacional) |
| Admin Status | {{ interface.enabled if interface.enabled is defined else 'N/A' }} | Status administrativo da interface | Status administrativo da interface (ou 'N/A' se não houver status administrativo) |
| VLANs | {% for vlan in interface.untagged_vlan.all() %}{{ vlan.vid }} {% endfor %} | VLANs da interface | Lista de VLANs da interface (se houver) |

## Exmplo

Este template de renderização é projetado para gerar configurações de interfaces no formato adequado para um roteador Juniper. Ele percorre todas as interfaces do dispositivo no NetBox que têm endereços IP associados e gera configurações para essas interfaces.

Aqui está como o template funciona:

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

A saída gerada após a renderização deste template será algo semelhante ao seguinte:

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

Neste exemplo:

- O loop `{%- for interface in device.interfaces.all() -%}` percorre todas as interfaces do dispositivo no NetBox.
- A condição `{%- if interface.ip_addresses.all() %}` verifica se a interface tem endereços IP associados a ela.
- `{{ interface.name.split('.')[0].split(':')[0] }}` é usado para extrair o nome da interface no formato desejado. Por exemplo, se o nome da interface for "ge-0/0/0.0:1", ele será convertido em "ge-0/0/0".
- O template então gera as configurações para cada interface, incluindo o endereço IP (obtido do loop `{%- for ip in interface.ip_addresses.all() %}`).

A saída resultante é uma série de configurações de interfaces formatadas corretamente para um dispositivo Juniper. Cada interface tem sua própria configuração, incluindo seu nome e endereço IP, se aplicável.
