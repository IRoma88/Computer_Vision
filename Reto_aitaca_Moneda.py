# -*- coding: utf-8 -*-

# Importar librerías
import numpy as np
import cv2
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

#Importar foto
cincuenta_cent = cv2.imread('/content/Moneda_50_cent.jpg')

#Mostrar imagen
cv2_imshow(cincuenta_cent)

img = cincuenta_cent

# Redimensionar imagen
alto, ancho = img.shape[:2]

# Determinar si la imagen es horizontal o vertical usando la relación de aspecto
if ancho > alto:
    # Rotar la imagen 90 grados en sentido antihorario (horizontal)
    img = cv2.transpose(img)  # Realiza la transposición
    img = cv2.flip(img, flipCode=0)  # Rota 90 grados antihorario al hacer flip
    print("Imagen girada 90 grados contrario a las agujas del reloj")
else:
    print("La imagen ya está en vertical")

# Mostrar la imagen (ya sea rotada o no)
plt.imshow(img)
plt.show()

#Recortar imagen
imagen_recortada = img[0:3000, 0:3500]

# Mostramos imagen
plt.imshow(imagen_recortada)
plt.show()

# Aplicar difuminado gaussiano
imagen_difuminada = cv2.GaussianBlur(imagen_recortada, (11, 11), 0)

# Mostrar la imagen difuminada
plt.imshow(imagen_difuminada)
plt.show()

imagen_recortada_gris = cv2.cvtColor(imagen_difuminada, cv2.COLOR_BGR2GRAY)
#imagen_recortada_gris = cv2.cvtColor(imagen_recortada, cv2.COLOR_BGR2GRAY)

circulo = cv2.HoughCircles(imagen_recortada_gris, cv2.HOUGH_GRADIENT, 1, 255,
                            param1=85, param2=90, minRadius=180, maxRadius=400)

# Rest of your code remains the same
circulo = np.uint16(np.around(circulo))

for i in circulo[0,:]:
    cv2.circle(imagen_recortada_gris,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(imagen_recortada_gris,(i[0],i[1]),2,(0,0,255),3)

print("He encontrado {} objeto".format(len(circulo)))

# Mostramos imagen
plt.imshow(imagen_recortada_gris)
plt.show()

# Radio del círculo
radio = circulo[0][0][2]

# Diámetro de la moneda
diametro = radio * 2

# Imagen ampliada
print("Imagen con el círculo")
cv2_imshow(imagen_recortada_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Diámetro y radio de la moneda
print("El radio de la moneda es:", radio, "pixels")
print("El diámetro de la moneda es:", diametro, "pixels")
print("\nRealizado por Iván Romaña.")
print("\.")
