'''
A code that will plot a bar chart showing the amount of each point groups and compare two folders of different csv

CAUTION: The files must have the point group values under the name 'Point group' to work

Made by Leo Arogundade (15/07/24)
'''

# Importing libraries
import os
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Function list
def read_point_groups(folder_path):
    '''
    Reads point groups from all CSV files in the specified folder
    
    Input: File path to .csv files
    Output: List of point groups
    '''
    
    point_groups = [] # Initializes an empty list to store point groups
    for file_name in os.listdir(folder_path): # Iterates over all files in the folder
        if file_name.endswith('.csv'): # Checks if the file is a CSV file
            file_path = os.path.join(folder_path, file_name) # Creates the full file path
            with open(file_path, mode='r') as file: # Opens the file in read mode
                reader = csv.reader(file) # Creates a CSV reader object
                for row in reader: # Iterates over rows in the CSV file
                    if row[0] == 'Point group': # Checks if the row is a point group row
                        point_groups.append(row[1]) # Adds the point group to the list
                        break # Breaks after the first point group row
    return point_groups # Returns the list of point groups

def count_point_groups(point_groups):
    '''
    Counts the occurrences of each point group in the list
    
    Input: List of point groups
    Output: Point group counts
    '''

    return Counter(point_groups) # Returns a Counter object with point group counts

def point_group_bar_chart_func(folder1_path, folder2_path):
    '''
    Reads and counts point groups from two folders and plots a comparison bar chart
    
    Input: Paths to the two folder
    Output: The bar chart with point group data plotted of both .csv folders
    '''

    point_groups_folder1 = read_point_groups(folder1_path) # Reads point groups from the first folder
    point_groups_folder2 = read_point_groups(folder2_path) # Reads point groups from the second folder
    counts_folder1 = count_point_groups(point_groups_folder1) # Counts point groups in the first folder
    counts_folder2 = count_point_groups(point_groups_folder2) # Counts point groups in the second folder
    all_point_groups = set(counts_folder1.keys()).union(set(counts_folder2.keys())) # Combines keys from both counters
    labels = list(all_point_groups) # Prepares labels for the bar chart
    counts1 = [counts_folder1.get(pg, 0) for pg in labels] # Gets counts for the first folder, defaulting to 0
    counts2 = [counts_folder2.get(pg, 0) for pg in labels] # Gets counts for the second folder, defaulting to 0
    x = np.arange(len(labels)) # Defines the label locations for the x-axis
    width = 0.35 # Defines the width of the bars
    fig, ax = plt.subplots() # Creates a new figure and axes for the plot
    rects1 = ax.bar(x - width/2, counts1, width, label='Racemic', edgecolor='black') # Plots bars for the first folder
    rects2 = ax.bar(x + width/2, counts2, width, label='Sohncke', edgecolor='black') # Plots bars for the second folder
    ax.set_xlabel('Point Groups') # Sets the x-axis label
    ax.set_ylabel('Counts') # Sets the y-axis label
    ax.set_title('Comparison of Point Groups between Racemic and Sohncke') # Sets the plot title
    ax.set_xticks(x) # Sets the x-axis ticks
    ax.set_xticklabels(labels, rotation=45, ha='right') # Sets the x-axis tick labels with rotation and alignment
    ax.legend() # Adds a legend to the plot
    fig.tight_layout() # Adjusts the layout to fit everything
    filename = 'Point Group'
    plt.savefig(os.path.join(f'{filename}.png')) # Saves the plot as an image file
    print(f'The bar chart has been generated under the name: {filename}')

def point_group_bar_chart_scaled_func(folder1_path, folder2_path):
    '''
    Reads and counts point groups from two folders and plots a comparison bar chart
    
    Input: Paths to the two folder
    Output: The bar chart with point group data plotted of both .csv folders
    '''

    point_groups_folder1 = read_point_groups(folder1_path) # Reads point groups from the first folder
    point_groups_folder2 = read_point_groups(folder2_path) # Reads point groups from the second folder
    counts_folder1 = count_point_groups(point_groups_folder1) # Counts point groups in the first folder
    counts_folder2 = count_point_groups(point_groups_folder2) # Counts point groups in the second folder
    all_point_groups = set(counts_folder1.keys()).union(set(counts_folder2.keys())) # Combines keys from both counters
    labels = list(all_point_groups) # Prepares labels for the bar chart
    counts1 = [counts_folder1.get(pg, 0) for pg in labels] # Gets counts for the first folder, defaulting to 0
    counts2 = [counts_folder2.get(pg, 0) for pg in labels] # Gets counts for the second folder, defaulting to 0
    scale_factor = 307 / 51 # Defines the scale factor for the second folder counts
    counts2 = [count * scale_factor for count in counts2] # Scales the counts of the second folder
    x = np.arange(len(labels)) # Defines the label locations for the x-axis
    width = 0.35 # Defines the width of the bars
    fig, ax = plt.subplots() # Creates a new figure and axes for the plot
    rects1 = ax.bar(x - width/2, counts1, width, label='Racemic', edgecolor='black') # Plots bars for the first folder
    rects2 = ax.bar(x + width/2, counts2, width, label='Sohncke (scaled)', edgecolor='black') # Plots bars for the second folder
    ax.set_xlabel('Point Groups') # Sets the x-axis label
    ax.set_ylabel('Counts') # Sets the y-axis label
    ax.set_title('Comparison of Point Groups between Racemic and Sohncke (Scaled)') # Sets the plot title
    ax.set_xticks(x) # Sets the x-axis ticks
    ax.set_xticklabels(labels, rotation=45, ha='right') # Sets the x-axis tick labels with rotation and alignment
    ax.legend() # Adds a legend to the plot
    fig.tight_layout() # Adjusts the layout to fit everything
    filename = 'Point Group (Scaled)'
    plt.savefig(os.path.join(f'{filename}.png')) # Saves the plot as an image file
    print(f'The bar chart has been generated under the name: {filename}')
  
# Paths to the folders
folder1_path = r'racemic'
folder2_path = r'sohncke'

point_group_bar_chart_func(folder1_path, folder2_path)
point_group_bar_chart_scaled_func(folder1_path, folder2_path)