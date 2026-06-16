# Cleaning Log

## Source 1: Worldometers Population Table (scrape_population.py)

### Issue 1: Garbled Unicode Minus Signs
- **Detected:** Negative values displayed as `â\x88\x92440,456` instead of `-440,456`
- **Cause:** The minus sign (Unicode U+2212) was encoded in UTF-8 as 3 bytes (0xE2 0x88 0x92) but rendered incorrectly during text extraction
- **Fix:** `df.replace('â\x88\x92', '-', regex=True)` — replaced garbled sequence with standard hyphen-minus across all cells
- **Records affected:** All rows with negative values in Net Change and Migrants columns

### Issue 2: Commas in Numeric Values
- **Detected:** Population values like `1,476,625,576` stored as strings
- **Fix:** `df[col].str.replace(',', '', regex=False)` for all numeric columns
- **Records affected:** All rows

### Issue 3: Percentage Signs
- **Detected:** Values like `0.87%` and `37.6%` in Yearly Change, Urban Pop %, and World Share columns
- **Fix:** `df[col].str.replace('%', '', regex=False)` for all numeric columns
- **Records affected:** All rows with percentage values

### Issue 4: Garbled Column Names
- **Detected:** Column names displayed `Density (P/KmÂ²)` instead of `Density (P/Km²)`
- **Cause:** Same UTF-8 encoding issue as the minus signs
- **Fix:** `df.columns = df.columns.str.replace('Â²', '²')`

### Issue 5: Rank Column
- **Detected:** `#` column contained row numbers from the HTML table (1-234)
- **Decision:** Dropped — redundant with DataFrame index and not meaningful for analysis
- **Fix:** `df.drop(columns=['#'])`

### Issue 6: Type Conversion
- **Detected:** All columns stored as `object` (string) type after cleaning
- **Fix:** `pd.to_numeric(df[col], errors='coerce')` for all numeric columns
- **Result:** Integer columns (Population, Net Change, Density, Land Area, Migrants) → int64; decimal columns (Yearly Change, Fert. Rate, Median Age, Urban Pop %, World Share) → float64
- **Coerced values:** `errors='coerce'` converts unconvertible values to NaN rather than crashing

## Source 2: API Countries (fetch_api.py)

### Issue 7: Nested JSON Structures
- **Detected:** Languages field contained a list of dictionaries: `[{'name': 'Pashto', ...}, {'name': 'Uzbek', ...}]`
- **Fix:** Extracted `name` field from each dictionary, joined with comma separator: `', '.join([l['name'] for l in langs])`
- **Applied to:** Languages and Currencies fields

### Issue 8: Missing Fields
- **Detected:** Some countries had missing languages or currencies (empty lists)
- **Fix:** `country.get('languages', [])` returns empty list instead of KeyError; empty list produces empty string after join

## Merge (merge_data.py)

### Issue 9: Country Name Mismatches
- **Detected:** 37 of 234 countries had no API match after initial left join
- **Cause:** Three types of naming differences between sources
- **Fix:** 37-entry mapping dictionary applied before merge
- **Result:** 0 unmatched records after mapping

| Mismatch Type | Example (Scraped → API) | Count |
|---------------|-------------------------|-------|
| Shortened names | United States → United States of America | 15 |
| Encoding differences | CÃ´te d'Ivoire → Ivory Coast | 3 |
| Convention differences | St. Vincent & Grenadines → Saint Vincent and the Grenadines | 19 |
