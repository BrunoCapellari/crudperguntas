import json
import os

ARQUIVO = "perguntas.json"

def carregar_dados():
    """Lê o arquivo JSON e retorna uma lista de perguntas."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  
    return []

def salvar_dados(perguntas):
    """Salva toda a lista de perguntas em JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, indent=4, ensure_ascii=False)

def validar_pergunta(pergunta):
    """Confere se a pergunta está completa."""
    if not pergunta.get("pergunta"):
        return False
    if not pergunta.get("opcao1") or not pergunta.get("opcao2") or not pergunta.get("opcao3"):
        return False
    if pergunta.get("correta") not in [0, 1, 2]:
        return False
    return True

def adicionar(perguntas, nova):
    """Adiciona nova pergunta ao JSON."""
    if not validar_pergunta(nova):
        raise ValueError("Dados incompletos ou incorretos.")
    perguntas.append(nova)
    salvar_dados(perguntas)
    return perguntas

def atualizar(perguntas, indice, nova):
    """Atualiza pergunta existente."""
    if indice < 0 or indice >= len(perguntas):
        raise IndexError("Índice inválido.")
    if not validar_pergunta(nova):
        raise ValueError("Campos incompletos.")
    perguntas[indice] = nova
    salvar_dados(perguntas)
    return perguntas

def excluir(perguntas, indice):
    """Remove uma pergunta pelo índice."""
    if indice < 0 or indice >= len(perguntas):
        raise IndexError("Índice inválido.")
    removida = perguntas.pop(indice)
    salvar_dados(perguntas)
    return perguntas
