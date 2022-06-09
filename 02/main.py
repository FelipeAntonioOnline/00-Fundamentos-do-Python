"""Programa pede cinco números e retorna o maior deles."""

print("Descubra Qual É O Maior Número Dentre Cinco\n")
num1, num2, num3, num4, num5 = input(
    "Insira cinco números separados por espaço: "
).split()
num_list = [num1, num2, num3, num4, num5]
num_list = map(int, num_list)
print(f"O maior número é: {max(num_list)}")
