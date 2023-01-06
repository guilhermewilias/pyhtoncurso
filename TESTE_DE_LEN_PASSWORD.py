var_user = input ('Digite o nome de usuario cadastrado no site : ')
var_password = input ('Digite a senha do usuario : ')

if len (var_password) >= 5 :
    print ('Acesso liberado!')
else :
    print ('Acesso restrito! Senha sem total de digitos necessarios...')

