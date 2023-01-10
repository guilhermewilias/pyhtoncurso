# FUNÇÃO WHILE DENTRO DE WHILE :

quantidade_linhas = 5
quantidade_colunas = 5

contador_linhas = 1
contador_colunas = 1

while contador_linhas <= quantidade_linhas :
    while contador_colunas <= quantidade_colunas :
        print (f'{contador_linhas=}, {contador_colunas=}')
        contador_colunas += 1
        contador_linhas += 1


print ("\n")
print ("Sequencia de linhas e colunas chegaram ao final ! ")