# range можно использовать в качестве счетчика


questions = ['a', 'b', 'c', 'd']
answers = [111, 222, 333, 444]

# индексация списка
for i in range(len(questions)):
    print('i', i)
    print('q',questions[i])
    print('a',answers[i])
