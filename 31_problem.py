import matplotlib.pyplot as plt

# Smartphone brands and market share
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Realme"]
market_share = [35, 30, 15, 10, 10]

# Highlight maximum market share
explode = [0.1, 0, 0, 0, 0]

# Create pie chart
plt.pie(
    market_share,
    labels=brands,
    autopct="%1.1f%%",
    explode=explode
)

# Add title
plt.title("Smartphone Market Share")

# Display chart
plt.show()