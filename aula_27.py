# Flag (Bandeira) = Marcar um local
# None = Não tem valor 
# IS e NOT IS = É e NÃO É (Tipoo, Valor, Identidade)
# ID = Identidade

var_1 = "a" 
var_2 = "a" #mesmo ID que var_1 pois são coisas iguais.
print (id (var_1))
print (id(var_2))

var_3 = "b"
var_4 = "c"
print (id (var_3))
print (id (var_4)) #ID diferentes pois não são coisas iguais.

print ("\n")

#CONDIÇÕES :

var_condição = True

if var_condição :
    print ("Faça algo...")
else :
    print ("Não faça algo.")

# IS e IS NOT :
var_teste_none = None
var_teste_none = True

print (var_teste_none, var_teste_none is None) #Is 
print (var_teste_none, var_teste_none is not None) # Is not