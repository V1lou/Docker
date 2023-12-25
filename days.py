from datetime import datetime

# получаем текущую дату
current_date = datetime.now()

# получаем дату Нового года для текущего года
new_year = datetime(current_date.year + 1, 1, 1)

# вычисляем количество дней до Нового года
days_left = (new_year - current_date).days

# записываем результат в файл
with open('days.txt', 'w') as file:
    file.write(f'До Нового года осталось {days_left} дней')
