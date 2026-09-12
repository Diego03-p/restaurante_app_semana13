import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, parent, restaurante_servicio, al_cerrar_sesion):
        super().__init__(parent)
        self.servicio = restaurante_servicio
        self.al_cerrar_sesion = al_cerrar_sesion

        self.configure(padx=20, pady=20)
        self._crear_interfaz()

    def _crear_interfaz(self):
        top_frame = tk.Frame(self)
        top_frame.pack(fill="x", pady=5)

        tk.Label(top_frame, text="Panel Principal - Restaurante App", font=("Arial", 14, "bold")).pack(side="left")
        btn_logout = tk.Button(top_frame, text="Cerrar Sesión", bg="#f44336", fg="white", command=self.al_cerrar_sesion)
        btn_logout.pack(side="right")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, pady=10)

        tab_productos = ttk.Frame(notebook)
        notebook.add(tab_productos, text="Productos")
        self._crear_tabla_productos(tab_productos)

        tab_usuarios = ttk.Frame(notebook)
        notebook.add(tab_usuarios, text="Usuarios")
        self._crear_tabla_usuarios(tab_usuarios)

        tab_ventas = ttk.Frame(notebook)
        notebook.add(tab_ventas, text="Ventas")
        tk.Label(tab_ventas, text="Funcionalidad de Ventas (Pendiente de implementación gráfica)", font=("Arial", 11, "italic")).pack(pady=30)

    def _crear_tabla_productos(self, parent):
        columnas = ("codigo", "nombre", "precio", "stock")
        tabla = ttk.Treeview(parent, columns=columnas, show="headings")

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio ($)")
        tabla.heading("stock", text="Stock")

        for prod in self.servicio.obtener_productos():
            tabla.insert("", "end", values=(prod.codigo, prod.nombre, f"{prod.precio:.2f}", prod.stock))

        tabla.pack(fill="both", expand=True, padx=5, pady=5)

    def _crear_tabla_usuarios(self, parent):
        columnas = ("identificacion", "nombre")
        tabla = ttk.Treeview(parent, columns=columnas, show="headings")

        tabla.heading("identificacion", text="Identificación")
        tabla.heading("nombre", text="Nombre")

        for usr in self.servicio.obtener_usuarios():
            tabla.insert("", "end", values=(usr.identificacion, usr.nombre))

        tabla.pack(fill="both", expand=True, padx=5, pady=5)