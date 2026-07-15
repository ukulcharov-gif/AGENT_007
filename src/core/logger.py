from datetime import datetime


class Logger:

    def __init__(self):
        print("Logger создан")

    def log(self, message):
        current_time = datetime.now()

        with open("logs/agent.log", "a", encoding="utf-8") as file:
            file.write(f"{current_time} - {message}\n")