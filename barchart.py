import matplotlib.pyplot as plt
from collections import Counter

lst = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
total_responses = len(lst)

dictionary = {}

for value in lst:
    if value in dictionary:
        dictionary[value] += 1
    else:
        dictionary[value] = 1
response_frequencies = dictionary

percentages = [round((value / total_responses) * 100) for value in response_frequencies.values()]
plt.bar(response_frequencies.keys(), response_frequencies.values())
plt.title("Response Frequencies")
plt.xlabel("Responses")
plt.ylabel("Frequency")
for i in range(len(percentages)):
    plt.text(list(response_frequencies.keys())[i], list(response_frequencies.values())[i], str(percentages[i]) + "%", ha='center', va='bottom')

plt.show()