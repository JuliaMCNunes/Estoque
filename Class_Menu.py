from Class_Estoque import * 
from Class_Gerenciar_Estoque import * 

class Menu:
    def __init__(self):
        catalogo = Estoque()
        catalogo1 = Gerenciador()
        catalogo1.gerenciar = catalogo
        
        while True:
            print('====================================================='
                    '\nInforme a opção desejada:'                            
                    '\n-----------------------------------------------------'                                                       
                    '\n1 - Cadastrar fabricante'                             
                    '\n-----------------------------------------------------'                                                       
                    '\n2 - Cadastrar produto'                                
                    '\n-----------------------------------------------------'                                                       
                    '\n3 - Procurar produto'                                 
                    '\n-----------------------------------------------------'                                                       
                    '\n4 - Alterar informações'                   
                    '\n-----------------------------------------------------'
                    '\n5 - Deletar cadastros'
                    '\n-----------------------------------------------------'                                                      
                    '\n6 - Efetuar abastecimento de produtos no estoque'      
                    '\n-----------------------------------------------------'                                                       
                    '\n7 - Efetuar retirada de produtos no estoque'          
                    '\n-----------------------------------------------------'                                                       
                    '\n8 - Ver movimentação de estoque'                      
                    '\n-----------------------------------------------------'                                                       
                    '\n9 - Ver as entradas de produtos no estoque'           
                    '\n-----------------------------------------------------'                                                       
                    '\n10 - Ver as saidas de produtos no estoque'             
                    '\n-----------------------------------------------------'                                                       
                    '\n0 - Sair\n'                                           
                    '=====================================================')
            selecao = input(': ')
            
            if selecao == '1':
                codigo = None
                nome = input('\nInforme o nome do fabricante: ')
                cnpj = input('Informe o CNPJ do fabricante: ')
                razao_social = input('Informe a razão social do fabricante: ')
                catalogo.cadastrar_fabricantes(codigo, nome, cnpj, razao_social)
                
            elif selecao == '2':
                cod = None
                codigo_fabricante = int(input('\nInforme o código do fabricante do produto: '))
                descricao = input('Informe a descrição do produto: ')
                valor = float(input('Informe o valor unitário do produto: '))
                quantidade = 0
                catalogo.cadastrar_produtos(cod, descricao, codigo_fabricante, valor, quantidade)
                
            elif selecao == '3':
                print('\nDigite 0 para listar todos os produtos cadastrados no sistema.'
                      '\nDigite um código especifico para listar o produto correspondente.')
                codi = int(input(': '))
                catalogo.mostrar_itens(codi)
                
            elif selecao == '4':
                print('\nDigite 1 para alterar as informações de produtos cadastrados.'
                      '\nDigite 2 para alterar as informações de fabricantes cadastrados.')
                selecionar = input(': ')
                if selecionar == '1':
                    codi = input('\nInforme o código do produto que deseja alterar: ')
                    atributo = input('Informe o atributo que deseja alterar: ')
                    info = input('Informe a nova informação: ')
                    catalogo.alterar_informacoes(selecionar, atributo, info, codi)
                elif selecionar == '2':
                    codi = input('\nInforme o código do fabricante que deseja alterar: ')
                    atributo = input('Informe o atributo que deseja alterar: ')
                    info = input('Informe a nova informação: ')
                    catalogo.alterar_informacoes(selecionar, atributo, info, codi)
                    
            elif selecao == '5':
                print('\nDigite 1 para deletar cadastro de produto.'
                      '\nDigite 2 para deletar cadastro de fabricante.')
                selecionar = input(': ')
                if selecionar == '1':
                    codi = int(input('\nInforme o código do produto a ser deletado do sistema: '))
                    catalogo.excluir_informacoes(selecionar, codi)
                elif selecionar == '2':
                    codi = int(input('\nInforme o código do fabricante a ser deletado do sistema: '))
                    catalogo.excluir_informacoes(selecionar, codi)
                    
            elif selecao == '6':
                cod = None
                observacoes = input('Adicione alguma observação a entrada do produto: ')
                cod_entrada = int(input('Informe o código do pedido: '))
                cod_produtos = int(input('Informe o código do produto requerido: '))
                codi = int(input('Confirme o código do produto: '))
                info = int(input('Informe a quantidade do produto: '))
                catalogo1.entrada(cod, observacoes, cod_entrada, cod_produtos, info, codi)
                
            elif selecao == '7':
                codi = int(input('\nInforme o código do produto que está sendo retirado do estoque: '))
                info = int(input('Informe a quantidade do produto: '))
                catalogo1.saida(info, codi)
                
            #elif selecao == '8':
                #catalogo1.imprimir_t()
                
            #elif selecao == '9':
                #catalogo1.imprimir_e()
                
            #elif selecao == '10':
                #catalogo1.imprimir_s()
                
            elif selecao == '0':
                break
            
            else:
                print('\nOpção inválida!\n')
