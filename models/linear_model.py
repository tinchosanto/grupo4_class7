from .base_model import BaseModel

class LinearModel(BaseModel):

    def train(self, data):
        print("Entrenando el modelo lineal con los datos:", data)

    def predict(self, data):
        print("Prediciendo con el modelo lineal usando los datos:", data)
        return [x * 0.5 for x in data]