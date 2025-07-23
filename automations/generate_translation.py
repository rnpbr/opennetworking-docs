import os
import json
from datetime import datetime
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SRC_DIR = "docs/pt"
DST_DIR = "docs/en"
DICT_PATH = "automations/dict_path.json"
STATE_FILE = "automations/.translation_state.json"


def load_translation_dict():
    """
    Carrega o dicionário de tradução a partir de um arquivo JSON.
    Caso ocorra erro no carregamento, imprime a mensagem e retorna um dicionário vazio.
    """
    if os.path.exists(DICT_PATH):
        try:
            with open(DICT_PATH, "r", encoding="utf-8") as f:
                # Tenta carregar e retornar o dicionário
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {e}")
        except Exception as e:
            print(f"Erro inesperado ao carregar o dicionário: {e}")
    else:
        print(f"O arquivo {DICT_PATH} não foi encontrado.")

    # Retorna um dicionário vazio em caso de erro
    return {}


def translate_path(path, translation_dict=None):
    if translation_dict is None:
        translation_dict = load_translation_dict()

    path_parts = path.split("/")
    translated_parts = [translation_dict.get(part, part) for part in path_parts]
    return "/".join(translated_parts)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def needs_translation(src_path, dst_path, state):
    src_modified_time = os.path.getmtime(src_path)
    last_info = state.get(src_path)
    if not os.path.exists(dst_path) or last_info is None:
        return True
    return src_modified_time > last_info["timestamp"]

def translate_text_gemini(text):
    prompt = f"Traduza a seguinte documentação do português para o inglês:\n\n{text} sem alterar a estrutura da documentação. e nem adicionar nada e não alterar os links ou referencias.\n\nTradução:"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()

def remove_code_block_formatting(text):
    lines = text.splitlines()
    if lines and "```" in lines[0]:
        lines = lines[1:]
    if lines and "```" in lines[-1]:
        lines = lines[:-1]
    return "\n".join(lines)

def translate_files():
    state = load_state()
    updated = False
    for root, _, files in os.walk(SRC_DIR):
        for file_name in files:
            if file_name.endswith(".md"):
                src_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(src_path, SRC_DIR)
                translated_relative_path = translate_path(relative_path)
                dst_path = os.path.join(DST_DIR, translated_relative_path)
                if needs_translation(src_path, dst_path, state):
                    with open(src_path, "r", encoding="utf-8") as src_file:
                        original_text = src_file.read()
                    print(f"Traduzindo arquivo: {src_path}")
                    translated_text = translate_text_gemini(original_text)
                    translated_text = remove_code_block_formatting(translated_text)
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    with open(dst_path, "w", encoding="utf-8") as dst_file:
                        dst_file.write(translated_text)
                    state[src_path] = {
                        "timestamp": os.path.getmtime(src_path),
                        "datetime": datetime.now().isoformat()
                    }
                    updated = True
                    print(f"Tradução concluída e salva em: {dst_path}")
                else:
                    print(f"Nenhuma modificação detectada em: {src_path}")
    if updated:
        save_state(state)

if __name__ == "__main__":
    translate_files()