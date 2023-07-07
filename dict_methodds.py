# словари
name = 'max'
age = 20
has_car = True

friend = (name, age, has_car)

friend_inverse = (age, has_car, name)

# словарь, обьявление
friend = {
    'name': 'max',
    'has_car': True,
    'age': 20
}
print(type(friend))

# В словарях используют не индексы и "ключи" - name, has car, age

print(friend['age'])
print(friend['has_car'])

# Функции

print(len(friend))

# Оператор на вхождение
# проверяет по ключам

print('name' in friend)

# Методы ( действия с словарем): 1.добавить, 2.удалить, 3.изменить
# добавить, изменить

print(friend)

friend['has_wife'] = False
friend['has_wife'] = True # существующий ключ заменяется
print(friend)
# Удалить
del friend['has_wife']
print(friend)
# Методы: получить значение
# Ключи
print(list(friend.keys()))
# Значение
print(friend.values())
# пары кюч значение - кортежи
print(friend.items())

print(20 in friend)
print(20 in friend.values())