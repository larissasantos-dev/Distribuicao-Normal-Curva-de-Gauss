# Trabalho: Distribuição Normal (Curva de Gauss)

## Divisão
- Larissa: Partes B e C (código), Parte A + base de dados + fórmulas (relatório)
- Lana: Partes D, E, F (código), resultados + interpretação + Parte G (relatório)

## Decisões combinadas
- Desvio-padrão e variância: **amostrais** (divisor n - 1)
- Assimetria: g1 = (1/n) * soma(((xi - media) / desvio)^3)
- Nomes de variáveis: `notas`, `media`, `desvio`
- Só podem ser usados: csv, math, matplotlib

## Funções da Larissa (parte_larissa.py)
- carregar_notas(caminho), calcular_media(notas), calcular_mediana(notas),
  calcular_modas(notas), calcular_variancia(notas, media),
  calcular_desvio_padrao(notas, media), calcular_assimetria(notas, media, desvio)

## Funções da Lana (parte_lana.py)
- regra_empirica(notas, media, desvio), calcular_z(valor, media, desvio),
  gerar_grafico(notas, media, desvio)

## Valores de referência (math score)
n = 1000 | mín 0 | máx 100 | média 66,089 | mediana 66,0 | moda 65
variância 229,919 | desvio 15,1631 | assimetria -0,2781