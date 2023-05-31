import os
import pandas as pd

# Define the folder path where your files are located
folder_path = r'data'

# Load the dataset
df = pd.read_excel('MODEL_DATA.xlsx')

# Get the character columns to transform
# change it to your needs
character_columns = df.columns[2:12]

# Iterate through each character column
for column_name in character_columns:
    # Pivot the dataset
    # change it to your needs
    df_pivot = df.pivot(index='GENOTYPE', columns='REPLICATION', values=column_name)

    # Rename the columns
    # change it to your needs
    df_pivot.columns = ['r1', 'r2', 'r3']

    # Reset the index
    df_pivot.reset_index(inplace=True)

    # Save the transformed dataset with the characters in the filename
    output_filename = f'{column_name}.xlsx'
    output_file_path = os.path.join(folder_path, output_filename)
    df_pivot.to_excel(output_file_path, index=False)
