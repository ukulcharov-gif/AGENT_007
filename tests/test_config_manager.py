from src.utils.config_manager import ConfigManager


def main():
    config = ConfigManager()

    data = {
        "profession": "QA Engineer",
        "country": "Poland",
        "keywords": "remote"
    }

    config.save_search(data)

    result = config.load_search()

    print(result)


if __name__ == "__main__":
    main()