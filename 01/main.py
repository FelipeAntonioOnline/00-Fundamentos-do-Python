"""Programa para calcular a taxa de crescimento populacional de dois países e
 verificar o momento em que as populações irão atingir o mesmo valor."""

from crescimento import pop_iguala

print("Programa Para Comparar Populações\n")
print("Instruções:")
print("Por favor insira os dados requeridos do modo apropriado.")
print("Comece com os dados da população menor.\n")

pop_1 = int(input("População da menor cidade: "))
taxa_c_1 = float(input("Taxa de crescimento da menor cidade: "))
taxa_c_1 = taxa_c_1 / 100
pop_2 = int(input("População da maior cidade: "))
taxa_c_2 = float(input("Taxa de crescimento da menor cidade: "))
taxa_c_2 = taxa_c_2 / 100

pop_1_f, pop_2_f, tempo = pop_iguala(pop_1, taxa_c_1, pop_2, taxa_c_2)

print("População da primeira cidade:")
print(f"Inicial: {pop_1}")
print(f"Final: {round(pop_1_f)}")

print("População da segunda cidade:")
print(f"Inicial: {pop_2}")
print(f"Final: {round(pop_2_f)}")

print(f"Tempo para atingir esses números: {tempo}")
