import csv
import math

def carregar_notas(caminho):
    """Le o CSV e devolve a lista de notas de matematica (int)."""
    notas, invalidos = [], 0
    with open(caminho, newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            try:
                notas.append(int(linha["math score"]))
            except(ValueError, KeyError):
                invalidos += 1
    print(f"Registros carregados: {len(notas)} | invalidos/ausentes: {invalidos}")
    return notas

def calcular_media(notas):
    """Media aritmetica: soma de todos os valores divididas pela quantidade."""
    return sum(notas) / len(notas)

def calcular_mediana(notas):
    """Valor central da lista ordenada. Se n é par, média dos dois centrais."""
    ordenadas = sorted(notas)
    n = len(ordenadas)
    meio = n // 2
    if n % 2 == 1:
        return float(ordenadas[meio])
    return (ordenadas[meio - 1] + ordenadas[meio]) / 2

def calcular_modas(notas):
    """Valor(es) maqis frequente(s). Pode haver mais de uma moda."""
    frequencias = {}
    for nota in notas:
        frequencias[nota] = frequencias.get(nota, 0) + 1
    maior = max(frequencias.values())
    return sorted(n for n, f in frequencias.items() if f == maior)

def calcular_variancia(notas, media):
    """Variância amostral: soma dos quadrados dos desvios dividida por (n - 1)."""
    soma = sum((x - media) ** 2 for x in notas)
    return soma / (len(notas) - 1)

def calcular_desvio_padrao(notas, media):
    """Desvio-padrão amostral: raiz quadrada da variância amostral."""
    return math.sqrt(calcular_variancia(notas, media))

def calcular_assimetria(notas, media, desvio):
    """Assimetria g1 = (1/n) * soma(((x - media) / desvio) ** 3).
    Positiva: cauda à direita. Negativa: cauda à esquerda. Perto de 0: simétrica."""
    n = len(notas)
    return sum(((x - media) / desvio) ** 3 for x in notas) / n

if __name__ == "__main__":
    # Teste com lista pequena (resultado conhecido: média 5, moda 4)
    teste = [2, 4, 4, 4, 5, 5, 7, 9]
    m = calcular_media(teste)
    print("TESTE -> média:", m, "| mediana:", calcular_mediana(teste),
          "| modas:", calcular_modas(teste),
          "| desvio:", round(calcular_desvio_padrao(teste, m), 4))

    notas = carregar_notas("C:/Users/Larissa/Desktop/Lala/IFSP/Estatistica/projeto_python_teste/projeto_distribuicao_normal_curva_de_gauss/Distribuicao-Normal-Curva-de-Gauss/StudentsPerformance.csv")
    media = calcular_media(notas)
    desvio = calcular_desvio_padrao(notas, media)

    print("\n--- Medidas estatísticas (math score) ---")
    print("Quantidade de dados:", len(notas))
    print("Menor nota:", min(notas))
    print("Maior nota:", max(notas))
    print("Amplitude total:", max(notas) - min(notas))
    print("Média:", round(media, 4))
    print("Mediana:", calcular_mediana(notas))
    print("Moda(s):", calcular_modas(notas))
    print("Variância amostral:", round(calcular_variancia(notas, media), 4))
    print("Desvio-padrão amostral:", round(desvio, 4))
    print("Assimetria:", round(calcular_assimetria(notas, media, desvio), 4))
