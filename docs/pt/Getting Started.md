# Getting started

Este guia abrangente o conduzirá pela configuração de um ambiente de simulação de rede, utilizando as ferramentas Netbox, Containerlab e Netreplica.

## Pré-requisitos:

- **Conhecimento básico em:**
    - Linux e SSH (Recomendação de curso: <a href="https://www.youtube.com/watch?v=aW4Owxgcvq4&list=PLnDvRpP8BnezDTtL8lm6C-UOJZn-xzALH" target="_blanck">Introdução ao Linux</a>)
    - Docker Basico (Recomendação de curso: <a href="https://www.youtube.com/watch?v=c2y_yz9B6_M&list=PLg7nVxv7fa6dxsV1ftKI8FAm4YD6iZuI4&index=1" target="_blanck">Docker para Iniciantes</a>)


## Passos:

### 1. Instalando o Netbox:

O Netbox é uma plataforma centralizada para gerenciamento de infraestrutura de rede, fornecendo documentação detalhada de dispositivos, endereços IP e conexões físicas. Ele permite a criação de templates de configuração usando Jinja2, facilitando a automação e padronização na configuração de dispositivos como roteadores e switches. Essa capacidade é essencial para manter ambientes de simulação de rede organizados e prontos para escalar conforme necessário.

- **Documentação Oficial:** <a href="http://netboxlabs.com/docs/netbox/en/stable/installation/" target="_blanck">NetboxLabs</a>
- **Guia De Instalação:** [Instalação do NetBox e Importações](Guias/Netbox/index.md)
- **Resumo:**
    - Certifique-se de ter o Docker instalado em sua maquina
    - Baixe o repositorio oficial do netbox em sua maquina
    - Configure o netbox acessando o .env
    - Suba o compose

### 2. Instalando o Containerlab:

O Containerlab é responsável por simplificar a criação e gerenciamento de topologias de rede complexas utilizando contêineres Docker. Ele permite definir e interconectar dispositivos de rede virtualizados de maneira eficiente, facilitando a configuração de ambientes de simulação e testes de redes. Essa abordagem baseada em Docker simplifica a replicação de ambientes reais em laboratórios virtuais, proporcionando flexibilidade e escalabilidade na configuração de infraestruturas de rede.

- **Documentação Oficial:** <a href="https://containerlab.dev/install/" target="_blanck">Containerlab</a>
- **Resumo:**
    - Instale o Docker e o Docker Compose.
    - Baixe o binário do Containerlab e adicione-o ao seu PATH.

### 3. Instalando o Netreplica:

O Netreplica sincroniza dados do Netbox em ambientes de simulação usando contêineres Docker. Ele permite testar configurações sem afetar o ambiente de produção, garantindo consistência nos dados e configurações entre diferentes cenários de rede.

- **Documentação Oficial:** <a href="https://github.com/netreplica/nrx?tab=readme-ov-file#how-to-install" target="_blanck">Netreplica</a>
- **Guia De Instalação:** [Instalação do NetReplica via Docker](Guias/Netreplica/index.md)
- **Resumo:**
    - Utilize o Docker Compose para iniciar o Netreplica em um contêiner Docker.
    - Configure o Netreplica para sincronizar com o Netbox.

### 4. Configurando e Executando o NetReplica com o Netbox:

Agora vamos detalhar o processo de configuração para integrar o Netreplica ao Netbox. Esta etapa é crucial para garantir que os dados e configurações do Netbox sejam replicados corretamente em ambientes de simulação ou testes, utilizando o Netreplica.

- **Documentação Oficial:** <a href="https://github.com/netreplica/nrx?tab=readme-ov-file#how-to-use" target="_blanck">Netreplica how to use</a>
- **Guia De Configuração:** [Guia de Configurando o NetReplica](Guias/Netreplica/NetReplica Guia Configuração e Execução com NetBox.md)
- **Resumo:**
    - Crie um token de API no Netbox para o Netreplica.
    - Configure o Netreplica para usar o token de API e a URL do Netbox.
    - Inicie o Netreplica e verifique se ele está sincronizando com o Netbox.

### 5. Criando e Configurando Templates no Netbox:

Os templates de configuração de dispositivos são essenciais para fornecer as configurações necessárias ao Netreplica, que posteriormente serão aplicadas nas simulações de rede.

- **Documentação Oficial:** <a href="http://netboxlabs.com/docs/netbox/en/stable/features/configuration-rendering/" target="_blanck">Netbox Configuration Rendering</a>
- **Guia De Configuração:** [Criação de Templates de configurações](Guias/Netbox/Render_Templates/index.md)
- **Resumo:**
    - Crie modelos de configuração para dispositivos de rede, como roteadores e switches.
    - Utilize Jinja2 para criar templates dinâmicos que se adaptam às suas topologias.
