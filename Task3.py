import re

# Cтворення функції яка форматує номери
def normalize_phone(phone_number):
    formatted_number = re.sub(r'[^0-9+]','',phone_number) # Видалення всіх символів крім чисел та плюса в рядку phone_numver
    
    # Перевірка першого символу чи це початок коду, тобто +
    if formatted_number[0] != '+':
        # Створення умови, якщо починається з 380 то додаємо значок +, інакше додаємо код +38
        if formatted_number.startswith('380'):
            formatted_number = '+' + formatted_number
        else:
            formatted_number = '+38' + formatted_number
    
    # Функція повертає форматовани номер телефону
    return formatted_number


'''
#Приклад використання
print(normalize_phone("+38(050)123-32-34"))  
print(normalize_phone("0503451234")) 
print(normalize_phone("(050)8889900"))  
print(normalize_phone("38050-111-22-22")) 
print(normalize_phone("38050 111 22 11"))  
'''