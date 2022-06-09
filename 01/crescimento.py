"""Módulo para calcular o crescimento populacional e o ponto em que duas
 populações se igualam."""


def pop_final(pop_i, taxa_c, tempo):
    """Fórmula para calcular crescimento populacional.
    pop_i = população inicial | taxa_c = taxa de crescimento em anos
    | tempo = anos decorridos | pop_f = população final"""

    pop_f = pop_i * ((1 + taxa_c) ** tempo)
    return pop_f
