
# ELK-Lab

Este laboratório simula, via Containerlab, a interligação entre três roteadores representando a conexão GO–MS–MT no backbone da RNP, com roteamento dinâmico via OSPF, exportação de fluxos via IPFIX e análise/visualização via Elastic Stack (Elasticsearch, Kibana, Fleet Server e Elastic Agent).

---

## 1. Descrição

### Objetivo do Lab

O laboratório `elk-lab` tem como principal objetivo simular o envio e análise de fluxos de tráfego IPFIX em uma topologia de três roteadores interligados (GO, MS e MT), utilizando OSPF para roteamento dinâmico e ferramentas do Elastic Stack para observabilidade e análise de tráfego em tempo real.

**Topologia do Lab**
[Topologia do Lab](../../../img/labs_imgs/Topologia_ELK.svg)

**Descrição da Topologia**

* Três roteadores (GO, MS, MT) interligados em topologia linear com links ponto a ponto /31.
* Roteamento dinâmico via OSPF.
* Exportação de fluxos IPFIX para o **Fleet Server**.
* Elastic Agent instalado para recebimento dos fluxos e envio ao Elasticsearch.
* Visualização de dados e análise via Kibana.
* Rede externa `br-lab` conecta os elementos de rede à pilha ELK.

---

## 2. Aplicações

### Exemplos de Aplicações

O `elk-lab` pode ser aplicado a diferentes contextos educacionais e de pesquisa, permitindo a simulação de cenários reais de exportação de tráfego e análise com Elastic Stack.

#### Possíveis Aplicações:

* **Ensino de IPFIX em ambientes reais**: Aplicação prática da exportação de fluxos para ferramentas de análise.
* **Capacitação em Elastic Stack para redes**: Demonstra a integração do IPFIX com Elastic Agent e o uso de dashboards no Kibana.
* **Análise forense e de tráfego de rede**: Suporte a estudos sobre padrões de tráfego, anomalias e ameaças.
* **Integração com SIEMs baseados em Elasticsearch**: Avaliação de pipelines de dados para uso com segurança de redes.
* **Visualização de fluxos de tráfego**: Composição de dashboards dinâmicos em tempo real.

---

## 3. Requisitos

Abaixo estão listados os requisitos mínimos de hardware e software necessários para executar o laboratório. Certifique-se de incluir as ferramentas essenciais, como **Containerlab** e **Docker**, além da rede `br-lab`.
para saber mais sobre este itens acesse: [Primeiros Passos - preparando o ambiente](../../Ferramentas/Primeiros passos - preparando o ambiente.md).

E tenha a stack ELK previamente instalado, para saber mais sobre a instalação do zabbix acesse: [Instalação do ELK](../../Ferramentas/Elasticsearch/index.md)

### 🖥️ Tabela de Requisitos

| Requisito           | Detalhes              |
| ------------------- |-----------------------|
| **CPUs**            | 6 vCPUs               |
| **Memória RAM**     | 16 GB                 |
| **Espaço em Disco** | 15 GB (recomendado)   |
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

## 4. Implantação do Lab

### 4.1 Download e Preparação

Execute o script abaixo para baixar os arquivos do laboratório:

=== "Linux/Mac"

    ```bash
    curl -L -o get.sh "https://git.rnp.br/redes-abertas/labs/-/raw/main/elk-lab/get.sh?ref_type=heads&inline=false" && sh get.sh && cd elk-lab
    ```


=== "Windows"

    ```bash
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/labs/-/raw/main/elk-lab/get.bat?ref_type=heads&inline=false" && call get.bat && cd elk-lab
    ```


---

## 5. Acesso aos Dispositivos

### 5.1 IPs e Portas

| Dispositivo       | IP de Acesso  | Porta(s) | Serviço           |
| ----------------- |---------------| -------- | ----------------- |
| **Roteador GO**   | 172.10.10.6   | 22       | SSH               |
| **Roteador MS**   | 172.10.10.7   | 22       | SSH               |
| **Roteador MT**   | 172.10.10.8   | 22       | SSH               |
| **Fleet Server**  | 172.10.10.110 | 8220     | Ingestão de dados |
| **Elasticsearch** | 172.10.10.108 | 9200     | Banco de dados    |
| **Kibana**        | 172.10.10.109 | 5601     | Interface Web     |

### 5.2 Credenciais de Acesso

| Serviço        | Usuário                                            | Senha         |
| -------------- | -------------------------------------------------- |---------------|
| SSH Roteadores | `admin`                                            | `admin@123`   |
| Kibana         | `elastic`                                          | `admin@123`   |


---

## 6. Coleta e Exportação de Fluxos
Para configurar a coleta de dados utilizando o IPFIX, com nosso guia de [configuração de IPFIX](../../Ferramentas/Elasticsearch/Configurando IPFIX no ELK.md).
