import seaborn as sns
import matplotlib.pyplot as plt

# Gráfico de regressão
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title("Regressão: Conta Total vs. Gorjeta")
plt.show()
