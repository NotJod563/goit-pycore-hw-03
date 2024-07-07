from datetime import datetime 

#Створення функції в якій буде підрахунок днів
def get_days_from_today(date):
    #Пробуємо зробити операції над введеним рядком, у випадку проблем з форматом дати все що в блоці try не буде виконаним
    try:
        #Перетворення отриманого рядку в змінну з потрібним форматом
        input_date = datetime.strptime(date, "%Y-%m-%d")
        #Присвоєння змінній поточної дати
        today_date = datetime.today()
        #Створення змінної та присвоєння їй різниці між поточною датою та датою яка прийшла в функцію з викликом
        delta_days = today_date - input_date
        #Повертаємо різницю в форматі днів
        return delta_days.days
    except ValueError:
        return "Не вірний формат дати, перевірте що він співпадає з форматом 'РРРР-ММ-ДД'"

'''
#Перевірка роботи функції   
print(get_days_from_today("2024-07-02"))
'''