
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
rolls = [random.randrange(1, 7) for i in range(600)]
values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'


sns.set_style('whitegrid')  # default is white with no grid


# create and display the bar plot
axes = sns.barplot(x=values, y=frequencies, palette='bright')

# set the title of the plot
axes.set_title(title)


# label the axes
axes.set(xlabel='Die Value', ylabel='Frequency')


# scale the y-axis to add room for text above bars
axes.set_ylim(top=max(frequencies) * 1.10)

plt.show()