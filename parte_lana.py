import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


#    PARTE DA LANA                                             #
#    Parte D: regra 68-95-99,7                                 #
#    Parte E: escores padronizados (z)                         #
#    Parte F: representação gráfica                            #


def regra_empirica(notas, media, desvio):
    total = len(notas)
    resultados = {}
    for k in (1, 2, 3):
        inferior = media - k * desvio
        superior = media + k * desvio
        quantidade = sum(1 for nota in notas if inferior <= nota <= superior)
        resultados[k] = {
            "inferior": inferior,
            "superior": superior,
            "quantidade": quantidade,
            "percentual": quantidade / total * 100,
        }
    return resultados


def calcular_z(valor, media, desvio):
    return (valor - media) / desvio


def e_atipico(z):
    return abs(z) > 3


def escores_pedidos(notas, media, desvio):
    valores = [
        ("Menor nota", min(notas)),
        ("Maior nota", max(notas)),
        ("Nota 50", 50),
        ("Nota 75", 75),
        ("Nota 90", 90),
    ]
    linhas = []
    for nome, valor in valores:
        z = calcular_z(valor, media, desvio)
        linhas.append((nome, valor, z, e_atipico(z)))
    return linhas


def densidade_normal(x, media, desvio):
    expoente = -((x - media) ** 2) / (2 * desvio ** 2)
    return math.exp(expoente) / (desvio * math.sqrt(2 * math.pi))


def gerar_grafico(notas, media, desvio, arquivo="histograma_curva_normal.png"):
    fig, ax = plt.subplots(figsize=(10, 6))

    limites = list(range(0, 105, 5))
    ax.hist(notas, bins=limites, density=True, color="#9ecae1",
            edgecolor="white", label="Notas observadas")

    xs = [i / 10 for i in range(0, 1001)]
    ys = [densidade_normal(x, media, desvio) for x in xs]
    ax.plot(xs, ys, color="#d62728", linewidth=2.2, label="Curva normal teórica")

    ax.axvline(media, color="#2ca02c", linewidth=2,
               label=f"Média = {media:.2f}".replace(".", ","))
    ax.axvline(media - desvio, color="#ff7f0e", linestyle="--", linewidth=1.8,
               label=f"Média − 1 desvio = {media - desvio:.2f}".replace(".", ","))
    ax.axvline(media + desvio, color="#ff7f0e", linestyle="--", linewidth=1.8,
               label=f"Média + 1 desvio = {media + desvio:.2f}".replace(".", ","))

    ax.set_title("Distribuição das notas de matemática (n = %d)" % len(notas))
    ax.set_xlabel("Nota de matemática")
    ax.set_ylabel("Densidade")
    ax.set_xlim(0, 100)
    ax.legend()
    fig.savefig(arquivo, dpi=150, bbox_inches="tight")
    plt.close(fig)


def gerar_boxplot(notas, arquivo="boxplot_notas.png"):
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.boxplot(notas, showmeans=True)
    ax.set_title("Gráfico de caixa das notas de matemática")
    ax.set_ylabel("Nota de matemática")
    ax.set_xticks([])
    fig.savefig(arquivo, dpi=150, bbox_inches="tight")
    plt.close(fig)
