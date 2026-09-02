# Tarea Clase 7 — Tarea GIT

# Enunciado
1. Crear un repositorio en GitHub
2. Agregar a cada integrante del equipo como colaboador
3. crear un programa en python a eleccion y subir el codigo al repositorio
4. Cada integrante deberia clonarse el repositorio
5. Cada integrante deberia crear un branch y hacer un cambio en el programa(al menos dos archivos)
6. Una vez que tengan los cambios cada integrante debe enviar un pull request para hacer merge a la rama principal(main)
7. Un integrante designado(el creador del repo) Debera aprobar el pull request
8. Enviar la URL del repositorio en Github

# Integrantes - Grupo 4

1. Michel Albert Cárdenas Carrasco
2. Ramiro Sanchez Condori
3. Agustin Acebo Pedraza
4. Rodrigo Ojeda Ajata

## Proyecto

Programa en Python que permite seleccionar desde la consola uno de dos modelos de
machine learning —un modelo lineal o un modelo de árbol— para entrenarlo con un
conjunto de datos de ejemplo y generar predicciones.

El código implementa el patrón de diseño **Factory** (`ModelFactory`) para crear la
instancia del modelo elegido, y una clase base (`BaseModel`) de la que heredan ambos
modelos.

## Estructura del proyecto

```text
grupo4_class7/
├── main.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── linear_model.py
│   ├── tree_model.py
│   └── model_factory.py
└── test/
    └── test.py
```


## Requisitos

- Python 3.13

## Cómo ejecutarlo

Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

Para ejecutar los tests:

```bash
python test/test.py
```
