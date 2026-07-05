import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as f:
            pickle.dump(self.__cache, f)

    def __load(self):
        with open(self.__datasource, 'rb') as f:
            self.__cache = pickle.load(f)

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        if self.__cache.get(key) is not None:
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return list(self.__cache.values())

    def clear(self):
        self.__cache = {}
        self.__dump()
