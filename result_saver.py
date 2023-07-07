import os
import csv
import webbrowser
import time
from dotenv import load_dotenv

class ResultSaver:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde el archivo .env
        
        directorio_base = os.getenv("DIRECTORIO_BASE")
        self.directorio_resultados = os.path.join(directorio_base, os.getenv("DIRECTORIO_RESULTADOS"))
        self.enlaces_abiertos = {}

    def guardar_resultados(self, codigos_detectados, archivo):
        # Crear la carpeta de resultados si no existe
        if not os.path.exists(self.directorio_resultados):
            os.makedirs(self.directorio_resultados)

        # Leer los códigos ya escaneados
        codigos_previos = self.leer_codigos_escaneados()

        # Procesar los nuevos códigos detectados
        for codigo in codigos_detectados:
            contenido, tipo, (x, y, w, h) = codigo

            # Verificar si el código ya ha sido escaneado antes
            if contenido in codigos_previos:
                numero_qr = codigos_previos[contenido]
                print(f"El código QR {contenido} ya ha sido escaneado antes (Número: {numero_qr})")

                tiempo_espera = 15  # Tiempo de espera por defecto
                if contenido in self.enlaces_abiertos:
                    tiempo_apertura = self.enlaces_abiertos[contenido]
                    tiempo_transcurrido = time.time() - tiempo_apertura
                    tiempo_restante = tiempo_espera - tiempo_transcurrido
                    if tiempo_restante > 0:
                        print(f"Debe esperar {tiempo_restante:.1f} segundos para volver a abrir este QR.")
                        continue

                self.abrir_enlace(contenido)
                self.enlaces_abiertos[contenido] = time.time()
            else:
                # Obtener el número del nuevo código QR
                numero_qr = len(codigos_previos) + 1
                codigos_previos[contenido] = numero_qr

                # Guardar el nuevo código QR en el archivo de códigos escaneados
                self.guardar_codigos_escaneados(codigos_previos)

                # Crear el archivo de resultados para el nuevo código QR
                archivo_resultados = os.path.join(self.directorio_resultados, archivo)
                with open(archivo_resultados, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([numero_qr, contenido])

                print(f"Se ha guardado el código QR {contenido} en el archivo {archivo_resultados}")
                self.abrir_enlace(contenido)
                self.enlaces_abiertos[contenido] = time.time()

    def leer_codigos_escaneados(self):
        codigos_previos = {}
        archivo_codigos = os.path.join(self.directorio_resultados, f"{os.getenv('ARCHIVO_CODIGOS')}.csv")
        if os.path.exists(archivo_codigos):
            with open(archivo_codigos, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    numero_qr, contenido = row
                    codigos_previos[contenido] = int(numero_qr)
        return codigos_previos

    def guardar_codigos_escaneados(self, codigos_previos):
        archivo_codigos = os.path.join(self.directorio_resultados, f"{os.getenv('ARCHIVO_CODIGOS')}.csv")
        with open(archivo_codigos, "w", newline="") as file:
            writer = csv.writer(file)
            for contenido, numero_qr in codigos_previos.items():
                writer.writerow([numero_qr, contenido])

    def abrir_enlace(self, enlace):
        webbrowser.open(enlace)
