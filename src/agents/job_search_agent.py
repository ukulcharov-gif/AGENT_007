from src.utils.config_manager import ConfigManager


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