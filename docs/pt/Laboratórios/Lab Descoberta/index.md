# Lab Descoberta

## :material-bookmark: **Introdução**

Este laboratório simula uma rede com 2 roteadores configurados com OSPF e SNMP, integrando o Zabbix e o Netbox para importação e gerenciamento automatizado de dispositivos.

---

## :fontawesome-solid-prescription-bottle: 1. **Descrição**

### :octicons-goal-16: 1.1 **Objetivo do Lab**

O objetivo deste laboratório é importar os dispositivos de rede e suas configurações no Netbox a partir do Zabbix, além de demonstrar o funcionamento básico do roteamento OSPF entre dois roteadores conectados em anel e monitorados via SNMP.


### :material-lan: 1.2 **Topologia do Lab**
Abaixo a topologia em formato imagem, representando os roteadores, servidores e suas conexões.

![Topologia.svg](../../../img/labs_imgs/Topologia_discovery_lab.svg)

Os roteadores estão configurados com as seguintes tecnologias:

- **OSPF (Open Shortest Path First)**: Utilizado para roteamento dinâmico na rede, permitindo que os roteadores troquem informações sobre rotas e atualizações de topologia.
- **SNMP (Simple Network Management Protocol)**: Utilizado para monitoramento e gerenciamento da rede, permitindo o acesso a informações de telemetria dos dispositivos.
---

## :material-tools: **2. Requisitos**
### :material-alert: 2.1 Pré requisitos

Para iniciar o laboratório, é necessário a instalação e configuração dos seguintes componentes:

- Netbox
- Containerlab
- Docker
- Python

Caso o seu ambiente não esteja configurado, siga os passos [Guia de Configuração](/Getting Started)


### :material-alert: 2.2 Tabela de Requisitos Computacionais

| Requisito           | Detalhes |
|---------------------| --- |
| **CPUs**            | 4 vCPUs (mínimo recomendado) |
| **Memória RAM**     | 12 GB |
| **Espaço em Disco** | 10 GB |
| **Containerlab**    | 0.64.0 |
| **Rede Criada**     | br-lab |

!!! tip "Dica" 
    Verifique se a versão do Docker e do Containerlab são compatíveis para evitar erros durante a implantação.
---

## :octicons-tools-16: 3. Instalação

### :material-network-strength-4-cog: 3.1 Configurando a Rede Docker

Antes de iniciar os containers, crie a rede bridge que interligará os dispositivos:

```bash
docker network create \
  --driver=bridge \
  --opt com.docker.network.bridge.name=br-lab \
  --subnet=172.10.10.0/24 \
  br-lab
```

### :material-git: 3.2 Clonando o Repositório do Lab

Clone o repositório do laboratório:
```bash
git clone https://git.rnp.br/redes-abertas/labs/-/tree/main/discovery-lab
```

Entre no repositório:
```bash
cd discovery-lab/
```

---

## :fontawesome-solid-house-chimney: 4. Implantação do Ambiente

### :material-router-wireless: 4.1 Subindo os Roteadores com Containerlab

Inicie a topologia com o comando:

```bash
sudo clab deploy -t clab/discovery-lab.clab.yaml
```
    
!!! warning "Debug" 
    Os dispositivos podem levar cerca de 10 minutos para estarem totalmente operacionais.
    Caso ocorra algum erro, verifique a saída do comando para possíveis mensagens de erro. Use `docker logs <container_name>` para depurar.


### :material-server: 4.2 Levantando o Zabbix
!!! tip "Dica" 
    Caso você já possua um ambiente Zabbix configurado, basta pular esse passo.

Para subir o container com o Zabbix:

```bash
docker compose -f zabbix-docker/docker-compose.yml up -d
```
A interface web do Zabbix ficará disponível na porta 81.

---
## :material-relation-one-to-one: 5. Integração com Zabbix e Netbox
Neste passo é preciso que você crie um token de API tanto no Zabbix quanto no Netbox para adicionar o token no arquivo .env

### :material-import: 5.1 Importação dos Roteadores para o Zabbix

