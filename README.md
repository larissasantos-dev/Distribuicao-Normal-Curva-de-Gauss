# Trabalho: Distribuição Normal (Curva de Gauss)

## Divisão
- Larissa: Partes B e C (código), Parte A + base de dados + fórmulas (relatório)
- Lana: Partes D, E, F (código), resultados + interpretação + Parte G (relatório)

## Decisões combinadas
- Desvio-padrão e variância: **amostrais** (divisor n - 1)
- Assimetria: g1 = (1/n) * soma(((xi - media) / desvio)^3)
- Nomes de variáveis: `notas`, `media`, `desvio`
- Só podem ser usados: csv, math, matplotlib

## Funções da Pessoa 1 (parte_pessoa1.py)
- carregar_notas(caminho) -> lista de int
- calcular_media(notas) -> float
- calcular_mediana(notas) -> float
- calcular_modas(notas) -> lista
- calcular_variancia(notas, media) -> float (amostral)
- calcular_desvio_padrao(notas, media) -> float (amostral)
- calcular_assimetria(notas, media, desvio) -> float

## Funções da Pessoa 2 (parte_pessoa2.py)
- regra_empirica(notas, media, desvio) -> contagens e percentuais
- calcular_z(valor, media, desvio) -> float
- gerar_grafico(notas, media, desvio) -> salva histograma_curva_normal.png