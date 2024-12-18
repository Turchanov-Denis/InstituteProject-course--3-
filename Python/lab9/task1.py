import openpyxl

# Создаем новый Excel файл
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Employee Data"

# Заголовки таблицы
headers = ['Таб. номер', 'Фамилия', 'Отдел', 'Сумма по окладу',
    'Сумма по надбавкам', 'Сумма зарплаты', 'НДФЛ', 'Сумма НДФЛ', 'Сумма к выдаче']
ws.append(headers)

# Данные сотрудников
employees = [
    {'number': '0002', 'name': 'Петров П.П.',
        'department': 'Бухгалтерия', 'salary': 3913.04, 'bonus': 2608.70},
    {'number': '0005', 'name': 'Васин В.В.',
        'department': 'Бухгалтерия', 'salary': 5934.78, 'bonus': 913.04},
    {'number': '0001', 'name': 'Иванов И.И.',
        'department': 'Отдел кадров', 'salary': 6000.00, 'bonus': 4000.00},
    {'number': '0003', 'name': 'Сидоров С.С.',
        'department': 'Отдел кадров', 'salary': 5000.00, 'bonus': 4500.00},
    {'number': '0006', 'name': 'Львов Л.Л.', 'department': 'Отдел кадров',
        'salary': 4074.07, 'bonus': 2444.44},
    {'number': '0007', 'name': 'Волков В.В.',
        'department': 'Отдел кадров', 'salary': 1434.78, 'bonus': 1434.78},
    {'number': '0004', 'name': 'Мишин М.М.',
        'department': 'Столовая', 'salary': 5500.00, 'bonus': 3500.00}
]

# Добавляем данные сотрудников и вычисления
for employee in employees:
    salary = employee['salary']
    bonus = employee['bonus']
    total_salary = salary + bonus
    ndfl = total_salary * 0.13
    net_salary = total_salary - ndfl

    ws.append([
        employee['number'],
        employee['name'],
        employee['department'],
        salary,
        bonus,
        total_salary,
        13,  # процент НДФЛ
        ndfl,
        net_salary
    ])

# Итоги по отделам
ws.append(['Бухгалтерия Итог', '', '', 
           f"=SUMIF(C2:C5, \"Бухгалтерия\", D2:D5)", 
           f"=SUMIF(C2:C5, \"Бухгалтерия\", E2:E5)", 
           f"=SUMIF(C2:C5, \"Бухгалтерия\", F2:F5)", 
           f"13%", 
           f"=SUMIF(C2:C5, \"Бухгалтерия\", H2:H5)", 
           f"=SUMIF(C2:C5, \"Бухгалтерия\", I2:I5)"])

ws.append(['Отдел кадров Итог', '', '', 
           f"=SUMIF(C6:C9, \"Отдел кадров\", D6:D9)", 
           f"=SUMIF(C6:C9, \"Отдел кадров\", E6:E9)", 
           f"=SUMIF(C6:C9, \"Отдел кадров\", F6:F9)", 
           f"13%", 
           f"=SUMIF(C6:C9, \"Отдел кадров\", H6:H9)", 
           f"=SUMIF(C6:C9, \"Отдел кадров\", I6:I9)"])

ws.append(['Столовая Итог', '', '', 
           f"=SUMIF(C10:C10, \"Столовая\", D10:D10)", 
           f"=SUMIF(C10:C10, \"Столовая\", E10:E10)", 
           f"=SUMIF(C10:C10, \"Столовая\", F10:F10)", 
           f"13%", 
           f"=SUMIF(C10:C10, \"Столовая\", H10:H10)", 
           f"=SUMIF(C10:C10, \"Столовая\", I10:I10)"])

ws.append(['Общий итог', '', '', 
           f"=SUM(D2:D10)", f"=SUM(E2:E10)", f"=SUM(F2:F10)", 
           f"13%", f"=SUM(H2:H10)", f"=SUM(I2:I10)"])


# Сохраняем файл
wb.save("employee_salaries.xlsx")
