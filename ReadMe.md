## Folder-based Character Column Transformation

This script allows you to transform character columns of a dataset and save the transformed files in a specified folder.
**Important:**
THIS CODE WAS CREATED FOR USING IT WITH THIS [anova_analysis](https://github.com/Insight-deviler/anova-analysis) PACKAGE FOR DATA TRANSFORMATION OR IT CAN BE USED AS STANDALONE BASED ON YOUR NEEDS

## Model Dataset

Model dataset can be found in this [repo](https://github.com/Insight-deviler/Genotype-Character-Mean-Calculator) or given below
- This is the input file:
        | GENOTYPE | REPLICATION | Days to Maturity | PLANT HEIGHT (cm) |
        |----------|-------------|------------------|-------------------|
        | G1       | R1          | 4                | 5                 |
        | G1       | R2          | 5                | 6                 |
        | G1       | R3          | 4                | 9.3               |
        | G2       | R1          | 3                | 9.9               |
        | G2       | R2          | 6                | 7.5               |
- This is the output file: 
        1. ```Days to maturity.xlsx```
                | GENOTYPE | r1 | r2 | r3 |
                |----------|----|----|----|
                | G1       |  3 | 15 | 40 |
                | G2       | 13 | 12 | 79 |
                | G3       | 88 | 17 | 56 |
                | G4       | 75 | 16 | 10 |
                | G5       | 65 | 24 | 23 |
                | G6       | 26 | 58 | 12 |
        2. ```PLANT HEIGHT (cm)```
                | GENOTYPE | r1   | r2   | r3  |
                |----------|------|------|-----|
                | G1       | 5.4  | 6.0  | 9.1 |
                | G2       | 5.8  | 5.5  | 8.3 |
                | G3       | 5.7  | 5.6  | 0.1 |
                | G4       | 5.7  | 7.7  | 5.9 |
                | G5       | 4.2  | 1.4  | 0.3 |

## Requirements

- Python 3.x
- pandas package

## Usage

1. Place the dataset file in the same directory as the script.
2. Modify the `folder_path` variable in the script to specify the folder where you want to save the transformed files.
3. Run the script.

## Code

A working code has been provided within the repo for easy understanding of the use case.
Take a look at it.✌️
## Output

The script will iterate through the specified character columns of the dataset and perform the following steps for each column:
- Pivot the dataset based on the 'GENOTYPE' and 'REPLICATION' columns.
- Rename the columns to 'r1', 'r2', and 'r3'.
- Reset the index.
- Save the transformed dataset as an Excel file in the specified folder.

The transformed files will be saved in the specified folder with filenames corresponding to the character columns of the dataset.
