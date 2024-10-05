# Exercício: Crie gráficos usando seaborn com o dataset 'tips'.

import seaborn as sns
import matplotlib.pyplot as plt

# Carregando o dataset
tips = sns.load_dataset("tips")

# Gráfico de barras
sns.barplot(data=tips, x='day', y='total_bill')
plt.title("Gráfico de Barras: Conta Total por Dia")
plt.show()
