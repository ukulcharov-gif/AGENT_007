from models.vacancy import Vacancy
from src.parsers.base_parser import BaseParser


class FakeParser(BaseParser):

    def get_vacancies(self):

        vacancies = [

            Vacancy(
                title="QA Engineer",
                company="Siemens",
                country="Germany",
                city="Berlin",
                salary="4200 €",
                link="https://example1.com"
            ),

            Vacancy(
                title="Python Developer",
                company="BMW",
                country="Germany",
                city="Munich",
                salary="4800 €",
                link="https://example2.com"
            ),

            Vacancy(
                title="System Administrator",
                company="Bosch",
                country="Germany",
                city="Stuttgart",
                salary="3900 €",
                link="https://example3.com"
            )

        ]

        return vacancies