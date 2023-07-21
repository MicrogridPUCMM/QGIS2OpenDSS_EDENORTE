import os
import pandas as pd

# Get the current directory
directory = os.getcwd()

# Get all .txt files in the directory
txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]

# Create an empty DataFrame
df = pd.DataFrame()

# Loop through each text file
for file_name in txt_files:
    # Read the contents of the text file
    with open(file_name, "r") as file:
        data = file.readlines()
    print(data)
    for i in range(len(data)):
        data[i] = float(data[i][0:data[i].find("\n")])
    
    # Create a new column in the DataFrame with the file name
    column_name = os.path.splitext(file_name)[0]  # Remove the file extension
    df[column_name] = data

# Create a new Excel file
excel_file = "output.xlsx"

# Write the DataFrame to the Excel file
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' created successfully.")
