import seaborn as sns
import matplotlib.pyplot as plt

# Pair Grid
g = sns.pairplot(tips)
plt.title("Pair Grid: Tips Dataset")
plt.show()
