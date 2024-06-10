import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = r"C:\Users\sreev\OneDrive\Desktop\diabetes analysis\diabetes.xlsx"
df = pd.read_excel(file_path)

# Columns that should not have zero values
columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace zeros with NaN for specific columns
df[columns_with_zeros] = df[columns_with_zeros].replace(0, np.nan)

# Fill missing values with the median of each column
df[columns_with_zeros] = df[columns_with_zeros].fillna(df[columns_with_zeros].median())

# Display basic statistics
print("Basic statistics:")
print(df.describe())

# Plot histograms for all numerical features
df.hist(figsize=(12, 10))
plt.suptitle('Histograms of numerical features')
plt.show()

# Plot box plots to visualize outliers
plt.figure(figsize=(12, 10))
df.boxplot(column=columns_with_zeros)
plt.title('Box plots of features with previously zero values')
plt.show()

# Plot a pairplot to visualize relationships between features
sns.pairplot(df, hue='Outcome', diag_kind='kde')
plt.suptitle('Pair plots of features colored by Outcome', y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation heatmap')
plt.show()

# Save the cleaned data to a new Excel file
output_path = './diabetes_cleaned.xlsx'
df.to_excel(output_path, index=False)

print("Cleaned data saved to:", output_path)
