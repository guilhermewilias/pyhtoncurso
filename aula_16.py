# Função do IF / ELIF / ELSE 
# Traduc -> SE / SE NÃO SE / SE NÃO

var_condicao1 = False
var_condicao2 = False
var_condicao3 = False
var_condicao4 = False

if var_condicao1 :
    print ('Código para condição #1') #Não será executada pois é falsa, caso fosse verdadeira, seria executada
elif var_condicao2 :
    print ('Código para condição #2') #Não será executada pois é falsa, caso fosse verdadeira, seria executada
elif var_condicao3 :
    print ('Código para condição #3') #Não será executada pois é falsa, caso fosse verdadeira, seria executada
elif var_condicao4 :
    print ('Código para condição #4') #Não será executada pois é falsa, caso fosse verdadeira, seria executada
else :
    print ('nenhuma condição foi satisfeita') #Foi executada pois na checagem todos deram FALSE, se algum fosse TRUE, executaria a var que foi TRUE.


var_condicao_fora = True

if var_condicao_fora :
    print ('Valido, siga!')
else :
    print ('não valido, saia!')