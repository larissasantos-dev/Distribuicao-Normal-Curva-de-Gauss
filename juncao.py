from parte_larissa import (
    carregar_notas,
    calcular_media,
    calcular_mediana,
    calcular_modas,
    calcular_variancia,
    calcular_desvio_padrao,
    calcular_assimetria,
)
from parte_lana import (
    regra_empirica,
    calcular_z,
    e_atipico,
    escores_pedidos,
    gerar_grafico,
    gerar_boxplot,
)


#    JUNÇÃO DAS DUAS PARTES (função auxiliar + programa principal)


def fmt(numero, casas=2):
    return f"{numero:.{casas}f}".replace(".", ",")


def main():
    # ---------- Parte B (Larissa) ----------
    notas = carregar_notas("StudentsPerformance.csv")
    media = calcular_media(notas)
    desvio = calcular_desvio_padrao(notas, media)

    # ---------- Parte C (Larissa) ----------
    print("\n--- Parte C: medidas estatísticas (math score) ---")
    print("Quantidade de dados:", len(notas))
    print("Menor nota:", min(notas))
    print("Maior nota:", max(notas))
    print("Amplitude total:", max(notas) - min(notas))
    print("Média aritmética:", fmt(media, 3))
    print("Mediana:", fmt(calcular_mediana(notas), 1))
    print("Moda(s):", calcular_modas(notas))
    print("Variância amostral:", fmt(calcular_variancia(notas, media), 3))
    print("Desvio-padrão amostral:", fmt(desvio, 4))
    print("Coeficiente de assimetria:", fmt(calcular_assimetria(notas, media, desvio), 4))

    # ---------- Parte D (Lana) ----------
    print("\n--- Parte D: regra 68-95-99,7 ---")
    esperado = {1: 68.27, 2: 95.45, 3: 99.73}
    for k, r in regra_empirica(notas, media, desvio).items():
        print(f"Média ± {k} desvio: [{fmt(r['inferior'])}; {fmt(r['superior'])}] | "
              f"{r['quantidade']} notas | {fmt(r['percentual'])}% "
              f"(esperado ≈ {fmt(esperado[k])}%)")

    # ---------- Parte E (Lana) ----------
    print("\n--- Parte E: escores z ---")
    for nome, valor, z, atipico in escores_pedidos(notas, media, desvio):
        print(f"{nome}: {valor} | z = {fmt(z)} | atípico: {'Sim' if atipico else 'Não'}")
    atipicas = sorted(x for x in notas if e_atipico(calcular_z(x, media, desvio)))
    print(f"Notas com |z| > 3 em toda a base: {len(atipicas)} -> {atipicas}")

    # ---------- Parte F (Lana) ----------
    gerar_grafico(notas, media, desvio)
    gerar_boxplot(notas)
    print("\nGráficos salvos: histograma_curva_normal.png e boxplot_notas.png")


if __name__ == "__main__":
    main()
