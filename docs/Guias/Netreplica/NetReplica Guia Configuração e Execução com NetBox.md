

# :material-content-duplicate: NetReplica Guia: Configuração e Execução com NetBox

Este guia descreve as configurações necessárias para integrar o NetReplica com o NetBox. O NetReplica é uma ferramenta usada para replicar e analisar redes, enquanto o NetBox é uma plataforma de gerenciamento de ativos de rede.

## :octicons-tools-24: Passo 1: Execução Direta com NRX

---

!!! tip "Observação"
    antes de prosseguir verifique se o NetReplica está instalado e se o NetBox está instalado, pode ter mais informações aqui: [Intalação Netreplica](index.md)

O `nrx` é a interface de linha de comando do NetReplica que permite configurar e executar tarefas diretamente sem a necessidade de criar um arquivo de configuração. A seguir, são apresentados os principais comandos que você pode usar:

### :octicons-command-palette-24: Comandos Básicos

1 **Comando para Exportar uma Topologia**:

   ```bash
   nrx -c conf/<Nome_da_Topologia>.conf
   ```

Este comando utiliza o arquivo de configuração `.conf` para exportar a topologia especificada.

2 **Exportar a partir de uma URL de API do NetBox**:

   ```bash
   nrx -a http://<ip_do_netbox>:<porta> -t '<tags>' -s '<site>' -o clab
   ```

Este comando permite a exportação utilizando parâmetros diretamente na linha de comando, como URL da API do NetBox, tags, site, e formato de saída.

3 **Utilizar Tokens de Autenticação**:

Para passar o token de autenticação sem usar um arquivo de configuração:

   ```bash
   export NB_API_TOKEN='seu_token_aqui'
   nrx -a http://<ip_do_netbox>:<porta> -t '<tags>' -s '<site>' -o clab
   ```

4 **Especificar o Diretório de Saída**:

   ```bash
   nrx -c conf/<Nome_da_Topologia>.conf -D /caminho/para/saida
   ```

Este comando permite definir um diretório específico para a saída dos arquivos exportados.

5 **Ignorar Certificado TLS**:

   ```bash
   nrx -c conf/<Nome_da_Topologia>.conf --insecure
   ```

Este comando desativa a verificação do certificado TLS.

### :material-text-box-search-outline: Argumentos Comuns do `nrx`

- `-c, --config CONFIG`: Define o arquivo de configuração a ser utilizado.
- `-a, --api API`: Define a URL da API do NetBox.
- `-s, --site SITE`: Especifica o site do NetBox a ser exportado.
- `-t, --tags TAGS`: Define as tags do NetBox a serem exportadas.
- `-o, --output OUTPUT`: Define o formato de saída (ex.: 'clab', 'cyjs').
- `-D, --dir DIR`: Define o diretório de saída.
- `--insecure`: Desativa a verificação do certificado TLS.

---

## :material-file-document: Passo 2: Configuração do Arquivo `.conf`

---

O arquivo de configuração `.conf` fornece um meio estruturado de definir as variáveis necessárias para a exportação de topologias. Ele é particularmente útil quando você deseja reutilizar as mesmas configurações ou quando há muitas opções a serem definidas.

Claro, aqui está o arquivo de configuração com uma explicação detalhada para cada campo:

---

## Arquivo de Configuração Completo

```bash
# NetBox API URL. Alternativamente, use o argumento --api ou a variável de ambiente NB_API_URL
NB_API_URL           = 'https://demo.netbox.dev'
# NetBox API Token. Alternativamente, use a variável de ambiente NB_API_TOKEN
NB_API_TOKEN         = ''
# Realizar validação do certificado TLS
TLS_VALIDATE         = true
# Tempo limite para requisições API, em segundos
API_TIMEOUT          = 10
# Otimização de consultas em massa da API do NetBox
[NB_API_PARAMS]
interfaces_block_size = 4
cables_block_size =     64

# Nome da topologia, opcional. Alternativamente, use o argumento --name
TOPOLOGY_NAME        = 'DemoSite'
# Formato de saída a ser usado para exportação: 'gml' | 'cyjs' | 'clab'. Alternativamente, use o argumento --output
OUTPUT_FORMAT        = 'clab'
# Sobrescrever diretório de saída. Por padrão, será criado um subdiretório correspondente ao nome da topologia. Alternativamente, use o argumento --dir. Variáveis de ambiente são suportadas
OUTPUT_DIR           = '$HOME/nrx'
# Caminho de busca dos templates. O caminho padrão é ['./templates','$HOME/.nr/templates']. Variáveis de ambiente são suportadas
TEMPLATES_PATH       = ['./templates','$HOME/.nr/custom','$HOME/.nr/templates']
# Caminho do mapa de plataforma. Se não fornecido, 'platform_map.yaml' no diretório atual é verificado primeiro, e depois nas pastas TEMPLATES_PATH. Variáveis de ambiente são suportadas
PLATFORM_MAP         = '$HOME/.nr/platform_map.yaml'

# Lista de Funções de Dispositivos do NetBox a serem exportadas
EXPORT_DEVICE_ROLES  = ['router', 'core-switch', 'distribution-switch', 'access-switch', 'tor-switch', 'server']
# Site do NetBox a ser exportado. Alternativamente, use o argumento --sites
EXPORT_SITES          = ['DM-Akron']
# Tags do NetBox a serem exportadas. Alternativamente, use o argumento --tags
EXPORT_TAGS          = []
# Exportar configurações de dispositivos, quando disponíveis
EXPORT_CONFIGS       = true

# Níveis de funções de dispositivos para visualização
[DEVICE_ROLE_LEVELS]
unknown =              0
server =               0
tor-switch =           1
access-switch =        1
leaf =                 1
distribution-switch =  2
spine =                2
core-switch =          3
super-spine =          3
router =               4
```

