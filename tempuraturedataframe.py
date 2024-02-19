import pandas as pd

# Part a) Create a DataFrame named 'temperatures' from a dictionary
data = {
    'Maxine': [72, 68, 75],
    'James': [69, 71, 73],
    'Amanda': [74, 70, 72]
}
temperatures = pd.DataFrame(data)

# Part b) Recreate the DataFrame with custom indices
custom_indices = ['Morning', 'Afternoon', 'Evening']
temperatures = pd.DataFrame(data, index=custom_indices)

# Part c) Select Maxine's temperature readings
maxine_temperatures = temperatures['Maxine']

# Part d) Select the row for 'Morning' temperature readings
morning_temperatures = temperatures.loc['Morning']

# Part e) Select the rows for 'Morning' and 'Evening' temperature readings
morning_evening_temperatures = temperatures.loc[['Morning', 'Evening']]

# Part f) Select the columns for 'Amanda' and 'Maxine'
amanda_maxine_temperatures = temperatures[['Amanda', 'Maxine']]

# Part g) Select specific elements
amanda_maxine_morning_afternoon = temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]

# Part h) Get descriptive statistics
temperature_stats = temperatures.describe()

# Part i) Transpose the DataFrame
temperatures_transposed = temperatures.T

# Part j) Sort columns in alphabetical order
temperatures_sorted = temperatures.reindex(sorted(temperatures.columns), axis=1)

# Printing the results
print("Original DataFrame:")
print(temperatures)
print("\nMaxine's Temperatures:")
print(maxine_temperatures)
print("\nMorning Temperatures:")
print(morning_temperatures)
print("\nMorning and Evening Temperatures:")
print(morning_evening_temperatures)
print("\nAmanda and Maxine's Temperatures:")
print(amanda_maxine_temperatures)
print("\nAmanda and Maxine's Morning and Afternoon Temperatures:")
print(amanda_maxine_morning_afternoon)
print("\nDescriptive Statistics:")
print(temperature_stats)
print("\nTransposed DataFrame:")
print(temperatures_transposed)
print("\nSorted DataFrame:")
print(temperatures_sorted)