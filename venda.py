import random
import time
import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np

print("==============================================================")
print("                          VENDA                               ")
print("==============================================================")

def pagamento():
    print("|_____________________________________________________________|")
    print("|                   Meios de Pagamentos                       |")
    global dinheiro
    dinheiro = 1
    print('| 1 - Dinheiro                                                |')
    global cartaocredito
    cartaocredito = 2
    print('| 2 - Carão de Crédito                                        |')
    global cartaodebito
    cartaodebito = 3
    print('| 3 - Débito                                                  |')
    global pix
    pix = 4
    print('| 4 - Pix                                                     |')
    global boleto
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
    global aprovado
    aprovado = 1
    print('| Aprovado                                                    |')
    global analise
    analise = 2
    print('| Analise                                                     |')
    global rejeitado
    rejeitado = 3
    print('| Rejeitado                                                   |')
    print('|_____________________________________________________________|')
    
 
    y = random.randint(2,3)
    for i in tqdm (range (100),
                colour='#FFD700',
               desc="Verificando Status...",
               ascii=False, ncols=80):
               time.sleep(0.03)
    time.sleep(2)
    if y  == 1:
        print(f'Staus : {aprovado} - Apravado')     
    elif y == 2:
        print(f'Status : {analise} - Analise') 
    elif y == 3:
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

print(f'Forma de pagamento : {dinheiro}')

datas = pd.date_range('20230605', periods=4, freq= 'M')
datas2 = pd.date_range('20231024', periods=4, freq= 'D')

df2 = pd.DataFrame({" CODIGO":range(4),
                    #"DATA":pd.Timestamp('20231024'),
                    "COMPRA":datas,
                    "PARCELAS":pd.Series(random.randint(2, 8) , index=list(range(4)), dtype='float32'),
                    "QNT":np.array([3]*4, dtype='int32'),
                    "PAGAMENTO":pd.Categorical([dinheiro, cartaocredito, pix, cartaodebito]),
                    "LOJA":'VEST PE CALÇADOS',
                    "VENDA":datas2,
                    "TOTAL" : pd.Series(random.randint(2,8) * np.array([3]*4)),
                    })

print(df2)


print(" =============================================================")
