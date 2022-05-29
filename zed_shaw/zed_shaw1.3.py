formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("раз","два","три","четыре"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Спят в конюшне пони,",
    "начал пес дремать,",
    "только мальчик Джонни",
    "не ложится спать!"
))

days = "Пн Вт Ср Чт Пт Сб Вс"
months = "Янв\nФевр\nМарт\nАпр\nМай\nИюнь\nИюль\nАвг"

print("Это дни недели: ", days)
print("А это месяцы: ", months)

print("""
Что же тут творится ?
Используются три двойные кавычки.
Мы можем набрать текста сколько угодно.
Даже 4 строки,5 или 6
""")