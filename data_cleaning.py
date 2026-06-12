import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset information
print("\nDATASET INFO")
print(df.info())

# Shape
print("\nROWS AND COLUMNS")
print(df.shape)

# Columns
print("\nCOLUMN NAMES")
print(df.columns)

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())# Basic statistics
print("\nSTATISTICS")
print(df.describe())
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))

plt.hist(df['math score'])

plt.title('Math Score Distribution')

plt.xlabel('Math Score')

plt.ylabel('Number of Students')

plt.savefig('charts/math_score_distribution.png')

plt.show()

# Gender Distribution Chart

plt.figure(figsize=(8,5))

sns.countplot(x='gender', data=df)

plt.title('Gender Distribution')

plt.savefig('charts/gender_distribution.png')
plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(x='gender', y='math score', data=df)

plt.title('Math Score by Gender')

plt.savefig('charts/math_score_gender.png')

plt.show()
# Reading Score Distribution
plt.figure(figsize=(8,5))

plt.hist(df['reading score'])

plt.title('Reading Score Distribution')

plt.xlabel('Reading Score')

plt.ylabel('Number of Students')

plt.savefig('charts/reading_score_distribution.png')

plt.show()