import time
import sqlite3
import math
import string
from datetime import date

SAIR = "-1"
SUCESSO = 1

conexao = sqlite3.connect('pizzaria.db')

cursor = conexao.cursor()

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
            time.sleep(0.6)
            return 1
            
            
def tela_login():
    print("\n Login")
    checar_login()
    #checar senha no banco de dados
    
def tela_cadastro():
    print("\n Cadastro de Cliente")
    cadastro_cliente()
    #checar nome como não null

    print("\n Cadastro de Endereço")
    cadastro_endereco()
    #checar endereco como não null


def cadastro_cliente():
    in_nome = registrar_nome()
    in_cpf = registrar_cpf()
    in_email = registrar_email()
    in_senha = registrar_senha()
    query = """
    INSERT INTO cliente (nome, cpf, email, senha)
    VALUES (?, ?, ?, ?);
    """
    cursor.execute(query, (in_nome, in_cpf, in_email, in_senha))
    conexao.commit()

def registrar_nome():
    in_nome = None
    while in_nome != "-1":
        in_nome = input("\tNome completo: ")
        if in_nome == "-1":
            print("\nCadastro Cancelado!")
            time.sleep(0.6)
        elif len(in_nome) == 0:
            print("\nNome Inválido!")
            time.sleep(0.6)
        else:
            return in_nome
    tela_inicial()

def registrar_cpf():
    in_cpf = None
    while in_cpf != "-1":
        in_cpf = input("\tCPF: ")
        if in_cpf == "-1":
            print("\nCadastro Cancelado!")
            time.sleep(0.6)
        elif len(in_cpf) != 11 or contem_nao_numericos(in_cpf):
            print("\nCPF Inválido!")
            time.sleep(0.6)
        else:
            return in_cpf
    tela_inicial()

def contem_nao_numericos(input_string):
    for char in input_string:
        if not char.isdigit():
            return True
    return False

def registrar_email():
    in_email = None
    while in_email != "-1":
        in_email = input("\tEmail: ")
        if in_email == "-1":
            print("\nCadastro Cancelado!")
            time.sleep(0.6)
        elif len(in_email) == 0 or nao_contem_arroba(in_email):
            print("\nEmail Inválido!")
            time.sleep(0.6)
        else:
            return in_email
    tela_inicial()

def nao_contem_arroba(input_string):
    for char in input_string:
        if char == '@':
            return False
    return True

def registrar_senha():
    in_senha = None
    while in_senha != "-1":
        in_senha = input("\tSenha: ")
        if in_senha == "-1":
            print("\nCadastro Cancelado!")
            time.sleep(0.6)
        elif len(in_senha) == 0:
            print("\nSenha Inválida!")
            time.sleep(0.6)
        else:
            return in_senha
    tela_inicial()

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

        query3 = """
        SELECT * FROM endereco
        WHERE ID = (SELECT MAX(id) FROM endereco);
        """
        cursor.execute(query3)
        ultimo_endereco_id = cursor.fetchall()

        query4 = """
        UPDATE cliente SET id_endereco = ? WHERE id = ?;
        """
        data = (ultimo_endereco_id[0][0], ultimo_cliente_id[0][0])
        cursor.execute(query4, data)
        conexao.commit()

def checar_login():
    print("\n\t CPF:")
    in_cpf = input()
    print("\n\t Senha:")
    in_senha = input()
    if len(in_cpf)==0 or len(in_senha)==0:
        print("Todos os dados devem ser informados!")
    else:
        query = """
        SELECT id, senha FROM cliente
        WHERE cpf = ?;
        """
        cursor.execute(query, (in_cpf,))
        cliente_id, senha = (cursor.fetchall())[0]

        if(senha == in_senha):
            print("\n\t Qual será o seu pedido?")
            criar_pedido(cliente_id)
            qtde_sabores, pizza_id = tamanho()
            sabor(qtde_sabores, pizza_id)
        else:
            print("Senha inválida!")

def criar_pedido(id_cliente):
    query = """
    INSERT INTO pedido (data, id_cliente)
    VALUES (?, ?);
    """
    print(date.today())
    print(type(date))
    cursor.execute(query, (date.today(), id_cliente))
    conexao.commit()

def tamanho():
    print("\n\t Tamanhos disponíveis:")
    query = """
    SELECT * FROM tamanho
    """
    cursor.execute(query)
    tamanhos = cursor.fetchall()
    for tamanho in tamanhos:
        print(f"\t - {tamanho[1]:4}")
    in_tamanho = input()

    query2 = """
    SELECT id, preco, qtde_sabores FROM tamanho
    WHERE nome = ?;
    """
    cursor.execute(query2, (in_tamanho,))
    tamanho_id, preco, qtde_sabores = (cursor.fetchall())[0]

    print(tamanho_id)
    print(preco)

    query3 = """
    INSERT INTO pizza (id_tamanho, preco)
    VALUES (?, ?);
    """
    cursor.execute(query3, (tamanho_id, preco))
    conexao.commit()

    query4 = """
    SELECT id FROM pizza
    WHERE ID = (SELECT MAX(id) FROM pizza);
    """
    cursor.execute(query4)
    pizza_id = cursor.fetchall()

    return qtde_sabores, pizza_id[0][0]

def sabor(qtde_sabores, pizza_id):
    print(f"\t Escolha até {qtde_sabores} sabor(es)")

    print("\n\t Sabores disponíveis:")
    query = """
    SELECT * FROM sabor
    """
    cursor.execute(query)
    sabores = cursor.fetchall()
    for sabor in sabores:
        print(f"\t - {sabor[1]:4}: {sabor[2]}")
    print(type(qtde_sabores))
    for opcao in range(qtde_sabores):
        in_sabor = input("\t Sabor:")
        query2 = """
        SELECT id, preco FROM sabor
        WHERE nome = ?;
        """
        cursor.execute(query2, (in_sabor,))
        sabor_id, preco = (cursor.fetchall())[0]

        print(pizza_id)
        print(type(pizza_id))
        print(sabor_id)
        print(type(sabor_id))

        query3 = """
        INSERT INTO pedido_sabor (id_pizza, id_sabor)
        VALUES (?, ?);
        """
        cursor.execute(query3, (pizza_id, sabor_id))
        conexao.commit()

while True:
    tela_inicial()