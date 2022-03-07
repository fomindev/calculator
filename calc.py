# Импортируем все нужное
import time # time.sleep(Задержка) В скобочках вписываем задержку. Пример: time.sleep(3) | Зажержка будет в 3 секунды
from config import *
from pyfiglet import Figlet

# Красивое название | Библиотека - Figlet
# Чтобы сделать такой "Начальный текст" нужно:
# Прописываем "from pyfiglet import Figlet" | и все :)

preview_text = Figlet(font='slant') # Выбираем шрифт 
print(preview_text.renderText(' Calc . exe')) # Сюда вставляем текст "Начального текста"
print("_" * 10) # Просто красивая четочка после "Начального текста". Символ " _ " Умножаем(*) на число которое хотим

# Инфомрация
print('Это калькулятор написанный на Python')
time.sleep(2)

print('Действия в этом калькуляторе:')
print('Сложить(+), Вычесть(-), Умножить(*), Разделить(:)')

# Переменные
one = int(input('Введите ваше первое число: ')) # Вводим первое число
two = int(input('Введите ваше второе число: ')) # Вводим второе число
time.sleep(0.7)

# Еще одна переменная. Тут пользователь будет выбирать действие.
fun = input('Введите функцию: ')
time.sleep(0.5)

# Этот пункт не обязателен, просто прикольно выглядит
print('Подождите идет расчет.')
time.sleep(1.5)
print('Подождите идет расчет. .')
time.sleep(1.5)
print('Подождите идет расчет. . .')
time.sleep(1.7)
print('Расчет окончен! Результат:')
time.sleep(0.3)

# Логика
if fun == "+":
    print(f'{one} + {two} = {one+two}\n {author}') # Случай если пользователь выберет "+"

if fun == "-":
    print(f'{one} - {two} = {one-two}\n {author}') # Случай если пользователь выберет "-"

if fun == '*':
    print(f'{one} * {two} = {one*two}\n {author}') # Случай если пользователь выберет "*"

if fun == ':':
    print(f'{one} : {two} = {one/two}\n {author}') # Случай если пользователь выберет ":"

# Информация
# Переменные:
# {one} - первое число которое вводит пользователь
# {two} - второе число которое ввожит пользователь
# {fun} - Действие которое вводит пользователь

# Переменные из "calc|config.py"
# author = "Тут будет написан текст автора"
# Так же можно вписать свои переменные и импортировать их в код

# Условия
# Условий несколько, каждое условие отвечает за свое действие.
#if fun == '{fun}':
    #print('{one} {fun} {two} = {{one} {fun} {two}}\n {author}')

