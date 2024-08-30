# Contribua

Texto de contribuição

## :material-tools: Ferramentas

Este projeto foi desenvolvido com as seguintes ferramentas:

* [poetry](https://python-poetry.org/) para gerenciamento de dependências
* [taskpy](https://github.com/taskipy/taskipy) para automação de tarefas
* [mkdocs](https://www.mkdocs.org/) para documentação
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) para tema de documentação
* [commitizen](https://commitizen-tools.github.io/commitizen/) para padronização de mensagens de commit


## :fontawesome-solid-user-gear: Como contribuir

Primeiramente, obrigado por fazer parte deste projeto! Sua ajuda é muito bem-vinda.

Para contribuir com o projeto, siga as etapas abaixo:

1. clone o repositório para sua máquina local:


```bash
git clone https://git.rnp.br/gci/dev/inovacao-ciberinfraestrutura/docs.git
```

2. Instale as dependências do projeto:

primeiramente, instale o pipx para instalar o poetry docemtação [aqui](https://pypa.github.io/pipx/)

Agora, instale o poetry, que é o gerenciador de dependências do projeto:

```bash
pipx install poetry
```

agora dentro da pasta do projeto, instale as dependências do projeto:

```bash
poetry install
```

pronto, agora você tem todas as dependências do projeto instaladas.


## Estrutura de pastas

O projeto é organizado da seguinte forma:

```mermaid
flowchart TD
    A[./] --> B[docs]
    B --> C[Ferramentas]
    B --> D[Guias]
    B --> E[inventarios]
    B --> F[Laboratórios]
    B --> G[Templates]
```

onde cada pasta tem a seguinte função:

- `docs`: contém a documentação do projeto, escrita em Markdown.
- `Ferramentas`: contém as ferramentas que foram testadas e documentadas nos laboratórios.
- `Guias`: contém as guias de configuração dos laboratórios e ultilizações mais específicas do laboratórios
- `inventarios`: contém os inventários dos laboratorios no formato de importação do netbox.
- `Laboratórios`: contém os laboratórios que foram testados e documentados de topologias de redes.
- `Templates`: contém os templates do netreplica para vendors ainda não suportados por padrão.

### :simple-googledocs: docs

A documentação do projeto é escrita em Markdown e está localizada na pasta docs. Para contribuir, 
edite os arquivos Markdown existentes ou crie novos, seguindo a estrutura de pastas e arquivos já estabelecida. 
Cada arquivo deve incluir um título e uma descrição, tornando-o uma página da documentação.

A estrutura de pastas deve seguir o padrão do nome da seção correspondente, 
com um arquivo index.md para a página inicial da seção. As demais páginas necessárias também devem ser em Markdown. 
A organização do site é feita automaticamente pelo MkDocs.

Exmplo:

``` bash
docs/
    ├── Seção/
    │   ├── index.md
```

## Mão na massa

Agora que você já tem as dependecias instaladas e entendeu como ele funciona, você pode começar a contribuir com o código,
a seguir algumas dicas para contribuir com o projeto assim como ultilizar as ferramentas de automação e padronização do projeto.

!!! info "Dica"
    antes de começar a editar o código, é importante entrar no ambiente virtual do poetry, para isso, execute o seguinte comando:

    ```bash
    poetry shell
    ```

### :material-tools: Ferramentas

o projeto conta com algumas ferramentas de automação e padronização, como o `taskpy` e o `black`, que são usadas para automatizar tarefas e padronizar o código, respectivamente.


#### :material-code-tags-check: Documentação

A documentação do projeto é escrita em Markdown e está localizada na pasta docs, seguindo a estrutura de pastas, subpastas e arquivos existentes.
onde toda a padronização e a recomendada pelo [mkdocs](https://www.mkdocs.org/) e [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), logo para visualizar a documentação localmente, execute o seguinte comando:

```bash
task docs
```

!!! info "Dica"
    Para contribuir com a documentação, você pode editar os arquivos Markdown diretamente ou criar novos arquivos conforme necessário, seguindo a estrutura de pastas, subpastas e arquivos existentes.

!!! info "Dica"
    Você pode ultilizar qualquer feature disponivel no mkdocs de personalizações, para saber mais acesse a documentação abaixo:

links uteis:

- <a taget="_blank" href="https://squidfunk.github.io/mkdocs-material/reference/admonitions/">mkdocs-admonitions</a>: documentação para as admonitions(anotações de documentação)
  - <a taget="_blank" href="https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search">mkdocs-emojis</a> : documentação para os emojis
- <a taget="_blank" href="https://mermaid.js.org/syntax/flowchart.html">mermaid</a> : documentação para o mermaid(diagrama de fluxo em markdown)


#### Commits :material-code-tags-check:

O projeto utiliza o `commitizen` para padronizar as mensagens de commit. Para criar um commit, execute o seguinte comando:

!!! Warning "Observação"
 você deve esta dentro do ambiente virtual do poetry, se não, execute o seguinte comando:
 ```bash
 poetry shell
 ```

```bash
task commit
```

Agora é só preencher as informações solicitadas e o commit será feito de forma padronizada. Após o commit, você pode fazer o push para o repositório remoto.

## Não achei o que preciso aqui

Caso não tenha encontrado o que precisa, você pode abrir uma [issue no projeto](https://git.rnp.br/redes-abertas/docs/-/issues) relatando o que não consegue fazer ou o que precisa ser melhor documentado

## Melhoria contínua

Esse documento pode ser melhorado por qualquer pessoa que tenha interesse em melhora-lo. Então, sinta-se a vontade para fornecer mais dicas as pessoas que desejam contribuir também :heart:






