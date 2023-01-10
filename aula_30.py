# Repetições
# While (Enquanto) -> Repetição.
# Executa uma ação enquanto uma condição for verdadeira.
# Loop infinito -> Quando o código não tem fim. 

# var_condição = True

var_contador = 0

while var_contador < 10 : #Contar até 10.
    var_contador +=1  #Sempre contar de 1 em 1. 
    print (var_contador) #Printar a variavel var_contandor (0), porém dentro do bloco WHILE.  
    if var_contador == 7 : #Se var_contador tiver 7
        break # Parar no 7.

print ("Sequencia numerica terminada.")  

print ("\n")

var_contador2 = 0 
while var_contador2 <= 100 : #Contar até 100. 
    var_contador2 +=1  #Contar de 1 em 1. 

    if var_contador2 == 6 : # Quando o var_contador2 chegar no numero 6, irá mostrar a mensagem : 
        print ("Não vou mostrar o número 6! Olhem a função CONTINUE.")
        continue # Função para continuar o loop do WHILE.

    if var_contador2 >= 10 and var_contador2 <= 27 : #Quando chegar nos numeros entre 10 e 27 :
        print ("Não vou mostar o :", var_contador2) #Não vai mostrar os numeros entre 10 e 27, e sim esta mensagem. 
        continue # Função para continuar o loop do WHILE. 

    print (var_contador2)
    if var_contador2 == 40 : #Quando chegar no numero 40
        break # Parar a contagem (ou seja, o contador não vai chegar em 100, por que o BREAK parou no 40 por conta do IF a cima do BREAK.)



 