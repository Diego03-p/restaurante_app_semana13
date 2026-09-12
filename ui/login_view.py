import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, restaurante_servicio, al_ingresar_exitoso):
        super().__init__(parent)
        self.servicio = restaurante_servicio
        self.al_ingresar_exitoso = al_ingresar_exitoso

        self.configure(padx=30, pady=30)
        self._crear_interfaz()

    def _crear_interfaz(self):
        tk.Label(self, text="SISTEMA RESTAURANTE APP", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self, text="Inicio de Sesión", font=("Arial", 11)).pack(pady=5)

        tk.Label(self, text="Usuario:").pack(anchor="w", pady=(10, 0))
        self.ent_usuario = tk.Entry(self, width=30)
        self.ent_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(anchor="w", pady=(5, 0))
        self.ent_clave = tk.Entry(self, width=30, show="*")
        self.ent_clave.pack(pady=5)

        btn_ingresar = tk.Button(self, text="Ingresar", bg="#4CAF50", fg="white", width=15, command=self._validar)
        btn_ingresar.pack(pady=15)

    def _validar(self):
        usuario = self.ent_usuario.get().strip()
        clave = self.ent_clave.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Por favor, ingrese usuario y contraseña.")
            return

        if self.servicio.validar_acceso(usuario, clave):
            self.ent_usuario.delete(0, tk.END)
            self.ent_clave.delete(0, tk.END)
            self.al_ingresar_exitoso()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Intente de nuevo.")