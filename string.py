# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula ")
# print(text)
# text = '''Laudate omnes gentes laudate
# Magnificat in secula
# Et anima mea laudate
# Magnificat in secula 
# '''
# print(text)
# # Строка может содержать ряд специальных символов - управляющих последовательностей или escape-последовательности:
# # \: позволяет добавить внутрь строки слеш
# # \': позволяет добавить внутрь строки одинарную кавычку
# # \": позволяет добавить внутрь строки двойную кавычку
# # \n: осуществляет переход на новую строку
# # \t: добавляет табуляцию (4 отступа)
# text = "Message:\n\"Hello World\""
# print(text)
# # Отлючение работы специальных символов:
# path = r"C:\python\name.txt"
# print(path)
# # Форматирование с f:
# userName = "Tom"
# userAge = 37
# user = f"name: {userName}  age: {userAge}"
# print(user)
# # строка - это неизменяемый (immutable) тип
# string = "hello world"
# # string[1] = "R" #Ошибка
# name = "Tom"
# surname = "Smith"
# fullname = name + " " + surname
# print(fullname)
# name = "Tom"
# age = 33
# info = "Name: " + name + " Age: " + str(age)
# print(info)
# # Повторение строки:
# print("a" * 3)
# str1 = "1a"
# str2 = "aa"
# # При сравнении строк принимается во внимание символы и их регистр. 
# # Так, цифровой символ условно меньше, чем любой алфавитный символ. 
# # Алфавитный символ в верхнем регистре условно меньше, чем алфавитные символы в нижнем регистре.
# print(str1 > str2)
# str1 = "Tom"
# str2 = "tom"
# print(str1.lower() == str2.upper())
# # с помощью функции ord() мы можем получить числовое значение для символа в кодировке Unicode:
# print(ord("A"))
# text = "hello world"
# exist = "hello" in text
# print(exist)
# print("hello" not in text)


# Методы строки:
# isalpha(): возвращает True, если строка состоит только из алфавитных символов
# islower(): возвращает True, если строка состоит только из символов в нижнем регистре
# isupper(): возвращает True, если все символы строки в верхнем регистре
# isdigit(): возвращает True, если все символы строки - цифры
# isnumeric(): возвращает True, если строка представляет собой число
# startswith(str): возвращает True, если строка начинается с подстроки str
# endswith(str): возвращает True, если строка заканчивается на подстроку str
# lower(): переводит строку в нижний регистр
# upper(): переводит строку в вехний регистр
# title(): начальные символы всех слов в строке переводятся в верхний регистр
# capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
# lstrip(): удаляет начальные пробелы из строки
# rstrip(): удаляет конечные пробелы из строки
# strip(): удаляет начальные и конечные пробелы из строки
# ljust(width): если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю
# rjust(width): если длина строки меньше параметра width, то слева от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по правому краю
# center(width): если длина строки меньше параметра width, то слева и справа от строки равномерно добавляются пробелы, чтобы дополнить значение width, 
# а сама строка выравнивается по центру
# find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
# replace(old, new[, num]): заменяет в строке одну подстроку на другую
# split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
# partition(delimeter): разбивает строку по разделителю на три подстроки и возвращает кортеж из трех элементов - подстрока до разделителя, разделитель и подстрока после разделителя
# join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель

# string = input("Введите число: ")
# if string.isnumeric():
#     number = int(string)
#     print(number)
# file_name = "hello.py"
# starts_with_hello = file_name.startswith("hello")   
# ends_with_exe = file_name.endswith("exe") 
# string = "   hello  world!  "
# string = string.strip()
# print(string)
# print("iPhone 7:", "52000".ljust(10))
# print("Huawei P10:", "36000".rjust(10))
# print("Huawei P10:", "36000".center(10)) 
# welcome = "Hello world! Goodbye world!"
# index = welcome.find("wor",10)
# print(index)
# index = welcome.find("wor",10,15)
# print(index)
# phone = "+1-234-567-89-10"
# edited_phone = phone.replace("-", " ")
# print(edited_phone)
# edited_phone = phone.replace("-", "", 2)
# print(edited_phone) 
# text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# splitted_text = text.split()
# print(splitted_text)
# splitted_text = text.split(" ", 5)
# print(splitted_text)
# text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# text_parts = text.partition("дуб")
# print(text_parts)
# words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
# sentence = " ".join(words)
# print(sentence)
# sentence = " | ".join(words)
# print(sentence)


# text = "Hello, {first_name}.".format(first_name="Tom")
# print(text)     
# info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
# print(info)
# info = "Name: {0}\t Age: {1}".format("Bob", 23)
# print(info)
# text = "Hello, {0} {0} {0}.".format("Tom")
# print(text)
# text = "Hello, {0} {0} {0}.".format("Tom",23)
# print(text)

# Еще один способ передачи форматируемых значений в строку представляет использование подстановок или специальных плейсхолдеров, на место которых вставляются определенные значения.
# s: для вставки строк
# d: для вставки целых чисел
# f: для вставки дробных чисел. Для этого типа также можно определить через точку количество знаков в дробной части.
# %: умножает значение на 100 и добавляет знак процента
# e: выводит число в экспоненциальной записи
# welcome = "Hello {:s}"
# name = "Tom"
# formatted_welcome = welcome.format(name)
# print(formatted_welcome)
# source = "{:,d} символов"
# print(source.format(5000))
# n = 5000
# source = f"{n:,d} символов"
# print(source)
# number = 23.8589578
# print("{:.3f}".format(number))
# print("{:,.2f}".format(10001.23554))
# number = .12345
# print("{:%}".format(number))
# print("{:.0%}".format(number))
# print(f"{number:%}")       
# print(f"{number:.1%}")
# number = 12345.6789
# print("{:e}".format(number))     
# print("{:.0e}".format(number))
# print(f"{number:e}")     
# print(f"{number:.1e}") 

# Форматирование без метода format
# в начале идет строка, которая содержит те же плейсхолдеры, которые были рассмотрены выше (за исключением плейсхолдера %), после строки ставится знак процента %, 
# а затем список значений, которые вставляются в строку. Фактически знак процента представляют операцию, в результате которой образуется новая строка:
info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)
number = 23.8589578
print("%0.2f  - %e" % (number, number))

# С помощью специальных символов можно задать длину строки при форматировании:
# <N: выравнивает строку по левому краю и дополняет ее пробелами с правой стороны до длины N
# >N: выравнивает строку по правому краю и дополняет ее пробелами с левой стороны до длины N
# ^N: выравнивает строку по центру и дополняет ее пробелами с левой и правой стороны до длины N
# .N: задает точную длину строки. Если в ней больше N символов, то она усекается
str = "Hello World"
print(f"{str:>16}!")     
print(f"{str:<16}!")   
print(f"{str:^16}!")
print(f"{str:.16}!") 
print(f"{str:.5}!") 