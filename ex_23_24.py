# Exercicio

# Peça ao usuário para digitar seu nome. 
# Peça ao usuário para digitar sua idade.
# Se nome e idade foram digitados, exiba :

# 1-) Seu nome é {Name}
# 2-) Seu nome contém ou nãoo espaços
# 3-) Seu nome tem {n} letras
# 4-) A primeira letra do seu nome é {Letra}
# 5-) A ultima letra do seu nome é {Letra}

# Caso não for digitado em nome ou idade, exiba : "Desculpe, você não preencheu os campos."

var_name = input ('Digite o seu nome --> ')
var_age = input ('Digite a sua idade --> ')

#Exericicio 01 :
print (f'Seu nome é {var_name}')

#Exercicio 02 :
if ' ' in var_name :
    print ('Tem espaço no nome!')
else :
    print ('Não tem espaço no nome!')

#Exercicio 03 :
print ('O seu nome tem', len (var_name), 'letras')

#Exericio 04 :
print ('A primeira letra do nome digitado é --> ', var_name [0] )

#Exercicio 05 :
print ('A ultima letra do nome digitado é --> ', var_name [8])

# Caso não digite nada no nome e idade
if var_name == '' or var_age == '':
    print ('Desculpe, você não preencheu os campos!')




