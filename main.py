import pandas as pd
from tabulate import tabulate

def table_head(): # объявляем функцию для ввода названий столбцов
    head = [] # объявляем пустой список для названий столбцов
    column_number = 1 # объявляем начальное количество столбцов
    while True: # запускаем бесконечный цикл
        if column_number > 2: # проверяем, превышает ли количество столбцов значение 2
            answer = input('Do you want more columns? (y/n) - ') # спрашиваем, хочет ли пользователь добавить еще столбцов
            if answer.lower() == 'n': # проверяем отрицательный ответ
                break # прекращаем работу цикла
            elif answer.lower() != 'y': # проверяем правильность написания ответа
                continue # запускаем новую итерацию цикла, если ответ был введен некорректно
        head.append(input(f'Enter name of column {column_number} - ')) # добавляем название столбца, которое вводит пользователь
        column_number += 1 # увеличиваем количество столбцов
    return head # возвращаем названия столбцов

def table_body(head_length): # объявляем функцию для ввода содержимого таблицы, которой передаем количество столбцов
    body = [] # объявляем пустой список для содержимого таблицы
    row = [] # объявляем пустой список для содержимого одной строки
    rows_number = 1 # объявляем начальное количество строк
    while True: # запускаем бесконечный цикл
        if rows_number > 2: # проверяем, превышает ли количество строк значение 2
            answer = input('Do you want more rows? (y/n) - ') # спрашиваем, хочет ли пользователь добавить еще строк
            if answer.lower() == 'n': # проверяем отрицательный ответ
                break # прекращаем работу цикла
            elif answer.lower() != 'y': # проверяем правильность написания ответа
                continue # запускаем новую итерацию цикла, если ответ был введен некорректно
        row.clear() # очищаем список значений строки
        print(f'Row {rows_number}:') # выводим номер заполняемой строки
        for i in range(head_length): # запускаем цикл, который будет осуществлять количество итераций, равное количеству столбцов в таблице
            row.append(input(f'Enter value {i + 1} - ')) # добавляем в строку значение, которое вводим пользователь
        body.append(row) # добавляем в содержимое таблицы строку
        rows_number += 1 # увеличиваем количество строк
    return body # возвращаем содержимое таблицы

def main():
    head = table_head() # объявляем переменную, которой присваиваем список названий столбцов
    body = table_body(len(head)) # объявляем переменную, которой присваиваем вложенный список содержимого таблицы

    table = pd.DataFrame(body, columns=head) # создаем DataFrame, которому передаем содержимое таблицы и названия столбцов
    table.to_csv(input('Enter table name - ') + '.csv', index=False) # преобразуем DataFrame в csv-файл, название которого вводит пользователь
    print(tabulate(table, showindex=False, headers=head)) # выводим DataFrame в консоль с помощью модуля tabulate

if __name__ == '__main__':
    main()