import numpy as np


class Searcher:
    def __init__(self, index):
        self.index = index

    def search(self, queryFeatures):
        results = {}
        for (k, features) in self.index.items():
            d = self.hamming_distance(features, queryFeatures)
            results[k] = d
        results = sorted([(v, k) for (k, v) in results.items()])
        return results

    def hamming_distance(self, hashA, hashB):
        d = hashA - hashB
        return d