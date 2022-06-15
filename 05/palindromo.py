"""Programa para verificar se uma string pode ser considerada palíndromo."""

from unicodedata import normalize


def _remover_acentos(txt=str):
    """Insira string para retorná-la com as vogais sem acento."""
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


def verifica_pali(teste_pali=str):
    """Insira uma string e retorna se é um palíndromo ou não."""

    teste_pali_limpo = _remover_acentos(teste_pali.lower())
    teste_pali_check = ""
    for letra in teste_pali_limpo:
        if letra.isalpha():
            teste_pali_check += letra
    if teste_pali_check == teste_pali_check[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo")
