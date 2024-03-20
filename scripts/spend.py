import xlrd
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xls_file_path = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\archive\avg_spend.xls"

csv_file_path = r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\spend.csv'


workbook = xlrd.open_workbook(xls_file_path)


sheet = workbook.sheet_by_index(0)

header = sheet.row_values(2)

with open(csv_file_path, 'w', newline='',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    
    csv_writer.writerow(header)
    
    for row_idx in range(3, sheet.nrows):
        csv_writer.writerow(sheet.row_values(row_idx))


import pandas as pd
import numpy as np

# Load the CSV file
csv_file = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\spend.csv"
df = pd.read_csv(csv_file)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=['2022*'])

# Rename columns
df_unpivot.rename(columns={"Unnamed: 0": "Region", "variable": "Year", "value": "Average spendings(month)"}, inplace=True)

# Exclude the row with region 'Республика Казахстан'
df_unpivot = df_unpivot[df_unpivot['Region'] != 'Республика Казахстан']



# Remove rows with NaN in 'Average spendings(month)' column
df_unpivot.dropna(subset=['Average spendings(month)'], inplace=True)

# Print and save the result
print(df_unpivot)
df_unpivot.to_csv(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\spend_piv.csv', index=False)