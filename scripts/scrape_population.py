import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')

# Extract header names
header_cells = rows[0].find_all('th')
columns = [cell.text.strip() for cell in header_cells]
print(columns)

# Extract all data rows
data = []
for row in rows[1:]:
    cells = row.find_all('td')
    if len(cells) == 0:
        continue
    values = [cell.text.strip() for cell in cells]
    data.append(values)

df = pd.DataFrame(data, columns=columns)

# Fix garbled minus sign
df = df.replace('â\x88\x92', '-', regex=True)

# Drop the rank column (#) 
df = df.drop(columns=['#'])

# Remove commas and % signs
for col in df.columns[1:]:    # skip Country column
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = df[col].str.replace('%', '', regex=False)
    
# Fix column names
df.columns = df.columns.str.replace('Â²', '²')

# Convert numeric columns
numeric_cols = ['Population 2026', 'Yearly Change', 'Net Change', 
                'Density (P/Km²)', 'Land Area (Km²)', 'Migrants (net)',
                'Fert. Rate', 'Median Age', 'Urban Pop %', 'World Share']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv('data/raw/population_scraped.csv', index=False)
print('Saved:', df.shape[0], 'countries')
