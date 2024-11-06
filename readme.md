# Aplicación de Gestión de Notas con Flask

Esta es una aplicación simple de gestión de notas implementada utilizando el framework web Flask en Python. La aplicación permite a los usuarios ver una lista de notas, ver detalles de una nota específica según su código y manejar errores de página no encontrada.

## Funcionalidades

- **Ver Notas**: Los usuarios pueden acceder a una lista de notas disponibles.

- **Ver Detalles de Nota**: Los usuarios pueden ver los detalles de una nota específica proporcionando su código.

- **Manejo de Errores**: La aplicación maneja errores de página no encontrada (404) y proporciona una respuesta amigable al usuario.

## Requisitos Previos

- Python (3.6 o superior)
- Flask (Instalable mediante `pip install flask`)

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:

```shell
git clone https://github.com/luisaap-dev/Flask-RapidNotes
```

2. Accede al directorio del repositorio:

```shell
cd Flask-RapidNotes
```

3. Crear entorno virtual (opcional pero recomendado)
- (windows)
```shell
python -m venv nombre_del_entorno
```
- (linux)
```shell
python3 -m venv nombre_del_entorno
```

4. Activar el entorno virtual (opcional pero recomendado):

- Windows (CMD):
```shell
nombre_del_entorno\Scripts\activate
```
- Windows (PowerShell):
```shell
.\nombre_del_entorno\Scripts\Activate
```
- Linux/Ubuntu:
```shell
source nombre_del_entorno/bin/activate
```

5. Instala las dependencias utilizando `pip`:

```shell
pip install -r requirements.txt
```

6. Ejecuta la aplicación:

```shell
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`. Abre esta URL en tu navegador web para usar la aplicación.

## Uso

1. Accede a la página de inicio en tu navegador para ver la lista de notas.

2. Haz clic en el enlace de una nota para ver sus detalles.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la configuración de la aplicación Flask y las rutas.

- `controllers/controller.py`: Contiene la lógica de controladores para manejar las solicitudes y la gestión de notas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas agregar nuevas características, resolver problemas o mejorar la aplicación, siéntete libre de crear un pull request.

## Autor

Esta aplicación fue desarrollada por [Luis Ares](https://github.com/luisaap-dev).

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE). Puedes obtener más información en el archivo `LICENSE`.



