## Introdução

Este laboratório simula uma rede com 3 roteadores em uma topologia em anel, configurados utilizando OSPF para roteamento dinâmico e SNMP para envio de telemetria pela rede.

## **1. Topologia e Configurações**

A topologia consiste em três roteadores (PB, PE, JPA) conectados em um anel. Cada roteador está configurado com interfaces de rede e endereços IP, além de protocolos OSPF para roteamento e SNMP para monitoramento, como podemos ver na imagem a seguir.

![Topologia.png](./Topologia.png)

Os roteadores estão configurados com as seguintes tecnologias:

- **OSPF (Open Shortest Path First)**: Utilizado para roteamento dinâmico na rede, permitindo que os roteadores troquem informações sobre rotas e atualizações de topologia.
- **SNMP (Simple Network Management Protocol)**: Utilizado para monitoramento e gerenciamento da rede, permitindo o acesso a informações de telemetria dos dispositivos.

## **2. Execução**

Para iniciar o laboratório, siga estas etapas:

1. Tenha os pre-requisitos devidamente instalados
2. execute este comando

```bash
Comando para subir via gitlab aqui
```

## **3. Acesso**

Existem duas formas de acesso aos dispositivos na rede:

- **Acesso via SSH aos roteadores**: Utilize um cliente SSH para se conectar aos roteadores utilizando o endereço IP de cada dispositivo ou o nome atribuído pelo Containerlab, juntamente com as credenciais de login fornecidas. O endereço IP de gerência de cada roteador é exibido após a execução do laboratório pelo Containerlab.

    Exemplo:

    ```bash
    
    ssh admin@<endereço_IP_do_roteador>
    ```

    ou

    ```bash
    
    ssh admin@<nome_do_roteador>
    ```

- **Acesso ao Graphite (Servidor de Tepologia)**: Acesse o Graphite através do navegador utilizando o endereço IP e a porta configurados. Você também pode acessar diretamente clicando no ícone de SSH no roteador desejado.

    URL: **`http://<endereço_IP_do_Graphite>:8080/graphite/`**

    Credenciais:

  - Usuário: admin
  - Senha: admin@123

## **4. Monitoramento**

Para monitorar a rede e os dispositivos, você pode utilizar ferramentas como edgeshark para análise de pacotes ou ferramentas de monitoramento SNMP.

- **edgeshark**: Capture e analise o tráfego de rede para diagnóstico de problemas e monitoramento de desempenho.
- **Monitoramento SNMP**: Utilize ferramentas compatíveis com SNMP para monitorar métricas de desempenho e saúde da rede.
