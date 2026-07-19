from src.parsers.base_parser import BaseParser
from models.vacancy import Vacancy


class JsonPlaceholderParser(BaseParser):

    def get_vacancies(self):
        vacancies = []

        vacancies.append(
            Vacancy(
                title="Python Developer",
                company="Demo Company",
                country="Germany",
                city="Berlin",
                salary="4500",
                link="https://example.com/job/1"
            )
        )

        return vacancies