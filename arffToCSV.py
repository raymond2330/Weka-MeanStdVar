from scipy.io import arff
import pandas as pd

# Load ARFF file
arff_file_path = 'Rice_Cammeo_Osmancik.arff'
data, meta = arff.loadarff(arff_file_path)

# Convert ARFF data to a Pandas DataFrame
df = pd.DataFrame(data)

# Decode the 'Class' column from bytes to string
df['Class'] = df['Class'].str.decode('utf-8')

# Save the DataFrame to a CSV file
csv_file_path = 'Rice_Cammeo_Osmancik.csv'
df.to_csv(csv_file_path, index=False)
