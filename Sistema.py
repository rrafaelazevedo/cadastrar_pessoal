from Pessoa import Endereco, PessoaFisica, Pessoa, PessoaJuridica
from datetime import date, datetime

# lista global para armazenar pessoas físicas
lista_pf = []
lista_pj = []

def main():
    while True:
        opcao = int(input('Digite uma opção: 1 - Pessoa Física | 2 - Pessoa Juridica | 0 - Sair '))

        if opcao == 1:
            while True:
                opcao_pf = int(input('Digite uma opção: 1 - Cadastrar pessoa física | 2 - Listar pessoa física | 3 - Remover CPF da lista | 4 - Atualizar cadastro na lista | 0 - Voltar ao menu anterior '))
                
                # cadastrar uma pessoa física
                if opcao_pf == 1:
                    nova_pf = PessoaFisica()
                    novo_end_pf = Endereco()
                    nova_pf.nome = input('Digite o nome da pessoa física: ')
                    nova_pf.cpf = input('Digite o CPF: ')
                    nova_pf.rendimento = float(input('Digite o rendimento mensal (somente números): '))
                    data_nascimento = input('Digite a data de nascimento (dd/MM/yyyy): ')  # solicita data de nascimento
                    nova_pf.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - nova_pf.data_nascimento).days // 365  #calcula a idade da pessoa

                    if idade >= 18:
                        print('A pessoa tem mais de 18 anos')
                    else:
                        print('A pessoa tem menos de 18 anos. Retornando ao menu...')
                        continue  # retorna ao início do looping

                    # cadastro de endereço_pf
                    novo_end_pf.logradouro = input('Digite o logradouro: ')
                    novo_end_pf.numero = input('Digite um número: ')
                    end_comercial = input('Este endereço é comercial? (S/N): ')
                    novo_end_pf.endereco_comercial = end_comercial.strip().upper() == 'S'
                    nova_pf.endereco = novo_end_pf
                    lista_pf.append(nova_pf)                    
                    print('Cadastro realizado com sucesso!')

                # listar pessoas físicas
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'\nNome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data de Nascimento: {cada_pf.data_nascimento.strftime("%d/%m/%Y")}')
                            print(f'Imposto a ser pago: R${cada_pf.calcular_imposto(nova_pf.rendimento):.2f}')
                            print('Digite qualquer tecla para continuar...')
                            input()
                    else:
                        print('LISTA VAZIA []')
                
                
                # remover pessoa física da lista
                elif opcao_pf == 3:                    
                    remover_cpf = input('Insira o CPF da pessoa a ser removida: ')                    
                    cpf_encontrado = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == remover_cpf:
                            lista_pf.remove(cada_pf)
                            cpf_encontrado = True
                            print('Pessoa Física removida!')
                            break
                    
                    if not cpf_encontrado:
                        print('Pessoa não listada no database.')    

                # atualizar dados da pessoa física
                elif opcao_pf == 4:
                    atualizar_cpf = input('Digite o CPF da pessoa que deseja atualizar: ')
                    pessoa_atualizada = None

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == atualizar_cpf:
                            pessoa_atualizada = cada_pf
                            break

                    if pessoa_atualizada:
                        while True:
                            print('Escolha o que deseja atualizar:')
                            print('1 - Nome')
                            print('2 - Rendimento mensal')
                            print('3 - Data de nascimento')
                            print('4 - Endereço')
                            print('0 - Voltar')
                            opcao_atualizar = int(input('Digite a opção desejada: '))
                            
                            if opcao_atualizar == 1:
                                pessoa_atualizada.nome = input(f'Nome ({pessoa_atualizada.nome}): ') or pessoa_atualizada.nome
                                print('Nome atualizado com sucesso!')
                                
                            
                            elif opcao_atualizar == 2:
                                pessoa_atualizada.rendimento = float(input(f'Rendimento mensal ({pessoa_atualizada.rendimento}): ') or pessoa_atualizada.rendimento)
                                print('Rendimento mensal atualizado com sucesso!')

                            elif opcao_atualizar == 3:
                                data_nascimento = input(f'Data de Nascimento (dd/MM/yyyy) ({pessoa_atualizada.data_nascimento.strftime("%d/%m/%Y")}): ')
                                if data_nascimento:
                                    pessoa_atualizada.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                                print('Data de nascimento atualizada com sucesso!')

                            elif opcao_atualizar == 4:
                                novo_endereco = pessoa_atualizada.endereco
                                novo_endereco.logradouro = input(f'Logradouro ({novo_endereco.logradouro}): ') or novo_endereco.logradouro
                                novo_endereco.numero = input(f'Número ({novo_endereco.numero}): ') or novo_endereco.numero
                                end_comercial = input(f'Endereço comercial (S/N) ({ "S" if novo_endereco.endereco_comercial else "N"}): ')
                                if end_comercial:
                                    novo_endereco.endereco_comercial = end_comercial.strip().upper() == 'S'
                                print('Endereço atualizado com sucesso!')

                            elif opcao_atualizar == 0:
                                break

                            else:
                                print('Opção inválida, por favor digite uma das opções indicadas.')

                    else:
                        print('Pessoa Física não encontrada.')
                
                

                # sair do menu atual
                elif opcao_pf == 0:
                    print('Retornando ao menu anterior')
                    break
                
                else:
                    print('Opção inválida, por favor digite uma das opções indicadas.')
                

        elif opcao == 2:                
                opcao_pj = int(input('Digite uma opção: 1 - Cadastrar pessoa jurídica | 2 - Listar pessoa jurídica | 3 - Remover CNPJ da lista | 4 - Atualizar cadastro na lista | 0 - Voltar ao menu anterior '))
                if opcao_pj == 1:
                    nova_pj = PessoaJuridica()
                    novo_end_pj = Endereco()
                    nova_pj.nome = input('Digite o nome da pessoa jurídica: ')
                    nova_pj.cnpj = input('Digite o CNPJ: ')
                    nova_pj.rendimento = float(input('Digite o rendimento mensal da companhia (somente números): '))
                    # cadastro de endereço_pj
                    novo_end_pj.logradouro = input('Digite o logradouro: ')
                    novo_end_pj.numero = input('Digite um número: ')   
                    end_comercial_pj = input('Seu endereço é comercial? S/N: ')
                    novo_end_pj.endereco_comercial = end_comercial_pj.strip().upper() == 'S'
                    nova_pj.endereco = novo_end_pj
                    lista_pj.append(nova_pj)            
                    print('Cadastro realizado com sucesso!')

                # listar pessoas físicas
                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f'\nNome: {cada_pj.nome}')
                            print(f'Endereço: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}')
                            print(f'CNPJ: {cada_pj.cnpj}')                           
                            print(f'Imposto a ser pago: R${cada_pj.calcular_imposto(nova_pj.rendimento):.2f}')

                            
                            print('Digite qualquer tecla para continuar...')
                            input()
                    else:
                        print('LISTA VAZIA []')
                
                
                # remover pessoa física da lista
                elif opcao_pj == 3:                    
                    remover_cnpj = input('Insira o CNPJ da pessoa a ser removida: ')
                    
                    cnpj_encontrado = False

                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == remover_cnpj:
                            lista_pj.remove(cada_pj)
                            cpf_encontrado = True
                            print('Pessoa Jurídica removida!')
                            break
                    
                    if not cnpj_encontrado:
                        print('Pessoa jurídica não listada no database.')
                
                # atualizar dados da pessoa juridica
                elif opcao_pj == 4:                    
                    atualizar_cnpj = input('Digite o CNPJ da pessoa jurídica que deseja atualizar: ')
                    pessoa_atualizada = None

                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == atualizar_cnpj:
                            pessoa_atualizada = cada_pj
                            break
                    
                    if pessoa_atualizada:
                        while True:
                            print('Escolha o que deseja atualizar:')
                            print('1 - Nome')
                            print('2 - Rendimento mensal')
                            print('3 - Endereço')
                            print('0 - Voltar')
                            opcao_atualizar = int(input('Digite a opção desejada: '))

                            if opcao_atualizar == 1:
                                pessoa_atualizada =


        elif opcao == 0:
            print('Obrigado por utilizar o nosso sistema!')
            break
    
        else:
            print('Opção inválida! Por favor, digite uma das opções válidas.')

if __name__ == '__main__':
    main()  # chama a função principal
