from .base_model import BaseModel


class AverageModel(BaseModel):
    """
    Modelo simple que utiliza el promedio de los datos
    para generar predicciones.
    """

    def train(self, data):
        if not data:
            raise ValueError("Los datos no pueden estar vacíos")

        self.average = sum(data) / len(data)
        print("Entrenando el modelo promedio con los datos:", data)
        print("Promedio calculado:", self.average)

    def predict(self, data):
        if not hasattr(self, "average"):
            raise ValueError("El modelo debe ser entrenado antes de predecir")

        print("Prediciendo usando el promedio:", self.average)
        return [self.average for _ in data]