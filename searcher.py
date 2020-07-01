import numpy as np

# Класс движка поисковой системы:
# Сравниваниет параметры индексированного датасета
# и сравнивает с параметрами изображения-образца
# через расчет метрики
class Searcher:
    def __init__(self, index):
        self.index = index

    def search(self, queryFeatures):
        results = {}
        for (k, features) in self.index.items():
            d = self.hamming_distance(features, queryFeatures)
            results[k] = d
        # Результаты сортируются по возрастанию метрики
        results = sorted([(v, k) for (k, v) in results.items()])
        return results
    # Расчет метрики расстояние Хэмминга
    # На сколько позций отличаются хэш-строки изображения
    def hamming_distance(self, hashA, hashB):
        d = hashA - hashB
        return d
