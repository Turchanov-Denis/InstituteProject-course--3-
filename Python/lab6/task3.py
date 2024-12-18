import xml.etree.ElementTree as ET

with open(r'C:\Users\Firo\Desktop\junk\InstituteProject-course--3-\Python\lab6\source\ex_3.xml', encoding='windows-1251') as file:
    xml_data = file.read()
root = ET.fromstring(xml_data)

# Находим все элементы <СведТов>, которые содержат информацию о товарах
for product in root.findall('.//ТаблСчФакт//СведТов'):
    name = product.get('НаимТов') 
    quantity = product.get('КолТов') 
    price = product.get('ЦенаТов')  

    
    name_text = name if name is not None else 'Не указано'
    quantity_text = quantity if quantity is not None else 'Не указано'
    price_text = price if price is not None else 'Не указано'

    print(f"Товар: {name_text}, Количество: {quantity_text}, Цена: {price_text}")
