from .base_model import BaseModel

class TreeModel(BaseModel):

    def train(self, data):
        print("Entrenando el modelo de árbol con los datos:", data)

    def predict(self, data):
        print("Prediciendo con el modelo de árbol usando los datos:", data)
        return [x * 0.8 for x in data]