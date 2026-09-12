from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, ruta_productos="datos/productos.json", ruta_usuarios="datos/usuarios.json"):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self._productos = []
        self._usuarios = []
        self._cargar_datos()

    def _cargar_datos(self):
        datos_prod = ArchivoServicio.cargar_json(self.ruta_productos)
        self._productos = [Producto.desde_diccionario(p) for p in datos_prod]

        datos_usr = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self._usuarios = [Usuario.desde_diccionario(u) for u in datos_usr]

    def validar_acceso(self, usuario_id: str, clave: str) -> bool:
        for usr in self._usuarios:
            if usr.identificacion == usuario_id and usr.clave == clave:
                return True
        return False

    def obtener_productos(self) -> list:
        return self._productos

    def obtener_usuarios(self) -> list:
        return self._usuarios