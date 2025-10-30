'''
A code that will go through a csv file containing point groups, and remove the structures from the data set that contain a perticular point group that is not desired.

Made by Leo Arogundade (22/07/2024)
'''

# Importing libraries
import csv

# Path to the original CSV file
csv_file_path = r'all_descriptor_data_test.csv'

# Path to the new CSV file where filtered data will be saved
new_csv_file_path = r'filtered_descriptor_data.csv'

# Point group to filter out
point_group_to_filter = 'Cs'

# List to store the rows that do not have the specified point group and counter to count how many rows were removed
filtered_rows = []
wrong_point_group_counter = 0

# Open and read the original CSV file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames  # Get the headers from the original CSV
    
    # Iterate through each row in the CSV
    for row in csv_reader:
        if row['Point group'] != point_group_to_filter:
            filtered_rows.append(row)
        else:
            wrong_point_group_counter += 1

# Write the filtered data to the new CSV file
with open(new_csv_file_path, mode='w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(filtered_rows)

print(f'Filtered data saved to {new_csv_file_path}\n{wrong_point_group_counter} rows were removed')