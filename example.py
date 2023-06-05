from anova_analysis import ANOVA_RBD
import os

folder_path = r'C:/Users/python/data/'

# listing files in the folder_path 
for file in os.listdir(folder_path):
  
# Checking whether the folder contains excel files
    if file.endswith('.xlsx') or file.endswith('.xls'):

# Joining the file path and name of the excel file:
        file_path = os.path.join(folder_path, file)
        print(f"processing file: {file}")
       
      # Where: 
      #   3 is replication,
      #   153 is treatment,  os.path.basename(file) for getting file name
        ANOVA_RBD.RBD(3,153,file_path,os.path.basename(file))
