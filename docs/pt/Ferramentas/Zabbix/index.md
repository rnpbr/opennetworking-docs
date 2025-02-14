# Guia de Instalação do Zabbix

## :octicons-book-24: 1. Introdução

Este guia apresenta a instalação do **Zabbix**, uma ferramenta de monitoramento de código aberto que será utilizada para coleta e análise de métricas no laboratório **br-lab**. O Zabbix proporciona monitoramento em tempo real de dispositivos, servidores e aplicações, auxiliando na identificação e solução de problemas. A instalação utiliza o Docker Compose para provisionar os serviços de forma ágil e pré-configurada, garantindo uma implementação prática e eficiente no ambiente do laboratório.

---

## :material-network-pos: 2. O que é o Zabbix?

O **Zabbix** é uma plataforma de monitoramento de código aberto que coleta, processa e exibe métricas de desempenho de servidores, aplicações e dispositivos de rede. Ele oferece uma interface gráfica intuitiva, notificações de alertas e relatórios para identificar problemas e ajudar administradores no gerenciamento proativo de suas infraestruturas.

### Principais componentes:
- **Servidor Zabbix**: Processa dados de monitoramento, armazena no banco de dados e envia alertas.
- **Interface Web (Frontend)**: Permite a visualização, configuração e análise das métricas.
- **Agente Zabbix**: Coleta métricas do host onde está instalado.
- **Banco de Dados**: Armazena dados históricos, configurações e estatísticas de desempenho.

---

## :octicons-checklist-24: 3. Pré-requisitos

Certifique-se de atender aos seguintes pré-requisitos antes da instalação:

1. **Rede br-lab configurada**:
    - A rede **br-lab** é obrigatória para isolar os serviços no ambiente. Para mais detalhes sobre essa configuração, consulte o guia [**Primeiros Passos: Preparando o Ambiente**](../Primeiros passos: preparando o ambiente.md).

2. **Pacotes Necessários**:
    - `docker`, `docker-compose`, `curl`.

---

## :octicons-tools-24: 4. Preparando o Ambiente

Para inicializar rapidamente o ambiente do Zabbix na rede **br-lab**, utilizaremos o Docker Compose com um script automatizado.

## :fontawesome-brands-docker: 5. Baixando o Docker Compose

Para baixar o Docker Compose, execute o seguinte comando:

=== "Linux/ Mac"

    ```bash
        curl -L -o get.sh "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/Zabbix/get.sh?inline=false" && sh get.sh && cd Zabbix
    ```

=== "Windows"
```bash
    curl -L -o get.bat "https://git.rnp.br/redes-abertas/docker-composes/-/raw/main/Zabbix/get.bat?inline=false" && call get.bat && cd Zabbix
```

Esse comando faz o download do script de instalação e, em seguida, navega para o diretório **Zabbix**.

---

## :octicons-container-24: 5. Subindo os containers

Para iniciar os serviços do Zabbix, use o comando abaixo:

```bash
docker compose up -d
```

Este comando iniciará os seguintes containers:

1. **PostgreSQL**: Banco de dados que armazena as métricas do Zabbix.
    - **IP**: `172.10.10.118`
    - **Credenciais de acesso**:
        - **Usuario**: `zabbix`
        - **Senha**: `zabbixdatabase`
    - **Porta Padrão**: `5432` (exposta apenas dentro da rede **br-lab**).

2. **Servidor Zabbix**: Componente principal que processa dados e envia alertas.
    - **IP**: `172.10.10.115`
    - **Porta Padrão**: `10051` (para conexão com agentes).
   - **Documentação**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>    

3. **Frontend Zabbix**: Interface Web para configuração e visualização.
    - **IP**: `172.10.10.116`
    - **Porta Padrão**: `880` (acessível externamente).
   - **Documentação**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>
   
4. **Agente Zabbix**: Responsável por coletar métricas do host principal.
    - **IP**: `172.10.10.117`
    - **Porta Padrão**: `10050`.
   - **Documentação**: <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a>

Para verificar se todos os containers estão em execução, utilize:

```bash
docker compose ps
```

## :fontawesome-solid-display: 6. Acessando o Zabbix Frontend

Depois que os serviços forem inicializados, a interface Web do Zabbix estará disponível no endereço:

```bash
  http://<IP_DO_SERVIDOR>:880
```


### 6.1. Credenciais de acesso

As credenciais padrão para login no Frontend Zabbix são:

- **Usuário**: `Admin`
- **Senha**: `zabbix`

### 6.2. Alterando a senha padrão

Por questões de segurança, altere a senha do usuário administrador após o primeiro login:

- Navegue para **Administration > Users**.
- Selecione o usuário **Admin** e clique em **Change Password**.

## :octicons-rocket-24: 8. Próximos Passos

Com o ambiente do Zabbix configurado, você pode:

- Adicionar templates personalizados para monitoramento de serviços específicos.
- Integrar o Zabbix com outras ferramentas de automação e monitoramento.

Consulte a <a href="https://www.zabbix.com/documentation/7.0/en/manual/installation/containers" target="_blanck">Zabbix documentation</a> para explorar mais funcionalidades e boas práticas.