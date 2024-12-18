import json
from jsonschema import validate, ValidationError, SchemaError

# Открытие и чтение файла schema.json
with open('schema.json', 'r', encoding='utf-8') as schema_file:
    schema = json.load(schema_file)

# Открытие и чтение файла ex_1.json
with open('ex_1_invalid.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Пытаемся провести валидацию
try:
    validate(instance=data, schema=schema)
    print("Файл прошел валидацию!")
except ValidationError as e:
    print("Ошибка валидации:", e.message)
except SchemaError as e:
    print("Ошибка схемы:", e.message)
