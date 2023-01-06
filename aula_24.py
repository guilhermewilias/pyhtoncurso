# Formatação básica de strings.

# %s = string
# %d = int
# %f = float
# . <numero de digitos apos o ponto>f
# (Caractere)(<>^)(Quantidade)
# > = Direita
# < = Esquerda
# ^ = Centro
# Sinal = + -]
# Por exemplo : 0>-100, .1f

var_variavel = 'ABC'
print (f'{var_variavel}')
print (f'{var_variavel : >10}') # Vão ter 10 caracteres de ESPAÇO antes do abc (esquerda)
print (f'{var_variavel :$>10}') # Vão ter 10 caracteres de $ antes do abc (esquerda) 