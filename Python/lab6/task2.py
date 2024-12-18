from bs4 import BeautifulSoup

# Чтение исходного XML файла
with open("./source/ex_2.xml", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "xml")

# Добавление нового элемента Item
new_item = soup.new_tag("Item")
new_item_artname = soup.new_tag("ArtName")
new_item_artname.string = "Сыр Чеддер"
new_item.append(new_item_artname)

new_item_barcode = soup.new_tag("Barcode")
new_item_barcode.string = "2000000000151"
new_item.append(new_item_barcode)

new_item_qnt = soup.new_tag("QNT")
new_item_qnt.string = "180"
new_item.append(new_item_qnt)

new_item_qntpack = soup.new_tag("QNTPack")
new_item_qntpack.string = "180"
new_item.append(new_item_qntpack)

new_item_unit = soup.new_tag("Unit")
new_item_unit.string = "шт"
new_item.append(new_item_unit)

new_item_sn1 = soup.new_tag("SN1")
new_item_sn1.string = "00000015"
new_item.append(new_item_sn1)

new_item_sn2 = soup.new_tag("SN2")
new_item_sn2.string = "01.06.2020"
new_item.append(new_item_sn2)

new_item_qntrows = soup.new_tag("QNTRows")
new_item_qntrows.string = "12"
new_item.append(new_item_qntrows)

# Добавление нового элемента в раздел <Detail>
soup.Detail.append(new_item)

# Пересчёт значений в Summary
summ = float(soup.Summary.Summ.string) + 180.0  
summ_rows = int(soup.Summary.SummRows.string) + 1  

# Обновление значений в Summary
soup.Summary.Summ.string = str(summ)
soup.Summary.SummRows.string = str(summ_rows)

# Сохранение изменённого файла
with open("ex_2_mod.xml", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("Изменения сохранены в ex_2_mod.xml")
