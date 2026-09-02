class BaseModel:
    """
    clase base para agrupar modelos
    """

    # entrenar
    def train(self, data):
        raise NotImplementedError("El método 'train' debe ser implementado por la subclase")
    
    #predecir
    def predict(self, data):
        raise NotImplementedError("El método 'predict' debe ser implementado por la subclase")
