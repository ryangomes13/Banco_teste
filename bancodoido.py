import sqlite3

conexao = sqlite3.connect("banco_teste.db")
cursor = conexao.cursor()

cursor.execute('DROP TABLE IF EXISTS clientes')

cursor.execute('''
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    cidade TEXT,
    salario INTEGER
)
''')

dados = [
    ('Ana', 30, 'São Paulo', 1500),
    ('Bruno', 25, 'Rio de Janeiro', 2300),
    ('Carlos', 40, None, 5800),
    ('Daniela', 35, 'Belo Horizonte', 3500), 
    ('Eduardo', 28, 'Recife', None)
]

cursor.executemany("INSERT INTO clientes (nome, idade, cidade, salario) VALUES (?, ?, ?, ?)", dados)
conexao.commit()
print("Banco criado com sucesso!")

conexao.close()