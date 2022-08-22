import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/workspace/dio-curso-python-introProg/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    lista_media = []
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    for x in aluno_nota:
        #print(x)
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media
        #print(sum(lista_notas))

def copia_arquivo(nome_arquivo):            # Função para copiar arquivo em outro diretório.
    shutil.copy(nome_arquivo, 'C:/workspace/')

def move_arquivo(nome_arquivo):             # Função para mover arquivo de uma pasta para outra.
    shutil.move(nome_arquivo, 'C:/workspace/')

if __name__ == '__main__':
    #move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha. \n')     # Esta alinha é para escrever novo texto, se o texto não existir ele criará, se existir ele sobrescreverá todo o texto existente.
    #aluno = 'Pablo, 7, 7, 8, 10\n'
    #atualizar_arquivo('notas.txt', aluno)     # Esta linha é sempre usada para atualizar texto, não duplicar, mudar texto aqui e rodar programa.
    #ler_arquivo('teste.txt')
