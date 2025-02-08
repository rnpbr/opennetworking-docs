import os
from google import genai
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()


# Configura a chave da API do Gemini
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
# client = genai.Client(api_key="AIzaSyD4X-i-Womcq24sLd4aaktUPoa1xLsSQ10")

# Diretórios de origem (Português) e destino (Inglês)
SRC_DIR = "docs/pt"
DST_DIR = "docs/en"


# Função para traduzir texto usando o modelo do Gemini
def translate_text_gemini(text):
    # Configura o prompt para tradução
    prompt = f"Traduza a seguinte documentação do português para o inglês:\n\n{text} sem alterar a estrutura da documentação. e nem adicionar nada"

    # Usa o método generate_content para obter a tradução
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    # Retorna o texto traduzido
    return response.text.strip()


# Remove a primeira e a última linha **apenas se** forem marcações de bloco de código
def remove_code_block_formatting(text):
    # Divide o texto em linhas
    lines = text.splitlines()

    # Remove a primeira linha, se contiver "```" em qualquer lugar
    if lines and "```" in lines[0]:
        lines = lines[1:]

    # Remove a última linha, se contiver "```" em qualquer lugar
    if lines and "```" in lines[-1]:
        lines = lines[:-1]

    # Retorna o texto atualizado (reunindo as linhas restantes)
    return "\n".join(lines)

# Função para verificar se um arquivo precisa de tradução
def needs_translation(src_path, dst_path):
    # Se o arquivo traduzido não existe, precisamos traduzir
    if not os.path.exists(dst_path):
        return True

    # Se o arquivo existe, verificamos timestamps (foi modificado após última tradução?)
    src_modified_time = os.path.getmtime(src_path)  # Timestamp do arquivo original
    dst_modified_time = os.path.getmtime(dst_path)  # Timestamp do arquivo traduzido

    return src_modified_time > dst_modified_time


# Função para ler, traduzir e salvar os arquivos
def translate_files():
    for root, _, files in os.walk(SRC_DIR):
        for file_name in files:
            if file_name.endswith(".md"):  # Processa apenas arquivos Markdown
                src_path = os.path.join(root, file_name)

                # Caminho correspondente no diretório de destino
                relative_path = os.path.relpath(src_path, SRC_DIR)
                dst_path = os.path.join(DST_DIR, relative_path)

                # Verifica se precisa traduzir
                if needs_translation(src_path, dst_path):
                    with open(src_path, "r", encoding="utf-8") as src_file:
                        original_text = src_file.read()

                    print(f"Traduzindo arquivo: {src_path}")
                    translated_text = translate_text_gemini(original_text)

                    # Remove formatos de bloco de código, apenas no início e no fim, se existirem
                    translated_text = remove_code_block_formatting(translated_text)

                    # Garante que o diretório de saída existe
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                    # Salva o arquivo traduzido
                    with open(dst_path, "w", encoding="utf-8") as dst_file:
                        dst_file.write(translated_text)

                    print(f"Tradução concluída e salva em: {dst_path}")
                else:
                    print(f"Nenhuma modificação detectada em: {src_path}")




# Executa a tradução
if __name__ == "__main__":
    translate_files()