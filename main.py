Nome = input('Digite seu nome: ')
Salario = float(input('Salario: '))
Simular = int(input('Quantos meses deseja simular: '))
Gastos = {}


while True:
    Gastos_fixos =input("Nome do gasto(Ou sair): ").lower()
        
    if Gastos_fixos == 'sair':
        break
        
    valor = float(input(f'Valor de {Gastos_fixos}: '))    
    Gastos[Gastos_fixos]= valor
        
print('\n--- Gasto Cadastrados ---')
for gastos_fixos, valor in Gastos.items(): 
   print(f'{gastos_fixos}: R$:{valor:.2f}')
        
total = sum(Gastos.values())
print(f'\nTotal de gastos: R$ {total:.2f}')
    

Restante =  Salario - total 
print(f'O que sobra por mês: R$ {Restante}')

# statos funanceiros 

if Restante < 0:
    print('Tá vivendo no vermelho')
elif Restante == 0:
    print('Ta sobrevivendo por aparelhos')
else:
    acumulado = 0
    
    print('\n --- Simulador mês a mês ---')
    for mes in range(0, Simular, +1):
        acumulado += Restante
        print(f'Mês {mes}: acumulado = R$ {acumulado:.2f}')
    
    print(f'\nTotal guardado em {Simular} meses: R$ {acumulado:.2f}')
    
# classificação final

if acumulado > 10000:
    print('Rico detectado')
elif acumulado >= 5000:
    print('Ta indo bem')
else:
    print('Da pra melhorar')