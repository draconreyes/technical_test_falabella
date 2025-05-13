# Technical Test Falabella - Customers Project

Este proyecto es una aplicación Django para la gestión de clientes, productos y compras, con funcionalidades de consulta y reporte.

## Requisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clona el repositorio o descarga el código fuente.**

2. **Crea un entorno virtual en windows:**

   ```powershell
   python -m venv venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   venv\Scripts\activate
   ```

3. **Instala los paquetes requeridos:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **No es necesario realizar migraciones** ya que la base de datos SQLite ya está incluida y migrada.

5. **Inicia el servidor de desarrollo de Django:**

   ```powershell
   python manage.py runserver
   ```

6. **Accede a la aplicación web:**

   Abre tu navegador y visita:
   
   [http://localhost:8000/customer_lookup/](http://localhost:8000/customer_lookup/)

   Allí podrás consultar clientes, ver sus compras y exportar información.

## Usuarios de ejemplo
- Usuario 1: tipo de documento **C.C** y número de documento **12345678**
- Usuario 1: tipo de documento **C.C** y número de documento **11223344**

## Notas
- Todos los endpoints de la API están disponibles bajo `/api/`.
- Puedes ver la API de los modelos en: [http://localhost:8000](http://localhost:8000)
- El archivo `requirements.txt` contiene todos los paquetes necesarios para el backend.
