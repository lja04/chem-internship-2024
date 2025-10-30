'''
A code that will take two sets of .csv files that contain the same descriptors and plot histograms to compare them

IMPROVEMENTS:
- Set the scale up so that you do not have to do it manually

CAUTION: The .csv files must contain the same descriptors in the same format

Made by Leo Arogundade (12/07/2024)
'''

# Importing libraries
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

# Function list
def generate_list_of_descriptor_values(filepath_to_csv_folders):
    '''
    A function that converts the descriptor information from the .csv files to lists in python
    
    Input: The file path to the .csv files
    Output: A python generated list of the descriptor names and values
    '''
    
    # Initialize empty lists for each descriptor
    descriptors = [
        'Asphericity', 'Eccentricity', 'Internal Shape Factor',
        'Normalised principle moment ratio 1', 'Normalised principle moment ratio 2',
        'First (smallest) principle moment of inertia', 'Second principle moment of inertias',
        'Third (largest) principle moment of inertia', 'Radius of Gyration',
        'Molecule Sphericity Index', 'Plane of best fit', 'Topological polar surface area',
        'Molecular weight'
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

def histogram_generator_not_scaled(path_to_save_folder, filepath_to_csv_folders):
    '''
    A function that generates a histogram of the descriptors from two different folders of .csv, with no scaling
    
    Input: The path to the folder where the .png will be saved and the path to the folder of the .csvs
    Output: .png of the histograms
    '''
    
    bin_list = [5, 10, 25, 50]  # List of bin sizes for histograms
    dataset1, dataset2, descriptors = generate_list_of_descriptor_values(filepath_to_csv_folders)  # Generate lists of descriptor values from CSV files
    
    for descriptor in descriptors:  # Iterate over each descriptor
        data1 = dataset1[descriptor]  # Get data for the current descriptor from dataset1
        data2 = dataset2[descriptor]  # Get data for the current descriptor from dataset2
        
        plt.figure(figsize=(10, 6))  # Create a new figure with specified size
        
        for sub_idx, bins in enumerate(bin_list, start=1):  # Iterate over each bin size in bin_list with a subplot index starting from 1
            # Plot histograms for dataset 1 and dataset 2 on the same subplot
            plt.subplot(2, 2, sub_idx)  # Create a 2x2 grid of subplots and select the current subplot
            plt.hist(data2, bins=bins, edgecolor='black', alpha=0.5, label='Racemic')  # Plot histogram for dataset2
            plt.hist(data1, bins=bins, edgecolor='black', alpha=0.5, label='Schncke')  # Plot histogram for dataset1
            plt.title(f'{descriptor}, Bins={bins}')  # Set the title for the current subplot
            plt.xlabel(descriptor)  # Set the x-axis label for the current subplot
            plt.ylabel('Frequency')  # Set the y-axis label for the current subplot
            plt.legend()  # Add a legend to the current subplot
            plt.tight_layout()  # Adjust subplot parameters to give specified padding
        
        plt.savefig(f'{path_to_save_folder}/{descriptor}.png')  # Save the figure as a PNG file
        plt.close()  # Close the figure to free up memory
        print(f'Histogram saved as: {path_to_save_folder}/{descriptor}.png')  # Print a message indicating where the histogram was saved

def histogram_generator_scaled(path_to_save_folder, filepath_to_csv_folders):
    '''
    A function that generates a histogram of the descriptors from two different folders of .csv, with scaling
    
    Input: The path to the folder where the .png will be saved and the path to the folder of the .csvs
    Output: .png of the histograms
    '''
    
    bin_list = [5, 10, 25, 50]  # List of bin sizes for histograms
    dataset1, dataset2, descriptors = generate_list_of_descriptor_values(filepath_to_csv_folders)  # Generate lists of descriptor values from CSV files
    
    # Calculate scaling factor for dataset1 frequencies
    scaling_factor = 307 / 51  # Define the scaling factor based on the given counts

    for descriptor in descriptors:  # Iterate over each descriptor
        data1 = dataset1[descriptor]  # Get data for the current descriptor from dataset1
        data2 = dataset2[descriptor]  # Get data for the current descriptor from dataset2
        
        # Calculate histograms
        hist1, bins1 = np.histogram(data1, bins=bin_list)  # Calculate histogram for dataset1
        hist2, bins2 = np.histogram(data2, bins=bin_list)  # Calculate histogram for dataset2
        
        # Scale histogram counts of dataset1
        scaled_hist1 = hist1 * scaling_factor  # Scale the histogram counts for dataset1
        
        plt.figure(figsize=(10, 6))  # Create a new figure with specified size
        
        for sub_idx, bins in enumerate(bin_list, start=1):  # Iterate over each bin size in bin_list with a subplot index starting from 1
            # Plot histograms for dataset 1 and dataset 2 on the same subplot
            plt.subplot(2, 2, sub_idx)  # Create a 2x2 grid of subplots and select the current subplot
            plt.hist(data2, bins=bins, edgecolor='black', alpha=0.5, label='Racemic')  # Plot histogram for dataset2
            plt.hist(data1, bins=bins, edgecolor='black', alpha=0.5, weights=np.ones_like(data1) * scaling_factor, label='Schncke (Scaled)')  # Plot scaled histogram for dataset1
            plt.title(f'{descriptor}, Bins={bins}')  # Set the title for the current subplot
            plt.xlabel(descriptor)  # Set the x-axis label for the current subplot
            plt.ylabel('Frequency')  # Set the y-axis label for the current subplot
            plt.legend()  # Add a legend to the current subplot
            plt.tight_layout()  # Adjust subplot parameters to give specified padding
        
        plt.savefig(f'{path_to_save_folder}/{descriptor} (Scaled).png')  # Save the figure as a PNG file
        plt.close()  # Close the figure to free up memory
        print(f'Histogram saved as: {path_to_save_folder}/{descriptor} (Scaled).png')  # Print a message indicating where the histogram was saved

# Define the paths to folders containing CSV files for the two datasets
filepath_to_csv_folders = [
    r'sohncke',  # Path to folder containing 'sohncke' CSV files
    r'racemic'  # Path to folder containing 'racemic' CSV files
]

# Define the path to the folder where non-scaled histograms will be saved
path_to_save_folder_not_scaled = r'not_scaled'

# Define the path to the folder where scaled histograms will be saved
path_to_save_folder_scaled = r'scaled'

# Call the function to generate and save scaled histograms
histogram_generator_scaled(path_to_save_folder_scaled, filepath_to_csv_folders)

# Call the function to generate and save non-scaled histograms
histogram_generator_not_scaled(path_to_save_folder_not_scaled, filepath_to_csv_folders)

