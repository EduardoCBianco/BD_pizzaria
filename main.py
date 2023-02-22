import time
import sqlite3
import math
import string
from datetime import date
import random

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
            return 1
        
        case '2':
            tela_login()
            return 1

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
    
    tela_inicial()


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
    if len(in_cep)==0 or len(in_nome_rua)==0 or len(in_numero)==0:
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
    cliente_id = checar_cpf()
    checar_senha(cliente_id)

    print("\n\t Qual será o seu pedido?")
    pedido_id = criar_pedido(cliente_id)
    numero_pizzas = input("\n\t Quantidade de pizzas: ")
    total_pizzas = []
    for pizza in range(int(numero_pizzas)):
        qtde_sabores, pizza_id, preco_tamanho = tamanho()
        preco_sabor = sabor(qtde_sabores, pizza_id)
        preco_borda = borda(pizza_id)
        preco_pizza = total_pizza(pedido_id, pizza_id, preco_tamanho,\
                        preco_sabor, preco_borda)
        total_pizzas.append(preco_pizza)
    print("\n\t Deseja acompanhamentos? ('1' para sim, '0' para não)")
    acomp = int(input())
    if acomp == 1:
        preco_bebida = acompanhamentos(pedido_id)
    else:
        preco_bebida = 0
    total = sum(total_pizzas) + preco_bebida
    print(f"\t O total do seu pedido é de {total}")
    print("\n\t Prosseguir? ('1' para seguir, '0' para cancelar)")
    fim = int(input())
    if fim == 0:
        tela_inicial()
    else:
        preco_entrega = entrega(pedido_id)
        print(f"\t O total da entrega é de {preco_entrega}")
        print(f"\t O total com entrega é de {total + preco_entrega}")
        print(f"\t Pedido realizado com sucesso!")
        finalizar_pedido(pedido_id, total + preco_entrega)

def checar_cpf():
    in_cpf = None
    while in_cpf != "-1":
        in_cpf = input("\n\t CPF:")
        if in_cpf == "-1":
            print("\nLogin Cancelado!")
            time.sleep(0.6)
        elif len(in_cpf) == 0:
            print("\nCampo Vazio!")
            time.sleep(0.6)
        else:
            query = """
            SELECT id FROM cliente
            WHERE cpf = ?;
            """
            cursor.execute(query, (in_cpf,))
            cliente_id = cursor.fetchall()
            if len(cliente_id) == 0:
                print("\nCliente não cadastrado!")
                time.sleep(0.6)
            else:
                return cliente_id[0][0]
    tela_inicial()

def checar_senha(id_cliente):
    in_senha = None
    while in_senha != "-1":
        in_senha = input("\n\t Senha:")
        if in_senha == "-1":
            print("\nLogin Cancelado!")
            time.sleep(0.6)
        elif len(in_senha) == 0:
            print("\nCampo Vazio!")
            time.sleep(0.6)
        else:
            query = """
            SELECT senha FROM cliente
            WHERE id = ?;
            """
            cursor.execute(query, (id_cliente,))
            senha_cadastrada = cursor.fetchall()[0][0]
            if in_senha != senha_cadastrada:
                print("\nSenha Incorreta!")
                time.sleep(0.6)
            else:
                return True
    tela_inicial()

def criar_pedido(id_cliente):
    query = """
    INSERT INTO pedido (data, id_cliente)
    VALUES (?, ?);
    """
    cursor.execute(query, (date.today(), id_cliente))
    conexao.commit()

    query2 = """
    SELECT id FROM pedido
    WHERE ID = (SELECT MAX(id) FROM pedido);
    """
    cursor.execute(query2)
    pedido_id = cursor.fetchall()
    return pedido_id[0][0]

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
    tamanho_id, preco_tamanho, qtde_sabores = (cursor.fetchall())[0]

    query3 = """
    INSERT INTO pizza (id_tamanho)
    VALUES (?);
    """
    cursor.execute(query3, (tamanho_id,))
    conexao.commit()

    query4 = """
    SELECT id FROM pizza
    WHERE ID = (SELECT MAX(id) FROM pizza);
    """
    cursor.execute(query4)
    pizza_id = cursor.fetchall()

    return qtde_sabores, pizza_id[0][0], preco_tamanho

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

    preco_max = 0
    for opcao in range(qtde_sabores):
        in_sabor = input("\t Sabor:")
        if len(in_sabor) == 0:
            break
        query2 = """
        SELECT id, preco FROM sabor
        WHERE nome = ?;
        """
        cursor.execute(query2, (in_sabor,))
        sabor_id, preco = (cursor.fetchall())[0]

        if preco > preco_max:
            preco_max = preco
        query3 = """
        INSERT INTO pedido_sabor (id_pizza, id_sabor)
        VALUES (?, ?);
        """
        cursor.execute(query3, (pizza_id, sabor_id))
        conexao.commit()
    preco_sabor = preco_max
    return preco_sabor

