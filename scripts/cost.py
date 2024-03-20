import xlrd
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xls_file_path = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\archive\avg_cost.xls"

csv_file_path = r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost.csv'


workbook = xlrd.open_workbook(xls_file_path)


sheet = workbook.sheet_by_index(0)

header = sheet.row_values(2)

with open(csv_file_path, 'w', newline='',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    
    csv_writer.writerow(header)
    
    for row_idx in range(3, sheet.nrows):
        csv_writer.writerow(sheet.row_values(row_idx))

# Load the CSV file
# Load the CSV file
csv_file = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost.csv"
df = pd.read_csv(csv_file)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=['2022.0'])

# Rename columns
df_unpivot.rename(columns={"Unnamed: 0": "Region", "variable": "Year", "value": "Average cost of living space(per square m)"}, inplace=True)

# Exclude the rows with regions 'Республика Казахстан', 'Жезказган', and 'Конаев'
df_unpivot = df_unpivot[~df_unpivot['Region'].isin(['Республика Казахстан', 'Жезказган', 'Конаев'])]

# Remove rows with NaN in 'Average cost of living space(per square m)' column
df_unpivot.dropna(subset=['Average cost of living space(per square m)'], inplace=True)

# Convert non-numeric values to NaN
df_unpivot['Average cost of living space(per square m)'] = pd.to_numeric(df_unpivot['Average cost of living space(per square m)'], errors='coerce')

# Convert the column to integers
df_unpivot['Average cost of living space(per square m)'] = df_unpivot['Average cost of living space(per square m)'].fillna(0).astype(int)

# Print and save the result
print(df_unpivot)
df_unpivot.to_csv(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost_piv.csv', index=False)