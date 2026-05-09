import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"],
    "Sales": [50000, 70000, 30000, 15000, 10000],
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("sales_data.csv", index=False)

# Read CSV file
sales_data = pd.read_csv("sales_data.csv")

# Plot bar chart
plt.bar(sales_data["Product"], sales_data["Sales"])

# Add title and labels
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# Display chart
plt.show()
