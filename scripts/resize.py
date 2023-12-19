from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize((target_width, target_height))
                resized_img.save(output_path)
                print(f"Imagen {filename} redimensionada con éxito.")
        except Exception as e:
            print(f"Error al procesar la imagen {filename}: {str(e)}")

if __name__ == "__main__":
    input_folder = r"C:\Users\saixa\Downloads\archive(7)\bw"
    output_folder = r"C:\Users\saixa\Downloads\archive(7)\bwresized"
    target_width = 300
    target_height = 400

    # Redimensiona las imágenes
    resize_images(input_folder, output_folder, target_width, target_height)
