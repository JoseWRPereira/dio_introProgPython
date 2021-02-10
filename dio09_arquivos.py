
def escreverArquivo(texto):
    diretorio = '/home/josewrpereira/MOOC/digital-Innovation-One/dio09w.txt'
    #diretorio = '~/MOOC/digital-Innovation-One/dio09w.txt'##Não funciona
    arq = open(diretorio, 'w')
    arq.write(texto)
    arq.close()

def criarArquivo( arquivo ):
    arq = open(arquivo, 'w')
    arq.write('')
    arq.close()

def atualizarArquivo(texto):
    arq = open('dio09.txt', 'a')
    arq.write(texto)
    arq.close()

def lerArquivo( nomeArquivo ):
    arq = open(nomeArquivo, 'r')
    txt = arq.read()
    print(txt)

def atualizarNotas( arquivo, texto ):
    arq = open(arquivo, 'a')
    arq.write(texto+'\n')
    arq.close()

def mediaNotas( arquivo ):
    arq = open( arquivo, 'r')
    alunoNota = arq.read()
    arq.close()
    alunoNota = alunoNota.split('\n')
    alunoNota.pop(-1)
    print(alunoNota)
    bibnotas = []
    for x in alunoNota:
        lista = x.split(',')
        print(lista)
        aluno = lista[0]
        lista.pop(0)
        soma = 0
        for i in lista:
            soma += int(i)
        media = soma/len(lista)
        bibnotas.append({aluno:media})
    return( bibnotas )


if __name__ == '__main__':
    #escreverArquivo('Escrevendo...')
    #atualizarArquivo('\nAtualizando...')
    #lerArquivo('dio09.txt')
    criarArquivo('notas.txt')
    atualizarNotas('notas.txt', 'José,10,9,8,7')
    atualizarNotas('notas.txt', 'William,9,9,8,9')
    media = mediaNotas('notas.txt')
    print( media )
    #lerArquivo('notas.txt')