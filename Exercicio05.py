import math
#Declarar
A: int = 0
B: int = 0
C: int = 0
X1: int = 0
X2: int = 0
#Incio
A = int(input('Defina um valor para A da equação de 2° Grau:'))
B = int(input('Defina um valor para B da equação de 2° Grau:'))
C = int(input('Defina um valor para C da equação de 2° Grau:'))
X1 = (-B +(math.sqrt(B**2 -(4*A*C))))/(2*A)
X2 = (-B -(math.sqrt(B**2 -(4*A*C))))/(2*A)
print ('Aqui estão as raízes:',X1, X2)
#Fim
