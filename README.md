# 🔎 Detector de Códigos de Barras y QR

Este proyecto es un detector de códigos de barras y códigos QR en imágenes estáticas y en tiempo real utilizando la cámara del dispositivo. El detector utiliza la biblioteca OpenCV y PyZbar para el procesamiento de imágenes y la decodificación de los códigos.

## 📝 Descripción

El detector consta de los siguientes archivos:

- [📄 `main.py`](main.py): El archivo principal que ejecuta el detector en imágenes estáticas.
- [📄 `detector.py`](detector.py): Contiene la clase `BarcodeQRDetector` que se encarga de detectar los códigos de barras y QR codes en una imagen.
- [📄 `live_detector.py`](live_detector.py): Contiene la clase `LiveBarcodeQRDetector` que hereda de `BarcodeQRDetector` y permite la detección en tiempo real utilizando la cámara.
- [📄 `result_saver.py`](result_saver.py): Contiene la clase `ResultSaver` que se encarga de guardar los resultados de los códigos detectados y abrir los enlaces correspondientes.

## 📚 Librerías utilizadas

- 🌐 OpenCV: Biblioteca de visión por computadora utilizada para el procesamiento de imágenes y la detección de códigos de barras y QR.
- 📦 PyZbar: Biblioteca utilizada para la decodificación de los códigos de barras y QR codes.
- ⚙️ dotenv: Biblioteca utilizada para cargar las variables de entorno desde el archivo `.env`.

## 🔧 Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

```
opencv-python
pyzbar
python-dotenv
```

Puedes instalar las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## 💻 Uso

1. Clonación del repositorio:

   Clona el repositorio en tu dispositivo:

   ```bash
   git clone https://github.com/ElJoamy/Detector-QRbarras.git
   ```

2. Instalación de dependencias:

   Asegúrate de tener instaladas las siguientes bibliotecas:

   ```bash
   pip install -r requirements.txt
   ```

   Las bibliotecas necesarias se encuentran en el archivo `requirements.txt` y se pueden instalar con el comando anterior.

3. Configuración de variables de entorno:

   - Crea un archivo `.env` en el mismo directorio que los archivos `.py`. Puedes utilizar el archivo de ejemplo [`env.example`](.env.example) como referencia.

     ```
     DIRECTORIO_BASE=Detector-QRbarras
     DIRECTORIO_RESULTADOS=resultados_qr
     ARCHIVO_CODIGOS=codigos_escaneados
     ```

     `DIRECTORIO_BASE` es el nombre de la carpeta base donde se almacenarán los resultados y archivos relacionados.

   - Guarda el archivo `.env` con las configuraciones.

4. Ejecución:

   - Para detectar códigos QR en tiempo real:

     Ejecuta el archivo [`main.py`](main.py):

     ```bash
     python main.py
     ```

     El programa se ejecutará y mostrará el live stream de la cámara con los códigos detectados y sus enlaces correspondientes. Los resultados se guardarán en un archivo .csv en la carpeta `resultados_qr`, junto con dos archivos adicionales para verificación y memoria de los códigos detectados.

     Además, hay un delay de 15 segundos para que cuando se lea un código QR, no se vuelva a leer el mismo código hasta que hayan pasado los 15 segundos.

## 👍 Mejoras futuras

- Agregar funcionalidad para guardar y abrir enlaces con diferentes navegadores.
- Mejorar los criterios de filtrado de falsos positivos.
- Implementar una interfaz gráfica más amigable para el usuario.

## 🤝 Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor, abre un issue o envía una pull request.

## 📜 Licencia

Este proyecto se encuentra bajo la [Licencia MIT](LICENSE).