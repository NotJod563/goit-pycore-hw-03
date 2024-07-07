from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7) # Дата кінця наступного тижня
    last_week = today - timedelta(days=7)
    upcoming_birthdays = []

    # Проходимось циклом по списку всіх робітників
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Перевірка чи день народження в цьому році ще не наступив та чи він далі ніж 7 днів з сьогоднішнього дня
        if today <= birthday_this_year < next_week:
            # Якщо день попадає на вихідний то переносимо його на наступний понеділок
            if birthday_this_year.weekday() >= 5:
                days_until_monday = (7 - birthday_this_year.weekday()) % 7
                birthday_this_year += timedelta(days=days_until_monday)
                upcoming_birthdays.append({user["name"]: birthday_this_year.strftime("%Y.%m.%d")}) # Наповнення списку днів народження
                
        # Тут відбувається перевірка чи день народження з минулого тижня припадали на вихідний день, якщо так, то треба їх поздоровити в цей понеділок, а значить відобразити в списку :)       
        elif birthday_this_year > last_week and birthday_this_year.weekday() >= 5:
            days_until_monday = (7 - birthday_this_year.weekday()) % 7
            birthday_this_year += timedelta(days=days_until_monday)
            upcoming_birthdays.append({user["name"]: birthday_this_year.strftime("%Y.%m.%d")}) # Наповнення списку днів народження
    
    return upcoming_birthdays # Повертаємо список днів народжень як результат роботи функції

'''
users = [
    {"name": "John Doe", "birthday": "1990.07.01"},
    {"name": "Jane Smith", "birthday": "1985.07.14"}
]

upcoming_birthdays_list = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays_list)
'''