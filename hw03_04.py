from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Oksana Yahovkina", "birthday": "1987.02.24"},
    {"name": "Dmytro Yahovkin", "birthday": "1989.03.05"}
]

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    for user in users:
        today = datetime.now().date()
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = datetime(today.year, birth_date.month, birth_date.day).date()
        future_date = today + timedelta(days=7)
        day_of_week = congratulation_date.weekday()

        if (congratulation_date >= today and congratulation_date <= future_date) and (day_of_week != 5 and day_of_week != 6):
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name":user["name"], "birthday": congratulation_date_str})
    
    return upcoming_birthdays



upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)