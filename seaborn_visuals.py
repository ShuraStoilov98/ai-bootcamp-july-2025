import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")  # data on restaurant tips
#print(df.head())

"""
# Scatter
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="smoker")
plt.title("Bill vs Tip")
plt.show()
"""
# Bar 
sns.barplot(data=df, x="day", y="tip", hue="sex", palette="pastel")
plt.title("Average Total Bill per Day by Sex")
plt.show()
"""
# Box plot
sns.boxplot(data=df, x="day", y="tip", hue="sex")
plt.title("Tip Distribution per Day")
plt.show()

# Histpgram
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bills")
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
"""