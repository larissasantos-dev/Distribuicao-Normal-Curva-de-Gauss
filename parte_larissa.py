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

if __name__ == "__main__":
    notas = carregar_notas("C:/Users/Larissa/Desktop/Lala/IFSP/Estatistica/projeto_python_teste/projeto_distribuicao_normal_curva_de_gauss/Distribuicao-Normal-Curva-de-Gauss/StudentsPerformance.csv")