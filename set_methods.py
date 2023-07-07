# set
# set набор уникальных данных
# обьявление
office = {'max', 'kate', 'john', 'leo', 'leo'}

print(type(office))
print(office)

# 1 уникальность
office = ['max', 'kate', 'john', 'leo', 'leo']

print(set(office))

# операции со множествами
office = {'max', 'kate', 'john', 'leo', 'leo'}
freelance = {'max', 'kate', 'poll'}
print(office - freelance)
print(freelance - office)
print(freelance & office)
print(office | freelance)
