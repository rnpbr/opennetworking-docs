# Netbox

# Instalação do Netbox e importações

## 1. Instalação

Para instalar o NetBox usando o Docker, siga os passos abaixo:

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. Se ainda não tiver, você pode encontrá-los nos seguintes links:
    - Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
    - Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
2. Clone o repositório oficial do NetBox Docker Compose no GitHub:
    
    ```
    git clone <https://github.com/netbox-community/netbox-docker.git>
    ```
    
3. Acesse o diretório clonado:
    
    ```
    cd netbox-docker
    ```
    
4. acesse os arquivo de ambiente `.env` a partir do exemplo fornecido:
    
    ```
    cd env
    ```
    
5. Edite o arquivo `.env` para ajustar as configurações conforme necessário. Especificamente, você pode alterar as credenciais de banco de dados, senhas, configurações de e-mail, etc., de acordo com suas preferências e requisitos, por padrão para execução rápida ele vem todo configurado mas é altamente recomendado alterar tais informações caso deseje por ele em produção.
6. se quiser alterar a versão do netbox, edite pelo compose na parte da versão da imagem.
**Obs.**: mudanças entre versões distantes podem ocasionar erro, procure pelas versões corretas em [https://github.com/netbox-community/netbox-docker/releases](https://github.com/netbox-community/netbox-docker/releases)
7. Construa e execute os contêineres Docker:
    
    ```
    tee docker-compose.override.yml <<EOF
    version: '3.4'
    services:
      netbox:
        ports:
          - 8000:8080
    EOF
    docker compose pull
    docker compose up
    docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
    ```
    
    **Observação:** A porta de comunicação utilizada pode diferir da porta 8000, caso alguma outra aplicação ativa utilize esta porta. Neste caso, verifique uma outra porta disponível (por exemplo: 8080 ou 8081) e não esqueça de substituir adequadamente nos passos seguintes.
    
8. Aguarde até que os contêineres sejam construídos e inicializados.
9. Abra o navegador da web e acesse: **[http://localhost:8000/](http://localhost:8000/)**.
    
    **Observação:** Se você deseja acessar o NetBox de uma máquina diferente, substitua "localhost" pelo endereço IP da máquina onde o Docker está sendo executado.
    
10. Será solicitado que você defina a senha de administração.
11. Para criar o usuário de administração, execute o seguinte comando no terminal após a inicialização dos contêineres:
    
    ```bash
    bashCopy code
    docker-compose exec <nome do container netbox> /opt/netbox/netbox/manage.py createsuperuser
    ```
    

## 2. Acesso

Após concluir a instalação do NetBox no Docker, você pode acessá-lo via navegador da web. Por padrão, o NetBox estará disponível localmente em [http://localhost:8000/](http://localhost:8000/). No entanto, se você deseja acessar o NetBox de forma segura através de um túnel SSH, siga as etapas abaixo:

### 2.1 Acesso via tunel ssh

1. Agora, para acessar o NetBox de forma segura através de um túnel SSH, você precisará de um servidor remoto com acesso SSH, onde o Docker não precisa estar instalado.
2. No servidor remoto, execute o seguinte comando para criar um túnel SSH para o NetBox:
    
    ```
    ssh -N -L 8080:localhost:8080 usuario@endereco_do_servidor
    ```
    
    - Substitua `usuario` pelo nome de usuário do servidor remoto.
    - Substitua `endereco_do_servidor` pelo endereço IP ou nome de domínio do servidor remoto.
3. Após inserir sua senha SSH, o túnel será estabelecido. Agora, o servidor remoto redirecionará as solicitações da porta 8080 para o NetBox na porta 8000.
4. Em seu computador local, abra o navegador da web e acesse:
    
    ```
    <http://localhost:8080/>
    ```
    
    Você será redirecionado para o NetBox que está sendo executado no servidor remoto por meio do túnel SSH. Agora você pode acessar o NetBox com segurança.
    

Lembre-se de que o túnel SSH manterá a conexão ativa enquanto o terminal do servidor remoto estiver aberto. Se você deseja manter o túnel funcionando em segundo plano, adicione a opção `-f` ao comando SSH no passo 9:

```
ssh -f -N -L 8080:localhost:8000 usuario@endereco_do_servidor
```

Com isso, você poderá acessar o NetBox de forma segura por meio de um túnel SSH, garantindo a proteção dos seus dados durante a transmissão.

## 3. Importação

Para a importação deve-se organizar os arquivos em formato CSV corretamente formatado, contendo os campos indicados a seguir. Além disso, é importante que a importação siga a ordem da numeração dos arquivos conforme consta na preparação dos dados.

### 3.1. Preparação dos dados

A importação dos arquivos csv deve seguir a numeração estabelecida e conter as informações indicadas. Os nomes (**em negrito**) indicam os locais de importação, e as informações abaixo (*em itálico*) indicam os campos necessários para a importação.

1. **manufacturers**
*name, slug*
2. **platforms**
*name, slug, manufacturer, napalm_driver, description*
    
    **tags**
    *name, items, slug, color, description*
    
3. **device_roles**
*name, color, vm_role, description, slug, tag*
    
    **device_types**
    *model, manufacturer, part_number, u_height, is_full_depth, slug*
    
    **sites**
    *name, status, slug, latitude, longitude*
    
    **tenants**
    *name, slug*
    
4. **devices**
*name, status, device_role, manufacturer, device_type, site, platform, tag*
5. **interfaces**
*name, device, label, enabled, type, description*
    
    **VRFs**
    *name, rd, tenant, enforce_unique, description, import_targets, export_targets, comments, tags*
    
6. **circuit_types**
*name, slug*
    
    **IP_addresses**
    *address, vrf, tenant, status, role, device, interface, dns_name, description*
    
    **providers**
    *name, slug*
    
7. **circuits**
*cid, provider, type, status, tenant, description*

### 3.2. A importação

1. **Faça login como superusuário**: Acesse o NetBox com as credenciais de admin.
2. **Encontre a opção de importação**: Verifique a seção relacionada aos dados que deseja importar, e procure por um **ícone** de importação como vemos na Figura 1 abaixo:
    
    ![**Figura 1**: ao clicar no ícone importação é possivel fazer o upload do arquivo CSV.](netbox_imgs/import.png)
    **Figura 1**: ao clicar no ícone importação é possivel fazer o upload do arquivo CSV.
    
3. **Selecione o arquivo CSV**: Faça o upload do arquivo CSV com os dados preparados, cada CSV precisa conter os campos conforme descrito a Subseção 3.1.
4. **Inicie a importação**: Clique em "Enviar" ou "Importar" para começar o processo.
5. **Verifique os resultados**: Analise o relatório de importação para confirmar o sucesso.

<aside>
💡 **Observação:** após realizar a importação do arquivos do item `7.`, é necessário incluir as terminações manualmente.
Para isso, sigas as instruções abaixo para completar a configuração. clique no circuito criado e no ícone `edit` conforme destacado na imagem abaixo
Então edite as informações de `side*` e `interface*`
</aside>

- Clique em Circuits para ver os circuitos criados na etapa 7. Selecione com 1 clique um dos Circuit ID criado, conforme o indicado na Figura 2.
    
    **Observação**: as etapas devem ser feitas para todo Circuito ID existente.
    

![**Figura 2**: clique no circuit (seta a esquerda), em seguida selecione o Circuirt ID (detacados e indicados com a seta) para realizar a configuração.](netbox_imgs/circuitID.png)
**Figura 2**: clique no circuit (seta a esquerda), em seguida selecione o Circuirt ID (detacados e indicados com a seta) para realizar a configuração.

- Após clicar em um dos circuitos, as configurações do circuito é similar a apresentada na Figura 3. As teminações devem ser editadas clicando no ícone `Edit` conforme destacado na imagem abaixo. Ao clicar no ícone, o Netbox encaminha para a parte de Cables em Conexões, conforme mostra a Figura 4.

![Figura 3: tela de um Circuit ID. As edições de de cada Temination deve ser realizada clicando em `Edit` (destacado com a seta).](netbox_imgs/circuitEdit.png)
**Figura 3:** tela de um Circuit ID. As edições de de cada Temination deve ser realizada clicando em `Edit` (destacado com a seta).

- A Figura 4 apresenta a criação dos cabos de conexão, a numeração dos cabos seguem apenas a ordem de criação. Os itens `Side*` e `Interface*` devem ser preenchidos para finalizar a configuração da etapa 7.

![Figura 4: tela de configuração dos cabos para conexão para a conexão entre os dispositivos.](netbox_imgs/circuitCable.png)
**Figura 4:** tela de configuração dos cabos para conexão para a conexão entre os dispositivos.

<aside>
💡 Lembre-se de adaptar as subcategorias e locais de importação de acordo com as funcionalidades específicas do seu NetBox. Cada categoria pode ter campos e configurações únicas para a importação.
</aside>
