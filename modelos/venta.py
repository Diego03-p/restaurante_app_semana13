class Venta:
    def __init__(self, id_venta: str, usuario_nombre: str, producto_nombre: str, precio: float, fecha: str):
        self.id_venta = id_venta
        self.usuario_nombre = usuario_nombre
        self.producto_nombre = producto_nombre
        self.precio = precio
        self.fecha = fecha

    def a_diccionario(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "usuario_nombre": self.usuario_nombre,
            "producto_nombre": self.producto_nombre,
            "precio": self.precio,
            "fecha": self.fecha
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Venta':
        return Venta(
            id_venta=datos.get("id_venta", ""),
            usuario_nombre=datos.get("usuario_nombre", ""),
            producto_nombre=datos.get("producto_nombre", ""),
            precio=float(datos.get("precio", 0.0)),
            fecha=datos.get("fecha", "")
        )