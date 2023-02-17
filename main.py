import time

class Cliente:
    def __init__(self):
        pass
    
    @property
    def cpf(self):
        return self.cpf
    
    @cpf.setter
    def set_cpf(self, in_cpf):
        self.cpf = in_cpf

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def set_nome(self, in_nome):
        self.nome = in_nome

    @property
    def email(self):
        return self.email
    
    @email.setter
    def set_email(self, in_email):
        self.email = in_email



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
    print("\n Login")
    print("\n\t CPF:")
    in_cpf = input()
    #checar nome no banco de dados
    in_senha = input()
    #checar senha no banco de dados
    
def tela_cadastro():
    print("\n Cadastro de Cliente")
    
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
    receber_cep()
    receber_nome_rua()
    receber_numero_local()
    receber_complemento()
    receber_descricao()
    
def receber_cep():
    pass

def receber_nome_rua():
    pass

def receber_numero_local():
    pass

def receber_complemento():
    pass

def receber_descricao():
    pass

while True:
    tela_inicial()

