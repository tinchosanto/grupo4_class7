import os
import sys
import unittest

# Agrega la raíz del proyecto al path para poder importar el paquete `models`
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base_model import BaseModel
from models.linear_model import LinearModel
from models.tree_model import TreeModel
from models.model_factory import ModelFactory


class TestBaseModel(unittest.TestCase):
    def test_train_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            BaseModel().train([1, 2, 3])

    def test_predict_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            BaseModel().predict([1, 2, 3])


class TestLinearModel(unittest.TestCase):
    def setUp(self):
        self.model = LinearModel()
        self.data = [10, 20, 30, 40]

    def test_predict_returns_half_of_each_value(self):
        self.assertEqual(self.model.predict(self.data), [5.0, 10.0, 15.0, 20.0])

    def test_train_does_not_fail(self):
        # El método solo imprime; no debe lanzar excepciones.
        self.model.train(self.data)


class TestTreeModel(unittest.TestCase):
    def setUp(self):
        self.model = TreeModel()
        self.data = [10, 20, 30, 40]

    def test_predict_returns_80_percent_of_each_value(self):
        self.assertEqual(self.model.predict(self.data), [8.0, 16.0, 24.0, 32.0])

    def test_train_does_not_fail(self):
        self.model.train(self.data)


class TestModelFactory(unittest.TestCase):
    def test_create_linear_model(self):
        self.assertIsInstance(ModelFactory.create_model("1"), LinearModel)

    def test_create_tree_model(self):
        self.assertIsInstance(ModelFactory.create_model("2"), TreeModel)

    def test_create_model_with_unknown_type(self):
        with self.assertRaises(ValueError):
            ModelFactory.create_model("3")


if __name__ == "__main__":
    unittest.main()
