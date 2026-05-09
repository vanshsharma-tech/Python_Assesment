# Program to generate random temperature data
# and plot histogram

import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data
temperatures = np.random.randint(15, 45, 100)

# Plot histogram
plt.hist(temperatures, bins=10)

# Add title and labels
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# Display grid
plt.grid(True)

# Show histogram
plt.show()