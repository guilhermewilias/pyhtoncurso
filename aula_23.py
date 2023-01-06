# Interpolação básica de strings em py
# %s = VALOR STRING
# %f = VALOR FLOAT 
# % (VARIAVEIS INTERPOLADAS)

var_name = 'guilherme'
var_preco = 100.47382
var_interpolacao = '%s, o preço é %.2f' % (var_name, var_preco)

print (var_interpolacao)