import pyodbc

dados_conexao = "Driver={SQL Server};Server=DESKTOP-L79M8K7\SQLEXPRESS;Database=bd_PDV;"
conexão = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

# Criando um cursor para executar as consultas SQL
cursor = conexão.cursor()
