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