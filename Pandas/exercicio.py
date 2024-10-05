# Exercício: Crie um DataFrame e realize operações de filtragem e agrupamento.

import pandas as pd

# Criando um DataFrame
dados = {
    'Produto': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Vendas': [100, 200, 150, 300, 250, 400]
}
df = pd.DataFrame(dados)

# Filtrando produtos A
df_a = df[df['Produto'] == 'A']

# Agrupando e somando as vendas por produto
df_agrupado = df.groupby('Produto').sum()

print("DataFrame filtrado (Produto A):\n", df_a)
print("\nVendas por produto:\n", df_agrupado)
