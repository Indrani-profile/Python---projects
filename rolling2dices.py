import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize variables
n_rolls = 1000
results = [0] * 12

# Create the initial bar plot
fig, ax = plt.subplots()
bar = ax.bar(range(1, 13), results)
ax.set_xlabel('Sum of Two Dice')
ax.set_ylabel('Frequency (%)')
ax.set_title('Dynamic Dice Rolling Simulation')
ax.set_ylim(0, 100)

# Function to update the plot
def update(frame):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    results[total - 1] += 1
    total_rolls = frame + 1  # Incremental total rolls
    percentages = [freq / total_rolls * 100 for freq in results]
    for i, b in enumerate(bar):
        b.set_height(percentages[i])
    return bar

# Create the animation
ani = FuncAnimation(fig, update, frames=range(n_rolls), repeat=False)

# Display the animation
plt.show()