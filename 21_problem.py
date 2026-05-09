# Program to generate a NumPy array of student marks
# and convert it into a Pandas DataFrame

import numpy as np
import pandas as pd

# Generate NumPy array of student marks
marks = np.array([[78, 85, 90], [88, 76, 95], [67, 80, 72], [92, 89, 96], [75, 70, 84]])

# Convert NumPy array into Pandas DataFrame
df = pd.DataFrame(
    marks,
    columns=["Math", "Science", "English"],
    index=["Student1", "Student2", "Student3", "Student4", "Student5"],
)

# Display DataFrame
print("Student Marks DataFrame:\n")
print(df)

# Display highest marks subject-wise
print("\nHighest Marks in Each Subject:\n")
print(df.max())

# Display average marks subject-wise
print("\nAverage Marks in Each Subject:\n")
print(df.mean())

# Display subject-wise statistics
print("\nSubject-wise Statistics:\n")
print(df.describe())
