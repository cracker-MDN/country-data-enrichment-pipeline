import pandas as pd

df_pop = pd.read_csv('data/raw/population_scraped.csv')
df_api = pd.read_csv('data/raw/api_countries.csv')

print('Population:', df_pop.shape)
print('API:', df_api.shape)

name_map = {
    'United States': 'United States of America',
    'Russia': 'Russian Federation',
    'DR Congo': 'Congo (Democratic Republic of the)',
    'Iran': 'Iran (Islamic Republic of)',
    'Tanzania': 'Tanzania, United Republic of',
    'United Kingdom': 'United Kingdom of Great Britain and Northern Ireland',
    'South Korea': 'Korea (Republic of)',
    "CÃ´te d'Ivoire": 'Ivory Coast',
    'Venezuela': 'Venezuela (Bolivarian Republic of)',
    'North Korea': "Korea (Democratic People's Republic of)",
    'Syria': 'Syrian Arab Republic',
    'Bolivia': 'Bolivia (Plurinational State of)',
    'Czech Republic (Czechia)': 'Czech Republic',
    'Laos': "Lao People's Democratic Republic",
    'State of Palestine': 'Palestine, State of',
    'Moldova': 'Moldova (Republic of)',
    'Eswatini': 'Swaziland',
    'RÃ©union': 'Réunion',
    'Brunei': 'Brunei Darussalam',
    'Sao Tome & Principe': 'Sao Tome and Principe',
    'CuraÃ§ao': 'Curaçao',
    'Micronesia': 'Micronesia (Federated States of)',
    'St. Vincent & Grenadines': 'Saint Vincent and the Grenadines',
    'U.S. Virgin Islands': 'Virgin Islands (U.S.)',
    'Faeroe Islands': 'Faroe Islands',
    'Turks and Caicos': 'Turks and Caicos Islands',
    'Saint Kitts & Nevis': 'Saint Kitts and Nevis',
    'Sint Maarten': 'Sint Maarten (Dutch part)',
    'British Virgin Islands': 'Virgin Islands (British)',
    'Caribbean Netherlands': 'Bonaire, Sint Eustatius and Saba',
    'Saint Martin': 'Saint Martin (French part)',
    'Saint Barthelemy': 'Saint Barthélemy',
    'Wallis & Futuna': 'Wallis and Futuna',
    'Saint Pierre & Miquelon': 'Saint Pierre and Miquelon',
    'Saint Helena': 'Saint Helena, Ascension and Tristan da Cunha',
    'Falkland Islands': 'Falkland Islands (Malvinas)',
    'Holy See': 'Vatican City'
}

df_pop['merge_key'] = df_pop['Country (or dependency)'].replace(name_map)

merged = df_pop.merge(df_api, left_on='merge_key', right_on='Country', how='left')
print('Merged:', merged.shape)
print('Missing enrichment:', merged['Country'].isna().sum())

# Drop the redundant columns
merged = merged.drop(columns=['merge_key', 'Country'])

# Rename for clarity
merged = merged.rename(columns={'Country (or dependency)': 'Country'})

print(merged.shape)
print(merged.columns.tolist())
merged.to_csv('data/cleaned/enriched_countries.csv', index=False)
print('Saved to data/cleaned/enriched_countries.csv')

