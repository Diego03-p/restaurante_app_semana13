# Aplicación de Gestión de Restaurante - Semana 16

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando **Tkinter / ttk** para la interfaz gráfica y **JSON** para el almacenamiento de datos.

## 🚀 Características y Funcionalidades

- **Inicio de Sesión (Login):**
  - Autenticación mediante credenciales almacenadas en `datos/usuarios.json`.
  - Atajo de teclado: Tecla `Enter` para iniciar sesión rápidamente.

- **Gestión de Usuarios (CRUD):**
  - Consulta de usuarios en tabla dinámica (`ttk.Treeview`).
  - Formulario para **Registrar**, **Actualizar** y **Eliminar** usuarios.
  - Carga automática de datos en el formulario al seleccionar una fila (`<<TreeviewSelect>>`).
  - Atajo de teclado: Tecla `Escape` para limpiar el formulario.

- **Visualización de Productos y Registro de Ventas:**
  - Listado de productos disponibles.
  - Selección de producto y usuario mediante menús desplegables (`ttk.Combobox`).
  - Cálculo automático del total de venta y persistencia en `datos/ventas.json`.

## 🛠️ Requisitos e Instalación

- Python 3.8 o superior.
- Sin dependencias externas adicionales (utiliza la librería estándar `tkinter`).

### Ejecución:
```bash
python main.py