## Explicação dos Campos

### Configurações da API do NetBox

1. **NB_API_URL**
    - **Descrição**: URL da API do NetBox.
    - **Exemplo**: `'https://demo.netbox.dev'`
    - **Uso**: Define a URL para onde o NetReplica deve enviar as requisições API. Se você estiver usando uma instância local do NetBox, altere para `'http://localhost:8000'`.

2. **NB_API_TOKEN**
    - **Descrição**: Token de autenticação da API do NetBox.
    - **Exemplo**: `'my_api_token'`
    - **Uso**: Este token é necessário para autenticar as requisições à API do NetBox. Deve ser obtido no painel de administração do NetBox.

3. **TLS_VALIDATE**
    - **Descrição**: Se deve realizar a validação do certificado TLS.
    - **Exemplo**: `true`
    - **Uso**: `true` ativa a validação do certificado TLS para garantir a segurança da comunicação. `false` desativa a validação, o que pode ser útil em ambientes de teste, mas não é recomendado para produção.

4. **API_TIMEOUT**
    - **Descrição**: Tempo limite para requisições API, em segundos.
    - **Exemplo**: `10`
    - **Uso**: Define o tempo máximo que o NetReplica deve esperar por uma resposta da API antes de considerar a requisição como falhada.

### Configurações de Otimização da API

5. **[NB_API_PARAMS]**
    - **Descrição**: Parâmetros para otimizar consultas em massa na API do NetBox.
    - **Exemplo**:
      ```bash
      interfaces_block_size = 4
      cables_block_size = 64
      ```
    - **Uso**: Controla o número de interfaces e cabos processados em cada consulta em massa. Ajustar esses valores pode melhorar o desempenho dependendo do tamanho da sua base de dados.

### Configurações de Exportação

6. **TOPOLOGY_NAME**
    - **Descrição**: Nome da topologia para exportação.
    - **Exemplo**: `'DemoSite'`
    - **Uso**: Define o nome usado para identificar a topologia exportada. É útil para organização e identificação dos arquivos exportados.

7. **OUTPUT_FORMAT**
    - **Descrição**: Formato de saída para exportação dos dados.
    - **Exemplo**: `'clab'`
    - **Uso**: Define o formato dos dados exportados. Pode ser `'gml'`, `'cyjs'`, `'clab'`, entre outros formatos compatíveis.

8. **OUTPUT_DIR**
    - **Descrição**: Diretório onde os arquivos exportados serão salvos.
    - **Exemplo**: `'$HOME/nrx'`
    - **Uso**: Define o caminho onde os arquivos exportados serão armazenados. Pode substituir o diretório padrão se especificado.

9. **TEMPLATES_PATH**
    - **Descrição**: Caminho para os templates usados durante a exportação.
    - **Exemplo**: `'./templates'`
    - **Uso**: Define onde procurar os templates para a exportação. Pode incluir múltiplos diretórios para maior flexibilidade.

10. **PLATFORM_MAP**
    - **Descrição**: Caminho para o arquivo de mapeamento de plataformas.
    - **Exemplo**: `'$HOME/.nr/platform_map.yaml'`
    - **Uso**: Arquivo que define como as plataformas são mapeadas para os parâmetros de nó. É usado para personalizar a visualização dos dispositivos na exportação.

### Configurações de Exportação de Dispositivos

11. **EXPORT_DEVICE_ROLES**
    - **Descrição**: Lista de funções de dispositivos do NetBox a serem exportadas.
    - **Exemplo**: `['router', 'core-switch']`
    - **Uso**: Define quais tipos de dispositivos (por exemplo, roteadores, switches) devem ser incluídos na exportação.

12. **EXPORT_SITES**
    - **Descrição**: Lista de sites do NetBox a serem exportados.
    - **Exemplo**: `['DM-Akron']`
    - **Uso**: Define quais sites específicos devem ser exportados. Pode incluir múltiplos sites.

13. **EXPORT_TAGS**
    - **Descrição**: Lista de tags do NetBox a serem exportadas.
    - **Exemplo**: `['production', 'datacenter']`
    - **Uso**: Define quais tags devem ser usadas para filtrar dispositivos durante a exportação.

14. **EXPORT_CONFIGS**
    - **Descrição**: Se as configurações dos dispositivos devem ser exportadas, quando disponíveis.
    - **Exemplo**: `true`
    - **Uso**: Se `true`, as configurações dos dispositivos serão incluídas na exportação.

### Níveis de Função de Dispositivos

15. **[DEVICE_ROLE_LEVELS]**
    - **Descrição**: Define os níveis de visualização para diferentes funções de dispositivos.
    - **Exemplo**:
      ```bash
      unknown =              0
      server =               0
      tor-switch =           1
      access-switch =        1
      leaf =                 1
      distribution-switch =  2
      spine =                2
      core-switch =          3
      super-spine =          3
      router =               4
      ```
    - **Uso**: Define a ordem de visualização dos dispositivos na exportação. Dispositivos com níveis mais altos são exibidos com mais destaque.

---

Esse arquivo de configuração permite uma personalização detalhada da forma como o NetReplica interage com o NetBox e exporta os dados, 
ajudando a atender a necessidades específicas de visualização e exportação.


### :fontawesome-solid-arrow-right-to-bracket: **Próximos Passos**

Agora para se aprofundar mais pode conferir o proximo guia que mostra como criar e configurar novos Templates e adicionar novas imagens ao netreplica. confira aqui [NetReplica Criando Templates](NetReplica%20Criando%20Templates.md).

### :fontawesome-solid-link: Referências

- <a target="_blank" href="https://github.com/netreplica/nrx?tab=readme-ov-files">NetReplica GitHub Repository</a>