import numpy as np
import pandas as pd

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Perform operations
total = np.sum(data)
mean = np.mean(data)
std_dev = np.std(data)

# Display results
print("NumPy Array:", data)
print("Sum:", total)
print("Mean:", mean)
print("Standard Deviation:", std_dev)

# Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=["Numbers"])

# Display the first few records
print("\nFirst Few Records:")
print(df.head())