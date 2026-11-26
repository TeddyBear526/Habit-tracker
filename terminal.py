from models import Habitmanager, Habit

habitmanager = Habitmanager()

print("Welcome to your HabitManager!")
while True:


    print("Vad vill du göra?")
    print("1. Visa vanor")
    print("2. Lägg till vana")
    print("3. checka av vana")
    print("4. Avsluta")

    choice = input("Välj ett alternativ (1-4): ")

    if choice == "1":
        habits = habitmanager.load_habits()
        if not habits:
            print("Inga vanor sparade.")

    elif choice == "2":
        name = input("Ange vanans namn: ")
        count = 0
        habit = Habit(name, count)
        habitmanager.add_habit(habit)
        print("Vanan har sparats.")

    elif choice == "3":
        habits = habitmanager.load_habits()
        if not habits:
            print("Inga vanor")
        else:
            for number, habit in enumerate(habits, start=1):
                print(f"{number}. {habit.get_name()}: {habit.get_count()}")
            try:
                selected = int(input("Vilken vana vill du checka av? ")) - 1

                if 0 <= selected < len(habits):
                    habitmanager.increase_count()
                    print("Vanan har checkats av.")
                else: 
                    print("Ogiltigt nummer.")
            except ValueError:
                print("Ange ett nummer.")


    elif choice == "4":
        break

    else:
        print("Ogiltigt val.")
