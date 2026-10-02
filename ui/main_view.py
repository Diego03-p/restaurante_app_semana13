import tkinter as tk
from tkinter import ttk, messagebox
from modelos.venta import Venta
from modelos.usuario import Usuario

class MainView(ttk.Frame):
    def __init__(self, parent, servicio, al_cerrar_sesion):
        super().__init__(parent)
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion
        
        self.pack(fill="both", expand=True)
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cabecera
        frame_top = ttk.Frame(self)
        frame_top.pack(fill="x", padx=10, pady=10)
        
        lbl_titulo = ttk.Label(frame_top, text="Sistema de Gestión del Restaurante", font=("Arial", 14, "bold"))
        lbl_titulo.pack(side="left")
        
        btn_logout = ttk.Button(frame_top, text="Cerrar Sesión", command=self.al_cerrar_sesion)
        btn_logout.pack(side="right")

        # Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Tab Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Productos")
        self.crear_tab_productos()

        # Tab Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self.crear_tab_usuarios()

        # Tab Ventas
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas")
        self.crear_tab_ventas()

    # --- PESTAÑA PRODUCTOS ---
    def crear_tab_productos(self):
        tree = ttk.Treeview(self.tab_productos, columns=("ID", "Nombre", "Precio"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre del Producto")
        tree.heading("Precio", text="Precio ($)")
        
        tree.column("ID", width=50, anchor="center")
        tree.column("Nombre", width=200, anchor="w")
        tree.column("Precio", width=100, anchor="e")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for p in self.servicio.obtener_productos():
            p_id = getattr(p, 'id', getattr(p, 'id_producto', getattr(p, 'identificacion', '')))
            tree.insert("", "end", values=(p_id, p.nombre, f"{p.precio:.2f}"))

    # --- PESTAÑA USUARIOS ---
    def crear_tab_usuarios(self):
        # Formulario
        frame_form = ttk.LabelFrame(self.tab_usuarios, text=" Formulario de Usuario ")
        frame_form.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_form, text="Identificación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ent_user_id = ttk.Entry(frame_form)
        self.ent_user_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.ent_user_nombre = ttk.Entry(frame_form)
        self.ent_user_nombre.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Clave:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ent_user_clave = ttk.Entry(frame_form, show="*")
        self.ent_user_clave.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Rol:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.combo_user_rol = ttk.Combobox(frame_form, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.combo_user_rol.set("Cliente")
        self.combo_user_rol.grid(row=1, column=3, padx=5, pady=5)

        # Botones (usando command=)
        frame_btn = ttk.Frame(frame_form)
        frame_btn.grid(row=2, column=0, columnspan=4, pady=10)

        ttk.Button(frame_btn, text="Registrar", command=self.registrar_usuario).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Actualizar", command=self.actualizar_usuario).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=5)
        ttk.Button(frame_btn, text="Limpiar", command=self.limpiar_form_usuario).pack(side="left", padx=5)

        # Tabla de usuarios
        self.tree_usuarios = ttk.Treeview(self.tab_usuarios, columns=("ID", "Nombre", "Rol"), show="headings")
        self.tree_usuarios.heading("ID", text="Identificación")
        self.tree_usuarios.heading("Nombre", text="Nombre")
        self.tree_usuarios.heading("Rol", text="Rol")
        
        self.tree_usuarios.column("ID", width=100, anchor="center")
        self.tree_usuarios.column("Nombre", width=200, anchor="w")
        self.tree_usuarios.column("Rol", width=120, anchor="center")
        self.tree_usuarios.pack(fill="both", expand=True, padx=10, pady=5)

        # Eventos (bind)
        self.tree_usuarios.bind("<<TreeviewSelect>>", self.al_seleccionar_usuario)
        self.combo_user_rol.bind("<<ComboboxSelected>>", self.al_cambiar_rol)
        
        # Atajos de teclado
        self.ent_user_id.bind("<Return>", lambda e: self.registrar_usuario())
        self.ent_user_nombre.bind("<Return>", lambda e: self.registrar_usuario())
        self.ent_user_clave.bind("<Return>", lambda e: self.registrar_usuario())
        self.tab_usuarios.bind_all("<Escape>", lambda e: self.limpiar_form_usuario())

        self.cargar_usuarios()

    def cargar_usuarios(self):
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)
        for u in self.servicio.obtener_usuarios():
            self.tree_usuarios.insert("", "end", values=(u.identificacion, u.nombre, u.rol))

    def al_seleccionar_usuario(self, event):
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            return
        item = self.tree_usuarios.item(seleccion[0])
        identificacion = item["values"][0]
        
        usuario = self.servicio.obtener_usuario_por_id(identificacion)
        if usuario:
            self.ent_user_id.delete(0, tk.END)
            self.ent_user_id.insert(0, usuario.identificacion)
            self.ent_user_nombre.delete(0, tk.END)
            self.ent_user_nombre.insert(0, usuario.nombre)
            self.ent_user_clave.delete(0, tk.END)
            self.ent_user_clave.insert(0, usuario.clave)
            self.combo_user_rol.set(usuario.rol)

    def al_cambiar_rol(self, event):
        pass

    def registrar_usuario(self):
        identificacion = self.ent_user_id.get().strip()
        nombre = self.ent_user_nombre.get().strip()
        clave = self.ent_user_clave.get().strip()
        rol = self.combo_user_rol.get()

        if not identificacion or not nombre or not clave:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        nuevo_u = Usuario(identificacion, nombre, clave, rol)
        exito, msg = self.servicio.registrar_usuario(nuevo_u)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self.cargar_usuarios()
            self.limpiar_form_usuario()
        else:
            messagebox.showerror("Error", msg)

    def actualizar_usuario(self):
        identificacion = self.ent_user_id.get().strip()
        nombre = self.ent_user_nombre.get().strip()
        clave = self.ent_user_clave.get().strip()
        rol = self.combo_user_rol.get()

        if not identificacion:
            messagebox.showwarning("Atención", "Seleccione un usuario de la lista.")
            return

        u_actualizado = Usuario(identificacion, nombre, clave, rol)
        exito, msg = self.servicio.actualizar_usuario(u_actualizado)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self.cargar_usuarios()
            self.limpiar_form_usuario()
        else:
            messagebox.showerror("Error", msg)

    def eliminar_usuario(self):
        identificacion = self.ent_user_id.get().strip()
        if not identificacion:
            messagebox.showwarning("Atención", "Seleccione un usuario para eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el usuario {identificacion}?"):
            exito, msg = self.servicio.eliminar_usuario(identificacion)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self.cargar_usuarios()
                self.limpiar_form_usuario()
            else:
                messagebox.showerror("Error", msg)

    def limpiar_form_usuario(self):
        self.ent_user_id.delete(0, tk.END)
        self.ent_user_nombre.delete(0, tk.END)
        self.ent_user_clave.delete(0, tk.END)
        self.combo_user_rol.set("Cliente")
        if self.tree_usuarios.selection():
            self.tree_usuarios.selection_remove(self.tree_usuarios.selection())

    # --- PESTAÑA VENTAS ---
    def crear_tab_ventas(self):
        frame_form = ttk.LabelFrame(self.tab_ventas, text=" Registrar Venta ")
        frame_form.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_form, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_productos = ttk.Combobox(frame_form, state="readonly", width=30)
        self.combo_productos.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Cliente/Usuario:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.combo_usuarios = ttk.Combobox(frame_form, state="readonly", width=30)
        self.combo_usuarios.grid(row=0, column=3, padx=5, pady=5)

        self.cargar_combos_ventas()

        ttk.Label(frame_form, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ent_cantidad = ttk.Entry(frame_form, width=10)
        self.ent_cantidad.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.ent_cantidad.insert(0, "1")

        btn_registrar = ttk.Button(frame_form, text="Registrar Venta", command=self.registrar_venta)
        btn_registrar.grid(row=1, column=2, columnspan=2, padx=5, pady=10)

        self.tree_ventas = ttk.Treeview(self.tab_ventas, columns=("ID", "Producto", "Cliente", "Cantidad", "Total"), show="headings")
        self.tree_ventas.heading("ID", text="ID Venta")
        self.tree_ventas.heading("Producto", text="Producto")
        self.tree_ventas.heading("Cliente", text="Cliente")
        self.tree_ventas.heading("Cantidad", text="Cant.")
        self.tree_ventas.heading("Total", text="Total ($)")

        self.tree_ventas.column("ID", width=60, anchor="center")
        self.tree_ventas.column("Producto", width=150, anchor="w")
        self.tree_ventas.column("Cliente", width=150, anchor="w")
        self.tree_ventas.column("Cantidad", width=60, anchor="center")
        self.tree_ventas.column("Total", width=80, anchor="e")
        self.tree_ventas.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_ventas()

    def cargar_combos_ventas(self):
        prods = []
        for p in self.servicio.obtener_productos():
            p_id = getattr(p, 'id', getattr(p, 'id_producto', getattr(p, 'identificacion', '')))
            prods.append(f"{p_id} - {p.nombre}")
        self.combo_productos['values'] = prods
        if prods:
            self.combo_productos.current(0)

        users = [f"{u.identificacion} - {u.nombre}" for u in self.servicio.obtener_usuarios()]
        self.combo_usuarios['values'] = users
        if users:
            self.combo_usuarios.current(0)

    def cargar_ventas(self):
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)
        for v in self.servicio.obtener_ventas():
            prod = self.servicio.obtener_producto_por_id(v.id_producto)
            nombre_prod = prod.nombre if prod else "Desconocido"
            
            user = self.servicio.obtener_usuario_por_id(v.id_usuario)
            nombre_user = user.nombre if user else "Desconocido"

            self.tree_ventas.insert("", "end", values=(v.id_venta, nombre_prod, nombre_user, v.cantidad, f"{v.total:.2f}"))

    def registrar_venta(self):
        prod_sel = self.combo_productos.get()
        user_sel = self.combo_usuarios.get()
        cant_str = self.ent_cantidad.get().strip()

        if not prod_sel or not user_sel or not cant_str:
            messagebox.showwarning("Campos Incompletos", "Complete todos los campos.")
            return

        try:
            cantidad = int(cant_str)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un entero positivo.")
            return

        id_prod = prod_sel.split(" - ")[0]
        id_user = user_sel.split(" - ")[0]

        prod = self.servicio.obtener_producto_por_id(id_prod)
        if not prod:
            messagebox.showerror("Error", "Producto no encontrado.")
            return

        total = prod.precio * cantidad
        ventas_existentes = self.servicio.obtener_ventas()
        nuevo_id = len(ventas_existentes) + 1

        nueva_venta = Venta(id_venta=nuevo_id, id_producto=id_prod, id_usuario=id_user, cantidad=cantidad, total=total)
        exito, msg = self.servicio.registrar_venta(nueva_venta)

        if exito:
            messagebox.showinfo("Éxito", msg)
            self.cargar_ventas()
        else:
            messagebox.showerror("Error", msg)