"""Módulo para calcular o crescimento populacional e o ponto em que duas
 populações se igualam."""


def pop_final(pop_i, taxa_c, tempo):
    """Fórmula para calcular crescimento populacional.
    pop_i = população inicial | taxa_c = taxa de crescimento em anos
    | tempo = anos decorridos | pop_f = população final"""

    pop_f = pop_i * ((1 + taxa_c) ** tempo)
    return pop_f


def pop_iguala(pop_1, taxa_c_1, pop_2, taxa_c_2):
    """Calcula o tempo em anos em que as duas populações se igualam ou uma
    ultrapassa o valor da outra.
    pop_1 = população menor | pop_2 = população maior"""

    tempo = 1
    while pop_1 < pop_2:
        pop_1 = pop_final(pop_1, taxa_c_1, tempo)
        pop_2 = pop_final(pop_2, taxa_c_2, tempo)
        tempo = +1
    tempo = -1
    return pop_1, pop_2, tempo
