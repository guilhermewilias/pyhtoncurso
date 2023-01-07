# Exercicio 01 -) Faça um programa ue peça ao usuário para digitar um número inteiro, informe se este numero é par ou impar.
#                 Caso o usuario não digite um número inteiro, informa ao mesmo ue o número digitado pelo user não é inteiro.

print ("Exercicio 01 -)")

var_num_int = input ("Digite um numero inteiro : ")

if var_num_int % 2 == 0:
    print ("O numero digitado é par!")
else :
   print ("O numero digitado é impar!")



# Exercicio 02 -) Faça um programa que pergunte ao usuário a hora,e baseando-se no horário descrito, faça uma saldação apropriada.

print ("Exercicio 02 -) ")

var_horario = input ("Que horas são? ")

if var_horario < 12 :
    print ("Entendi, tenha um bom dia!")
elif var_horario < 18 : # USO IMPORTANTE DO ELIF!!!
    print ("Entendi, tenha uma boa tarde!")
else :
    print ("Tenha uma boa noite")


# Exercicio 03 -) Faça um programa que peça o primeiro nome do usuario. Se conter :
#                 4 Letras = Curto
#                 5,6 Letras = Médio
#                7 ou mais = Grande

print  ("Exercicio 03 -) ")

var_user = input ("Digite seu nome : ")

if len (var_user) <= 4 :
    print ("Seu nome é curto.")
if len (var_user) == 5 or len (var_user) == 6 :
    print ("Seu nome é médio.")
if len (var_user) >= 7 :
    print ("Seu nome é grande.") 


 

    

