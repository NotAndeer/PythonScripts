import cv2

# Crear objeto VideoCapture
cap = cv2.VideoCapture(0)

# Comprobar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

# Bucle para mostrar el contenido de la cámara
while True:
    # Leer el siguiente fotograma
    ret, frame = cap.read()

    # Comprobar si se pudo leer el fotograma
    if not ret:
        print("Error al capturar el fotograma.")
        break

    # Mostrar el fotograma en una ventana
    cv2.imshow('Cámara', frame)

    # Esperar a que se presione la tecla 'q' para salir
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
