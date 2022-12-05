# Usando a função input para coletar dados do usuário.
# Apenas para exibir no terminal 

# input('Qual seu nome? ')

var_nome = input ('Qual teu nome? ')
var_num_1 = int (input ('Digite um numero inteiro : ')) #Fizemos uma conversão para INT.
var_num_2 = int (input ('Digite outro numero inteiro : ')) #Fizemos uma conversão para INT.


print (f'O seu nome é {var_nome=}')
print (f'O 1º Numero digitado foi {var_num_1=}')
print (f'O 2º Numero digitado foi : {var_num_2=}')
print (f'A soma dos numeros digitados foi : {var_num_1 + var_num_2}')

