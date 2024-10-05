import seaborn as sns
import matplotlib.pyplot as plt

# Criando uma matriz de correlação
correlation_matrix = tips.corr()

# Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Matriz de Correlação")
plt.show()
