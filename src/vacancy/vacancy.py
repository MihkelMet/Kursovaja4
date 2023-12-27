import json
from abc import ABC, abstractmethod

from config import JSON_HH, JSON_SJ


class Vacancy(ABC):
    """Абстрактный класс для всех вакансий"""

    @classmethod
    @abstractmethod
    def get_data(cls):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


class VacancyHH(Vacancy):
    """Класс для вакансий с сайта HH"""

    def __init__(self, title: str, link: str, description: str, salary: dict) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: "
            f"{self.salary['from'] if self.salary and self.salary['from'] else '-'}"
        )

    @classmethod
    def get_data(cls) -> None:
        with open(JSON_HH, "r") as file:
            vacancies = json.load(file)
            vacancy_s = []
            for i in vacancies:
                vacancy = VacancyHH(
                    i["name"],
                    i["alternate_url"],
                    i["snippet"]["responsibility"],
                    i["salary"],
                )
                if vacancy.salary is None:
                    continue
                if vacancy.salary['from'] is None:
                    vacancy.salary['from'] = 0
                vacancy_s.append(vacancy)

        for vacancy in sorted(vacancy_s):
            print(vacancy)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary > other.salary
        raise ValueError("Можно сравнивать только объекты вакансий")

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary['from'] < other.salary['from']
        raise ValueError("Можно сравнивать только объекты вакансий")


class VacancySJ(Vacancy):
    """Класс вакансий с сайта SuperJob"""

    def __init__(self, title: str, link: str, description: str, salary: dict) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: {self.salary}"
        )

    @classmethod
    def get_data(cls) -> None:
        with open(JSON_SJ, "r") as file:
            vacancy = json.load(file)
            vacancy_s = []
            for i in vacancy:
                vacancy_s.append(
                    VacancySJ(
                        i["profession"],
                        i["link"],
                        i["candidat"],
                        i["payment_from"],
                    )
                )
        for vacancy in sorted(vacancy_s):
            print(vacancy)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary > other.salary
        raise ValueError("Можно сравнивать только объекты вакансий")

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary < other.salary
        raise ValueError("Можно сравнивать только объекты вакансий")
