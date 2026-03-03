#Declarar
Tempo:float = 0.0
Velocidade:float = 0.0
Litros:float = 0.0
Distância:float = 0.0
#Incio
Tempo = float(input('Insira o tempo da viagem:'))
Velocidade = float(input('Insira a velocidade média da viagem:'))
Distância = Velocidade*Tempo
Litros = Distância/12
print('Aqui está a quantidade de litros gastos na viagem:',Litros)
#Fim