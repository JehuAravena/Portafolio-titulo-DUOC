# Sistema de venta en línea de alimentos saludables - Olivias Panadería & Pastelería Saludable

## Contexto

Olivias Panadería & Pastelería Saludable es un negocio familiar que se enfoca en hacer productos de panadería y pastelería saludables, diseñando opciones para diferentes alergias alimentarias, en especial para personas con diabetes y celiaquía. Sin embargo, la pastelería no cuenta con una página web donde pueda comercializar sus productos y posicionar su marca, lo que limita la digitalización de su negocio.

## Problema

La pastelería no tiene una página web donde pueda comercializar sus productos y posicionar su marca, lo que limita la digitalización de su negocio.

## Objetivo

El objetivo de este proyecto es desarrollar un sistema de venta en línea para Olivias Panadería & Pastelería Saludable, que permita a la empresa comercializar sus productos y mejorar su presencia en Internet.

## Instalación

1. Asegúrate de tener instalado Python 3.10.6 en tu equipo.
2. Descarga o clona el repositorio en tu equipo.
3. En la carpeta del proyecto, ejecuta `pip install -r requirements.txt` para instalar todas las dependencias necesarias.
4. Enciende XAMPP Control Panel y asegúrate de que MariaDB esté en ejecución.
5. Crea una base de datos en MariaDB y cambia la configuración de la conexión en el archivo `.env`.
6. Ejecuta `python manage.py makemigrations` y luego `python manage.py migrate` para aplicar las migraciones necesarias a la base de datos.
7. Ejecuta `python manage.py runserver` para iniciar el servidor local.
8. Accede a la aplicación en tu navegador en `http://localhost:8000/`.

## Funciones

Para ver las funciones tanto del usuario administrador como el usuario cliente, sigue este enlace: [Ver funciones](https://drive.google.com/drive/folders/1WVMwt2dZ4GQo4f56mjoYOoD_6j1S2raO?usp=share_link)

## Uso

Una vez instalado el proyecto, puedes acceder a las siguientes vistas:

* Inicio: página de inicio de la tienda en línea.
* Nosotros: información sobre Olivias Panadería & Pastelería Saludable.
* Contacto: formulario para enviar mensajes o preguntas a la empresa.
* Tienda: página con la lista de productos disponibles para la venta en línea. Al hacer clic en un producto, se mostrará una página con más detalles y opciones para agregar al carrito de compras.
* Carrito de compras: resumen de los productos seleccionados para la compra, con opciones para modificar la cantidad o eliminar productos. Al hacer clic en "Realizar pedido", se redirigirá al servicio de pago de PayPal para completar la transacción.

## Créditos

Este proyecto ha sido desarrollado por Jehu Aravena y Renato Saldivia. Queríamos agradecer al profesor Pablo Saldaña por sus recomendaciones y apoyo durante el desarrollo de este proyecto.
