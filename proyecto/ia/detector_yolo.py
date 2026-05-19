import cv2
from ultralytics import YOLO


class DetectorYOLO:

    def __init__(self, model_path="data/weights/yolo26n.pt"):

        self.model = YOLO(model_path)

        self.clases = {
            0: 'person',
            1: 'bicycle',
            2: 'car',
            3: 'motorbike',
            5: 'bus',
            7: 'truck'
        }

    def detectar(self, frame):

        results = self.model.predict(
            frame,
            conf=0.5,
            verbose=False
        )[0]

        imagen_anotada = results.plot()

        conteo = {
            clase: 0
            for clase in self.clases.values()
        }

        detecciones = []

        for box in results.boxes:

            cls_id = int(box.cls[0])

            nombre = self.clases.get(cls_id)

            if nombre:

                conteo[nombre] += 1

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                conf = float(box.conf[0])

                detecciones.append({
                    "clase": nombre,
                    "confianza": conf,
                    "bbox": (x1, y1, x2, y2)
                })

        return imagen_anotada, conteo, detecciones