import cv2


class GestorROI:

    def __init__(self):

        self.rois = {
            0: {
                "carril_1": (0, 0, 640, 720),
                "carril_2": (640, 0, 1280, 720)
            },

            1: {
                "carril_3": (0, 0, 640, 720),
                "carril_4": (640, 0, 1280, 720)
            }
        }

    def obtener_rois(self, idx_camara, frame):

        resultado = {}

        for nombre, (x1, y1, x2, y2) in self.rois[idx_camara].items():

            roi = frame[y1:y2, x1:x2]

            resultado[nombre] = roi

        return resultado