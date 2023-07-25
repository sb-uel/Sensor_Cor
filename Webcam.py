import cv2
import numpy as np
from colors import Color, cores

def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_color = frame[y, x]
        r, g, b = pixel_color[2], pixel_color[1], pixel_color[0]

        melhorCorrespondencia = 0
        menorDistancia = 256 * 256 * 256
        for i in range(len(cores)):
            distancia = (r - cores[i].r) ** 2 + (g - cores[i].g) ** 2 + (b - cores[i].b) ** 2
            if distancia < menorDistancia:
                melhorCorrespondencia = i
                menorDistancia = distancia

        print("Cor: {} ({}, {}, {})".format(cores[melhorCorrespondencia].nome, r, g, b))

# Inicializa a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Define a função de callback para o evento de clique do mouse
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", get_color)

# Loop infinito
while True:
    # Captura o próximo frame de vídeo
    ret, frame = cap.read()

    # Exibe o frame de vídeo na janela
    cv2.imshow("Webcam", frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()