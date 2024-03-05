import pandas as pd

# Load CSV file into a Pandas DataFrame
csv_file_path = 'Rice_Cammeo_Osmancik_no_outliers.csv'
df = pd.read_csv(csv_file_path)

# Save DataFrame to ARFF file manually
arff_file_path = 'Rice_Cammeo_Osmancik_no_outliers.arff'

with open(arff_file_path, 'w') as f:
    # Write ARFF header
    f.write('@RELATION Rice_Cammeo_Osmancik_no_outliers\n\n')
    
    # Write ARFF attributes with explicit types
    for column, dtype in zip(df.columns, df.dtypes):
        if dtype == 'O':
            # Assuming the 'Class' column is categorical
            unique_classes = df['Class'].unique()
            class_values = ', '.join(unique_classes)
            f.write(f'@ATTRIBUTE {column} {{{class_values}}}\n')
        else:
            f.write(f'@ATTRIBUTE {column} Real\n')
    
    f.write('\n@DATA\n')
    
    # Write ARFF data
    for _, row in df.iterrows():
        # Convert 'Class' column from bytes to string
        row['Class'] = row['Class'].decode('utf-8') if isinstance(row['Class'], bytes) else row['Class']
        
        # Write the row to the ARFF file
        f.write(','.join(str(value) for value in row) + '\n')

print(f"ARFF file saved to: {arff_file_path}")
