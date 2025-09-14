import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2
from PIL import Image

def abrir_imagen(ruta):
    img = Image.open(ruta).convert("RGB")
    return np.array(img)

# Crea filtro circular en el centro del EspectroFourier
# Se puede cambiar por un Cuadrado si lo programas :)
def filtro_circ(Img, R):  
    n, m = Img.shape
    cy, cx = n // 2, m // 2
    Y, X = np.ogrid[:n, :m]
    dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
    Mask = dist <= R
    return Img * Mask

def TransfoFourier(Imagen, R=100):
    canales = [Imagen[:,:,i] for i in range(3)]  # R, G, B
    Color_Reconstruido = []

    for canal in canales:
        Fourier = fft2(canal)                 #Fourier
        ffase = np.fft.fftshift(Fourier)      #Pa' Corregir faseEspectro
        
        Filtro = filtro_circ(ffase, R)
        ffase_inv = np.fft.ifftshift(Filtro)  #Inversa de la fase
        canal_rec = np.fft.ifft2(ffase_inv)   #Fourier^{-1}
        
        Color_Reconstruido.append(np.abs(canal_rec))

    return np.stack(Color_Reconstruido, axis=-1) #Imagen recuperada

# ------------- Programa principal -----------------------

print('Ingrese Imagen ["Img.jpg"]')
Imagen = input().strip()

print('Valor para filtro de Radio: ')
R = int(input())

Imagen = abrir_imagen(Imagen)
New = TransfoFourier(Imagen, R)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(New.astype(np.uint8))
plt.title("Imagen Reconstruida")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(Imagen.astype(np.uint8))
plt.title("Imagen Original")
plt.axis("off")
plt.tight_layout()
plt.show()

print("¿Deseas guardar archivo? [y/n]")
Respuesta = input().strip().lower()

if Respuesta == 'y':
	#Image.fromarray(Imagen.astype(np.uint8)).save("original.jpg")
	Image.fromarray(New.astype(np.uint8)).save("recovered.jpg",quality=50)

	print("Archivos guardados como 'original.png' y 'recovered.png'")
