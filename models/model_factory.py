from .linear_model import LinearModel
from .tree_model import TreeModel
from .average_model import AverageModel


class ModelFactory:

    """
    Fábrica de modelos para crear instancias de diferentes tipos de modelos.
    """

    @staticmethod
    def create_model(model_type):
        if model_type == "1":
            return LinearModel()
        elif model_type == "2":
            return TreeModel()
        elif model_type == "3":
            return AverageModel()
        else:
            raise ValueError(f"Tipo de modelo desconocido: {model_type}")