import os
import pandas as pd

# Get the current directory where the script is located
script_directory = os.getcwd()

# List of columns to keep
columns_to_keep = ['movie_id', 'movie_name', 'tags', 'rating']

# Path to the previously merged CSV file
merged_file_path = os.path.join(script_directory, 'merged_data_filtered.csv')

# Read the merged CSV file
merged_data = pd.read_csv(merged_file_path)

# Create a new column 'tags' combining 'genre' and 'description'
merged_data['tags'] = merged_data['genre'] + ', ' + merged_data['description']+ ', ' + merged_data['director']+ ', ' + merged_data['star']

# Keep only the specified columns
merged_data = merged_data[columns_to_keep]
merged_data = merged_data.drop_duplicates()

# Save the updated data to a new CSV file in the current directory
output_file_path = os.path.join(script_directory, 'final_merged_data.csv')
merged_data.to_csv(output_file_path, index=False)

print("Final merged data saved successfully.")
