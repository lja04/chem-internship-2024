'''
This code will take a csv file which contains descriptor information and normalise the values before returning a new csv file containing the new values

Made by Leo Arogundade (22/07/2024)
'''

# Importing libraries
import pandas as pd
import numpy as np

# Function list
def normalize(values):
    """
    Returns the normalized values from a list

    Input: values - list of values of interest
    Output: list of normalized values 
    """
    val_min = min(values)
    val_max = max(values) - val_min

    values = np.array(values)
    values = np.divide(np.subtract(values, val_min), val_max)
    
    return list(values)

# Load the CSV file
file_path = r'filtered_all_descriptor_data.csv'  # Update this with the actual file path
df = pd.read_csv(file_path)

# Identify columns to normalize (all except 'Refcode' and 'Point group')
columns_to_normalize = df.columns.difference(['Refcode', 'Point group'])

# Apply normalization to the relevant columns
df[columns_to_normalize] = df[columns_to_normalize].apply(lambda col: normalize(col))

# Save the normalized DataFrame back to a CSV file
normalized_file_path = r'normalized_file.csv'  # Update this with the desired output file path
df.to_csv(normalized_file_path, index=False)

print("Normalization complete. Normalized data saved to:", normalized_file_path)
