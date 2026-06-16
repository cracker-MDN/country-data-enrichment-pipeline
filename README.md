# Country Data Enrichment Pipeline

A Python data pipeline that scrapes country population data from [Worldometers](https://www.worldometers.info/world-population/population-by-country/), enriches it with metadata from the [API Countries](https://www.apicountries.com/countries) REST API, and produces a merged dataset for regional analysis.

## Project Overview

This project demonstrates a two-source data pipeline: web scraping (HTML) and API access (JSON), merged on country name with a 37-entry name mapping dictionary to achieve 100% record linkage across 234 countries.

## Skills Demonstrated

- **Web scraping** — requests + BeautifulSoup to extract HTML table data
- **API access** — REST API fetch with JSON parsing and nested data flattening
- **Data cleaning** — garbled Unicode characters, commas, percentage signs, type conversion
- **Record linkage** — name mapping dictionary to resolve naming mismatches between sources
- **Data merging** — left join on mapped country names, 0 unmatched records
- **Analysis & visualisation** — 5 regional analyses using matplotlib, enabled by the API enrichment

## Data Sources

| Source | Type | Records | Fields Used |
|--------|------|---------|-------------|
| Worldometers Population Table | HTML (scraped) | 234 | Country, Population, Yearly Change, Net Change, Density, Land Area, Migrants, Fert. Rate, Median Age, Urban Pop %, World Share |
| API Countries | REST API (JSON) | 250 | Country, Capital, Region, Subregion, Languages, Currencies |

## Pipeline Steps

1. **Scrape** — fetch Worldometers population table, extract rows with BeautifulSoup
2. **Clean scraped data** — fix garbled minus signs, remove commas/percentage signs, convert types
3. **Fetch API** — pull all countries from API Countries endpoint, flatten nested JSON (languages, currencies)
4. **Merge** — left join on country name using a 37-entry mapping dictionary for name alignment
5. **Analyse** — 5 analyses leveraging the enriched dataset

## Key Findings

- Asia holds nearly 5 billion people — more than all other regions combined
- Strong inverse relationship between median age and fertility rate, with clear regional clustering
- Europe and Americas are net migration gainers; Asia and Africa are net losers
- Western Europe and North America are the most urbanised subregions; Southern Asia and Eastern Africa the least

## Project Structure

```
country-data-enrichment-pipeline/
├── data/
│   ├── raw/
│   │   ├── population_scraped.csv
│   │   └── api_countries.csv
│   └── cleaned/
│       └── enriched_countries.csv
├── scripts/
│   ├── scrape_population.py
│   ├── fetch_api.py
│   ├── merge_data.py
│   └── analyse.py
├── docs/
│   ├── methodology.md
│   ├── cleaning_log.md
│   ├── data_dictionary.md
│   ├── 01_population_by_region.png
│   ├── 03_fertility_vs_median_age.png
│   ├── 04_urban_pop_by_subregion.png
│   └── 05_migration_by_region.png
├── README.md
└── .gitignore
```

## How to Run

```bash
pip install requests beautifulsoup4 pandas matplotlib
python scripts/scrape_population.py
python scripts/fetch_api.py
python scripts/merge_data.py
python scripts/analyse.py
```

## Tools & Libraries

- Python 3.12
- requests, BeautifulSoup4, pandas, matplotlib
