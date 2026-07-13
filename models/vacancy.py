from dataclasses import dataclass


@dataclass
class Vacancy:
    title: str
    company: str
    country: str
    city: str
    salary: str
    link: str

    def show(self):
        print("=" * 50)
        print(f"Должность : {self.title}")
        print(f"Компания  : {self.company}")
        print(f"Страна    : {self.country}")
        print(f"Город     : {self.city}")
        print(f"Зарплата  : {self.salary}")
        print(f"Ссылка    : {self.link}")


# Проверка
if __name__ == "__main__":
    vacancy = Vacancy(
        title="QA Engineer",
        company="Siemens",
        country="Germany",
        city="Berlin",
        salary="4200 €",
        link="https://example.com"
    )

    vacancy.show()