#Declarar
QuantidadeDeHoras:int = 0
ValorPorHora: float = 0.0
Desconto:float = 0.0
NúmeroDeDependentes:int = 0
SalárioBruto:float = 0.0
SalárioFinal:float = 0.0
#Incio
QuantidadeDeHoras = int(input('Insira a quantidade de horas trabalhadas:'))
ValorPorHora = float(input('Insira o valor por hora:'))
Desconto = float(input('Insira o percentual do desconto:'))
NúmeroDeDependentes = int(input('Insira o número de dependentes:'))
SalárioBruto = QuantidadeDeHoras*ValorPorHora
Desconto = (Desconto/100)*SalárioBruto
SalárioFinal = (SalárioBruto-Desconto)+(100*NúmeroDeDependentes)
print ('Esse será o salário:', SalárioFinal)
#Fim