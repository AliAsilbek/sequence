# 2. Format
age = [34, 34, 214, 14]
name = 'Ali'

info = 'name {} age {}'.format(name, age)
print(info)

info = f'name {name} age {age}'
print(info)

# 3. неизменяемость строк = строка - константа

# 4. Обьявление
friends = ['max', 'kate', 'jonn']
friends.append('lia')
print(friends)
# индексы
print(friends[1])
print(friends[-1])
# срезы
print(friends[1:])

# операторы вхождения
print('max' in friends)
print(23 in friends)

# Основные методы (действия)
# 1.Добавление, 2.изменение, 3.удаление
# 1.
friends.append('poll')
print(friends)
friends.insert(2, 'maria')
print(friends)
# 2.
friends.append('maria')
friends.remove('maria')
print(friends)

# 3. добавление и удаление по индексу
friends[3] = 'leonid'
print(friends)
del friends[3]
print(friends)

#4. сортировка
print(friends.sort())
friends.reverse()
