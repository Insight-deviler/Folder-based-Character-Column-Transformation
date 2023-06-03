## Folder-based Character Column Transformation

This script allows you to transform character columns of a dataset and save the transformed files in a specified folder.
THIS CODE WAS CREATED FOR USING IT WITH THIS [anova_analysis](https://github.com/Insight-deviler/anova-analysis) PACKAGE FOR DATA TRANSFORMATION OR IT CAN BE USED AS STANDALONE BASED ON YOUR NEEDS

## Model Dataset

Model dataset can be found in this [repo](https://github.com/Insight-deviler/Genotype-Character-Mean-Calculator) or given below

        | GENOTYPE | REPLICATION | Days to Maturity | PLANT HEIGHT (cm) |
        |----------|-------------|------------------|-------------------|
        | G1       | R1          | 4                | 5                 |
        | G1       | R2          | 5                | 6                 |
        | G1       | R3          | 4                | 9.3               |
        | G2       | R1          | 3                | 9.9               |
        | G2       | R2          | 6                | 7.5               |


## Requirements

- Python 3.x
- pandas package

## Usage

1. Place the dataset file in the same directory as the script.
2. Modify the `folder_path` variable in the script to specify the folder where you want to save the transformed files.
3. Run the script.

## Output

The script will iterate through the specified character columns of the dataset and perform the following steps for each column:
- Pivot the dataset based on the 'GENOTYPE' and 'REPLICATION' columns.
- Rename the columns to 'r1', 'r2', and 'r3'.
- Reset the index.
- Save the transformed dataset as an Excel file in the specified folder.

The transformed files will be saved in the specified folder with filenames corresponding to the character columns of the dataset.
