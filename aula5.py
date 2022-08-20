lista = [1, 3, 7, 5, 4, 2, 15, 12]
list_animal = ['dog', 'cat', 'elephant', 'eagle', 'puma', 'tiger']
#print(list_animal[1])
#new_list = list_animal * 3
#print(new_list)

lista.sort()                 # comando para ordenar itens na array.
list_animal.sort()          # comando para ordenar itens na array.
print(lista)
print(list_animal)

if 'lobo' in list_animal:
    print(list_animal)
    print('There is a wolf in the list.')
else:
    print(list_animal)
    print('There is no wolf in the list. Will be included.')
    list_animal.append('wolf')      # adiciona item na array.
    print(list_animal)
    list_animal.reverse()           # reverte a ordem dos itens na array.
    print(list_animal)

list_animal.pop(1)      # remove item por local na array.
print(list_animal)

list_animal.remove('elephant')      # remove item pelo nome
print(list_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(list_animal))
tupla_animal = tuple(list_animal)
print(type(tupla_animal))
print(tupla_animal)
list_numerical = list(tupla)
print(type(list_numerical))
list_numerical[0] = 100
print(list_numerical)
