import imagehash
from PIL import Image


def createDHash(imagePath):
    return imagehash.dhash(Image.open(imagePath))

