import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de dispersão
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title("Gráfico de Dispersão: Conta Total vs. Gorjeta")
plt.show()
