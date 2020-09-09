import shutil
def escrever(texto):
    arquivo = open('teste.text', 'w')
    # diretorio = 'C:/projetos/teste.text'
    # arquivo = open(diretorio, 'w')

    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.text', 'a')
    arquivo.write(texto)
    arquivo.close()

# def copia_arquivo(nome_arquivo) ---> para copia arquivos
#     import shutil
#     shutil.copy(nome_arquivo, 'C:/projetos/globallabs/')

# def move_arquivo(nome_arquivo)
#     shutil.move(nome_arquivo, 'C:/projetos/globallabs/')

# def media_notas(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     aluno_nota = arquivo.read()
#     print(aluno_nota)
#     aluno_nota = aluno_nota.split('\n')
#     for x in aluno_nota:
#         print(x)


# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)

if __name__ == '__main__':
    # copia_arquivo('notas.txt')
    # move_arquivo('notas.txt')
    # media_notas('notas.txt')
    # escrever('Primeira linha.\n')
    atualizar_arquivo('Terceira linha\n')
    #  ler_arquivo('teste.txt')