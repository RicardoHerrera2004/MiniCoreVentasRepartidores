# Sistema Logístico Mini Core

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5/CSS3](https://img.shields.io/badge/HTML5_&_CSS3-E34F26?style=for-the-badge&logo=html5&logoColor=white)

## Acerca del Proyecto
Este proyecto es un **"Mini Core" básico** desarrollado como solución de backend para la gestión y cálculo de costos logísticos. El sistema permite filtrar envíos por rangos de fechas y calcula automáticamente el costo total por repartidor, cruzando datos de pesos y tarifas dinámicas por zona geográfica.

## Arquitectura: Patrón MVT (MVC de Django)
El sistema fue construido utilizando el framework de **Django**, aplicando su patrón de diseño nativo **MVT (Model-View-Template)**, el cual es la adaptación del clásico patrón MVC (Model-View-Controller):
* **Model (Modelo):** Base de datos relacional (SQLite) estructurada con modelos conectados por llaves foráneas (`Zona`, `Repartidor`, `Envio`).
* **View (Vista/Controlador):** Lógica de negocio en Python que captura peticiones, valida fechas, y utiliza el ORM de Django para realizar consultas transaccionales cruzadas y agregaciones complejas (Sum, Count, F objects) en memoria.
* **Template (Plantilla/Vista):** Interfaz gráfica limpia y minimalista renderizada con HTML dinámico y CSS puro, separando completamente el diseño de la lógica.

## Cómo correr el proyecto localmente

Sigue estos pasos para levantar el entorno de desarrollo en tu propia máquina:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
cd tu-repositorio
```

### 2. Crear y activar el entorno virtual
Es una buena práctica aislar las dependencias del proyecto.

En Windows:

```Bash
python -m venv venv
venv\Scripts\activate
```

En Mac/Linux:
```Bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```Bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
Genera las tablas a partir de los modelos del proyecto:

```Bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un superusuario (Admin)
Para poder ingresar al panel de administración y cargar datos de prueba:

```Bash
python manage.py createsuperuser
```

### 6. Encender el servidor
```Bash
python manage.py runserver
```

¡Listo! Tu proyecto ahora está corriendo en http://127.0.0.1:8000/. Puedes ingresar al panel de control en http://127.0.0.1:8000/admin/.

## Demostración del Proyecto

Haz clic en el siguiente enlace para ver un video explicativo del sistema en funcionamiento:
Ver Video en YouTube: https://youtu.be/KPj5ZfREl9I?si=PO87QcSHyghHPVtx

Desarrollado por: Ricardo Herrera - Estudiante de Ingeniería de Software 💻
