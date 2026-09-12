# Restaurante App - Semana 13 (Interfaz Gráfica de Usuario - Tkinter)

**Estudiante:** Diego Venancio Pluas Arriaga  
**Asignatura:** Programación Orientada a Objetos  

## Propósito
Esta versión representa la transición de la aplicación de consola hacia una Interfaz Gráfica de Usuario (GUI) utilizando **Tkinter**. Se establece una estructura modular limpia donde la interfaz no lee los datos directamente de archivos locales, sino que delega el acceso a la capa de servicios.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md