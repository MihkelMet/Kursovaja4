import requests

from config import URL_HH
from src.abstract_class_api import WorkWithAbstract
from src.data_json.work_with_json import WorkWithJson


class RequestHH(WorkWithAbstract):
    def __init__(self, keyword, area=113):
        self.url = URL_HH
        self.keyword = keyword
        self.area = area
        self.parameter = {"text": self.keyword, "area": self.area}

    def request(self):
        responce = requests.get(self.url, self.parameter)
        WorkWithJson.save_json(responce.json()["items"])