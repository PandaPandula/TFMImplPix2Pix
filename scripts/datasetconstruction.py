

import os

def cambiar_nombre_carpeta(ruta_carpeta):
    try:
        archivos = os.listdir(ruta_carpeta)

        for archivo in archivos:
            ruta_antigua = os.path.join(ruta_carpeta, archivo)

            if os.path.isfile(ruta_antigua):
                nuevo_nombre = archivo.replace("mask", "sat")

                ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

                os.rename(ruta_antigua, ruta_nueva)

                print(f'Renombrado: {ruta_antigua} -> {ruta_nueva}')

        print('Proceso completado.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

ruta_carpeta = r'C:\Users\saixa\Downloads\archive(4)\Forest Segmented\Forest Segmented\masks'

cambiar_nombre_carpeta(ruta_carpeta)
