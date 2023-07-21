import pandas as pd

def save_csv_to_excel(csv_files, columns_to_save, excel_file):
    # Read the first CSV file to get the common column
    first_csv = pd.read_csv(csv_files[0])
    common_column = first_csv.iloc[:, 0]

    # Create a DataFrame to store the data from CSV files (excluding the common column)
    df = pd.DataFrame()

    # Read and concatenate the remaining columns from the CSV files
    for csv_file in csv_files:
        data = pd.read_csv(csv_file, usecols=columns_to_save[1:])  # Exclude the common column
        df = pd.concat([df, data], axis=1)

    # Add the common column as the first column in the DataFrame
    df.insert(0, 'Common Column', common_column)

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)

# Example usage
csv_files = ['v_h6.csv', 'v_h7.csv', 'v_h8.csv', 'v_h9.csv', 'v_h10.csv', 'v_h11.csv', 'v_h12.csv', 'v_h13.csv', 'v_h14.csv', 'v_h15.csv', 'v_h16.csv', 'v_h17.csv', 'v_h18.csv', 'v_h19.csv', 'v_h20.csv', 'v_h21.csv', 'v_h22.csv', 'v_h23.csv', 'v_h24.csv', 'v_h25.csv', 'v_h26.csv', 'v_h27.csv', 'v_h28.csv', 'v_h29.csv']
columns_to_save = [0, 5]  # Indices of columns to save (0-indexed)
excel_file = 'output.xlsx'

save_csv_to_excel(csv_files, columns_to_save, excel_file)

