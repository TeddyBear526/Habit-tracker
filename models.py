import json

Habits = "Habittracker.json"

class Habitmanager:
    def __init__(self) -> None:
        pass
    def save_habits(habits : list[str]):
        with open(Habits, "w", encoding="utf-8") as file:
            json.dump(habits, file, indent=2, ensure_ascii=False)

    def load_habits():
        try:
            with open(Habits,"r",encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
