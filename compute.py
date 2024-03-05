import pandas as pd

# Load CSV file into a Pandas DataFrame
csv_file_path = 'Rice_Cammeo_Osmancik.csv'
df = pd.read_csv(csv_file_path)

# Exclude the 'Class' column before converting non-numeric values to NaN
numeric_df = df.drop(columns=['Class']).apply(pd.to_numeric, errors='coerce')

# Compute mean for each attribute
mean_values = numeric_df.mean()

# Compute standard deviation for each attribute
std_values = numeric_df.std()

# Compute variance for each attribute
variance_values = numeric_df.var()

# Display the results
print("Mean values:")
print(mean_values)

print("\nStandard Deviation values:")
print(std_values)

print("\nVariance values:")
print(variance_values)