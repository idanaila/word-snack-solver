import itertools


def lista():
    items = []
    with open(r'D:\Python\cuvinte\cuvinte.txt', encoding='utf-8') as input:
        for line in input:
            items.extend(line.strip().split(','))
        return items


lista1 = lista()

a = input("Introdu literele( fără spațiu intre ele ): ")
b = int(input("Cate litere are cuvantul: "))

l = []

for word in itertools.permutations(a, b):
    l.append(''.join(word))

for word in l:
    if word in lista1:
        print(word)