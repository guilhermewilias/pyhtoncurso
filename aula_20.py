# Operadores logicos : And (e) / or (ou) / not (não)
# Quando se usa AND - Todas as expressões precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor - considerados false (que já vi)

# AULA DE _OR_ :
# if (var_entrada == 'E' or var_entrada == 'e')

# Sisteminha nada haver :

var_entrada = input ('[E]ntrar ou [S]air:   ')
var_senha_digitada = input ('Digite a Senha : ')
var_senha_permitida = '123'

if (var_entrada == 'E' or var_entrada == 'e') and var_senha_digitada == var_senha_permitida :
    print ('você entrou.')
else :
    print ('você saiu')