def borda(pizza_id):
    print(f"\t Escolha a borda: ")

    print("\n\t Sabores disponíveis:")
    query = """
    SELECT * FROM borda
    """
    cursor.execute(query)
    bordas = cursor.fetchall()
    for borda in bordas:
        print(f"\t - {borda[1]:4}")

    in_borda = input("\t Borda:")
    query2 = """
    SELECT id, preco FROM borda
    WHERE nome = ?;
    """
    cursor.execute(query2, (in_borda,))
    borda_id, preco_borda = (cursor.fetchall())[0]

    query4 = """
    UPDATE pizza SET id_borda = ? WHERE id = ?;
    """
    data = (borda_id, pizza_id)
    cursor.execute(query4, data)
    conexao.commit()

    return preco_borda

def total_pizza(pedido_id, pizza_id, preco_tamanho, preco_sabor, preco_borda):
    total_pizza = preco_tamanho + preco_sabor + preco_borda
    query = """
    INSERT INTO pedido_pizza (id_pizza, id_pedido, valor)
    VALUES (?, ?, ?);
    """
    cursor.execute(query, (pizza_id, pedido_id, total_pizza))
    conexao.commit()
    return total_pizza

def acompanhamentos(pedido_id):
    numero_acomp = input("\n\t Quantidade de acompanhamentos: ")
    total_acomp = []
    for acomp in range(int(numero_acomp)):
        preco_bebida = bebida(pedido_id)
        total_acomp.append(preco_bebida)
    return sum(total_acomp)

def bebida(pedido_id):
    print("\n\t Bebidas disponíveis:")
    query = """
    SELECT * FROM acompanhamentos
    """
    cursor.execute(query)
    bebidas = cursor.fetchall()
    for bebida in bebidas:
        print(f"\t - {bebida[2]:4}")
    in_bebida = input()

    query2 = """
    SELECT id, preco FROM acompanhamentos
    WHERE nome = ?;
    """
    cursor.execute(query2, (in_bebida,))
    bebida_id, preco_bebida = (cursor.fetchall())[0]

    query3 = """
    INSERT INTO pedido_acompanhamentos (id_acompanhamento, id_pedido, valor)
    VALUES (?, ?, ?);
    """
    cursor.execute(query3, (bebida_id, pedido_id, preco_bebida))
    conexao.commit()
    return preco_bebida

def entrega(pedido_id):
    query = """
    SELECT nome FROM entregador
    WHERE id = ?;
    """
    id_entregador = random.randint(1, 2)
    cursor.execute(query, (id_entregador,))
    nome_entragdor = (cursor.fetchall())[0]
    print(f"\t A entrega será feita por: {nome_entragdor[0]}")

    valor_entrega = random.randrange(4, 10)
    query2 = """
    INSERT INTO pedido_entrega (id_pedido, id_entregador, preco)
    VALUES (?, ?, ?);
    """
    cursor.execute(query2, (pedido_id, id_entregador, valor_entrega))
    conexao.commit()
    return valor_entrega

def finalizar_pedido(pedido_id, valor_total):
    query = """
    UPDATE pedido SET preco = ? WHERE id = ?;
    """
    data = (valor_total, pedido_id)
    cursor.execute(query, data)
    conexao.commit()

while True:
    tela_inicial()