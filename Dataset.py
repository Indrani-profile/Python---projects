import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:/Users/indra/OneDrive/Desktop/Python Assignments/Assignment 4/Iris.csv')

# Define the file path
# file_path = r"C:\Users\gorij\OneDrive\Desktop\Data science-python programmig(661)\archive (1)\Iris.csv"

# Load the Iris dataset into a DataFrame with the first column as the index
df = pd.read_csv("Iris.csv", index_col=0)

# Display the DataFrame's head
print("DataFrame Head:")
print(df.head())

# Display the DataFrame's tail
print("\nDataFrame Tail:")
print(df.tail())

# Calculate descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].describe())

# Enable Matplotlib support for plotting

# Plot histograms for each numerical column
df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].hist()
plt.suptitle("Histograms of Iris Dataset Numerical Columns")
plt.show()
