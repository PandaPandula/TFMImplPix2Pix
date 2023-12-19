from PIL import Image
import os

def combinar_imagenes(carpeta1, carpeta2, carpeta_salida):
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    archivos_carpeta1 = os.listdir(carpeta1)

    for archivo1 in archivos_carpeta1:
        archivo2 = os.path.join(carpeta2, archivo1)

        if os.path.exists(archivo2):
            imagen1 = Image.open(os.path.join(carpeta1, archivo1))
            imagen2 = Image.open(archivo2)

            ancho1, alto1 = imagen1.size
            ancho2, alto2 = imagen2.size

            imagen_combinada = Image.new('RGB', (ancho1 + ancho2, max(alto1, alto2)))


            imagen_combinada.paste(imagen1, (0, 0))
            imagen_combinada.paste(imagen2, (ancho1, 0))

            nombre_salida = f"{archivo1}"
            ruta_salida = os.path.join(carpeta_salida, nombre_salida)
            imagen_combinada.save(ruta_salida)

            print(f"Imagen combinada guardada en {ruta_salida}")

if __name__ == "__main__":
    carpeta1 = r"C:\Users\saixa\Downloads\archive(7)\bwresized"
    carpeta2 = r"C:\Users\saixa\Downloads\archive(7)\trainresized"
    carpeta_salida = r"C:\Users\saixa\Downloads\archive(7)\train"

    combinar_imagenes(carpeta1, carpeta2, carpeta_salida)
