import math
#Declarar
Cateto1:int = 0
Cateto2:int = 0
Hipotenusa:int = 0
#Incio
Cateto1 = int(input('Insira o valor do cateto 1:'))
Cateto2 = int(input('Insira o valor do cateto 2:'))
Hipotenusa = math.sqrt((Cateto1**2)+(Cateto2**2))
print ('Aqui está o valor da Hipotenusa:', Hipotenusa)
#Fim