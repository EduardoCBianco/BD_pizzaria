import time
import sqlite3
import math
conexao = sqlite3.connect('pizzaria.db')

cursor = conexao.cursor()

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
    print("\n Login")
    print("\n\t CPF:")
    in_cpf = input()
    #checar nome no banco de dados
    in_senha = input()
    #checar senha no banco de dados
    
def tela_cadastro():
    print("\n Cadastro de Cliente")
    cadastro_cliente()
    #checar nome como não null

    print("\n Cadastro de Endereço")
    cadastro_endereco()
    #checar endereco como não null


def cadastro_cliente():
    in_nome = input("   Nome completo: ")
    in_cpf = input("   CPF: ")
    in_email = input("   Email: ")
    in_senha = input("   Senha: ")
    if len(in_nome)==0 or len(in_cpf)==0 or len(in_email)==0 or len(in_senha)==0:
        print("Todos os dados devem ser informados!")
    else:
        query = """
        INSERT INTO cliente (nome, cpf, email, senha)
        VALUES (?, ?, ?, ?);
        """
        cursor.execute(query, (in_nome, in_cpf, in_email, in_senha))
        conexao.commit()


def cadastro_endereco():
    in_cep = input("   CEP: ")
    in_nome_rua = input("   Nome da rua: ")
    in_numero = input("   Número: ")
    in_complemento = input("   Complemento: ")
    in_descricao = input("   Descrição: ")
    if len(in_cep)==0 or len(in_nome_rua)==0 or len(in_numero)==0 or \
        len(in_descricao)==0:
        print("Todos os dados devem ser informados!")
    else:
        query = """
        INSERT INTO endereco (cep, nome_rua, numero, complemento, descricao)
        VALUES (?, ?, ?, ?, ?);
        """
        cursor.execute(query, (in_cep, in_nome_rua, in_numero, in_complemento, in_descricao))
        conexao.commit()

        query2 = """
        SELECT * FROM cliente
        WHERE ID = (SELECT MAX(id) FROM cliente);
        """
        cursor.execute(query2)
        ultimo_cliente_id = cursor.fetchall()
        print("Ultimo cliente")
        print(ultimo_cliente_id[0][0])

        query3 = """
        SELECT * FROM endereco
        WHERE ID = (SELECT MAX(id) FROM endereco);
        """
        cursor.execute(query3)
        ultimo_endereco_id = cursor.fetchall()
        print("Ultimo endereco")
        print(ultimo_endereco_id[0][0])

        query4 = """
        UPDATE cliente SET id_endereco = ? WHERE id = ?;
        """
        data = (ultimo_endereco_id[0][0], ultimo_cliente_id[0][0])
        cursor.execute(query4, data)
        conexao.commit()
    
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