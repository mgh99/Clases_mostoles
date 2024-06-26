import cv2
import imageio
import numpy as np
from scipy.ndimage import gaussian_filter


# Función para convertir la imagen a sketch
def image_to_sketch(image_path, sigma=10):
    # Leer la imagen
    img = imageio.imread(image_path)
    
    # Convertir a escala de grises
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invertir la imagen en escala de grises
    inverted_img = 255 - gray_img
    
    # Aplicar filtro Gaussian para suavizar la imagen
    blurred_img = gaussian_filter(inverted_img, sigma=sigma)
    
    # Invertir la imagen suavizada
    inverted_blurred_img = 255 - blurred_img
    
    # Crear el sketch combinando la imagen en escala de grises y la imagen suavizada invertida
    sketch = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
    
    return sketch

# Ruta de la imagen de entrada
image_path = 'C:/Users/Asus/Desktop/pruebas/python/gato.png'

# Convertir la imagen a sketch
sketch = image_to_sketch(image_path)

# Guardar el sketch resultante
output_path = 'C:/Users/Asus/Desktop/pruebas/python/sketch_gato.png'
imageio.imwrite(output_path, sketch)

print("Sketch guardado exitosamente.")
