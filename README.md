# Insomnia to Mkdocs

Genera un sitio Mkdocs a partir de un archivo generado por Insomnia.

Consideraciones:

El archivo JSON debe denominarse __prueba.json__.

Existen las siguientes variables:

__directorio__ : donde se especifica el directorio a generar.

__nombre_sitio__ : donde se especifica el nombre del sitio (define el valor de __site_name__ en el archivo __mkdocs.yml__).

El archivo __index.md__ genera con el siguiente formato:
```
# API de nombre_sitio

API definida en Insomnia
```
