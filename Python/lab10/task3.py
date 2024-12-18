from docx import Document

doc = Document('test.docx')

table = doc.tables[0]

table_data = {}

for i, row in enumerate(table.rows):
    cells = [cell.text.strip() for cell in row.cells]
    
    if i == 0:  
        headers = cells
        table_data = {header: [] for header in headers}  
    else:
        for j, header in enumerate(headers):
            table_data[header].append(cells[j]) 

print(table_data.get('ATmega328'))
