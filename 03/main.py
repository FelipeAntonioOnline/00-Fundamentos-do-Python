"""Programa pede números e realiza a média aritimética entre eles."""

escolha = "s"
soma = 0
partes = 0

print("Vamos Calcular A Média Aritimética\n")

while escolha == "s":
    numero = int(input("Acrescente um número: "))
    soma += numero
    partes += 1
    escolha = input("Deseja acrescentar outro número? (s/n)")
    escolha.lower()

media_ari = soma / partes
print(f"A média é: {media_ari}")
