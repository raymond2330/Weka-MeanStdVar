import pandas as pd
from scipy.stats import zscore

# Load CSV file into a Pandas DataFrame
csv_file_path = 'Rice_Cammeo_Osmancik.csv'
df = pd.read_csv(csv_file_path)

# Identify and display outliers using z-score
z_scores = zscore(df.select_dtypes(include=['float64']))
outliers = (abs(z_scores) > 3).any(axis=1)
outliers_data = df[outliers]

print("Outliers:")
print(outliers_data)

# Ask user if they want to remove outliers
remove_outliers = input("Do you want to remove the outliers? (yes/no): ").lower()

if remove_outliers == 'yes':
    # Remove outliers from the DataFrame
    df_no_outliers = df[~outliers]

    # Save the DataFrame without outliers to a new CSV file
    csv_no_outliers_path = 'Rice_Cammeo_Osmancik_no_outliers.csv'
    df_no_outliers.to_csv(csv_no_outliers_path, index=False)

    print(f"\nDataFrame without outliers saved to: {csv_no_outliers_path}")
else:
    print("Outliers were not removed.")
