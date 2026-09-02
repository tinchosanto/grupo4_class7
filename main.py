from models.model_factory import ModelFactory

def main():

    """
    ejecuta el flujo principal de analisis de datos
    permitiendo seleccionar el modelo desde consola
    """

    print("=== seleccione modelo===")
    print("Opciones:")
    print("1. Modelo Lineal")
    print("2. Modelo de Árbol")

    model_type = input("Ingrese el número del modelo que desea usar: ").strip().lower()

    try:
        #crear el modelo usando factory
        model = ModelFactory.create_model(model_type)
    except ValueError as e:
        print(e)
        return 
    
    data = [10, 20, 30, 40]

    print("\n=== Entrenando el modelo ===")
    model.train(data)

    print("\n=== Generando predicciones ===")
    predictions = model.predict(data)

    print("\nPredicciones:", predictions)

if __name__ == "__main__":
    main()