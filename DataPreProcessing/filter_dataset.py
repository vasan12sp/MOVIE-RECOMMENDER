import os
import pandas as pd
import glob

# Get the current directory where the script is located
script_directory = os.getcwd()

# List of columns to keep
columns_to_keep = ['movie_id', 'movie_name', 'description', 'genre', 'rating', 'director', 'star']

# Initialize an empty DataFrame
merged_data = pd.DataFrame(columns=columns_to_keep)

# Loop through each CSV file in the current directory and merge the data
for genre_file in glob.glob(os.path.join(script_directory, '*.csv')):
    # Read the CSV file
    df = pd.read_csv(genre_file)

    # Filter movies after 2004, handling non-numeric values
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    # Extract genre from the filename
    genre = os.path.basename(genre_file).split('.')[0]

    # Apply genre-specific conditions
    if genre in ['history', 'biography', 'fantasy', 'family']:
        df = df[(df['year'] < 2018) & (df['year'] > 2014) & (df['rating'] > 8) | (df['year'] > 2017) & (df['rating'] > 7)]
    else:
        df = df[(df['year'] < 2017) & (df['year'] > 2013) & (df['rating'] > 7.5) |
                (df['year'] < 2014) & (df['year'] > 2004) & (df['rating'] > 8) |
                (df['year'] > 2016) & (df['year'] < 2022) & (df['rating'] > 6.5) |
                (df['year'] > 2021) & (df['rating'] > 5.8)]

    # Keep only the specified columns
    df = df[columns_to_keep]

    # Merge the data
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data to a new CSV file in the current directory
output_file_path = os.path.join(script_directory, 'merged_data_filtered.csv')
merged_data.to_csv(output_file_path, index=False)

print("Merged and filtered data saved successfully.")
