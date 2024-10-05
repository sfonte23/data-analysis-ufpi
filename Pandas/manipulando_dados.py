import pandas as pd

# Lendo um arquivo CSV
df = pd.read_csv('caminho/do/arquivo.csv')

# Filtrando dados
df_filtrado = df[df['Idade'] > 30]
print(df_filtrado)

# Agrupando dados
df_agrupado = df.groupby('Cidade').mean()
print(df_agrupado)
