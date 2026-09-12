class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Producto':
        return Producto(
            codigo=datos.get("codigo", ""),
            nombre=datos.get("nombre", ""),
            precio=float(datos.get("precio", 0.0)),
            stock=int(datos.get("stock", 0))
        )