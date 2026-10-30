
import json
import os
from datetime import date

# Available moods
MOODS = {
    "1": "Happy",
    "2": "Normal",
    "3": "Sad",
    "4": "Tired",
    "5": "Angry"
}

FILE_NAME = "moods.json"


# Load saved moods
def load_moods():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save moods
def save_moods(moods):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(moods, file, indent=4, ensure_ascii=False)


# Add a new mood
def add_mood(moods):
    print("\n--- Choose Your Mood ---")

    for key, value in MOODS.items():
        print(f"{key}. {value}")

    choice = input("Your mood: ")

    if choice in MOODS:
        new_mood = {
            "date": date.today().isoformat(),
            "mood": MOODS[choice]
        }

        moods.append(new_mood)
        save_moods(moods)

        print("Your mood has been saved successfully!")

    else:
        print("Invalid mood choice!")


# View mood history
def view_history(moods):
    print("\n--- Mood History ---")

    if not moods:
        print("No moods recorded yet.")
        return

    for item in moods:
        print(f"Date: {item['date']} | Mood: {item['mood']}")


# View mood statistics
def view_statistics(moods):
    print("\n--- Mood Statistics ---")

    if not moods:
        print("No data available.")
        return

    counts = {}

    for item in moods:
        mood = item["mood"]
        counts[mood] = counts.get(mood, 0) + 1

    total = len(moods)

    print(f"Total recorded moods: {total}")

    for mood, count in counts.items():
        percentage = (count / total) * 100
        print(f"{mood}: {count} time(s) - {percentage:.1f}%")

    most_common = max(counts, key=counts.get)
    print(f"\nMost frequent mood: {most_common}")


# Main program
def main():
    moods = load_moods()

    while True:
        print("\n========== MOOD TRACKER ==========")
        print("1. Add today's mood")
        print("2. View mood history")
        print("3. View mood statistics")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_mood(moods)

        elif choice == "2":
            view_history(moods)

        elif choice == "3":
            view_statistics(moods)

        elif choice == "4":
            print("Thank you for using Mood Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
