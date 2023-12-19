import os

def find_extra_images(folder1, folder2):
    images1 = set(os.listdir(folder1))
    images2 = set(os.listdir(folder2))

    extra_in_folder1 = images1 - images2
    extra_in_folder2 = images2 - images1

    return extra_in_folder1, extra_in_folder2

if __name__ == "__main__":
    folder1 = r"C:\Users\saixa\Downloads\archive(6)\train"
    folder2 = r"C:\Users\saixa\Downloads\archive(6)\trainmask"

    extras_folder1, extras_folder2 = find_extra_images(folder1, folder2)

    print(f"Imágenes en {folder1} pero no en {folder2}:")
    print(extras_folder1)

    print(f"\nImágenes en {folder2} pero no en {folder1}:")
    print(extras_folder2)
