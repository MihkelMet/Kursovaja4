from src.API.hh import RequestHH
from src.API.sj import RequestsSJ
from src.vacancy.vacancy import VacancyHH, VacancySJ


def dialog():
    """Функция помогает пользователю выбрать искомый сайт и профессию"""
    print('Нажмите 1 для поиска по сайту SJ, нажмите 2 для поиска на HH')
    site = int(input())
    print('Введите ключевое слово для поиска: ')
    key_word = input()
    if site == 1:
        a = RequestsSJ(key_word)
        a.request()
        VacancySJ.get_data()
    elif site == 2:
        b = RequestHH(key_word)
        b.request()
        VacancyHH.get_data()


dialog()