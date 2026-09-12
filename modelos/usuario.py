class Usuario:
    def __init__(self, identificacion: str, nombre: str, clave: str = "1234"):
        self.identificacion = identificacion
        self.nombre = nombre
        self.clave = clave

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "clave": self.clave
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Usuario':
        return Usuario(
            identificacion=datos.get("identificacion", ""),
            nombre=datos.get("nombre", ""),
            clave=datos.get("clave", "1234")
        )