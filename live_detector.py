import cv2
import detector
from result_saver import ResultSaver

# Uso de una cámara en tiempo real
class LiveBarcodeQRDetector(detector.BarcodeQRDetector):
    def __init__(self):
        super().__init__()
        self.result_saver = ResultSaver()

    def detectar_codigos_en_vivo(self):
        # Capturar video desde la cámara
        captura = cv2.VideoCapture(0)

        while True:
            # Leer un fotograma de video
            _, fotograma = captura.read()

            # Verificar el número de canales de la imagen
            if fotograma.ndim == 3:
                # La imagen tiene tres canales, convertir a escala de grises
                imagen_gris = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)
            elif fotograma.ndim == 2:
                # La imagen ya está en escala de grises
                imagen_gris = fotograma
            else:
                # Manejar el caso cuando la imagen no tiene el número correcto de canales
                print("Error: La imagen no tiene el número correcto de canales.")
                break

            # Continuar solo si la imagen tiene el número correcto de canales
            if imagen_gris is not None:
                # Aplicar procesamiento de imagen previo
                imagen_procesada = self.preprocesar_imagen(imagen_gris)

                # Detectar los códigos de barras y los QR codes
                codigos = self.detectar_codigos(imagen_procesada)

                # Mostrar los códigos detectados en la imagen
                for codigo in codigos:
                    contenido, tipo, (x, y, w, h) = codigo
                    cv2.rectangle(fotograma, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    texto = f"{contenido} ({tipo})"
                    cv2.putText(fotograma, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Mostrar la imagen con los códigos detectados
                cv2.imshow("Deteccion de codigos", fotograma)

                # Guardar los resultados
                self.result_saver.guardar_resultados(codigos, "links.csv")

                # Salir del bucle si se presiona la tecla 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # Liberar los recursos
        captura.release()
        cv2.destroyAllWindows()