# Telegraf Lab

Este laboratório simula, via Containerlab, a interligação entre três roteadores representando a conexão GO–MS–MT no backbone da RNP, com roteamento dinâmico via OSPF, exportação de fluxos via IPFIX e monitoramento via SNMP/Telemetria usando Telegraf, InfluxDB, Chronograf e Grafana.

---

## 1. Descrição

### Objetivo do Lab

O laboratório `telegraf-lab` tem como principal objetivo simular o monitoramento de tráfego de uma topologia com três roteadores interligados (GO, MS e MT), utilizando protocolos de roteamento dinâmico (OSPF), exportação de fluxos (IPFIX) e monitoramento com SNMP. A coleta e visualização de métricas de rede são realizadas com ferramentas modernas de observabilidade: **Telegraf**, **InfluxDB**, **Chronograf** e **Grafana**.

**Topologia do Lab**
[Topologia do Lab](../../../img/labs_imgs/Topologia_Telegraf.svg)

**Descrição da Topologia**

* Três roteadores (GO, MS, MT) interligados em topologia linear com links ponto a ponto /31.
* Roteamento dinâmico via OSPF entre os roteadores.
* Coleta de métricas de tráfego via IPFIX e SNMP.
* Observabilidade com a pilha TICK (Telegraf, InfluxDB, Chronograf) e Grafana.
* Rede externa `br-lab` conecta os nós à infraestrutura de monitoramento.

---

## 2. Aplicações

### Exemplos de Aplicações

Este laboratório pode ser explorado em diversos cenários acadêmicos e de pesquisa aplicada, servindo como base para experimentação de monitoramento e visualização de tráfego em redes com múltiplos roteadores.

#### Possíveis Aplicações:

* **Capacitação de equipes de redes e NOC**: Simula operações reais com OSPF, IPFIX e SNMP, facilitando a análise de comportamento de tráfego.
* **Análise de tráfego com IPFIX**: Permite exportar fluxos e estudar padrões de tráfego entre domínios.
* **Visualização de métricas com Grafana**: Apoia estudos de desempenho, gargalos e picos de utilização de rede.
* **Monitoramento distribuído com Telegraf**: Avalia a coleta simultânea de dados de múltiplos roteadores com diferentes protocolos.
* **Ensino de protocolos de roteamento e telemetria**: Ambiente ideal para aulas práticas de redes avançadas.

---

## 3. Requisitos

Abaixo estão listados os requisitos mínimos de hardware e software necessários para executar o laboratório. Certifique-se de incluir as ferramentas essenciais, como **Containerlab** e **Docker**, além da rede `br-lab`.
para saber mais sobre este itens acesse: [Primeiros Passos - preparando o ambiente](../../Ferramentas/Primeiros passos - preparando o ambiente.md).

E tenha a stack telegraf previamente instalado, para saber mais sobre a instalação do zabbix acesse: [Instalação do Telegraf](../../Ferramentas/Telegraf/index.md)

### 🖥️ Tabela de Requisitos

| Requisito           | Detalhes              |
| ------------------- |-----------------------|
| **CPUs**            | 6 vCPUs               |
| **Memória RAM**     | 12 GB                 |
| **Espaço em Disco** | 10 GB (recomendado)   |
| **Containerlab**    | 0.45.0 ou superior    |
| **Docker Engine**   | 23.0.3 ou superior    |
| **Imagens**         | `vr-vjunos:23.2R1.14` |
| **Rede Docker**     | `br-lab`              |

!!! warning "Atenção" 
    Verifique se o seu processador possui **suporte à virtualização por hardware** e se essa funcionalidade está **ativada na BIOS/UEFI**.  
    - Em processadores **Intel**, essa tecnologia é chamada de **VT-x** (Intel Virtualization Technology).  
    - Em processadores **AMD**, é conhecida como **AMD-V** (AMD Virtualization).  

    Sem essa funcionalidade ativada, as imagens como o **vJunos-router** não funcionarão corretamente, pois exigem execução em containers no modo `--privileged` com permissões estendidas (como `SYS_ADMIN`) e suporte à emulação de hardware.

---

## 4. Implantando o Lab

Você pode realizar a implantação por meio de um script pronto ou configurar manualmente os arquivos do lab.

### 4.1 Implantação Pronta

Execute o script abaixo para baixar e configurar o laboratório automaticamente:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/telegraf-lab/get.sh?ref_type=heads&inline=false" && sh get.sh && cd telegraf-lab
    ```

=== "Windows"

    ```bat
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/telegraf-lab/get.bat?ref_type=heads&inline=false" && call get.bat && cd telegraf-lab
    ```

!!! tip "Dica"
    No Linux/Mac, use `chmod +x get.sh` antes de executar o script, caso ele não esteja com permissão de execução.

---

## 5. Inicializando o Lab

Dentro do diretório baixado, inicie o laboratório com:

```bash
sudo containerlab deploy
```

Esse comando criará os containers dos roteadores, configurará os links e iniciará os serviços de monitoramento.

!!! tip "Depuração"
    Use `docker logs -f <nome_container>` para verificar o estado dos serviços, caso algo não funcione.

---

## 6. Acesso aos Dispositivos

### 6.1 IPs e Portas dos Serviços

| Dispositivo     | IP de Acesso  | Porta(s) | Serviço            |
| --------------- | ------------- |-----| ------------------ |
| **Roteador GO** | 172.10.10.6   | 22  | SSH                |
| **Roteador MS** | 172.10.10.7   | 22  | SSH                |
| **Roteador MT** | 172.10.10.8   | 22  | SSH                |
| **Telegraf**    | 172.10.10.114 | 161 | Coleta de métricas |
| **InfluxDB**    | 172.10.10.112 | 8086 | Banco de séries    |
| **Chronograf**  | 172.10.10.113 | 8888 | UI de análise      |
| **Grafana**     | 172.10.10.111 | 3000 | Dashboard Web      |
| **Graphite** | 172.10.10.119 | 8080    | Web UI (Graphite) |
### 6.2 Senhas de Acesso

| Serviço          | Usuário | Senha             |
| ---------------- | ------- |-------------------|
| Roteadores (SSH) | `admin` | `admin@123`       |
| Grafana          | `admin` | `admin`           |
| InfluxDB         | `admin` | `influxpassword`  |

!!! warning "Verificação de Inicialização"
    Antes de acessar os serviços, use `docker ps` e verifique os logs dos containers para garantir que estão funcionando corretamente.

---

## 7. Observabilidade e Visualização

### 7.1 Telegraf

O Telegraf está configurado para coletar métricas via:

* **SNMP**: leitura periódica dos roteadores.
* **IPFIX**: exportação de fluxos de tráfego.
* **Docker e sistema**: coleta de métricas locais dos containers.

### 7.2 InfluxDB

Banco de séries temporais onde as métricas do Telegraf são armazenadas. Pode ser acessado pela porta 8086.

### 7.3 Chronograf

Interface web de análise de métricas armazenadas no InfluxDB. Acessível em `http://172.10.10.113:8888`.

### 7.4 Grafana

Plataforma de visualização interativa onde os dados são apresentados em dashboards personalizados.


