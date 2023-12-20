from pathlib import Path

URL_HH = 'https://api.hh.ru/vacancies'
JSON_HH = Path(Path(__file__).parent, 'cache_json', 'cache_hh.json')

URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
JSON_SJ = Path(Path(__file__).parent, 'cache_json', 'cache_sj.json')