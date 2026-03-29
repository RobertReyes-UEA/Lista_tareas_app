# Lista de Tareas - Aplicación GUI con Tkinter

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación de escritorio tipo **To-Do List (Lista de Tareas)** utilizando Python y la librería Tkinter.

La aplicación permite gestionar tareas diarias de forma interactiva, aplicando una **arquitectura modular por capas** que separa la lógica de negocio, los modelos y la interfaz gráfica.

## Objetivo

Desarrollar una aplicación GUI que responda a eventos de usuario (teclado y ratón), permitiendo agregar, completar y eliminar tareas, además de generar un archivo ejecutable utilizando PyInstaller.


## Arquitectura del Proyecto

El proyecto está estructurado de la siguiente manera:

```
lista_tareas_app/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
└── ui/
    └── app_tkinter.py
```

###  Descripción de Capas

* **Modelos:** Representan la estructura de los datos (Tarea).
* **Servicios:** Contienen la lógica del negocio (gestión de tareas).
* **UI:** Maneja la interfaz gráfica y los eventos del usuario.
* **Main:** Punto de entrada de la aplicación.

##  Funcionalidades

Agregar tareas
Marcar tareas como completadas
Eliminar tareas
Visualización dinámica de tareas
Eventos de teclado (Enter para añadir tarea)
Eventos de ratón (doble clic para completar tarea)
Cambio visual de tareas completadas (✔)


## Tecnologías Utilizadas

* Python 3
* Tkinter
* PyInstaller


## Uso de la Aplicación

1. Escribir una tarea en el campo de texto.
2. Presionar el botón **"Añadir Tarea"** o la tecla **Enter**.
3. Seleccionar una tarea y:

   * Marcar como completada
   * Eliminarla

## Autor

**Robert Reyes**
