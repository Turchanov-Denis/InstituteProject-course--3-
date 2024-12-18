import json

# Открываем JSON файл с данными
with open('ex_2_correct.json', 'r') as file:
    data = json.load(file)

# Создаем словарь с именами пользователей и их номерами телефонов
user_phones = {user['name']: user['phoneNumber'] for user in data}

# Выводим полученный словарь
print(user_phones)
