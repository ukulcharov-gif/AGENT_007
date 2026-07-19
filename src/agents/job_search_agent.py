from src.utils.config_manager import ConfigManager
from src.parsers.json_placeholder_parser import JsonPlaceholderParser
from models.vacancy_manager import VacancyManager


class JobSearchAgent:

    def run(self):
        print("\n=== Поиск вакансий ===\n")

        config = ConfigManager()
        search = config.load_search()

        if search:
            print("Найден предыдущий поиск:")
            print(f"Профессия : {search['profession']}")
            print(f"Страна    : {search['country']}")
            print(f"Ключевые  : {search['keywords']}")

        profession = input("Введите профессию: ")
        country = input("Введите страну: ")
        keywords = input("Введите ключевые слова: ")

        print("\nПараметры поиска:")
        print(f"Профессия : {profession}")
        print(f"Страна    : {country}")
        print(f"Ключевые  : {keywords}")

        # Сохраняем параметры поиска
        config.save_search({
            "profession": profession,
            "country": country,
            "keywords": keywords
})

        print("\nПоиск сохранен.")

        # Получаем тестовые вакансии
        print("\nПоиск тестовых вакансий...")

        parser = JsonPlaceholderParser()
        vacancies = parser.get_vacancies()   

        # Создаем менеджер вакансий
        manager = VacancyManager()

        # Добавляем вакансии в менеджер
        for vacancy in vacancies:
            manager.add_vacancy(vacancy)

        # Выводим найденные вакансии
        print("\nНайденные вакансии:\n")
        manager.show_all()

        manager.save_to_json()

        print("\nВакансии сохранены.")