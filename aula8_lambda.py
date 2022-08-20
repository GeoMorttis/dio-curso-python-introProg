contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['dog', 'cat', 'chicken', 'wolf']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
divisao = lambda a, b: a / b

print(soma(5, 11))
print(subtracao(10, 3))
print(divisao(33, 3))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda  a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
subtracao = calculadora['subtracao']

print('A soma é: {}'.format(soma(10, 5)))
print('A subtração é: {}'.format(subtracao(10, 7)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))
print('A divisão é: {}'.format(divisao(100, 20)))
