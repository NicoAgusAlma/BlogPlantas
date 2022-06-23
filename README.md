<h1 align="center">
    MVT Final!
</h1>

<h4 align="center">
    Aqui todos los archivos con la entrega del proyecto final del curso de Python.
</h4>

## 📺 Video!
Aqui el [link](https://www.youtube.com/watch?v=02GNPHcmvF0) del video con la explicacion (resumida) de la pagina.

## 👥 Participantes en el proyecto:
El proyecto se llevo a cabo de la mano de 2 participantes: Nicolas Almazan y Neyen Luna
Las tareas se distribuyeron y ejecutaron de la siguiente manera:

Nicolas Almazan:

- Planeamiento general de la web
- Pagina "about me"
- Creacion de modelos segun requerimientos
- Implementacion de template
- Creacion de seccion blog
- Creacion de buscador integrado en toda la web
- Creacion de modelos y formularios de usuarios: login / register
- Creacion de modelo categorias y columna de filtro en blog
- Integracion de texto enriquecido para posteos en blog
- Creacion de relaciones entre modelos (ManyToMany / ForeignKey)
- Alta en GitHub
- Creacion de Video para YouTube


Neyen Luna:

- Planeamiento general de la web
- Unit Test
- Creacion de formularios e integracion en html
- Integracion de template con formularios y modelos propios+
- Integracion de comentarios en blog
- Creacion de galeria
- Integracion de usuarios y permisos en la web.
- Creacion de columna con posteos recientes en blog
- Mejoras en CSS
- Primera subida de datos a la base
- Creacion de modelo y formulario para imagenes de perfil
- Creacion / modificacion Readme


# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/NicoAgusAlma/BlogPlantas

cd BlogFinal
```
- Verificar cual es la ultima version y cambiar a esa rama
```bash
git checkout 12-6-2022
```

- En caso de desear un entorno virtual en Windows (No es obligatorio):
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- En caso de desear un entorno virtual en Linux (No es obligatorio):
```bash
python3 -m venv venv
source venv/bin/activate
```

- Crear el archivo BlogFinal/.env con el siguiente contenido exacto:
```bash
SECRET_KEY=django-insecure-)rkd(&-)y5v^pw4#_sa33gh%v*(-dr!y7l#mb0s-f)4(6$cee9
DEBUG=True
ALLOWED_HOSTS=*,
```

- Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

- Crear base de datos a partir de las migraciones
```bash
python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Crear estáticos
```bash
python manage.py collectstatic
```

- Ejecutar proyecto
```bash
python manage.py runserver
```