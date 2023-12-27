from dotenv import load_dotenv
import requests
import os
from config import URL_SJ, JSON_SJ
from src.data_json.work_with_json import WorkWithJson

load_dotenv()
# config = dotenv.dotenv_values(".env")

class RequestsSJ(WorkWithJson):
    """Класс, который отправляет запрос на сайт по поиску работы SuperJob"""

    def __init__(self, keyword, page=1) -> None:
        self.url = URL_SJ
        self.params = {"keywords": keyword, "page": page}

    def request(self) -> dict:
        """Метод класса, который обращается на сайт SJ по ключу и возвращает
        файл в формате json с данными о вакансиях"""
        headers = {
            "X-Api-App-Id": os.getenv("API_KEY")
        }
        try:
            responce = requests.get(self.url, params=self.params, headers=headers)
            responce.raise_for_status()
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        else:
            return WorkWithJson.save_json(responce.json()["objects"], JSON_SJ)
