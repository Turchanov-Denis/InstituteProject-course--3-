import json

input_file = './source/ex_3.json'
output_file = 'task3.json'  # Новый файл

with open(input_file, 'r') as file:
    data = json.load(file)

new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 2,
            "price": 50.00
        },
        {
            "name": "item 5",
            "quantity": 1,
            "price": 50.00
        }
      ]
}

data["invoices"].append(new_invoice)

with open(output_file, 'w') as file:
    json.dump(data, file, indent=2)

print("Updated JSON data saved to task3.json:")
print(json.dumps(data, indent=2))
