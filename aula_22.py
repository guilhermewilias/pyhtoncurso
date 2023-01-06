# Operadores logicos IN  e NOT IN 
# Strings são iteráveis =(navegar item por item.)
# 0 1 2 3 4 5 6 7 8
# G u i l h e r m e
# -9-8-7-6-5-4-3-2-1


var_nome = 'Guilherme'
var_encontrar = input ('Digite o que deseja encontrar : ')


# print (var_nome [2]) # 2 é a letra i [2] / quis checar qual a segunda letra do nome.
# print (var_nome [5]) # 5 é a letra e [5] / quis checar qual a quinta letra do nome. 

# Outra checagem >

print ('G' in var_nome)
print ('k' in var_nome)

print ('\n\n')

# Not in

print ('j' not in var_nome)
print ('G' not in var_nome)

if var_encontrar in var_nome:
    print (f'{var_encontrar} esta entre {var_nome}'  )
else :
    print (f'{var_encontrar} não esta entre {var_nome}')




