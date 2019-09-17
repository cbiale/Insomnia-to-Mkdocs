# Insomnia to Mkdocs

Genera un sitio Mkdocs a partir de un archivo JSON generado por Insomnia. Solo toma en cuenta lo especificado en los atributos __name__ y __description__.

Formato de invocación:

```
python genera.py nombre_directorio nombre_sitio nombre_archivo.json
```

Donde

- __nombre_directorio__ : especifica el directorio a generar.

- __nombre_sitio__ : especifica el nombre del sitio (define el valor de __site_name__ en el archivo __mkdocs.yml__).

- __nombre_archivo.json__ : especifica el archivo JSON generado por Insomnia.

El archivo __index.md__ genera con el siguiente formato:
```
# API de nombre_sitio

API definida en Insomnia
```
