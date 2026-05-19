import cv2
from PyQt6.QtCore import QThread, pyqtSignal


class CamaraThread(QThread):

    frame_actualizado = pyqtSignal(int, object)

    def __init__(self, idx_camara: int, fuente: str):
        super().__init__()

        self.idx_camara = idx_camara
        self.fuente = fuente

        self.running = True

    def run(self):

        cap = cv2.VideoCapture(self.fuente)

        while self.running:

            ret, frame = cap.read()

            if not ret:
                continue

            self.frame_actualizado.emit(self.idx_camara, frame)

        cap.release()

    def detener(self):
        self.running = False