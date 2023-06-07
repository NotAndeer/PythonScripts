import cv2

# Crear objeto VideoCapture
cap = cv2.VideoCapture(0)

# Comprobar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

# Variables para controlar el número de fotos y los nombres de archivo
num_fotos = 0
nombre_base = 'D:\\Escritorio\\LAB\\foto'

# Bucle para tomar las fotos
while num_fotos < 10:
    # Leer el siguiente fotograma
    ret, frame = cap.read()

    # Comprobar si se pudo leer el fotograma
    if not ret:
        print("Error al capturar el fotograma.")
        break

    # Incrementar el número de fotos y construir el nombre del archivo
    num_fotos += 1
    nombre_archivo = f"{nombre_base}_{num_fotos}.png"

    # Guardar la foto en la ubicación especificada
    cv2.imwrite(nombre_archivo, frame)
    print(f"Foto {num_fotos} guardada en: {nombre_archivo}")

    # Esperar 1 segundo antes de tomar la siguiente foto
    cv2.waitKey(1000)

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()