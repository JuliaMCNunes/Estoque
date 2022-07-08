from Class_Estoque import *
from datetime import datetime

class Gerenciador:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='estoque')
        self.cursorzinho = self.conexao.cursor()
        self.gerenciar = Estoque()
        
    def entrada(self):
        
        
        
        
        abast = input('\nInforme o código do produto: ')
        for i in range(len(self.gerenciar.lista_produtos)):
            if self.gerenciar.lista_produtos[i].cod == abast:
                en = int(input('Informe a quantidade do produto: '))
                self.gerenciar.lista_produtos[i].quantidade += en
                data = datetime.today().strftime('%d-%m-%Y %H:%M')
                self.movimentacao.append(f'Entrada de {en} unidades do produto ' + self.gerenciar.lista_produtos[i].cod + f' realizada no dia {data}')
                self.entrada_p.append(f'Entrada de {en} unidades do produto ' + self.gerenciar.lista_produtos[i].cod + f' realizada no dia {data}')
            else:
                cont += 1
                if cont == len(self.gerenciar.lista_produtos):
                    print('Código não encontrado!')
                    
    def saida(self):
        cont = 0
        retira = input('\nInforme o código do produto: ')
        for i in range(len(self.gerenciar.lista_produtos)):
            if self.gerenciar.lista_produtos[i].cod == retira:
                sa = int(input('Informe a quantidade do produto: '))
                if self.gerenciar.lista_produtos[i].quantidade > sa:
                    self.gerenciar.lista_produtos[i].quantidade -= sa
                    data = datetime.today().strftime('%d-%m-%Y %H:%M')
                    self.movimentacao.append(f'Saida de {sa} unidades do produto ' + self.gerenciar.lista_produtos[i].cod + f' realizada no dia {data}')
                    self.saida_p.append(f'Saida de {sa} unidades do produto ' + self.gerenciar.lista_produtos[i].cod + f' realizada no dia {data}')
                else:
                    print('O valor solicitado excede a quantidade no estoque.')
            else:
                cont += 1
                if cont == len(self.gerenciar.lista_produtos):
                    print('Código não encontrado!')

    def imprimir_t(self):
        for i in self.movimentacao:
            print('\n ', i)
            print('')

    def imprimir_e(self):
        for i in self.entrada_p:
            print('\n ', i)
            print('')
            
    def imprimir_s(self):
        for i in self.saida_p:
            print('\n ', i)
            print('')
