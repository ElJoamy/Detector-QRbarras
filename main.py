import cv2
from live_detector import LiveBarcodeQRDetector
from result_saver import ResultSaver

detector_en_vivo = LiveBarcodeQRDetector()

result_saver = ResultSaver()

detector_en_vivo.detectar_codigos_en_vivo()

codigos_detectados = detector_en_vivo.get_codigos_detectados()

result_saver.guardar_resultados(codigos_detectados)