1. Acesse a pasta de scripts:
```bash
cd scripts/
```
2. Crie e ative o ambiente virtual Python:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependências do python:
```bash
pip install -r requirements.txt
```
4. Configure o ambiente com as suas credenciais:
```bash
mv .env.example .env
nano .env
```
Exemplo de .env:
```bash
 # Zabbix
ZABBIX_TOKEN=zabbix_token                     # Token de API 
ZABBIX_URL=http://yourdomain/api_jsonrpc.php  # Url de acesso a API
ZABBIX_USER=Admin                             # Usuário Default
ZABBIX_PASSWORD=zabbix                        # Senha Default
ZABBIX_GROUP=Juniper                          # Grupo à adicionar os roteadores
ZABBIX_TEMPLATE="Juniper by SNMP"             # Template de monitoramento para roteadores Juniper

# Netbox
NETBOX_URL=http://yourdomain/api              # Url de acesso a API
NETBOX_TOKEN=netbox_token                     # Token de API 

# Devices
DEVICE_USERNAME=admin                         # Usuário Default de acesso aos roteadores
DEVICE_PASSWORD=admin@123                     # Senha Default de acesso aos roteadores
```
5. Agora para importar os roteadores para o Zabbix, execute o comando:
```bash
python3 import_zabbix.py
```

### :octicons-key-16: 5.2 Gerando Tokens de API
Criando Token de API no Zabbix.

1. Acesse a interface do Zabbix.
2. Vá em **Usuários** > **Tokens da API**.
3. Clique em **Criar**, preencha e copie o token gerado.
4. Atualize o campo `ZABBIX_TOKEN` no `.env`.

Criando Token de API no Netbox.

1. Acesse a interface do Netbox.
2. Navegue até **Admin** > **API Tokens**.
3. Clique em **Add**, associe a um usuário e copie o token.
4. Atualize o campo `NETBOX_TOKEN` no `.env`.

### :material-import: 5.3 Importação dos Roteadores para o Netbox
Agora com o ambiente totalmente configurado, você pode importar os roteadores ao Netbox com o comando:
```bash
python3 import_netbox.py
```

Com o script bem sucessido, você pode visualizar os roteadores dentro do Netbox com as suas respectivas informações!
___

## :material-access-point: 6. Acesso

Após o laboratório ser iniciado, você poderá acessar os dispositivos e serviços configurados na rede.

### :material-table: 6.1 Tabela de IPs e Portas de Serviço

Aqui está a tabela de dispositivos, IPs e portas de serviço disponíveis no laboratório.

| Dispositivo | IP de Acesso | Porta | Serviço |
| --- | --- | --- | --- |
| **RO** | 172.10.10.101 | 22 | SSH |
| **AC** | 172.10.10.102 | 22 | SSH |
| **Servidor de Monitoramento** | 172.20.20.1 | 8080 | Web (Graphite) |
| **Servidor Zabbix** | 172.10.10.115 | 81 | Zabbix |

### :material-key-link: 6.2 Senhas de Acesso

Aqui está a tabela com as senhas de acesso dos serviços configurados no laboratório.

| Serviço | Usuário | Senha |
| --- | --- | --- |
| **AC (SSH)** | admin | admin@123 |
| **RO (SSH)** | admin | admin@123 |
| **Graphite (Web)** | admin | admin@123 |
| **Servidor Zabbix(Web)** | Admin | zabbix |

!!! warning "Atenção" 
    antes de acessar acesse o log de um dispositivo para verificar se ele foi iniciado e configurado corretamente.
---

## :octicons-rocket-24: 7. Próximos Passos
Com o laboratório finalizado, você pode seguir algum passos abaixo como **extra**.

- Monitorar os roteadores via SNMP na interface do Zabbix.
- Explorar o Netbox para visualizar e gerenciar o inventário da rede.
- Modificar a topologia conforme a necessidade (em futuras versões personalizadas).
- Consultar o guia de OSPF para validar a comunicação dinâmica entre roteadores.
---

### :fontawesome-solid-paintbrush: 8. Conclusão

✅ Pronto! Seu ambiente agora está configurado, monitorado e documentado no Netbox. Sinta-se à vontade para personalizar ou expandir a topologia conforme os objetivos do seu estudo ou projeto.