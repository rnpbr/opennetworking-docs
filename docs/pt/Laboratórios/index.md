# Containerlab

**Containerlab** é uma ferramenta poderosa para criar e gerenciar laboratórios de rede virtualizados. Com ele, você pode simular topologias de rede complexas utilizando contêineres Docker. A seguir, você encontrará informações sobre os pré-requisitos, ferramentas recomendadas e como documentar seus laboratórios.

---

## Pré-requisitos

Antes de começar a utilizar o Containerlab, certifique-se de ter os seguintes pré-requisitos instalados:

### Docker

- O Docker é utilizado pelo Containerlab para criar e executar os contêineres que compõem a rede virtualizada.
- **Link**: [Documentação oficial do Docker](https://www.docker.com/get-started/).

### Containerlab

- Instale o Containerlab conforme as instruções fornecidas na documentação oficial.
- **Link**: [Documentação oficial do Containerlab](https://containerlab.dev/install/).

---

## Labs Disponíveis

Aqui está um exemplo de laboratório configurado para simular OSPF utilizando Junos:

### OSPF (Junos)

- Simulação de OSPF com Junos, uma das tecnologias de roteamento mais utilizadas.
- **Link**: [OSPF (Junos) Lab](ospf-lab/index.md).

### Discovery (Junos)

- Importação de roteadores com scripts, utilizando Zabbix e Netbox.
- **Link**: [Discovery (Junos) Lab](Lab Descoberta/index.md).

### ELK-Lab (Junos)
- Exportação de fluxos IPFIX para Elasticsearch com Elastic Agent.
- Visualização dos fluxos em tempo real com dashboards no Kibana.
- **Link**: [ELK-Lab (Junos)](ELK-Lab/index.md).

### Telegraf-Lab (junos)
- Exportação de fluxos de tráfego via Telegraf/IPFIX para InfluxDB.
- Dashboards prontos no Grafana para análise de tráfego por interface e protocolo.
- **Link**: [Telegraf-Lab (Junos)](Telegraf-Lab/index.md).

### Zabbix-Lab (junos)
- Monitoramento de roteadores via SNMP com coleta centralizada pelo Zabbix Server.
- Permite visualização de métricas e alertas em tempo real no frontend do Zabbix.
- **Link**: [Zabbix-Lab (Junos)](Zabbix-Lab/index.md).
---

## Ferramentas de Análise Recomendadas

Além do Containerlab, você pode utilizar as seguintes ferramentas de análise para monitorar e depurar sua rede virtualizada:

### LibreNMS

- Uma plataforma de monitoramento de rede baseada na web, que fornece insights sobre o desempenho e a saúde da rede. Ideal para monitoramento contínuo da rede em tempo real.

### Wireshark

- Ferramenta de captura e análise de pacotes que permite examinar o tráfego de rede em detalhes. Essencial para depuração e análise de protocolos de rede.

além destas ferramentas mencionadas ha outras que podem ser configuradas conforme suas necessidades, para saber mais acesse: [Ferramentas de Análise](../Ferramentas/index.md).


---

## Documentando Seus Labs

Para garantir que seus laboratórios sejam bem documentados e fáceis de entender, consulte a seção sobre **Documentação de Labs**. Lá, você encontrará boas práticas e exemplos para criar documentação clara e útil para os seus ambientes simulados.

- **Link**: [Documentação de Labs](Contribua/index.md).