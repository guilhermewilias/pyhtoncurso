# Introdução a FStrings (formatação de strings)


# inserir o f {} na string, para puxar algum valor de alguma outra variavel ja declarada em outra variavel :
# por exemplo --> var_linha_1 = f'{var_nome} = guilherme wilias 
# :.2f --> É o numero de decimais que vc quer mostrar para o user ... :.2f = 1.76, :.1f = 1.8
# Então a varivel "var_linha_1 = f'{var_nome} tem {var_altura:.2f} de altura'" irá mostrar : 
# guilherme wilias tem 1.76 de altura

var_nome = 'guilherme wilias'
var_altura = 1.76
var_peso = 65
var_imc = var_peso / var_altura **2
var_linha_1 = f'{var_nome} tem {var_altura:.2f} de altura'

print (var_linha_1)