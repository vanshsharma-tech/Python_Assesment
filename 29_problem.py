import pandas as pd

# Create DataFrame
data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Math": [85, 70, 92],
    "Science": [90, 65, 88],
    "English": [80, 75, 95]
}

df = pd.DataFrame(data)

# Calculate total and percentage
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

df["Percentage"] = df["Total"] / 3

# Function to assign grade
def assign_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 75:
        return "A"

    elif percentage >= 60:
        return "B"

    else:
        return "C"

# Apply grade function
df["Grade"] = df["Percentage"].apply(assign_grade)

# Display DataFrame
print(df)