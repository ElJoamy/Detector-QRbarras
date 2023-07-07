import cv2
from pyzbar import pyzbar

class BarcodeQRDetector:
    def __init__(self):
        self.filtro_falsos_positivos = True

    def detectar_codigos(self, imagen):
    # Aplicar procesamiento de imagen previo
        imagen_procesada = self.preprocesar_imagen(imagen)

        # Detectar los códigos de barras y los QR codes
        codigos = pyzbar.decode(imagen_procesada)

        # Detectar los códigos de barras y los QR codes
        codigos = pyzbar.decode(imagen_procesada)

        # Lista para almacenar los códigos detectados
        codigos_detectados = []

        # Iterar sobre los códigos detectados
        for codigo in codigos:
            # Extraer las coordenadas de los vértices del código
            (x, y, w, h) = codigo.rect

            # Filtrar falsos positivos si está habilitado
            if self.filtro_falsos_positivos and not self.validar_codigo(codigo):
                continue

            # Decodificar el contenido del código
            contenido = codigo.data.decode("utf-8")
            tipo = codigo.type

            # Agregar el código detectado a la lista
            codigos_detectados.append((contenido, tipo, (x, y, w, h)))

        return codigos_detectados

    def preprocesar_imagen(self, imagen):
        # Aplicar técnicas de procesamiento de imagen previo
        imagen_suavizada = cv2.GaussianBlur(imagen, (3, 3), 0)
        return imagen_suavizada


    def validar_codigo(self, codigo):
        # Aplicar criterios para filtrar falsos positivos
        # En este ejemplo, se filtran los códigos cuyo tamaño es menor a 100 píxeles
        (x, y, w, h) = codigo.rect
        tamano_minimo = 100
        if w < tamano_minimo or h < tamano_minimo:
            return False
        return True
