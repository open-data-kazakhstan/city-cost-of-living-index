import xlrd
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xls_file_path = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\archive\avg_cost.xls"

csv_file_path = r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost.csv'


region_translation = {
    'Актау': 'Akatau city',
    'Атырау': 'Atyrau city',
    'Актобе': 'Aktobe city',
    'Кокшетау': 'Kokshetau city',
    'Караганда': 'Karaganda city',
    'Костанай': 'Kostanai city',
    'Кызылорда': 'Kyzylorda city',
    'Уральск': 'Uralsk city',
    'Усть-Каменогорск': 'Ust-Kamenagorsk city',
    'Павлодар': 'Pavlodar city',
    'Петропавловск': 'Petropavlovsk city',
    'Семей': 'Semei city',
    'Талдыкорган': 'Taldykorgan city',
    'Тараз': 'Taraz city',
    'Туркестан': 'Turkistan city',
    'Астана': 'Astana city',
    'Алматы': 'Almaty city',
    'Шымкент': 'Shymkent city'
}

# Открытие файла Excel
workbook = xlrd.open_workbook(xls_file_path)
sheet = workbook.sheet_by_index(0)

# Получение заголовка
header = sheet.row_values(2)

# Открытие CSV файла для записи
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Запись заголовка
    csv_writer.writerow(header)
    
    # Запись данных
    for row_idx in range(3, sheet.nrows):
        row = sheet.row_values(row_idx)
        # Замена названий регионов на латиницу (предполагая, что регион находится в первой колонке)
        region_name = row[0]
        row[0] = region_translation.get(region_name, region_name)
        csv_writer.writerow(row)

# Load the CSV file
# Load the CSV file
csv_file = r"C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost.csv"
df = pd.read_csv(csv_file)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=['2022.0'])

# Rename columns
df_unpivot.rename(columns={"Unnamed: 0": "Region", "variable": "Year", "value": "Value"}, inplace=True)

# Удаление столбца Year
df_unpivot = df_unpivot.drop(columns=['Year'])

# Exclude the rows with regions 'Республика Казахстан', 'Жезказган', and 'Конаев'
df_unpivot = df_unpivot[~df_unpivot['Region'].isin(['Республика Казахстан', 'Жезказган', 'Конаев'])]

# Remove rows with NaN in 'Average cost of living space(per square m)' column
df_unpivot.dropna(subset=['Value'], inplace=True)

# Convert non-numeric values to NaN
df_unpivot['Value'] = pd.to_numeric(df_unpivot['Value'], errors='coerce')

# Convert the column to integers
df_unpivot['Value'] = df_unpivot['Value'].fillna(0).astype(int)

# Print and save the result
print(df_unpivot)
df_unpivot.to_csv(r'C:\Users\USER\Desktop\practice\city-cost-of-living-index\data\cost_piv.csv', index=False)