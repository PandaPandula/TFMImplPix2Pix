

import os

def cambiar_nombre_carpeta(ruta_carpeta):
    try:
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)

        # Iterar sobre cada archivo
        for archivo in archivos:
            # Construir la ruta completa del archivo
            ruta_antigua = os.path.join(ruta_carpeta, archivo)

            # Verificar si el archivo es un archivo y no un directorio
            if os.path.isfile(ruta_antigua):
                # Cambiar "mask" por "sat" en el nombre del archivo
                nuevo_nombre = archivo.replace("mask", "sat")

                # Construir la nueva ruta del archivo
                ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

                # Renombrar el archivo
                os.rename(ruta_antigua, ruta_nueva)

                print(f'Renombrado: {ruta_antigua} -> {ruta_nueva}')

        print('Proceso completado.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Especifica la ruta de la carpeta que contiene las imágenes
ruta_carpeta = r'C:\Users\saixa\Downloads\archive(4)\Forest Segmented\Forest Segmented\masks'

# Llama a la función para cambiar los nombres de los archivos
cambiar_nombre_carpeta(ruta_carpeta)