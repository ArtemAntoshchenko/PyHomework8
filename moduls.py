import random
import secrets
import math
import locale
from decimal import Decimal, ROUND_HALF_EVEN
from dataclasses import dataclass
import timeit

# number = random.randint(20, 35)
# print(number)
# # randrange(start, stop, step)
# number = random.randrange(2, 10)
# number = random.randrange(10)
# print(number)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)  
# random_number = random.choice(numbers)
# print(random_number)


# characters='fawengluindf124'
# password = "".join(secrets.choice(characters) for i in range(8))
# print(password)
# # secrets.randbelow(0, exclusive_upper_bound) - возвращает случайное целое число в диапазоне
# secure_number = secrets.randbelow(100)
# print(secure_number)
# # secrets.randbits(k): возвращает неотрицательное целое число с k случайными битами
# number = secrets.randbits(7)    
# print(number)

# # secrets.token_bytes([nbytes=None]): возвращает случайную строку байтов, содержащую nbytes байтов. Если nbytes равно None или не указано, используется разумное значение по умолчанию
# token = secrets.token_bytes(None)
# print(token)
# print(type(token))
# # secrets.token_hex([nbytes=None]): возвращает случайную текстовую строку в шестнадцатеричном формате
# # Строка содержит nbytes случайных байтов, каждый байт преобразован в две шестнадцатеричные цифры
# # Если nbytes равно None или не указано, используется разумное значение по умолчанию
# token = secrets.token_hex(16)
# print(token)
# # secrets.token_urlsafe([nbytes=None]): возвращает случайную текстовую строку, безопасную для URL, содержащую nbytes случайных байтов
# # Текст закодирован в Base64, поэтому в среднем каждый байт дает приблизительно 1,3 символа
# # Если nbytes равно None или не указано, используется разумное значение по умолчанию
# url_token = secrets.token_urlsafe(16)
# print(url_token)

# # pi и e - встроенные значения в math
# number = math.log(10, math.e)
# print(number)
# radius = 30
# area = math.pi * math.pow(radius, 2)
# print(area)

# n1 = math.pow(2, 3)
# print(n1)
# print(math.sqrt(9)) 
# print(math.ceil(4.56))  
# print(math.floor(4.56))  
# print(math.degrees(3.14159)) 
# print(math.radians(180))  
# print(math.cos(math.radians(60)))  
# print(math.sin(math.radians(90)))   
# print(math.tan(math.radians(0)))    
# print(math.log(8,2))    
# print(math.log10(100))    


# print(locale.getlocale())
# locale.setlocale(locale.LC_ALL, "en")
# number = 12345,6789
# formatted1 = locale.format_string("%.02f", number)
# print(formatted1)
# print(locale.getlocale())
# # format_string(str, num): подставляет число num вместо плейсхолдера в строку str
# # Применяются следующие плейсхолдеры:
# # d: для целых чисел
# # f: для чисел с плавающей точкой
# # e: для экспоненциальной записи чисел
# formatted2 = locale.format_string("%f", number)
# print(formatted2)   
# formatted3 = locale.format_string("%.2f", number)
# print(formatted3)   
# formatted4 = locale.format_string("%d", number)
# print(formatted4)  
# formatted5 = locale.format_string("%e", number)
# print(formatted5)   
# money = 234.678
# formatted6 = locale.currency(money)
# print(formatted6)


# number = Decimal("0.1")
# number = number + number + number
# print(number)
# number = Decimal("0.100")
# number = number + 2
# print(number)
# # number = Decimal("0.1")
# # number = number + 0.1   # здесь возникнет ошибка
# # print(number)
# number = Decimal("0.555678")
# print(number.quantize(Decimal("1.00")))  
# number = Decimal("0.999")
# print(number.quantize(Decimal("1.00")))   
# number = Decimal("10.025")      # 2 - ближайшее четное число
# print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))
# # ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше
# # ROUND_HALF_DOWN: округляет число в сторону повышения, если после него идет число больше 5
# # ROUND_05UP: округляет 0 до единицы, если после него идет число 5 и выше
# # ROUND_CEILING: округляет число в большую сторону вне зависимости от того, какое число идет после него
# # ROUND_FLOOR: не округляет число вне зависимости от того, какое число идет после него


# @dataclass
# class Person:
#     name: str
#     age: int
# # Вместо:
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
 
# #     def __repr__(self):
# #         return f"Person(name={self.name!r}, age={self.age!r}"
     
# #     def __eq__(self, other):
# #         if other.__class__ is self.__class__:
# #             return (self.name, self.age) == (other.name, other.age)
# #         return NotImplemented
# tom = Person("Tom", 38)
# bob = Person("Bob", 42)
# tomas = Person("Tom", 38)
# print(tom) 
# print(tom == tomas)     
# print(tom == bob)       

# @dataclass(unsafe_hash=True, order=True)
# class Person:
#     name: str
#     age: int =12
#     def __repr__(self):
#         return f"Person. Name: {self.name}  Age: {self.age}"
# tom = Person("Tom")
# print(tom.__hash__()) 
# print(tom)
# # Базовые параметры:
# # init: если равно True, то генерируется функция __init__(). По умолчанию равно True
# # repr: если равно True, то генерируется функция __repr__(), которая возвращает строковое представление объекта. По умолчанию равно True
# # eq: если равно True, то генерируется функция __eq__(), которая сравнивает два объекта. По умолчанию равно True
# # order: если равно True, то генерируются функции __lt__ (операция <), __le__ (<=), __gt__ (>), __ge__ (>=), которые применяются для упорядочивания объектов. По умолчанию равно False
# # unsafe_hash: если равно True, то генерируется функция __hash__(), которая возвращает хеш объекта. По умолчанию равно False

# # Хотя data-классы предназначены прежде всего для хранения различных данных, но также в них можно определять поведение с помощью дополнительных функций:
# @dataclass
# class Person:
#     name: str
#     age: int
 
#     def say_hello(self):
#         print(f"{self.name} says hello")
# tom = Person("Tom", 38)
# tom.say_hello()  


# timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
# stmt: действие(функция), выполнение которой надо измерить. По умолчанию это pass
# setup: код, который запускается перед запуском stmt. По умолчанию он также равен pass. Обычно применяется для импорта модулей, необходимых для выполнения нашего кода.
# timer: запускаемый таймер в виде объекта timeit.Timer. Обычно он имеет некоторое разумное значение по умолчанию, поэтому обычно этот параметр оставляют по умолчанию
# number: количество выполнений stmt, которое надо измерить. По умолчанию действие stmt выполняется 1000000.
# globals: устанавливает пространство имен, в котором выполняется код
def sum():
    result = 0
    for i in range(10000): 
        result +=i
    return result
execution_time = timeit.timeit(lambda: sum(), number=100)
print("Время выполнения функции sum:", execution_time)
action = "a=10; b=12; a+b"
print(timeit.timeit(action))

start = timeit.default_timer()
print("Start time:", start)
sum()
print("Execution time:", timeit.default_timer() - start)