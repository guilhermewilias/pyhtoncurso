# Constante = Variaveis que não irão mudar
# Nada que vai mudar -> ESCREVER EM MAIUSCULO (A VARIAVEL !)
# Muitas condições no mesmo IF = RUIM~
# Contagem de complexidade = RUIM. 

# EXEMPLOS PARA ENTENDER CONSTANTE :

var_velocidade = 61 # Velocidade do ATUAL do carro, em minusculo, então pode mudar.
var_local_carro = 101 #km # Local ATUAL em que o carro está, em minusculo, então pode mudar.

var_RADAR_1 = 60 # Velocidade máxima do radar, em MAIUSCULO, então não pode mudar.

var_LOCAL_1 = 100 # Local onde o radar está, em MAIUSCULO, então não pode mudar.

var_RADAR_RANGE = 1 # Distancia onde o radar pega, em MAIUSCULO, então não pode mudar.



var_velocidade_passando_radar_1 = var_velocidade > var_RADAR_1
var_carro_multado_radar_1 = var_local_carro >= (var_LOCAL_1 - var_RADAR_1)
 
if var_velocidade_passando_radar_1 :
    print ("Velocidade do carro atingiu vel. máxima permitida no radar 1.")

print ('\n')

if var_carro_multado_radar_1 and var_velocidade_passando_radar_1 :
    print ("Carro multado no radar 1!")

# if var_velocidade_passando_radar_1
#    print ('Carro passou da velocidade permitida no radar 1.')
     
#if var_local_carro >= (var_LOCAL_1 - var_RADAR_RANGE) and \
#        var_local_carro <= (var_LOCAL_1 + var_RADAR_1) and \
#           var_velocidade > var_RADAR_1 :
#        print ('Carro multado em radar 1')

print ("\n")

    
