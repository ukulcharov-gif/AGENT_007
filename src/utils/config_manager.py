import json
from pathlib import Path

class ConfigManager:

    def __init__(self):
        self.search_file = Path("data/search_config.json")

    def load_search(self):
        if self.search_file.exists():
            with open(self.search_file, "r", encoding="utf-8") as file:
                return json.load(file)

        return {} 

    def save_search(self, data):
        with open(self.search_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)   