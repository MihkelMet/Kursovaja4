from abc import ABC, abstractmethod


class WorkWithAbstract(ABC):
    """Абстрактный класс, который отправляет
    запросы на все сайты по поиску работы"""

    @abstractmethod
    def request(self):
        pass