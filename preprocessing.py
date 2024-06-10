import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r"C:\Users\sreev\OneDrive\Desktop\diabetes analysis\diabetes.xlsx"
df = pd.read_excel(file_path)

columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

df[columns_with_zeros] = df[columns_with_zeros].replace(0, np.nan)

df[columns_with_zeros] = df[columns_with_zeros].fillna(df[columns_with_zeros].median())

print("Basic statistics:")
print(df.describe())

df.hist(figsize=(12, 10))
plt.suptitle('Histograms of numerical features')
plt.show()

plt.figure(figsize=(12, 10))
df.boxplot(column=columns_with_zeros)
plt.title('Box plots of features with previously zero values')
plt.show()

sns.pairplot(df, hue='Outcome', diag_kind='kde')
plt.suptitle('Pair plots of features colored by Outcome', y=1.02)
plt.show()

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation heatmap')
plt.show()


output_path = './diabetes_cleaned.xlsx'
df.to_excel(output_path, index=False)

print("Cleaned data saved to:", output_path)
