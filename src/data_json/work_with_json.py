import json
from abc import ABC, abstractmethod

from config import JSON_HH


# class WorkWithJsonAbstract(ABC):
#     @classmethod
#     @abstractmethod
#     def save_json(cls, data):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def read_json(cls):
#         pass


class WorkWithJson:

    @classmethod
    def save_json(cls, data, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls, path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
