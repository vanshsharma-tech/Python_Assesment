# Program to create a line chart using Matplotlib

import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 45000]

# Create line chart
plt.plot(months, sales, marker='o', label="Monthly Sales")

# Add chart title
plt.title("Company Monthly Sales Data")

# Add labels
plt.xlabel("Months")
plt.ylabel("Sales Amount")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Display chart
plt.show()