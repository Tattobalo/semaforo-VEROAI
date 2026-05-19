import cv2
import numpy as np


class Preprocesador:

    @staticmethod
    def resize(frame):
        return cv2.resize(frame, (1280, 720))

    @staticmethod
    def reducir_ruido(frame):
        return cv2.GaussianBlur(frame, (3, 3), 0)

    @staticmethod
    def mejorar_contraste(frame):

        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        l, a, b = cv2.split(lab)

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        l = clahe.apply(l)

        lab = cv2.merge((l, a, b))

        return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    @staticmethod
    def sharpen(frame):

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        return cv2.filter2D(frame, -1, kernel)

    @classmethod
    def procesar(cls, frame):

        frame = cls.resize(frame)

        frame = cls.reducir_ruido(frame)

        frame = cls.mejorar_contraste(frame)

        frame = cls.sharpen(frame)

        return frame