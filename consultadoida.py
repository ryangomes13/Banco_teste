import sqlite3
import pandas as pd

conexao = sqlite3.connect("banco_teste.db")

print("Banco conectado com sucesso!")
print("Digite consultas SQL ou 'sair' para encerrar.\n")

while True:
    comando = input("SQL > ")

    if comando.strip().lower() == "sair":
        print("Encerrando conexão...")
        break

    try:
        if comando.strip().lower().startswith("select"):
            df = pd.read_sql_query(comando, conexao)
            print(df)
        else:
            cursor = conexao.cursor()
            cursor.execute(comando)
            conexao.commit()
            print(f"Comando executado com sucesso.")
    except Exception as e:
        print(f"ERRO: {e}")

conexao.close()