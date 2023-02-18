CREATE TABLE tamanho (
  id INTEGER PRIMARY KEY,
  nome STRING  NOT NULL,
  qtde_sabores INTEGER NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE tipo (
  id INTEGER PRIMARY KEY,
  nome STRING  NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE sabor (
  id INTEGER PRIMARY KEY,
  nome STRING  NOT NULL,
  descricao STRING  NOT NULL,
  id_tipo INTEGER REFERENCES tipo (id),
  preco INTEGER NOT NULL
);

CREATE TABLE borda (
  id INTEGER PRIMARY KEY,
  nome STRING  NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE pizza (
  id INTEGER PRIMARY KEY,
  id_tamanho INTEGER REFERENCES tamanho (id),
  id_sabor INTEGER REFERENCES sabor (id),
  id_borda INTEGER REFERENCES borda (id),
  preco INTEGER NOT NULL
);

CREATE TABLE acompanhamentos (
  id INTEGER PRIMARY KEY,
  id_tipo_acompanhamento INTEGER REFERENCES tipo_acompanhamentos (id),
  nome STRING  NOT NULL,
  descricao STRING  NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE tipo_acompanhamentos (
  id INTEGER PRIMARY KEY,
  tipo STRING  NOT NULL
);

CREATE TABLE cliente (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cpf INTEGER NOT NULL,
  nome STRING  NOT NULL,
  email STRING  NOT NULL,
  senha INTEGER NOT NULL,
  id_endereco INTEGER REFERENCES endereco (id),
  id_pedido INTEGER REFERENCES pedido (id)
);

CREATE TABLE pedido (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  preco INTEGER NOT NULL,
  data DATETIME NOT NULL
);

CREATE TABLE entregador (
  id INTEGER PRIMARY KEY,
  cpf INTEGER NOT NULL,
  nome STRING  NOT NULL,
  placa STRING  NOT NULL
);

CREATE TABLE endereco (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cep INTEGER NOT NULL,
  nome_rua STRING  NOT NULL,
  numero INTEGER NOT NULL,
  complemento STRING,
  descricao STRING  NOT NULL
);

CREATE TABLE pedido_pizza (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_pizza INTEGER REFERENCES pizza (id),
  id_pedido INTEGER REFERENCES pedido (id),
  valor INTEGER NOT NULL
);

CREATE TABLE pedido_acompanhamentos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_acompanhamento INTEGER REFERENCES acompanhamentos (id),
  id_pedido INTEGER REFERENCES pedido (id),
  valor INTEGER NOT NULL
);

CREATE TABLE pedido_entrega (
  id_entrega INTEGER REFERENCES entrega (id),
  id_entregador INTEGER REFERENCES entregador (id),
  preco INTEGER NOT NULL
);

INSERT INTO tamanho (
                          id,
                          nome,
                          qtde_sabores,
                          preco
                      )
                      VALUES (
                          1,
                          'Pequeno',
                          1,
                          20
                      );

INSERT INTO tamanho (
                          id,
                          nome,
                          qtde_sabores,
                          preco
                      )
                      VALUES (
                          2,
                          'Médio',
                          2,
                          30
                      );

INSERT INTO tamanho (
                          id,
                          nome,
                          qtde_sabores,
                          preco
                      )
                      VALUES (
                          3,
                          'Grande',
                          3,
                          40
                      );

INSERT INTO tipo (
                          id,
                          nome,
                          preco
                      )
                      VALUES (
                          1,
                          'Tradicional',
                          10
                      );

INSERT INTO tipo (
                          id,
                          nome,
                          preco
                      )
                      VALUES (
                          2,
                          'Especial',
                          20
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          1,
                          'Calabresa',
                          'Mussarela, molho, calabresa e orégano',
                          1,
                          5
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          2,
                          'Bacon',
                          'Mussarela, molho, bacon e orégano',
                          1,
                          5
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          3,
                          'Caipira',
                          'Mussarela, molho, frango, milho e orégano',
                          1,
                          5
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          4,
                          'Milho',
                          'Mussarela, molho, milho e orégano',
                          1,
                          5
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          5,
                          'Especial',
                          'Mussarela, molho, bacon, frango, batata palha, catupiry e orégano',
                          2,
                          10
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          6,
                          'Catupalha',
                          'Mussarela, molho, catupiry, batata palha e orégano',
                          2,
                          10
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          7,
                          'Funghi',
                          'Molho de tomate, mussarela, funghi especial, queijo tipo catupiry e orégano',
                          2,
                          10
                      );

INSERT INTO sabor (
                          id,
                          nome,
                          descricao,
                          id_tipo,
                          preco
                      )
                      VALUES (
                          8,
                          'Mignon',
                          'Molho de tomate, mussarela, mignon e orégano',
                          2,
                          10
                      );
  
INSERT INTO borda (
                          id,
                          nome,
                          preco
                      )
                      VALUES (
                          1,
                          'Cheddar',
                          5
                      );

INSERT INTO borda (
                          id,
                          nome,
                          preco
                      )
                      VALUES (
                          2,
                          'Chocolate',
                          5
                      );

INSERT INTO borda (
                          id,
                          nome,
                          preco
                      )
                      VALUES (
                          3,
                          'Catupiry',
                          5
                      );

INSERT INTO tipo_acompanhamentos (
                          id,
                          tipo
                      )
                      VALUES (
                          1,
                          'Refrigerante'
                      );

INSERT INTO tipo_acompanhamentos (
                          id,
                          tipo
                      )
                      VALUES (
                          2,
                          'Cerveja'
                      );

INSERT INTO tipo_acompanhamentos (
                          id,
                          tipo
                      )
                      VALUES (
                          3,
                          'Suco'
                      );

INSERT INTO acompanhamentos (
                          id,
                          id_tipo_acompanhamento,
                          nome,
                          descricao,
                          preco
                      )
                      VALUES (
                          1,
                          1,
                          'Coca-cola',
                          '800 ml',
                          '8'
                      );

INSERT INTO acompanhamentos (
                          id,
                          id_tipo_acompanhamento,
                          nome,
                          descricao,
                          preco
                      )
                      VALUES (
                          2,
                          2,
                          'Heineken',
                          '300 ml',
                          '8'
                      );

INSERT INTO acompanhamentos (
                          id,
                          id_tipo_acompanhamento,
                          nome,
                          descricao,
                          preco
                      )
                      VALUES (
                          3,
                          3,
                          'Suco de Laranja',
                          '300 ml',
                          '8'
                      );

INSERT INTO entregador (
                          id,
                          cpf,
                          nome,
                          placa
                      )
                      VALUES (
                          1,
                          '447.664.040-09',
                          'Will Herondale',
                          'KLM-0998'
                      );

INSERT INTO entregador (
                          id,
                          cpf,
                          nome,
                          placa
                      )
                      VALUES (
                          2,
                          '397.425.100-67',
                          'James Carstairs',
                          'FAY-1526'
                      );