import cv2
import os

# Crear objeto VideoCapture
cap = cv2.VideoCapture(0)

# Comprobar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

# Variables para contar el número de fotos tomadas y el límite de fotos a capturar
contador = 0
limite_fotos = 5
ruta_guardado = 'D:\\Escritorio\\LAB'

# Bucle para tomar fotos
while contador < limite_fotos:
    # Leer el siguiente fotograma
    ret, frame = cap.read()

    # Comprobar si se pudo leer el fotograma
    if not ret:
        print("Error al capturar el fotograma.")
        break

    # Generar el nombre de archivo único
    nombre_archivo = f"foto{contador}.png"
    ruta_completa = os.path.join(ruta_guardado, nombre_archivo)

    # Tomar la foto y guardarla en la ubicación especificada
    cv2.imwrite(ruta_completa, frame)
    print(f"Foto guardada en: {ruta_completa}")

    # Incrementar el contador
    contador += 1

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
