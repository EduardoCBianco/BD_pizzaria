import time

def tela_inicial():
    print("\n E.M. Pizzaria")
    print("\n\t 1 - Fazer Cadastro")
    print("\t 2 - Login")
    opcao_tela = input()

    if (trocar_tela(opcao_tela)):
        tela_inicial()
        

def trocar_tela(opcao):

    #checar_opcao_tela(opcao)

    match opcao:
        case '1':
            tela_cadastro()

        case '2':
            tela_login()

        case _:
            print("\n Opção Inválida!")
            time.sleep(0.8)
            return 1
            
            
def tela_login():
    in_nome = input()
    #checar nome no banco de dados
    in_senha = input()
    #checar senha no banco de dados
    
def tela_cadastro():
    print("\n\t Cadastro de Cliente")
    
    print("\n\t Nome Completo:")
    cadastro_nome()
    #checar nome como não null

    print("\n\t CPF:")
    cadastro_cpf()
    #checar cpf como não null

    print("\n\t E-mail:")
    cadastro_email()
    #checar email como não null
    
    print("\n\t Endereco:")
    cadastro_endereco()
    #checar endereco como não null


def cadastro_nome():
    in_nome = input()

def cadastro_cpf():
    in_cpf = input()

def cadastro_email():
    in_email = input()

def cadastro_endereco():
    in_email = input()
    

while True:
    tela_inicial()

