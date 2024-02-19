#Here is an alternative approach to creating a scatter plot of Anscombe's Quartet:

#First, import the necessary libraries and load the CSV file:
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/anscombe/anscombe.csv"
df = pd.read_csv(url)