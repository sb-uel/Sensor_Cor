import sys
import cv2
import math
from sklearn.cluster import KMeans
from colours import cores, Color

def extract_dominant_colors(image_path, num_colors):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape(image.shape[0] * image.shape[1], 3)
    
    kmeans = KMeans(n_clusters=num_colors,n_init= 10)
    kmeans.fit(image)
    
    colors = kmeans.cluster_centers_
    colors = colors.astype(int)
    
    dominant_colors = colors.tolist()

    return dominant_colors

def rgb_para_nome_cor(rgb, cores):
    min_distancia = float('inf')  # Inicializa a distância mínima com um valor alto
    cor_mais_proxima = None

    for cor in cores:
        # Calcula a distância Euclidiana entre os valores RGB
        distancia = math.sqrt((cor.r - rgb[0])**2 + (cor.g - rgb[1])**2 + (cor.b - rgb[2])**2)

        # Verifica se a distância atual é menor que a distância mínima encontrada até agora
        if distancia < min_distancia:
            min_distancia = distancia
            cor_mais_proxima = cor

    if cor_mais_proxima is not None:
        return cor_mais_proxima.nome
    else:
        return "Cor desconhecida"

# Verifica se o caminho da imagem e o número de cores foram fornecidos como argumentos
if len(sys.argv) > 1:
    caminho_imagem = sys.argv[1]

    # Extrai as cores predominantes da imagem
    cores_rgb = extract_dominant_colors(caminho_imagem, 1)
    nome_cor = [rgb_para_nome_cor(rgb, cores) for rgb in cores_rgb]
    cores_string = ', '.join(nome_cor)
    
    print("\n")
    print("Imagem = ", caminho_imagem)
    print("\n")
    print("Cor predominante = ", cores_string)
    print("\n")
else:
    print("Caminho da imagem ou número de cores não fornecidos.")