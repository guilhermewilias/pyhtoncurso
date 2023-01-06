# Operador logico NOT
# Usado para inverter expressões.
# not true = FALSE.
# not false = TRUE.

var_senha = input ('Senha : ')

#if var_senha == 'gui' :
#    print ('senha correta')
#else :
#    print ('senha incorreta ')

if not var_senha :
    print ('\n\nvocê não digitou nada.\n\n')


print (not True)
print ('\n\n')
print (not False)
