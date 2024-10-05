import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lineplot(data=tips, x="size", y="tip")
plt.show()