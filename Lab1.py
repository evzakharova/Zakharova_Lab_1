# Math:
# 1. Найти корни квадратного уравнения ax^2 + bx + c (math.sqrt)

# import math
# a = int(input("Введите значение 'a':"))
# b = int(input("Введите значение 'b':"))
# c = int(input("Введите значение 'c':"))
#
# if a == 0:
#     if b != 0:
#         x = -c / b
#         print(f"Уравнение станет линейным, корень: x ={x}")
#     else:
#         print("Уравнение некорректно: коэффициенты a и b не могут одновременно равняться нулю.")
# else:
#     D = b**2 - 4*a*c
#     if D > 0:
#         x1 = (-b + math.sqrt(D)) / (2*a)
#         x2 = (-b - math.sqrt(D)) / (2*a)
#         print(f"Корни уравнения: x1 ={x1} и x2 ={x2}")
#     elif D == 0:
#         x = -b / (2*a)
#         print(f"У уравнения есть один корень: x ={x}")
#     else:
#         print("Уравнение не имеет действительных корней")


# 2. Найти площадь круга

# import math
# r = int(input("Введите значение радиуса:"))
# s = math.pi * r**2
# print(f"Площадь круга с радиусом {r} равна {s}")


# Counter:
# 1. Вывести элементы массива, которые встречаются только один раз (или два/три/четыре раза), причём в том порядке,
# в котором они идут в массиве.

# from collections import Counter
# a = list(input("Введите данные через запятую:"))
# count = []
# for key, value in Counter(a).items():
#     if value == 2:
#         count.append(key)
# print(count)

# 2.Дан массив a из n целых чисел. Напишите программу, которая найдет наибольшее число,
# которое чаще других встречается в массиве (т.е. если три числа встречаются одинаковое количество раз,
# нужно найти наибольшее из них).

# from collections import Counter
#
# a = [int(num) for num in input("Введите числа через запятую:").split(",")]
# counter = Counter(a)
# final_num = 0
# max_count = 0
# for number, count in counter.items():
#     if count > max_count or (count == max_count and number > final_num):
#         final_num = number
#         max_count = count
# print(final_num)


# Itertools:
# 1. Нужно составить таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов используются пятибуквенные слова, в которых есть только буквы А, Т, О, М,
# причём буква «М» появляется ровно 1 раз. Каждая из других допустимых букв может встречаться в кодовом слове
# любое количество раз или не встречаться совсем. Сколько различных кодовых слов можно использовать?


# import itertools
#
# k = 0
# a = list(itertools.product('атом', repeat=5))
# for x in a:
#     if x.count('м') == 1:
#         k += 1
#
# print(k)


# 2. Ученик составляет шестибуквенные слова путём перестановки букв “НЕБО”
# (или любого другого слова/набора букв). Сколько различных слов можно составить?


# import itertools
# a = list(itertools.product("НЕБО", repeat=6)) #если кол-во букв меньше длины слова
# print(len(a))

# import itertools
# a = list(itertools.permutations("ОБЛАКА",6)) #если кол-во букв больше или равно длине слова
# print(len(a))


# Cycle:
# 1. Создайте функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа)
# заданное количество раз (tries) циклически. Один раз - один элемент списка.
# После вывода последнего значения последовательности процедура начнется с самого начала.

# Например, если в списке 2 элемента, а функция получила значение 3,
# то сначала выведется первый объект, потом последний, а потом опять первый.
# Результат работы функции представьте в виде строки, состоящей из tries количества символов.

# from itertools import cycle
#
#
# def infinite(lst, tries):
#     result = ''
#     cycle_lst = cycle(lst)
#     for _ in range(tries):
#         result += str(next(cycle_lst))
#     return result
#
#
# lst = [int(num) for num in input("Введите числа через запятую:").split(",")]
# tries = int(input("Введите количество раз:"))
# print(infinite(lst, tries))


# Обработка данных JSON:
#
# С помощью json модуля напишите скрипт, который считывает файл JSON, содержащий информацию о книгах
# (название, авторов, ISBN, количество страниц, статус публикации, тематику и т.д.), и выводит список всех книг,
# в которых количество страниц больше 500.
# (Файл books.json)


# import json
#
# with open('books.json','r', newline='') as file:
#     data = json.load(file)
#
# for book in data:
#     if book.get('pageCount', 0) > 500:
#         print(f"Название: {book.get('title')}")
#         print(f"Автор(ы): {', '.join(book.get('authors', []))}")
#         print(f"ISBN: {book.get('isbn')}")
#         print(f"Тематика: {book.get('categories')}")
#         print("______________")


# Манипулирование данными CSV:
# Используя модуль  csv, напишите скрипт, который читает CSV-файл, выполняет вычисления с данными и выводит результаты в новый CSV-файл.

# 1. Файл freshman_kgs.csv - создать столбец Weight diff, который будет отражать изменение веса с сентября по апрель.
# Вывести только те строки, в которых представлены респонденты мужского пола, чья разница в весе неотрицательна, а ИМТ в апреле больше двадцати.


# import csv

# with open("freshman_kgs.csv", mode="r") as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)

#     with open("result_kgs.csv", mode="w", newline="") as result_file:
#         csv_writer = csv.writer(result_file)
#         csv_writer.writerow(header + ["Weight diff"])

#         for row in csv_reader:
#             sex = row[0]
#             weight_diff = int(row[1]) - int(row[2])
#             bmi = float(row[4])

#             if sex == "M" and weight_diff >= 0 and bmi > 20.0:
#                 weight_diff = str(weight_diff)
#                 csv_writer.writerow(row + [weight_diff])

# print("Результаты сохранены в файле result_kgs.csv")

# 2. Файл homes.csv, где представлена статистика по продаже домов. Столбцы: цена продажи и запрашиваемая цена (в тыс.долларов),
# жилая площадь, количество комнат, ванных комнат, возраст дома, количество акров на участке, налог (в долларах).
# Нужно рассчитать среднюю итоговую стоимость дома с восемью комнатами, а также создать новый столбец,
# в котором были бы только дома со стоимостью более 180 и налогом менее 3500.

# import csv
# rows = []
# with open("homes.csv", mode="r", newline="") as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         rows.append(row)


# total_cost = 0
# count = 0
# for row in rows[1:]:
#     if len(row) > 3 and int(row[3]) == 8:
#         total_cost += (int(row[0])*1000 + int(row[8]))  # Необходимо перевести тысячи долларов в доллары
#         count += 1

# avg_cost = total_cost / count


# filtered_rows = [rows[0]]
# for row in rows[1:]:
#     if len(row) > 8 and int(row[0]) > 180 and int(row[8]) < 3500:
#         filtered_rows.append(row)


# with open("result_homes.csv", mode="w", newline="") as new_file:
#     writer = csv.writer(new_file)
#     for row in filtered_rows:
#         writer.writerow(row)

# print(f"Средняя итоговая стоимость дома с восемью комнатами: {avg_cost} долларов")
# print("Результаты сохранены в файле result_homes.csv")

