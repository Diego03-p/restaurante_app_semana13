class Usuario:
    def __init__(self, identificacion, nombre, clave, rol="Cliente"):
        self.identificacion = identificacion
        self.nombre = nombre
        self.clave = clave
        self.rol = rol

    def a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "clave": self.clave,
            "rol": self.rol
        }

    @staticmethod
    def desde_diccionario(datos):
        return Usuario(
            identificacion=datos.get("identificacion", ""),
            nombre=datos.get("nombre", ""),
            clave=datos.get("clave", ""),
            rol=datos.get("rol", "Cliente")
        )