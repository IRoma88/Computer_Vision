# 🪙 Detección de Moneda con OpenCV

Este proyecto utiliza **OpenCV** y la **Transformada de Hough** para detectar monedas en una imagen y calcular su radio y diámetro en píxeles.

---

## 🧠 Descripción del Proyecto

Se carga una imagen de una moneda (por ejemplo, una de 50 céntimos), se corrige su orientación, se recorta para enfocar la región de interés, se aplica un difuminado para mejorar la detección y se utiliza la función `HoughCircles` para encontrar la moneda y calcular su tamaño.

---

## 📷 Ejemplo de Flujo

1. **Importar imagen**: `/content/Moneda_50_cent.jpg`
2. **Corregir orientación** automáticamente según relación de aspecto
3. **Recortar región de interés**
4. **Aplicar filtro Gaussiano**
5. **Convertir a escala de grises**
6. **Detectar círculo con `cv2.HoughCircles()`**
7. **Dibujar el círculo y mostrar el resultado**
8. **Imprimir radio y diámetro en píxeles**

---

## ▶️ Ejecución

Este código está diseñado para ejecutarse en **Google Colab**:

1. Sube tu imagen (`Moneda_50_cent.jpg`) al entorno.
2. Ejecuta el script.
3. Verás la moneda detectada junto con sus dimensiones.

---

## 📁 Estructura

├── moneda_detection.py 

├── Moneda_50_cent.jpg 

├── README.md

├── requirements.txt 

└── .gitignore

## 📦 Requisitos

- Python 3.8+
- OpenCV
- matplotlib
- numpy

Instala dependencias con:

```bash
pip install -r requirements.txt
````

## ✍️ Autor
Realizado por Iván Romaña
📧 ivan.romana88@gmail.com
