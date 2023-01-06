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

var_name = input ('Digite o seu nome --> ') #Como se fosse um scanf (pois o usuario vai digitar o valor)
var_age = input ('Digite a sua idade --> ') #Como se fosse um scanf (pois o usuario vai digitar o valor)

if var_name and var_age :
    print (f'Seu nome é {var_name}') #Exercicio 01
else :
    print ('Desculpe, você não digitou nada...')

if ' ' in var_name : #Exercicio 02
    print ('Existe SIM espaços inseridos no nome digitado...') 
else :
    print ('NÃO existe espaço no nome digitado!')  

print ('O seu nome tem', len (var_name), 'letras') #Exercicio 03 # -----> LEN (VAR_NAME) É PARA SABER QUANTAS LETRAS OU DIGITOS TEM 

print ('A primeira letra do nome digitado é --> ', var_name [0] ) #Exercicio 04

print ('A ultima letra do nome digitado é --> ', var_name [8]) #Exericio 05
 
