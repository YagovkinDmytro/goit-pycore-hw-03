from datetime import datetime

date = "2025-02-28"

def get_days_from_today (date :str) -> int:
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_today = datetime.now()
        difference = date_today - date_object
        print(difference.days)
    except:
        print(f"Error: Invalid date: {date}")


get_days_from_today(date)