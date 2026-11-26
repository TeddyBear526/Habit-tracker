import json

class Habitmanager:

    def __init__(self, habits = "habits.json" ):
        self._filename = habits
        self._habits = self.load_habits()

    def save_habits(self):
        habits_data = [
            {"namn": habit.get_name(), "count": habit.get_count()}
            for habit in self._habits
        ]
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(habits_data, file, indent=2, ensure_ascii=False)

    def load_habits(self):
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                habits_data = json.load(file)
                return [
                    Habit(item["namn"], item["count"])
                    for item in habits_data
                ]
        except FileNotFoundError:
            return []

    def increase_count(self):
        pass

    def add_habit(self, habit):
        self._habits.append(habit)
        self.save_habits()

    def clear_habits(self):
        self._habits = []
        self.save_habits()

class Habit:
    def __init__(self, namn, count):
        self._namn = namn
        self._count = count

    def set_name(self, namn =""):
        self._namn = namn

    def get_name(self):
        return self._namn

    def set_count(self, count=0):
        self._count = count 

    def get_count(self):
        return self._count       