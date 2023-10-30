import random
import time
import datetime
from tqdm import tqdm 

print("==============================================================")
print("                          VENDA                               ")
print("==============================================================")

def pagamento():
    print("|_____________________________________________________________|")
    print("|                   Meios de Pagamentos                       |")
    dinheiro = 1
    print('| 1 - Dinheiro                                                |')
    cartaocredito = 2
    print('| 2 - Carão de Crédito                                        |')
    cartaodebito = 3
    print('| 3 - Débito                                                  |')
    pix = 4
    print('| 4 - Pix                                                     |')
    boleto = 5
    print('| 5 - Boleto                                                  |')
    print('|_____________________________________________________________|')

    x = int(input("Informa a opção de Pagamento : "))
    if x == 1 :
        print(f'Pagamento : {dinheiro} - Dinheiro')
    elif x == 2 :
        print(f'Pagamento : {cartaocredito} - Cartão Crédito')
    elif x == 3 :
        print(f'Pagamento : {cartaodebito} - Débito')
    elif x == 4 :
        print(f'Pagamento : {pix} - Pix')
    elif x == 5 :
        print(f'Pagamento : {boleto} - Boleto')

def processo():
    print(" =============================================================")
    print('                           STATUS                              ')
    aprovado = 1
    print('| Aprovado                                                    |')
    analise = 2
    print('| Analise                                                     |')
    rejeitado = 3
    print('| Rejeitado                                                   |')
    print('|_____________________________________________________________|')

    x = random.randint(1,3)
    for i in tqdm (range (100),
                colour='#FFD700',
               desc="Verificando Status...",
               ascii=False, ncols=80):
               time.sleep(0.03)
    time.sleep(2)
    if x  == 1:
        print(f'Staus : {aprovado} - Apravado')     
    elif x == 2:
        print(f'Status : {analise} - Analise') 
    elif x == 3:
        print(f'Status : {rejeitado} - Rejeitado')      
    now = datetime.datetime.now()
    print(f'Atualizado : {now}')
    

for i in tqdm (range (100),
                colour='CYAN',
               desc="Conectando...",
               ascii=False, ncols=80):
               time.sleep(0.03)


pagamento()
processo()



print(" =============================================================")