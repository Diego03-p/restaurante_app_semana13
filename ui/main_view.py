import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, servicio, al_cerrar_sesion):
        super().__init__(parent)
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Header superior
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=10, pady=10)

        lbl_titulo = ttk.Label(header_frame, text="Sistema de Gestión del Restaurante", font=("Arial", 14, "bold"))
        lbl_titulo.pack(side="left")

        btn_logout = ttk.Button(header_frame, text="Cerrar Sesión", command=self.al_cerrar_sesion)
        btn_logout.pack(side="right")

        # Contenedor de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        # 1. Pestaña Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Productos")
        self._crear_tab_productos()

        # 2. Pestaña Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self._crear_tab_usuarios()

        # 3. Pestaña Ventas (Semana 15)
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas")
        self._crear_tab_ventas()

    def _crear_tab_productos(self):
        columnas = ("id", "nombre", "precio")
        self.tree_productos = ttk.Treeview(self.tab_productos, columns=columnas, show="headings")
        self.tree_productos.heading("id", text="ID")
        self.tree_productos.heading("nombre", text="Nombre del Producto")
        self.tree_productos.heading("precio", text="Precio ($)")

        self.tree_productos.column("id", width=100, anchor="center")
        self.tree_productos.column("nombre", width=250)
        self.tree_productos.column("precio", width=120, anchor="e")

        self.tree_productos.pack(fill="both", expand=True, padx=10, pady=10)
        self.actualizar_productos()

    def _crear_tab_usuarios(self):
        columnas = ("id", "nombre", "rol")
        self.tree_usuarios = ttk.Treeview(self.tab_usuarios, columns=columnas, show="headings")
        self.tree_usuarios.heading("id", text="Cédula/ID")
        self.tree_usuarios.heading("nombre", text="Nombre Completo")
        self.tree_usuarios.heading("rol", text="Rol")

        self.tree_usuarios.column("id", width=100, anchor="center")
        self.tree_usuarios.column("nombre", width=220)
        self.tree_usuarios.column("rol", width=120)

        self.tree_usuarios.pack(fill="both", expand=True, padx=10, pady=10)
        self.actualizar_usuarios()

    def _crear_tab_ventas(self):
        # Formulario para registrar venta
        frame_form = ttk.LabelFrame(self.tab_ventas, text="Registrar Nueva Venta")
        frame_form.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_form, text="Cliente/Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.cbo_usuarios = ttk.Combobox(frame_form, state="readonly", width=25)
        self.cbo_usuarios.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Producto:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.cbo_productos = ttk.Combobox(frame_form, state="readonly", width=25)
        self.cbo_productos.grid(row=0, column=3, padx=5, pady=5)

        # Botón con evento command (Requisito Semana 15)
        btn_registrar = ttk.Button(frame_form, text="Registrar Venta", command=self._on_registrar_venta_click)
        btn_registrar.grid(row=0, column=4, padx=10, pady=5)

        # Tabla de Ventas
        columnas = ("id", "usuario", "producto", "precio", "fecha")
        self.tree_ventas = ttk.Treeview(self.tab_ventas, columns=columnas, show="headings")
        self.tree_ventas.heading("id", text="ID Venta")
        self.tree_ventas.heading("usuario", text="Cliente")
        self.tree_ventas.heading("producto", text="Producto")
        self.tree_ventas.heading("precio", text="Precio ($)")
        self.tree_ventas.heading("fecha", text="Fecha")

        self.tree_ventas.column("id", width=80, anchor="center")
        self.tree_ventas.column("usuario", width=150)
        self.tree_ventas.column("producto", width=150)
        self.tree_ventas.column("precio", width=90, anchor="e")
        self.tree_ventas.column("fecha", width=150, anchor="center")

        self.tree_ventas.pack(fill="both", expand=True, padx=10, pady=10)
        self.actualizar_ventas()

    def actualizar_productos(self):
        for row in self.tree_productos.get_children():
            self.tree_productos.delete(row)
        for p in self.servicio.obtener_productos():
            id_prod = getattr(p, "id", getattr(p, "id_producto", getattr(p, "identificacion", "")))
            precio_val = getattr(p, "precio", 0.0)
            self.tree_productos.insert("", "end", values=(id_prod, p.nombre, f"{float(precio_val):.2f}"))

    def actualizar_usuarios(self):
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)
        for u in self.servicio.obtener_usuarios():
            id_usr = getattr(u, "identificacion", getattr(u, "id", ""))
            rol_usr = getattr(u, "rol", getattr(u, "tipo", "Usuario"))
            self.tree_usuarios.insert("", "end", values=(id_usr, u.nombre, rol_usr))

    def actualizar_ventas(self):
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)
        for v in self.servicio.obtener_ventas():
            self.tree_ventas.insert("", "end", values=(v.id_venta, v.usuario_nombre, v.producto_nombre, f"{v.precio:.2f}", v.fecha))

        usuarios_nombres = [u.nombre for u in self.servicio.obtener_usuarios()]
        productos_nombres = [p.nombre for p in self.servicio.obtener_productos()]
        self.cbo_usuarios["values"] = usuarios_nombres
        self.cbo_productos["values"] = productos_nombres

    def _on_registrar_venta_click(self):
        usr_sel = self.cbo_usuarios.get()
        prod_sel = self.cbo_productos.get()

        exito, msj = self.servicio.registrar_venta(usr_sel, prod_sel)
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.actualizar_ventas()
        else:
            messagebox.showwarning("Atención", msj)