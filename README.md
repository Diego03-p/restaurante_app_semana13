# Restaurante App - Semana 15

Aplicación de gestión de restaurante desarrollada en Python aplicando la arquitectura MVC, persistencia de datos en JSON e interfaz gráfica interactiva con Tkinter.

## Novedades de la Semana 15
- **Módulo de Ventas:** Integración del modelo `Venta` y almacenamiento en `datos/ventas.json`.
- **Interfaz Gráfica (GUI):** Implementación de la pestaña de Ventas utilizando `ttk.Notebook`, `Combobox` y `Treeview`.
- **Eventos y Callbacks:** Uso de la propiedad `command=` para el registro de ventas en tiempo real.
- **Recursos Visuales:** Carpeta `assets/` agregada para la gestión de iconos e imágenes de la aplicación.

## Estructura del Proyecto
- `assets/`: Recursos visuales e iconos.
- `datos/`: Archivos JSON (`productos.json`, `usuarios.json`, `ventas.json`).
- `modelos/`: Clases de dominio (`Producto`, `Usuario`, `Venta`).
- `servicios/`: Lógica de negocio y manejo de archivos.
- `ui/`: Vistas de la interfaz gráfica (`login_view.py`, `main_view.py`).
- `main.py`: Punto de entrada de la aplicación.