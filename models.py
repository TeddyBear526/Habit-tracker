import json

Habits = "Habittracker.json"

class Habitmanager:
    def __init__(self):
        pass
    def save_habits(self, habits):
        with open(Habits, "w", encoding="utf-8") as file:
            json.dump(habits, file, indent=2, ensure_ascii=False)

    def load_habits(self):
        try:
            with open(Habits,"r",encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

