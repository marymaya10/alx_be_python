# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("\nReminder:", reminder)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.\n")
print("🚀 Click here to tweet! 🚀")

