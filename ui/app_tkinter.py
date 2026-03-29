# ui/app_tkinter.py

import tkinter as tk
from tkinter import messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Lista de Tareas")

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento teclado ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.completar_tarea).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        # Evento doble clic
        self.listbox.bind("<Double-1>", self.completar_tarea_evento)

    # ---------------- FUNCIONES ----------------

    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.completar_tarea(tarea.id)
            self.actualizar_lista()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.eliminar_tarea(tarea.id)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completado:
                texto = "[✔] " + texto
            self.listbox.insert(tk.END, texto)
