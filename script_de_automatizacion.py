# Descarga de Archivos

# Importar módulos necesarios
import os
import requests
from urllib.parse import urlparse

# Definir la función descargar_archivo
def descargar_archivo(url, carpeta_descarga):
    # Intentar ejecutar el bloque de código para descargar el archivo
    try:
        respuesta = requests.get(url)  # Enviar una solicitud HTTP GET a la URL

        # Comprobar el estado de la respuesta
        if respuesta.status_code == 200:  # Verifica si el estado de la respuesta es '200', lo que significa que la solicitud fue exitosa.
            # Analizar la URL para obtener el nombre del archivo
            analizar_url = urlparse(url)  # urlparse(url): Analiza la URL y la divide en componentes (esquema, dominio, ruta, etc.)
            nombrearchivo = os.path.basename(analizar_url.path)  # Extrae el nombre del archivo de la ruta URL

            # Construir la ruta completa del archivo
            ruta_archivo = os.path.join(carpeta_descarga, nombrearchivo)  # Une la carpeta de descarga y el nombre del archivo para obtener la ruta completa donde se guardará el archivo.

            # Abrir el archivo en modo escritura binaria y guardar el contenido
            with open(ruta_archivo, 'wb') as archivo:  # Abre el archivo en modo escritura binaria (wb)
                archivo.write(respuesta.content)  # Escribe el contenido de la respuesta HTTP en el archivo
            print(f"Descargado {nombrearchivo} a {carpeta_descarga}")

        # Manejo de errores
        else:
            print(f"Error al descargar {url}: Código de estado {respuesta.status_code}")  # Si la solicitud HTTP no fue exitosa (estado diferente a 200), imprime un mensaje indicando que la descarga falló.
    except Exception as e:
        # Capturar cualquier excepción que ocurra y mostrar un mensaje de error
        print(f"Error al descargar {url}: {e}")

# Organizar Archivos

# Importar el módulo os
import os

# Definir la función organizar_archivos
def organizar_archivos(carpeta_descarga):
    # Listar archivos en la carpeta de descarga
    for nombrearchivo in os.listdir(carpeta_descarga):  # Usa os.listdir(carpeta_descarga) para obtener una lista de todos los archivos y carpetas en la carpeta de descarga.
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_descarga, nombrearchivo)  # os.path.join(carpeta_descarga, nombrearchivo): Une la carpeta de descarga y el nombre del archivo para obtener la ruta completa del archivo.
    
        # Verificar si es un archivo
        if os.path.isfile(ruta_archivo):  # os.path.isfile(ruta_archivo): Verifica si la ruta es un archivo (no una carpeta)

            # Obtener la extensión del archivo
            extension_archivo = os.path.splitext(nombrearchivo)[1].lstrip('.').lower()  # os.path.splitext(nombrearchivo)[1]: Obtiene la extensión del archivo (incluyendo el punto)
                                                                              # .lstrip('.'): Elimina el punto de la extensión
                                                                              # .lower(): Convierte la extensión a minúsculas.
            # Construir la ruta de la carpeta de destino
            carpeta_destino = os.path.join(carpeta_descarga, extension_archivo)  # os.path.join(carpeta_descarga, extension_archivo): Construye la ruta de la carpeta de destino usando la extensión del archivo.

            # Crear la carpeta de destino si no existe
            if not os.path.exists(carpeta_destino):  # Verifica si la carpeta de destino ya existe.
                os.makedirs(carpeta_destino)  # Crea la carpeta de destino si no existe

            # Mover el archivo a la carpeta de destino
            destino_final = os.path.join(carpeta_destino, nombrearchivo)
            try:
                os.rename(ruta_archivo, destino_final)  # Mueve el archivo desde su ubicación actual a la carpeta de destino.
                print(f"Movido {nombrearchivo} a {carpeta_destino}")  # Imprime un mensaje indicando que el archivo fue movido exitosamente
            except FileExistsError:
                os.remove(destino_final)  # Eliminar el archivo existente
                os.rename(ruta_archivo, destino_final)  # Mover el archivo de nuevo
                print(f"Reemplazado {nombrearchivo} en {carpeta_destino}")

# Script Principal

# Lista de URLs
urls = [  # Define una lista de URLs de archivos que se descargarán.
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://www.learningcontainer.com/wp-content/uploads/2020/07/sample-image-file.jpg",  # URL alternativa
    "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"
]

# Carpeta de descargas
carpeta_descarga = "descargas"

# Obtener la ruta absoluta del script actual y crear la ruta completa para la carpeta de descargas
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_carpeta_descarga = os.path.join(ruta_actual, carpeta_descarga)
print(f"Carpeta de descargas: {ruta_carpeta_descarga}")  # Imprimir la ruta completa de la carpeta de descargas

# Crear la carpeta de descargas si no existe
if not os.path.exists(ruta_carpeta_descarga):  # Verifica si la carpeta de descargas ya existe.
    os.makedirs(ruta_carpeta_descarga)  # Crea la carpeta de descargas si no existe.

# Descargar archivos
for url in urls:
    descargar_archivo(url, ruta_carpeta_descarga)  # Itera sobre la lista de URLs y llama a descargar_archivo para cada URL

# Organizar archivos
organizar_archivos(ruta_carpeta_descarga)  # Llama a organizar_archivos para organizar los archivos descargados en carpetas según su extensión.
