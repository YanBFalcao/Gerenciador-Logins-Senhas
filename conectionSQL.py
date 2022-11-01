import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-T9A7732;"
    "Database=crmUsuarios;" 
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida!")

comando = conexao.cursor()

# ================================================= ~~ =================================================
#                                                FUNÇÕES
# ================================================= ~~ =================================================

#inserir = """ INSERT INTO Vendas (id_venda, cliente, produto, data_venda, preco, quantidade) VALUES 
#	(2, 'Yan', 'Headphones', '23/10/2022', 250, 1) """

#comando.execute(inserir)
#comando.commit()

# ================================================= ~~ =================================================
#                                                FUNÇÕES
# ================================================= ~~ =================================================