# Formatação de strings com o metodo FORMAT.
# .format = FUNÇÃO FORMAT 
# var_formato = 'a= {}, b = {}, c = {}' .format (var_a, var_b, var_c) 
# irá imprimir : a= A, b = B, c = 1.1
# obs... {:.2f} = número de decimais que queremos apresentar.

var_a = 'gui wilias'
var_b = 'tem dezenove anos'
var_c = 1.1
var_formato = 'a= {}, b = {}, c = {:.2f}' .format (var_a, var_b, var_c)

print (var_formato)

