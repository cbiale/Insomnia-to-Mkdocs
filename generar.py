import json
import shutil
import os
import sys

titulos = []
descripciones = []


nombre_directorio = ""
nombre_sitio = ""
nombre_archivo = ""

if len(sys.argv) == 4:
        nombre_directorio = sys.argv[1]
        nombre_sitio = sys.argv[2]
        nombre_archivo = sys.argv[3]
else:
        print("Error en argumentos, formato: python genera.py nombre_directorio nombre_sitio nombre_archivo.json")
        exit(1)

# abro archivo json
archivo = open(nombre_archivo)

# elimino directorio
try:
	shutil.rmtree(nombre_directorio, ignore_errors = True)
except:
	print("error al manejar directorios")
	exit(1)

# creo directorio
os.mkdir(nombre_directorio)

# cambio de directorio
os.chdir(nombre_directorio)

# creo archivo yml
f = open("mkdocs.yml","w+")
f.write("site_name: " + nombre_sitio)


# recorro archivo json de insomnia
valores_json = json.load(archivo)
for item in valores_json:
	if item == 'resources':	
		for recurso in valores_json[item]:
			for v in recurso:
				if v == "name":
					titulos.append(recurso[v])
				if v == "description":
					descripciones.append(recurso[v])


# creo directorio docs
os.mkdir("docs")

# cambio a directorio docs
os.chdir("docs")

# agrego archivo index.md
f = open("index.md","w+")
f.write("# API de " + nombre_sitio)
f.write("\n")
f.write("API definida en Insomnia")


# creo directorio api
os.mkdir("api")

# cambio de directorio
os.chdir("api")


# genero archivos de documentos en directorio /api
i = 1
for titulo, descripcion in zip(titulos, descripciones):
	if descripcion != "":
		f = open(str(i) + ".md","w+")
		f.write("# " + titulo)
		f.write("\n")
		f.write(descripcion)
		f.close()
		i = i + 1
