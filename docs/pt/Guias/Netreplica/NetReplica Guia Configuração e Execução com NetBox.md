

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

## Arquivo de Configuração Resumido

```bash
NB_API_URL           = 'http://localhost:8000'    # NetBox API URL or NB_API_URL env var
NB_API_TOKEN         = ''                         # API Token or NB_API_TOKEN env var
TLS_VALIDATE         = false                      # TLS certificate validation
API_TIMEOUT          = 10                         # API timeout (s)

TOPOLOGY_NAME        = 'lab'         # Topology name
OUTPUT_FORMAT        = 'clab'        # Output format: gml | cyjs | clab
OUTPUT_DIR           = 'conf/lab'    # Output directory (default: ./<topology>)
TEMPLATES_PATH       = ['templates']
PLATFORM_MAP         = 'templates/platform_map.yaml'   # Platform mapping file
EXPORT_CONFIGS       = true           # Export configs if available

EXPORT_DEVICE_ROLES  = []             # Device roles to export
EXPORT_SITES         = ['DM-Akron']   # Sites to export
EXPORT_TAGS          = []             # Tags to export
```

---


### Configurações da API do NetBox

### 1. **NB\_API\_URL**
 
  * **Descrição**: URL da API do NetBox.
  * **Uso**: Define o endereço da instância do NetBox a ser consultada pelo NetReplica.
  * **Exemplo**: `'http://localhost:8000'`.

### 2. **NB\_API\_TOKEN**

   * **Descrição**: Token de autenticação da API do NetBox.
   * **Uso**: Necessário para autenticar requisições à API.
   * **Exemplo**: `''` (deve ser preenchido com o token real).

### 3. **TLS\_VALIDATE**
  * **Descrição**: Controla a validação de certificados TLS.
  * **Uso**: `true` ativa validação (recomendado em produção); `false` desativa (útil em testes).
  * **Exemplo**: `false`.

### 4. **API\_TIMEOUT**

   * **Descrição**: Tempo limite para requisições à API, em segundos.
   * **Uso**: Define quanto tempo o NetReplica espera por uma resposta antes de considerar a requisição falha.
   * **Exemplo**: `10`.

---

### Configurações de Exportação

### 5. **TOPOLOGY\_NAME**

   * **Descrição**: Nome da topologia exportada.
   * **Uso**: Identifica os arquivos exportados e agrupa a topologia.
   * **Exemplo**: `'lab'`.

### 6. **OUTPUT\_FORMAT**

   * **Descrição**: Formato dos dados exportados.
   * **Uso**: Pode ser `'gml'`, `'cyjs'` ou `'clab'`.
   * **Exemplo**: `'clab'`.

### 7. **OUTPUT\_DIR**

   * **Descrição**: Diretório de destino dos arquivos exportados.
   * **Uso**: Substitui o diretório padrão de exportação.
   * **Exemplo**: `'conf/lab'`.

### 8. **TEMPLATES\_PATH**

   * **Descrição**: Lista de diretórios de templates usados na exportação.
   * **Uso**: Permite localizar templates personalizados.
   * **Exemplo**: `['templates']`.

### 9. **PLATFORM\_MAP**

   * **Descrição**: Arquivo de mapeamento de plataformas.
   * **Uso**: Define como cada plataforma de dispositivo será representada nos arquivos exportados.
   * **Exemplo**: `'templates/platform_map.yaml'`.

### 10. **EXPORT\_CONFIGS**

   * **Descrição**: Define se configurações dos dispositivos devem ser exportadas.
   * **Uso**: `true` inclui as configs, `false` as ignora.
   * **Exemplo**: `true`.

---

### Configurações de Filtro de Dispositivos

### 11. **EXPORT\_DEVICE\_ROLES**

   * **Descrição**: Lista de funções de dispositivos a serem exportadas.
   * **Uso**: Filtra quais dispositivos serão incluídos.
   * **Exemplo**: `[]` (exporta todas se vazio).

### 12. **EXPORT\_SITES**

   * **Descrição**: Lista de sites do NetBox a serem exportados.
   * **Uso**: Filtra dispositivos por site.
   * **Exemplo**: `['DM-Akron']`.

### 13. **EXPORT\_TAGS**

   * **Descrição**: Lista de tags usadas como filtro para exportação.
   * **Uso**: Somente dispositivos com essas tags serão exportados.
   * **Exemplo**: `[]` (exporta todos se vazio).

---

Esse arquivo de configuração permite uma personalização detalhada da forma como o NetReplica interage com o NetBox e exporta os dados, 
ajudando a atender a necessidades específicas de visualização e exportação.


### :fontawesome-solid-arrow-right-to-bracket: **Próximos Passos**

Agora para se aprofundar mais pode conferir o proximo guia que mostra como criar e configurar novos Templates e adicionar novas imagens ao netreplica. confira aqui [NetReplica Criando Templates](NetReplica%20Criando%20Templates.md).

### :fontawesome-solid-link: Referências

- <a target="_blank" href="https://github.com/netreplica/nrx?tab=readme-ov-files">NetReplica GitHub Repository</a>