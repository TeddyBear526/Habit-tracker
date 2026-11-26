import json

class Habitmanager:

    def __init__(self, habits = "habits.json" ):
        self._habits = habits

    def save_habits(self):
        with open(self._habits, "w", encoding="utf-8") as file:
            json.dump(self._habits, file, indent=2, ensure_ascii=False)

    def load_habits(self):
        try:
            with open(self._habits,"r",encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

class Habit:
    def __init__(self, namn, count):
        self._namn = namn
        self._count = count

    def set_name(self, namn =""):
        self._namn = namn

    def get_name(self):
        return self._namn

    def set_count(self, count=int):
        self._count = count 

    def get_count(self):
        return self._count       