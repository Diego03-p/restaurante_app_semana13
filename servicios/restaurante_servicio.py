from datetime import datetime
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, ruta_productos="datos/productos.json", ruta_usuarios="datos/usuarios.json", ruta_ventas="datos/ventas.json"):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas
        self._productos = []
        self._usuarios = []
        self._ventas = []
        self._cargar_datos()

    def _cargar_datos(self):
        datos_prod = ArchivoServicio.cargar_json(self.ruta_productos)
        self._productos = [Producto.desde_diccionario(p) for p in datos_prod]

        datos_usr = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self._usuarios = [Usuario.desde_diccionario(u) for u in datos_usr]

        datos_ventas = ArchivoServicio.cargar_json(self.ruta_ventas)
        self._ventas = [Venta.desde_diccionario(v) for v in datos_ventas]

    def validar_acceso(self, usuario_id: str, clave: str) -> bool:
        for usr in self._usuarios:
            if usr.identificacion == usuario_id and usr.clave == clave:
                return True
        return False

    def obtener_productos(self) -> list:
        return self._productos

    def obtener_usuarios(self) -> list:
        return self._usuarios

    def obtener_ventas(self) -> list:
        return self._ventas

    def registrar_venta(self, usuario_nombre: str, producto_nombre: str) -> tuple[bool, str]:
        if not usuario_nombre or not producto_nombre:
            return False, "Debe seleccionar un usuario y un producto válidos."

        prod_encontrado = None
        for p in self._productos:
            if p.nombre == producto_nombre:
                prod_encontrado = p
                break

        if not prod_encontrado:
            return False, "El producto seleccionado no existe."

        id_venta = f"V{len(self._ventas) + 1:03d}"
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        nueva_venta = Venta(
            id_venta=id_venta,
            usuario_nombre=usuario_nombre,
            producto_nombre=prod_encontrado.nombre,
            precio=prod_encontrado.precio,
            fecha=fecha_actual
        )

        self._ventas.append(nueva_venta)
        
        datos_guardar = [v.a_diccionario() for v in self._ventas]
        exito = ArchivoServicio.guardar_json(self.ruta_ventas, datos_guardar)

        if exito:
            return True, f"Venta {id_venta} registrada exitosamente."
        else:
            return False, "Error al guardar la venta en el archivo."