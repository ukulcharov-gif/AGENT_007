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

        path = Path(filename)

        if not path.exists():
            print("Файл не найден.")
            return

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.vacancies = []

        for item in data:
            vacancy = Vacancy(
                title=item["title"],
                company=item["company"],
                country=item["country"],
                city=item["city"],
                salary=item["salary"],
                link=item["link"]
            )

            self.vacancies.append(vacancy)

        print(f"Загружено вакансий: {len(self.vacancies)}")

    def find_by_country(self, country):

        result = []

        for vacancy in self.vacancies:
            if vacancy.country.lower() == country.lower():
                result.append(vacancy)

        return result

    def find_by_company(self, company):

        result = []

        for vacancy in self.vacancies:
            if vacancy.company.lower() == company.lower():
                result.append(vacancy)

        return result

    def find_by_keyword(self, keyword):

        result = []

        for vacancy in self.vacancies:
            if keyword.lower() in vacancy.title.lower():
                result.append(vacancy)

        return result
    
    def sort_by_salary(self):

        return sorted(
            self.vacancies,
            key=lambda vacancy: int(
                ''.join(filter(str.isdigit, vacancy.salary))
            ),
            reverse=True
        )

    def top_n(self, count):

        return self.sort_by_salary()[:count]

    def find_by_salary(self, min_salary):

        result = []

        for vacancy in self.vacancies:

            salary = int(
                ''.join(filter(str.isdigit, vacancy.salary))
            )

            if salary >= min_salary:
                result.append(vacancy)

        return result


if __name__ == "__main__":

    manager = VacancyManager()

    manager.load_from_json()

    print("\nВакансии из Германии:\n")

    print("\nТОП-2 вакансии по зарплате:\n")

for vacancy in manager.top_n(2):
    vacancy.show()