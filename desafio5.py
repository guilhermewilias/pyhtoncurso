def contar_pares_meias(meias):
  pares = 0
  while len(meias) > 0:
    

    meia = meias[0]
    meias = meias[1:]
    

    if meia in meias:
      

      meias.remove(meia)
      

      pares += 1
 
  return pares