# list
friends = ['max', 'kate', 'john', 'leo']

for friend in friends:
    hello = f'hello, {friend}'
    print(hello)
# str
friend = 'Максим Александрович Попов'
for letter in friend:
    print(letter)
# dic
friend = {
    'name': 'max',
    'has_car': True,
    'age': 20
}
# по ключам:
for key in friend:
    print(key)
    print(friend[key])
# по значениям
for val in friend.values():
    print(val)

for key, val in friend.items():
    print(key)
    print(val)

name, age, has_car = ('max', 23, True)
