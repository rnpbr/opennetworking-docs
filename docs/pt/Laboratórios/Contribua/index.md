# Documentando os laboratorios 

Contribuir para a documentação dos laboratórios no **Containerlab** é um processo simples, mas é importante seguir algumas etapas para garantir que todos os links e funcionalidades funcionem corretamente. Esta página fornece as instruções necessárias para documentar um laboratório, bem como para configurar os scripts essenciais para o funcionamento adequado do processo de implantação.

---

## 1. Criando a Documentação do Lab

### Criando Imagens para Representar Laboratórios

Na documentação e importante os laboratórios tenham imagens representando a topologia de rede do laboratório. Para isso, seguir o [Guia Criando Imagens para Representar Laboratórios](Guia Criando Imagens para Representar Laboratórios.md).

### Passos para Documentar o Lab

Aqui estão os principais passos para a documentação do seu laboratório:

1. **Criar Descrição e Objetivo do Lab**:
    - Descreva o que o laboratório faz e qual protocolo ou funcionalidade está sendo demonstrada.
2. **Documentar a Topologia do Lab**:
    - Utilize as imagens criadas para ilustrar a topologia da rede do laboratório. Se necessário, insira diagramas adicionais explicando como os dispositivos estão interconectados.
3. **Incluir Exemplos de Uso**:
    - Forneça exemplos de comandos e ações que os usuários podem executar dentro do laboratório para testar a funcionalidade.
4. **Listar Requisitos**:
    - Defina claramente os requisitos de hardware e software, como a versão do Docker, Containerlab e as configurações da rede.
5. **Instruções de Implantação**:
    - Documente a implantação do laboratório, seja a versão pronta ou personalizada. Certifique-se de seguir os guias de implantação com links adequados.
6. **Acessos e Credenciais**:
    - Crie uma tabela detalhando os IPs de cada dispositivo no laboratório e suas respectivas credenciais de acesso.

!!! tip "Dica"
    Para seguir um padrão consistente de documentação, você pode usar o [template](Template lab.md) que já vem estruturado com dicas. Ele servirá de base para você adaptar o conteúdo do seu laboratório, garantindo que todas as seções estejam corretamente abordadas.

para usar o template de documentação, basta acessar **docs/pt/Laboratórios/Contribua/Template lab.md** criar uma copia para pasta laboratorios e colocar o nome de seu laboratorio e preencher as informacoes.

---

## 2. Scripts para Download Rápido

Para garantir que o processo de download e implantação do laboratório funcione corretamente, é necessário incluir dois scripts essenciais dentro da pasta do laboratório no GitLab. Esses scripts permitirão que o laboratório seja baixado e configurado automaticamente com um simples comando.

### 2.1 Script `get.sh`

O script `get.sh` é utilizado em sistemas Linux/Mac para baixar e descompactar automaticamente o laboratório. Ele verifica se o comando `tar` está instalado e, se não estiver, instala o pacote necessário antes de baixar o arquivo.

### Como Funciona:

1. **Verificação de Dependências**: O script verifica se o pacote `tar` está instalado. Se não, ele tenta instalar usando o gerenciador de pacotes do sistema (`apt-get`, `dnf`, `yum`, ou `pacman`).
2. **Download e Descompactação**: O script baixa o arquivo `.tar` contendo o laboratório e o descompacta no diretório de destino.

### Script `get.sh`:

```bash
#!/bin/bash

# Função para verificar se um comando está instalado
check_command() {
    command -v "$1" >/dev/null 2>&1
}

# Função para instalar pacotes
install_package() {
    if [ -x "$(command -v apt-get)" ]; then
        sudo apt-get update
        sudo apt-get install -y "$1"
    elif [ -x "$(command -v dnf)" ]; then
        sudo dnf install -y "$1"
    elif [ -x "$(command -v yum)" ]; then
        sudo yum install -y "$1"
    elif [ -x "$(command -v pacman)" ]; then
        sudo pacman -Sy --noconfirm "$1"
    else
        echo "Erro: Gerenciador de pacotes não suportado. Instale '$1' manualmente."
        exit 1
    fi
}

if ! check_command tar; then
    echo "O pacote 'tar' não está instalado. Instalando..."
    install_package tar
fi

# URL do arquivo tar
URL="<https://git.rnp.br/redes-abertas/lab/-/archive/main/labs-main.tar?path=<nome-do-lab>>"

# Nome do arquivo para salvar
FILENAME="lab-main.tar"

# Diretório onde descompactar os arquivos
DEST_DIR="./"

# Baixar o arquivo
echo "Baixando $FILENAME..."
curl -L -o $FILENAME "$URL"

# Verificar se o download foi bem-sucedido
if [ $? -ne 0 ]; then
    echo "Erro ao baixar o arquivo."
    exit 1
fi

# Descompactar o arquivo
echo "Descompactando $FILENAME..."
tar -xf $FILENAME -C $DEST_DIR --strip-components=1

# Verificar se a descompactação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Erro ao descompactar o arquivo."
    exit 1
fi

# Remover o arquivo tar após descompactar
rm $FILENAME

echo "Download e descompactação concluídos com sucesso."

```

### Variáveis a Modificar:

- **`URL`**: Alterar a URL para corresponder ao repositório e ao caminho do laboratório dentro do GitLab.

---

### 2.2 Script `get.bat`

O script `get.bat` é usado em sistemas Windows para baixar e descompactar o laboratório de maneira similar ao `get.sh`, mas com comandos compatíveis com o ambiente Windows.

### Script `get.bat`:

```bat
@echo off
setlocal

REM URL do arquivo tar
set "URL=https://git.rnp.br/redes-abertas/docker-composes/-/archive/main/docker-composes-main.tar?path=<nome-do-lab>"

REM Nome do arquivo para salvar
set "FILENAME=lab-main.tar"

REM Diretório onde descompactar os arquivos
set "DEST_DIR=."

echo Baixando %FILENAME%...
curl -L -o %FILENAME% %URL%

REM Verificar se o download foi bem-sucedido
if not exist %FILENAME% (
    echo Erro ao baixar o arquivo.
    exit /b 1
)

echo Descompactando %FILENAME%...
tar -xf %FILENAME% -C %DEST_DIR% --strip-components=1

REM Verificar se a descompactação foi bem-sucedida
if %errorlevel% neq 0 (
    echo Erro ao descompactar o arquivo.
    exit /b 1
)

REM Remover o arquivo tar após descompactar
del %FILENAME%

echo Download e descompactação concluídos com sucesso.

endlocal
pause

```

### Variáveis a Modificar:

- **`URL`**: Alterar a URL para o caminho específico do seu laboratório no repositório GitLab.

---

## 3. Certificando-se de que os Scripts estão Corretos

Para garantir que o processo de download rápido funcione corretamente, **os dois scripts (get.sh e get.bat) devem ser incluídos na pasta do lab em questão dentro do repositório do laboratório**. Isso assegura que, ao usar os links de download, os usuários possam baixar e descompactar o laboratório de forma eficiente, sem problemas.

!!! tip "Dica"
    Quando for incluir os scripts no GitLab, verifique se as URLs estão configuradas corretamente com os nomes correspondentes à pasta do repositório e ao nome do laboratório.


---

Com essas etapas, você poderá contribuir efetivamente para a documentação do laboratório e garantir que todos os links de download e scripts estejam funcionando corretamente.