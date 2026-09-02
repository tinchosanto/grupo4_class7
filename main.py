def mostrar_menu():
    print("\n=== Programa de ejemplo ===")
    print("1. Saludar")
    print("2. Calcular promedio")
    print("3. Salir")


def saludar():
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola, {nombre}! Bienvenido(a) al programa.")


def calcular_promedio():
    try:
        cantidad = int(input("¿Cuántas notas deseas ingresar? "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        notas = []
        for i in range(1, cantidad + 1):
            nota = float(input(f"Ingresa la nota {i}: "))
            notas.append(nota)

        promedio = sum(notas) / len(notas)
        print(f"El promedio es: {promedio:.2f}")
    except ValueError:
        print("Debes ingresar números válidos.")


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        saludar()
    elif opcion == "2":
        calcular_promedio()
    elif opcion == "3":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
