import pandas as pd
import plotly.express as px


# importar tabela
tabela_clientes = pd.read_csv("/path/ClientesBanco.csv", encoding="latin1")

# tratar dados
tabela_clientes = tabela_clientes.drop("CLIENTNUM", axis=1) # exclui a coluna CLIENTNUM
display(tabela_clientes.info())  # Verifica se tem itens vazios
tabela_clientes = tabela_clientes.dropna() # Exclui as linhas que tem itens vazios
display(tabela_clientes.describe()) # Visão Geral da Tabela

# Verificar a quantidade de clientes ativos ou cancelados
display(tabela_clientes["Categoria"].value_counts())
display(tabela_clientes["Categoria"].value_counts(normalize=True))

# Criar gráfico de todas as colunas para análise de dados

for coluna in tabela_clientes:
  # criar gráfico
  fig = px.histogram(tabela_clientes, x= coluna, color="Categoria")
  # exibir gráfico
  fig.show()