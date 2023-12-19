import torch
from utils import save_checkpoint, load_checkpoint, inference
import torch.nn as nn
import torch.optim as optim
import config
from dataset import MapDataset
from generator import Generator
from discriminator import Discriminator
from torch.utils.data import DataLoader
from tqdm import tqdm
from PIL import Image
import numpy as np

#funcion inference para generar imagenes a partir de una imagen de entrada
def inference_image():
    #cargamos el modelo
    gen = Generator(in_channels=3, features=64).to(config.DEVICE)
    opt_gen = optim.Adam(gen.parameters(), lr=config.LEARNING_RATE, betas=(0.5, 0.999))
    load_checkpoint(
            config.CHECKPOINT_GEN, gen, opt_gen, config.LEARNING_RATE,
    )
    
    #cargamos la imagen de entrada
    input_image = np.array(Image.open(config.IMAGE_INFERENCE_PATH)) 
    augmentations = config.both_transform(image=input_image)
    input_image = augmentations["image"]

    input_image = config.transform_only_input(image=input_image)["image"]
    # llamamos a la funcion inference
    inference(gen, input_image, config.SAVE_INFER)


if __name__ == "__main__":
    inference_image()  


    