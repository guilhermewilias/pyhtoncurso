# Operadores logicos : And (e) / or (ou) / not (não)
# Quando se usa AND - Todas as expressões precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor - considerados false (que já vi)

# Sisteminha nada haver :

var_entrada = input ('[E]ntrar ou [S]air:   ')
var_senha_digitada = input ('Digite a Senha : ')
var_senha_permitida = 'essanãoéaminhasenha'

if var_entrada == 'E' and var_senha_digitada == var_senha_permitida :
    print ('você entrou.')
else :
    print ('você saiu')



