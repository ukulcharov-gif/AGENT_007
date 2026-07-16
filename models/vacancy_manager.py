import json
from pathlib import Path

from models.vacancy import Vacancy


class VacancyManager:

    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy: Vacancy):
        self.vacancies.append(vacancy)

    def show_all(self):
        for vacancy in self.vacancies:
            vacancy.show()

    def save_to_json(self, filename="data/vacancies/vacancies.json"):

        path = Path(filename)

        path.parent.mkdir(parents=True, exist_ok=True)

        data = []

        for vacancy in self.vacancies:
            data.append({
                "title": vacancy.title,
                "company": vacancy.company,
                "country": vacancy.country,
                "city": vacancy.city,
                "salary": vacancy.salary,
                "link": vacancy.link
        })

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="data/vacancies/vacancies.json"):
        # Здесь будет настоящий код
        pass