"""Classe para criar uma bomba de combustível."""


class BombaDeCombustivel:
    """Insira (tipo, valor_litro, quantidade) para criar bomba de combustível com
    operações básicas.

    tipo - tipo de combustível.

    valor_litro - valor litro na moeda desejada.

    quantidade - quantidade em litros do combustível.
    """

    def __init__(self, tipo=str, valor_litro=float, quantidade=float):
        self.tipo_combustivel = tipo
        self.valor_litro = valor_litro
        self.quantidade = quantidade

    def abastecer_por_valor(self, dinheiro=float) -> "float":
        """Insira (dinheiro) e a quantidade (abastecido) é retornada"""
        abastecido = dinheiro / self.valor_litro
        self.quantidade -= abastecido
        return abastecido

    def abastecer_por_litro(self, litros=float) -> "float":
        """Insira quantidade em (litros) e retorna valor (cobrado)."""
        cobrado = litros * self.valor_litro
        self.quantidade -= litros
        return cobrado

    def alterar_valor(self, novo_valor=float):
        """Insira (novo_valor) para alterar (valor_litro)."""
        self.valor_litro = novo_valor

    def alterar_tipo(self, novo_tipo=str):
        """Insira (novo_tipo) para alterar (tipo_combustivel)."""
        self.tipo_combustivel = novo_tipo

    def alterar_quantidade(self, nova_quantidade=float):
        """Insira (nova_quantidade) para alterar (quantidade)."""
        self.quantidade = nova_quantidade
