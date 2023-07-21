import pandas as pd

def convert_csv_to_excel(csv_file, excel_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Create Excel writer object
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    
    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False)
    
    # Save the Excel file
    writer.save()
    
    print(f"CSV file '{csv_file}' successfully converted to Excel file '{excel_file}'.")


# Specify the CSV file path and Excel file path
csv_file_path = 'path/to/input.csv'
excel_file_path = 'path/to/output.xlsx'

# Convert the CSV file to Excel
#convert_csv_to_excel("MAI_Mon_monfeed1h_1.csv", "MAI_Mon_monfeed1h_1.xlsx")
#convert_csv_to_excel("MAI_Mon_monfeed2h_1.csv", "MAI_Mon_monfeed2h_1.xlsx")
#convert_csv_to_excel("MAI_EXP_VOLTAGES.CSV","MAI_EXP_VOLTAGES.xlsx")
convert_csv_to_excel("losses_no_pv.csv","losses_no_pv_12h.xlsx")
convert_csv_to_excel("losses_with_pv.csv","losses_with_pv_12h.xlsx")
#convert_csv_to_excel("LossesnoPV.csv","LossesnoPV.xlsx")
