# объявляем переменную типы людей
types_of_people = 10
# объявляем  переменную x берём значение переменных в области видимости
# и подставляем в стороку
x = f"Существует {types_of_people} типов людей"
binary = 'Python'
do_not = 'нет'
y = f"Те , кто понимает {binary}, и те, кто - {do_not}."
print(x)
print(y)
print(f"Я сказал: {x}")
print(f"А ещё я сказал : '{y}'")
hilarious = False
joke_evalution = "Разве это не смешно ?! {} "
print(joke_evalution.format(hilarious))
w = "Это часть строки слева ..."
e = "а это справа."
print(w + e)