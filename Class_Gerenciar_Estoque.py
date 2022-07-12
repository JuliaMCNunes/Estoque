from Class_Estoque import *
from Class_Entrada import *
from Class_Saida import *
class Gerenciador:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='estoque')
        self.cursorzinho = self.conexao.cursor()
        self.gerenciar = Estoque()
        
    def entrada(self, cod, observacoes, cod_entrada, cod_produtos, info, codi):
        obj_entrada = Entrada(cod, observacoes)
        comando_sql = f'insert into Entrada (observacoes) value ("{obj_entrada.observacoes}")'
        self.cursorzinho.execute(comando_sql)
        self.conexao.commit()
        try:
            comando_sql = f'insert into Entrada_Produtos (cod_entrada, cod_produtos) value ({cod_entrada}, {cod_produtos})'
            self.cursorzinho.execute(comando_sql)
        except:
             print('\nCódigo não encontrado!\n')
        else:
            self.conexao.commit()
            try:
                comando_sql = f'update Produtos set quantidade = {info} where cod = {codi}'
                self.cursorzinho.execute(comando_sql)
            except:
                print('\nCódigo não encontrado!\n')
            else:
                self.conexao.commit()
                           
    def saida(self, cod, observacoes, cod_saida, cod_produtos, info, codi):
        obj_saida = Saida(cod, observacoes)
        comando_sql = f'insert into Saida (observacoes) value ("{obj_saida.observacoes}")'
        self.cursorzinho.execute(comando_sql)
        self.conexao.commit()
        try:
            comando_sql = f'insert into Saida_Produtos (cod_saida, cod_produtos) value ({cod_saida}, {cod_produtos})'
            self.cursorzinho.execute(comando_sql)
        except:
             print('\nCódigo não encontrado!\n')
        else:
            self.conexao.commit()
            try:
                comando_sql = f'update Produtos set quantidade = {info} where cod = {codi}'
                self.cursorzinho.execute(comando_sql)
            except:
                print('\nCódigo não encontrado!\n')
            else:
                self.conexao.commit()

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
