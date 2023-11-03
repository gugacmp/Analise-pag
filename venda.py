import random
import time

from pagamentos import pagamento, processo

class Produto():
    def cadastrar():
        global cadastro
        cadastro = str(input('Informe o Produto : '))
    def alterar():
        alterar = str(input(f'Altere o produto {cadastro}'))
    def deleta():
        print('Deletar Item S/N : ')
        delet = str(input('Deseja Deletar Item : '))
        if delet == 'S':
            if cadastro == cadastro:
                deletar = cadastro.remove(f'{cadastro}')
        else:
            print('Item não Deletado !')
        return deletar
class Cliente():
    def cadastrar():
        global cadcliente
        cadcliente = str(input('Informe o cliente : '))
    def alterar():
        altcliente = str(input(f'Alterar Cliente {cadcliente}'))
    def deletar():
        delet = str(input('Deseja Deletar Cliente : '))
        if delet == 'S':
            if cadcliente == cadcliente:
                deletar = cadcliente.remove(f'{cadcliente}')
        else:
            print('Cliente não Deletado !')
        return deletar
        
class Valores():

    def valores():
        global valor
        global somar
        global quantidade
        global desconto
        global pagar
        valor = int(input('Informe o valor : '))
        quantidade = int(input('Informe a quantidade : '))
        somar = valor * quantidade
        desconto = somar / 5
        pagar = somar - desconto
    def resumovenda():
        print(f'Valor Total dos Itens : {somar} R$ | Desconto {desconto} R$ | Valor a Pagar  : {pagar} R$' ) 
        


print('=================================================================')
print('                          PRODUTOS                                ')
print('=================================================================')

print(' ================================================================')
print('|                            MENU                                |')
print('| 1 - Vendas                                                     |')
print('| 2 - Pagamentos                                                 |')
print('| 3 - Sair                                                       |')
print('|________________________________________________________________|')
prod =  int(input("Selecione a opção  :"))
cad = 1
alt = 2
dell = 3
if  prod == 1:
    Produto.cadastrar()
    pagamento()
elif alt == 2:
    pagamento()

elif dell == 3:
    Produto.deleta()

print('__________________________________________________________________')

def resumo():
    print(f'Cliente : {cadcliente}')
    print(f'Produto : {cadastro}')
    Valores.resumovenda()


Cliente.cadastrar()
Valores.valores()
print('__________________________________________________________________')
print('                             RESUMO                               ')
resumo()
time.sleep(1)
processo()
