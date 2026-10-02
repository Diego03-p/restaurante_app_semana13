import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self.ruta_productos = os.path.join("datos", "productos.json")
        self.ruta_usuarios = os.path.join("datos", "usuarios.json")
        self.ruta_ventas = os.path.join("datos", "ventas.json")

    # --- METODOS AUXILIARES DE LECTURA/ESCRITURA ---
    def _leer_json(self, ruta):
        if hasattr(self.archivo_servicio, 'leer_json'):
            return self.archivo_servicio.leer_json(ruta)
        elif hasattr(self.archivo_servicio, 'cargar_json'):
            return self.archivo_servicio.cargar_json(ruta)
        elif hasattr(self.archivo_servicio, 'obtener_json'):
            return self.archivo_servicio.obtener_json(ruta)
        return []

    def _guardar_json(self, ruta, datos):
        if hasattr(self.archivo_servicio, 'guardar_json'):
            self.archivo_servicio.guardar_json(ruta, datos)
        elif hasattr(self.archivo_servicio, 'escribir_json'):
            self.archivo_servicio.escribir_json(ruta, datos)

    # --- PRODUCTOS ---
    def obtener_productos(self):
        datos = self._leer_json(self.ruta_productos)
        return [Producto.desde_diccionario(p) for p in datos]

    def obtener_producto_por_id(self, id_producto):
        productos = self.obtener_productos()
        for p in productos:
            if str(p.id) == str(id_producto):
                return p
        return None

    # --- USUARIOS ---
    def obtener_usuarios(self):
        datos = self._leer_json(self.ruta_usuarios)
        return [Usuario.desde_diccionario(u) for u in datos]

    def obtener_usuario_por_id(self, identificacion):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if str(u.identificacion) == str(identificacion):
                return u
        return None

    def validar_credenciales(self, identificacion, clave):
        usuarios = self.obtener_usuarios()
        for usuario in usuarios:
            if usuario.identificacion == identificacion and usuario.clave == clave:
                return usuario
        return None

    def registrar_usuario(self, usuario):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if u.identificacion == usuario.identificacion:
                return False, "El usuario ya existe."
        
        usuarios.append(usuario)
        datos = [u.a_diccionario() for u in usuarios]
        self._guardar_json(self.ruta_usuarios, datos)
        return True, "Usuario registrado exitosamente."

    def actualizar_usuario(self, usuario_actualizado):
        usuarios = self.obtener_usuarios()
        encontrado = False
        for i, u in enumerate(usuarios):
            if u.identificacion == usuario_actualizado.identificacion:
                usuarios[i] = usuario_actualizado
                encontrado = True
                break
        
        if not encontrado:
            return False, "Usuario no encontrado."

        datos = [u.a_diccionario() for u in usuarios]
        self._guardar_json(self.ruta_usuarios, datos)
        return True, "Usuario actualizado exitosamente."

    def eliminar_usuario(self, identificacion):
        usuarios = self.obtener_usuarios()
        usuarios_filtrados = [u for u in usuarios if u.identificacion != identificacion]
        
        if len(usuarios) == len(usuarios_filtrados):
            return False, "No se encontró el usuario a eliminar."

        datos = [u.a_diccionario() for u in usuarios_filtrados]
        self._guardar_json(self.ruta_usuarios, datos)
        return True, "Usuario eliminado exitosamente."

    # --- VENTAS ---
    def obtener_ventas(self):
        datos = self._leer_json(self.ruta_ventas)
        return [Venta.desde_diccionario(v) for v in datos]

    def registrar_venta(self, venta):
        ventas = self.obtener_ventas()
        ventas.append(venta)
        datos = [v.a_diccionario() for v in ventas]
        self._guardar_json(self.ruta_ventas, datos)
        return True, "Venta registrada exitosamente."