#Declarar
AnoDeNascimento:int = 0
AnoAtual:int = 0
Idade:int = 0
DaquiA17Anos:int = 0 
#Incio
AnoDeNascimento = int(input('Coloque o ano de nascimento:'))
AnoAtual = int(input('Coloque o ano atual:'))
Idade = AnoAtual - AnoDeNascimento
DaquiA17Anos = Idade + 17
print ('Aqui está a idade atual:', Idade, 'e a idade daqui a 17 anos:', DaquiA17Anos)
#Fim