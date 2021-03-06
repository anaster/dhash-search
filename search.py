from hash import createDHash
from searcher import Searcher
import numpy as np
import argparse
import os
import pickle
import cv2

# Обработка команд в консоли с обработкой трех обязательных параметров:
# 1. Название папки-датасета
# 2. Файл с индексами
# 3. Путь к ищображению-образцу
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where we stored our index")
ap.add_argument("-q", "--query", required=True,

                help="Path to query image")
args = vars(ap.parse_args())
queryImage = cv2.imread(args["query"])
cv2.imshow("Query", queryImage)
print("query: {}".format(args["query"]))
queryFeatures =createDHash(args["query"])
index = pickle.loads(open(args["index"], "rb").read())
searcher = Searcher(index)
results = searcher.search(queryFeatures)
# Вывод первых 10 результатов в формате "путь файла : расстояние Хэмминга"
# Если при поиске алгоритм нашел копию образца (расстояние Хэмминга 0)
# Поиск считается успешным
for j in range(0, 10):
    (score, imageName) = results[j]
    path = os.path.join(args["dataset"], imageName)
    result = cv2.imread(path)
    print("\t{}. {} : {:}".format(j + 1, imageName, score))
cv2.waitKey(0)
