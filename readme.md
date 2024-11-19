# Proyecto: Sistema de Gestión de Arriendos de Inmuebles
## Hito 1 - Conectando Django a una base de datos

Este proyecto tiene como objetivo desarrollar un sitio web para la gestión de inmuebles disponibles para arriendo utilizando Django y PostgreSQL.

## **Instalación del Entorno**

### **1. Requisitos Previos**

- Python 3.8 o superior.
- PostgreSQL instalado y configurado.
- Git (opcional, para gestionar el repositorio).

### **2. Clonar el Proyecto**

Si estás usando Git, clona el proyecto:

```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>

```

### 3. Crear y Activar el Entorno Virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 4. Configurar el Proyecto
En el archivo settings.py, configura la base de datos:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

### 5. Aplicar Migraciones
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

### 6. Ejecutar el Servidor

   ```bash
   python manage.py runserver
````

Observaciones

Asegúrate de que el servidor PostgreSQL esté activo antes de realizar las operaciones.
Utiliza la consola interactiva de Django (python manage.py shell) para probar las operaciones CRUD.

En caso de errores de migración, revisa las configuraciones de settings.py y verifica la instalación de PostgreSQL.


## **Pasos para Probar el Proyecto**

Configura correctamente el entorno virtual y la base de datos como se detalla en los pasos anteriores.
Realiza las migraciones necesarias.
Ejecuta el servidor local:

```bash

python manage.py runserver

```

Accede al sitio web en tu navegador en http://127.0.0.1:8000/.

Utiliza la consola de Django para crear, listar, actualizar y eliminar registros.
