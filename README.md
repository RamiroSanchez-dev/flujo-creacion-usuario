# Registro de usuario con envio de mail

## Introducción

A continuación se realizara una breve descripción del repositorio en cuestion.

El repostirio esta dividido en front y back. Cada uno esta pensado para ser ejecutado desde dichas carpetas.

Para un correcto funcionamiento es importante que el front corra en localhost:3000 y el back en  localhost:8000

## Front

El front esta desarrollado con react, mas especificamente con Next.js

### Instalación

Primero hay que intalar las dependencias
```
npm i 
```
correr en modo dev
```
npm run dev
```
## Back

El back esta desarrollado en python, con FastApi y SQLAlquemist.
Para la base de datos se utilizo SQLite ya que permitia trabajar con un modelo sin tener que instanciar una base perse.

### Instalación
Para instalar las dependecias del back, estando parado dentro del directorio
```
pip install -r requirements.txt
```
luego:
```
uvicorn main:app --reload
```
Esto dejara corriendo la instancia de uvicorn en el puerto 8000

## Sesiones

Para el manejo de sesiones se implemento un sistema de session tokens. Estos son generados uan vez que el usuario es dado de alta desde el backend.

Una vez devuelto, este token es guardado en el front mediante el uso de cookies. Dado que el ambiente de desarrollo fue localhost, la cookie no conto con las todas las opciones de seguridad.

## Mailing

Como se utilizo la API de MAILGUN en su version gratuita, esta no permite mandar mails a cuarquier mail, sino que debe ser colocado en una whitelist. Por dicho motivo, es que el mail se agrego el achivo html en la ruta:
```
back\mails\mail-registro.html
```
Recomiendo utilizar la extención de Live Preview de VSCode para facilitar la visualización.