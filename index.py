from hash import createDHash
from imutils.paths import list_images
import argparse
import pickle
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to where the computed images will be stored")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will we stored")
args = vars(ap.parse_args())
index = {}

for imagePath in list_images(args["dataset"]):
    k = imagePath[imagePath.rfind("/") + 1:]
    features = createDHash(imagePath)
    index[k] = features

f = open(args["index"], "wb")
f.write(pickle.dumps(index))
f.close()

print("[INFO] done...indexed {} images".format(len(index)))
