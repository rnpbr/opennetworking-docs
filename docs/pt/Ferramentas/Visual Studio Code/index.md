# :material-microsoft-visual-studio-code: Visual Studio Code

O Containerlab possui uma extensão oficial para o **Visual Studio Code**, que facilita significativamente a criação, edição, visualização e gerenciamento de topologias em formato YAML. Este guia mostra como instalar a extensão, explorar seus recursos e utilizá-la inclusive em ambientes remotos.

---

## :material-tools: 1. Instalação da Extensão

### :octicons-tools-16: Pré-requisitos

* Visual Studio Code instalado.
* Containerlab instalado (<a href="https://containerlab.dev/install/" target="_blank">documentação oficial</a>).
* Docker instalado e em execução no sistema.

### :material-package-variant: Instalação

1. Acesse o marketplace do Visual Studio Code.
2. Pesquise por: `Containerlab`.
3. Ou acesse diretamente: <a href="https://marketplace.visualstudio.com/items?itemName=srl-labs.vscode-containerlab" target="_blank">Containerlab Extension</a>.
4. Após instalar, você verá um **ícone do Containerlab** na barra lateral esquerda.

---

## :simple-rocket: 2. Uso Básico

#### :octicons-tools-16: Criando e Editando Topologias

* Crie arquivos com extensão `.clab.yml` para definir sua topologia.
* Clique no ícone do **Containerlab** na barra lateral e selecione **"Criar Topologia"**.
* Um novo arquivo será aberto com estrutura base para definição de nós e links.

#### :octicons-gear-16: Ações Rápidas via Explorer

Na visualização lateral:

* As topologias são listadas automaticamente.
* Clique com o **botão direito** sobre uma topologia para acessar:

  * `Deploy`
  * `Destroy`
  * `Redeploy`
  * `Graph`
* Estados do lab são exibidos com **ícones coloridos**:

  * 🟠 Criando contêineres
  * 🟢 Lab em execução
  * 🔴 Erro na criação

---

### :fontawesome-solid-display: 2.1 Aba dos Nós

Ao expandir uma topologia:

* Cada **nó** será listado com seu nome e status.
* Clique com o **botão direito** no nó para:

  * Conectar via SSH/Telnet.
  * Abrir terminal (docker exec).
  * Copiar informações: IP, MAC, vendor, nome.
  * Iniciar/parar/reiniciar o nó.
  * Salvar configurações do nó.
  * Visualizar logs.
  * Abrir porta web do nó (se aplicável).
  * Acessar o painel de *Link Impairments*.

#### :material-ethernet: Interfaces

* Clique com o botão esquerdo no nó para expandir suas interfaces.
* Para cada interface:

  * Estado da interface é exibido.
  * Clique com o botão direito → **"Abrir com Wireshark"** (requer o plugin do [Edgeshark](../Edgeshark) instalado).

---

### :material-vector-polyline-remove: 2.2 Visualizando Topologias com TopoViewer

* Na visualização lateral, clique com o **botão direito** em uma topologia.
* Selecione **"Graph Topo View"**.
* Será aberta uma visualização gráfica (TopoViewer) mostrando:

  * Nós com ícones customizáveis via `labels`.
  * Conexões.
  * Agrupamento e geolocalização (opcional via `geo-lat`, `geo-long`).

---

## :material-cloud-key: 3. Acesso Remoto via SSH

A extensão do Containerlab pode ser usada em conjunto com o **Remote - SSH** do VS Code, possibilitando uso remoto completo.

### :octicons-gear-16: Passo a Passo

1. Instale a extensão <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh" target="_blank">Remote - SSH</a>.
2. Clique no **ícone verde de SSH** no canto inferior esquerdo.
3. Selecione **"Conectar a um servidor remoto..."**.
4. Preencha as informações de conexão (host, usuário, etc).
5. Após conectado:

   * Instale a extensão `Containerlab` no host remoto (via VS Code).
   * Use normalmente a extensão com as topologias remotas.

---

## :material-book-search-outline: Documentação Oficial

* <a href="https://containerlab.dev/" target="_blank">Documentação oficial do Containerlab</a>
* <a href="https://marketplace.visualstudio.com/items?itemName=srl-labs.vscode-containerlab" target="_blank">Documentação da extensão no Marketplace</a>

---

