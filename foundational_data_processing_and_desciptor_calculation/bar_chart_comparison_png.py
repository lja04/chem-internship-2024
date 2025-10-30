'''
This code is for generating bar charts of descriptor information obtained through RDKit and CCDC to try and find trends in racemic and sohncke crystals.

IMPROVEMENTS
- Make it so the scaling occurs by counting how many lines there are, so it is a more transferrable program

Made by Leo Arogundade (11/07/2024)
'''

# Importing necessary libraries
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

def generate_list_of_descriptor_values(filepath_to_csv_folders):
    '''
    A function that converts the descriptor information from the .csv files to lists in python
    
    Input: The file path to the .csv files
    Output: A python generated list of the descriptor names and values
    '''
    
    # Initialize empty lists for each descriptor
    descriptors = [
        'Number of atoms', 'Number of bonds', 'Number of heavy atoms', 'Number of heteroatoms',
        'Number of rings', 'Number of aromatic rings', 'Number of sp3 hybridised carbons',
        'Number of operations'
    ]

       # Dictionary to store values for both datasets
    all_lists_dataset1 = {desc: [] for desc in descriptors}  # Initialize a dictionary with keys from 'descriptors' and empty lists as values for the first dataset
    all_lists_dataset2 = {desc: [] for desc in descriptors}  # Initialize a dictionary with keys from 'descriptors' and empty lists as values for the second dataset

    # Loop through each folder containing the .csv files
    for folder in filepath_to_csv_folders:  # Iterate over each folder in 'filepath_to_csv_folders'
        directory = folder  # Set 'directory' to the current folder path
        for filename in os.listdir(directory):  # Iterate over each file in the current folder
            if filename.endswith('.csv'):  # Check if the current file is a CSV file
                with open(os.path.join(directory, filename), 'r') as csvfile:  # Open the CSV file in read mode
                    reader = csv.reader(csvfile)  # Create a CSV reader object
                    for row in reader:  # Iterate over each row in the CSV file
                        if len(row) == 2:  # Check if the row has exactly 2 columns
                            descriptor_name = row[0].strip()  # Strip whitespace from the first column to get the descriptor name
                            value_str = row[1].strip()  # Strip whitespace from the second column to get the value as a string
                            
                            # Attempt to convert the value to float
                            try:  # Start a try block to catch conversion errors
                                value = float(value_str)  # Convert the value string to a float
                            except ValueError:  # If conversion fails, handle the error
                                continue  # Skip the rest of the loop and continue with the next row
                            
                            if descriptor_name in descriptors:  # Check if the descriptor name is in the 'descriptors' list
                                if folder == filepath_to_csv_folders[0]:  # Check if the current folder is the first folder in 'filepath_to_csv_folders'
                                    all_lists_dataset1[descriptor_name].append(value)  # Append the value to the corresponding list in 'all_lists_dataset1'
                                elif folder == filepath_to_csv_folders[1]:  # Check if the current folder is the second folder in 'filepath_to_csv_folders'
                                    all_lists_dataset2[descriptor_name].append(value)  # Append the value to the corresponding list in 'all_lists_dataset2'

    return all_lists_dataset1, all_lists_dataset2, descriptors  # Return the dictionaries and the descriptors list

def plot_descriptor_comparison(all_lists_dataset1, all_lists_dataset2, descriptors):
    '''
    Function to plot bar charts comparing descriptor values between two datasets.
    
    Input: Dictionaries of descriptor values and the list of descriptors
    Output: None (plots bar charts)
    '''
    
    for descriptor in descriptors:
        values1 = all_lists_dataset1[descriptor]
        values2 = all_lists_dataset2[descriptor]
        unique_values = sorted(set(values1 + values2)) # Define unique values across both datasets
        counts1 = [values1.count(v) for v in unique_values] # Count occurrences of each value in dataset 1
        counts2 = [values2.count(v) for v in unique_values] # Count occurrences of each value in dataset 2
        fig, ax = plt.subplots(figsize=(10, 6)) # Increase the figure size
        bar_width = 0.35 # Define bar width
        bar_positions1 = np.arange(len(unique_values)) # Define bar positions
        bar_positions2 = bar_positions1 + bar_width
        ax.bar(bar_positions1, counts1, width=bar_width, edgecolor = 'black', label='Racemic', linewidth = 0.6) # Plot bars for dataset 1
        ax.bar(bar_positions2, counts2, width=bar_width, edgecolor = 'black', label='Sohncke', linewidth = 0.6) # Plot bars for dataset 2
        ax.set_xticks(bar_positions1 + bar_width / 2) # Set x-axis labels and title
        ax.set_xticklabels(unique_values, rotation=45)
        ax.set_xlabel(f'{descriptor}')
        ax.set_title(f'Comparison of {descriptor}')
        ax.legend() # Add legend
        plt.tight_layout() # Adjust layout to prevent cutting off labels
        plt.savefig(os.path.join(f'{descriptor}.png')) # Show the plot
        print(f'Bar chart saved as: {descriptor}.png')
        plt.close()

def plot_descriptor_comparison_scaled(all_lists_dataset1, all_lists_dataset2, descriptors):
    '''
    Function to plot bar charts comparing descriptor values between two datasets, where the sohncke data has been scaled
    
    Input: Dictionaries of descriptor values and the list of descriptors
    Output: None (plots bar charts)
    '''
    scaling_factor = 307 / 51  # Define the scaling factor

    for descriptor in descriptors:
        values1 = all_lists_dataset1[descriptor]
        values2 = all_lists_dataset2[descriptor]
        unique_values = sorted(set(values1 + values2)) # Define unique values across both datasets
        counts1 = [values1.count(v) for v in unique_values] # Count occurrences of each value in dataset 1
        counts2 = [values2.count(v) * scaling_factor for v in unique_values] # Count occurrences of each value in dataset 2 and scale them
        fig, ax = plt.subplots(figsize=(10, 6)) # Increase the figure size
        bar_width = 0.35 # Define bar width
        bar_positions1 = np.arange(len(unique_values)) # Define bar positions
        bar_positions2 = bar_positions1 + bar_width
        ax.bar(bar_positions1, counts1, width=bar_width, edgecolor='black', label='Racemic', linewidth=0.6) # Plot bars for dataset 1
        ax.bar(bar_positions2, counts2, width=bar_width, edgecolor='black', label='Sohncke (Scaled)', linewidth=0.6) # Plot bars for dataset 2
        ax.set_xticks(bar_positions1 + bar_width / 2) # Set x-axis labels and title
        ax.set_xticklabels(unique_values, rotation=90)
        ax.set_xlabel(f'{descriptor}')
        ax.set_title(f'Comparison of {descriptor} (Sohncke has been scaled by 307/51)')
        ax.legend() # Add legend
        plt.tight_layout() # Adjust layout to prevent cutting off labels
        plt.savefig(os.path.join(f'{descriptor} (Scaled).png')) # Save the plot
        print(f'Bar chart saved as: {descriptor} (Scaled).png')
        plt.close()

# Filepaths to the CSV folders
filepath_to_csv_folders = [r'racemic', 
                           r'sohncke']

# Generate the descriptor values
all_lists_dataset1, all_lists_dataset2, descriptors = generate_list_of_descriptor_values(filepath_to_csv_folders)

# Plot the descriptor comparisons
plot_descriptor_comparison(all_lists_dataset1, all_lists_dataset2, descriptors)
plot_descriptor_comparison_scaled(all_lists_dataset1, all_lists_dataset2, descriptors)


