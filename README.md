# Página Retail
El proyecto consta de una página web responsiva creada utilizando el framework Django y la base de datos MySQL. Esta página sería de una tienda retail en la cual se encuentran diversos productos, así como también existen distintos usuarios con permisos específicos, esto gracias a las funciones que trae por defecto django.

## Funciones
- Crear usuarios
- Iniciar sesión
- Añadir productos
- Buscar productos
- Añadir productos al carro de compra
- Eliminar productos del carro de compra
- Etc.

## Vista previa de la página

### Vista página principal:
![](https://i.ibb.co/Cv5B85B/inicio.jpg)

### Vista Añadir producto:
![](https://i.ibb.co/3rXSZXJ/agregar-Producto.jpg)

### Vista producto:
![](https://i.ibb.co/bBpgJ4T/Vista-Producto.jpg)

### Vista crear usuario:
![](https://i.ibb.co/7GGNbPy/Registro.jpg)

### Vista iniciar sesión:
![](https://i.ibb.co/tXcQL93/inicio-Sesion.jpg)

### Vista carrito de compras:
![](https://i.ibb.co/MnHD0cc/Carrito.jpg)


## Setup
### Requisitos Previos
- Sistema operativo Windows
- Tener instalado MySQL
- Tener instalado Python versión 3.7.7
- Tener instalado pip versión 19.2.3

### Preparar el sistema
- Instalar Django
``` cmd
pip install Django==3.1.2
```
- Instalar mysqlclient
``` cmd
pip install mysqlclient
```
- Copiar el repositorio
``` cmd
git clone https://github.com/crhyss/paginaWed/
cd paginaWeb
```
- Prear base de datos en MySQL command line client
```MySQL command line client
CREATE DATABASE inventario;
```

- Cambiar configuración
Para que el programa se enlace con nuestro computador se deben cambiar la configuración dentro de paginaWed\paginaWed\settings.py

- Migrar las tablas al servidor
``` cmd
python manage.py migrate
```

### Iniciar el servidor de la página web
``` cmd
python manage.py runserver
```
### Crear Super usuario
``` cmd
python manage.py createsuperuser
```
