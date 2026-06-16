import requests
import pandas as pd

url = 'https://www.apicountries.com/countries'

response = requests.get(url)
print(response.status_code)
data = response.json()

rows = []
for country in data:
    # Languages - extract names, join with comma
    langs = country.get('languages', [])
    lang_names = ', '.join([l['name'] for l in langs])
    
    # Currencies - extract names, join with comma
    currs = country.get('currencies', [])
    curr_names = ', '.join([c['name'] for c in currs])
    
    rows.append({
        'Country': country.get('name', ''),
        'Capital': country.get('capital', ''),
        'Region': country.get('region', ''),
        'Subregion': country.get('subregion', ''),
        'Languages': lang_names,
        'Currencies': curr_names
    })

df_api = pd.DataFrame(rows)
print(df_api.shape)
print(df_api.head(10))

df_api.to_csv('data/raw/api_countries.csv', index=False)
print('Saved:', df_api.shape[0], 'countries')
