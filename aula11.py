
arquivo = open('teste.txt', 'r')
lista = [1, 10]
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero.')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética.')
except IndexError:
    print('Erro ao acessar um indice inválido da lista.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção.')
finally:
    print('Sempre executa.')
    print('Fechando arquivo.')
    arquivo.close()
