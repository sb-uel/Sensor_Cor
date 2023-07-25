import win32api
import win32gui
import time
import math
from colors import Color, cores

# Abre um handle para a tela do desktop
hdc = win32gui.GetDC(None)

# Loop infinito
while True:
    # Obtem a posicao atual do cursor
    cursorPos = win32api.GetCursorPos()

    # Obtem a cor do pixel sob o cursor
    cor = win32gui.GetPixel(hdc, cursorPos[0], cursorPos[1])

    # Extrai os componentes R, G e B da cor
    r = cor & 0xFF
    g = (cor >> 8) & 0xFF
    b = (cor >> 16) & 0xFF

    # Procura na tabela de cores a correspondencia mais proxima
    melhorCorrespondencia = 0
    menorDistancia = 256 * 256 * 256
    for i in range(len(cores)):
        distancia = (r - cores[i].r) ** 2 + \
            (g - cores[i].g) ** 2 + (b - cores[i].b) ** 2
        if distancia < menorDistancia:
            melhorCorrespondencia = i
            menorDistancia = distancia

    # Imprime o nome da cor mais proxima na tela
    print("Cor: {} ({}, {}, {})".format(
        cores[melhorCorrespondencia].nome, r, g, b))

    # Espera por um pequeno intervalo de tempo antes de repetir
    time.sleep(0.5)

# Fecha o handle da tela
win32gui.ReleaseDC(None, hdc)