from PIL import Image
import os

def combinar_imagenes(carpeta1, carpeta2, carpeta_salida):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener la lista de archivos en ambas carpetas
    archivos_carpeta1 = os.listdir(carpeta1)

    # Iterar sobre los archivos de la carpeta 1
    for archivo1 in archivos_carpeta1:
        # Comprobar si el archivo también existe en la carpeta 2
        archivo2 = os.path.join(carpeta2, archivo1)

        if os.path.exists(archivo2):
            # Abrir ambas imágenes
            imagen1 = Image.open(os.path.join(carpeta1, archivo1))
            imagen2 = Image.open(archivo2)

            # Obtener el tamaño de ambas imágenes
            ancho1, alto1 = imagen1.size
            ancho2, alto2 = imagen2.size

            # Crear una nueva imagen con el doble de ancho
            imagen_combinada = Image.new('RGB', (ancho1 + ancho2, max(alto1, alto2)))

            # Pegar la imagen de la carpeta 1 a la izquierda
            imagen_combinada.paste(imagen1, (0, 0))

            # Pegar la imagen de la carpeta 2 a la derecha
            imagen_combinada.paste(imagen2, (ancho1, 0))

            # Guardar la imagen combinada en la carpeta de salida
            nombre_salida = f"{archivo1}"
            ruta_salida = os.path.join(carpeta_salida, nombre_salida)
            imagen_combinada.save(ruta_salida)

            print(f"Imagen combinada guardada en {ruta_salida}")

if __name__ == "__main__":
    carpeta1 = r"C:\Users\saixa\Downloads\archive(7)\bwresized"
    carpeta2 = r"C:\Users\saixa\Downloads\archive(7)\trainresized"
    carpeta_salida = r"C:\Users\saixa\Downloads\archive(7)\train"

    combinar_imagenes(carpeta1, carpeta2, carpeta_salida)
