import os
import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class AplicacionRestaurante(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App - Sistema de Gestión")
        self.geometry("750x500")

        # Configurar icono desde la carpeta assets si existe
        ruta_ico = os.path.join("assets", "app.ico")
        if os.path.exists(ruta_ico):
            try:
                self.iconbitmap(ruta_ico)
            except Exception:
                pass

        self.servicio = RestauranteServicio()

        self.login_view = LoginView(self, self.servicio, self.mostrar_main)
        self.main_view = MainView(self, self.servicio, self.mostrar_login)

        self.mostrar_login()

    def mostrar_login(self):
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main(self):
        self.login_view.pack_forget()
        self.main_view.pack(fill="both", expand=True)
        # Refrescar los datos al iniciar sesión
        self.main_view.actualizar_ventas()

if __name__ == "__main__":
    app = AplicacionRestaurante()
    app.mainloop()