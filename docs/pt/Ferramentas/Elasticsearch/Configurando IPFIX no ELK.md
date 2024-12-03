# Configurando IPFIX no ELK

## :octicons-book-24: Introdução

O IPFIX (Internet Protocol Flow Information Export) é um padrão para exportação de informações de fluxo de rede, que permite monitorar e analisar o tráfego em tempo real. Este guia é voltado para a configuração do IPFIX na stack ELK (Elasticsearch, Logstash, Kibana). Antes de começar, certifique-se de que você possui os seguintes pré-requisitos:

- **Instalação da Stack ELK**: Consulte o guia de "Getting Started" para instalar o ELK.
- **Acesso ao Fleet**: Certifique-se de que o Fleet está configurado no seu ambiente ELK.


## :material-cursor-default-click: 1. Acesse a Sub-aba Fleet do Management

### O que é o Fleet Server e o Fleet Agent?

- **Fleet Server**: Um componente que gerencia a configuração e a comunicação entre os agentes e o servidor ELK. Ele permite o gerenciamento centralizado de agentes.
- **Fleet Agent**: Uma ferramenta que coleta dados de sistemas e os envia para o servidor ELK, facilitando a análise e monitoramento de dados.

!!! tip "Mais informações"
    para mais informações, acesse a documentação oficial sobre Fleet server: <a href="https://www.elastic.co/guide/en/fleet/current/fleet-server.html" target="_blank">Documentação do Elastic - Fleet</a>

## :material-tools: 2. Modificando a Política do Fleet

### O que são Políticas do Fleet Server?

As políticas do Fleet Server definem como os agentes se comportam, quais integrações são aplicadas e quais dados devem ser coletados. Essas políticas são essenciais para personalizar a coleta de dados conforme as necessidades do seu ambiente.

!!! tip "Mais informações"
    para mais informações, acesse a documentação oficial sobre políticas fleet: <a href="https://www.elastic.co/guide/en/fleet/current/agent-policy.html" target="_blank">Documentação do Elastic - Policies</a>

## :material-cursor-default-click: 3. Acesse a Política Fleet Server Policy

1. Na coluna **Agent Policy**, clique na política chamada **Fleet Server Policy**.
2. Nessa aba, você verá uma lista das integrações disponíveis para o agente.

### O que são Integrações?

As integrações são pacotes que definem como coletar dados de diferentes fontes. Elas facilitam a configuração do agente, permitindo que você adicione recursos e funcionalidades conforme necessário.

!!! tip "Mais informações"
    para mais informações, acesse a documentação oficial sobre integrações: <a href="https://www.elastic.co/guide/en/fleet/current/integrations.html" target="_blank">Documentação do Elastic - Integrações</a>

## :octicons-plus-16: 4. Adicionando a Integração de NetFlow

1. Clique em **Add Integration** e busque por **NetFlow**.
2. Selecione a opção **NetFlow Records**.

### :material-text-box: Resumo da Integração

Após selecionar a integração, será exibido um pequeno resumo explicando o que esta integração faz. Clique em **Add NetFlow Records** para prosseguir.


## :octicons-gear-24: 5. Configuração da Integração

Na aba de configuração, você verá as seguintes opções:

- **IP de Escuta**: O endereço IP onde o agente irá escutar os pacotes IPFIX.
- **Portal de Recepção**: O portal no qual os dados serão recebidos.

!!! warning "Observação"
    Você não precisa modificar essas configurações, pois elas estão definidas para funcionar com a configuração padrão. Para mais informações, acesse a documentação oficial: <a href="https://www.elastic.co/docs/current/integrations/netflow" target="_blank">Documentação do Elastic - Integrações NetFlow</a>


## :octicons-check-16: 6. Finalizando a Configuração

1. Clique em **Save and Continue**.
2. Em seguida, clique em **Save and Deploy Changes** para aplicar as alterações.


