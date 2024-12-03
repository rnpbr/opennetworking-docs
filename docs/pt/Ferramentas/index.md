# Ferramentas

## :octicons-book-24: **Introdução**

Antes de começar a usar as ferramentas de monitoramento, é fundamental configurar a base de comunicação entre os seus laboratórios. Para isso, utilizamos uma rede Docker dedicada chamada **br-lab**. A rede **br-lab** facilita a integração de ferramentas de análise com os laboratórios criados no Containerlab, eliminando a necessidade de configurar repetidamente cada ferramenta para diferentes laboratórios.

### :octicons-gear-24: **Passo 1: Configuração da Rede Docker br-lab**

Acesse o [Guia de Configuração da Rede br-lab](Primeiros passos: preparando o ambiente.md) para configurar sua rede Docker. Essa rede será responsável por conectar seus laboratórios ao sistema de monitoramento de forma eficiente, permitindo que múltiplas ferramentas funcionem de maneira integrada.

---

## :octicons-search-24: **Passo 2: Escolhendo a Ferramenta de Monitoramento**

Após configurar a rede **br-lab**, você poderá selecionar a ferramenta que melhor atenda às suas necessidades. Cada uma das ferramentas listadas abaixo oferece funcionalidades específicas para diferentes tipos de monitoramento, seja de dispositivos de rede, tráfego ou logs.

### :material-compare-horizontal: **Comparação de Ferramentas**

A tabela a seguir oferece uma visão geral das ferramentas que cobrimos em nossos tutoriais, destacando seus principais recursos, tipo de monitoramento e opções de preço:

!!! warning "EM DESENVOLVIMENTO"
    **Comparação das Ferramentas em Desenvolvimento sujeito a alteração**

| Ferramenta | Tipo de Monitoramento | Principais Recursos | Preço | Melhor Uso |
| --- | --- | --- | --- | --- |
| **ELK Stack** | Logs e eventos | Análise de logs, visualizações em tempo real | Gratuito (opções pagas) | Auditoria de logs e segurança |
| **LibreNMS** | Dispositivos de rede (SNMP) | Monitoramento SNMP, alertas, gráficos históricos | Gratuito | Monitoramento de dispositivos de rede |
| **EDSHARK** | Captura de pacotes | Análise detalhada de pacotes de rede | Gratuito | Troubleshooting e análise de tráfego |

---

## :material-test-tube: **Passo 3: Implementação e Testes**

Após selecionar a ferramenta mais adequada, siga os tutoriais específicos para configurar e integrar a solução escolhida com seu ambiente de rede criado no **Containerlab**. Cada guia oferece instruções passo a passo para garantir uma integração suave e funcional das ferramentas de monitoramento com seus laboratórios.

### :octicons-tools-24: **Exemplos de Cenários de Teste**:

- **Monitoramento de Dispositivos de Rede com LibreNMS**: Configure LibreNMS para monitorar switches e roteadores dentro do seu laboratório.
- **Análise de Logs e Eventos com ELK Stack**: Colete e visualize dados de logs gerados por dispositivos da rede.
- **Captura de Pacotes com EDSHARK**: Execute diagnósticos de rede e analise pacotes capturados diretamente dos roteadores.

---

## :material-tools: **Ferramentas Futuras**

Estamos constantemente testando e adicionando novas ferramentas ao nosso repertório. Algumas opções que consideramos explorar em breve incluem:

- **Zabbix**: Plataforma de monitoramento e visualização de dados.
- **Grafana**: Plataforma de monitoramento e visualização de dados.
- **Prometheus**: Servidor de monitoramento e visualização de dados.
- **Telegraf**: Coletor de métricas que se integra ao Prometheus e outros sistemas de monitoramento.
- **OpenElastic**: Uma solução escalável e flexível para auditoria de logs e eventos, baseada no Elastic Stack.
- **OpenNMS**: Ferramenta robusta para monitoramento de redes e sistemas, com foco em redes de grande escala.

Essas ferramentas podem ser integradas ao seu ambiente de laboratório com o **Containerlab**, 
permitindo que você crie um ecossistema robusto para gerenciamento e análise de redes.

---