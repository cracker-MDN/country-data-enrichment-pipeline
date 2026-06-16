# Data Dictionary

## Final Dataset: enriched_countries.csv

234 records × 16 columns

### Scraped Fields (from Worldometers)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Country | string | Country or dependency name (original scraped name) | India |
| Population 2026 | int64 | Estimated total population for 2026 | 1476625576 |
| Yearly Change | float64 | Annual population growth rate (percentage points) | 0.87 |
| Net Change | int64 | Absolute population change from previous year | 12760051 |
| Density (P/Km²) | int64 | Population per square kilometre | 497 |
| Land Area (Km²) | int64 | Total land area in square kilometres | 2973190 |
| Migrants (net) | int64 | Net migration (positive = inflow, negative = outflow) | -440456 |
| Fert. Rate | float64 | Average number of children per woman | 1.93 |
| Median Age | float64 | Median age of the population in years | 29.2 |
| Urban Pop % | float64 | Percentage of population living in urban areas | 37.6 |
| World Share | float64 | Country's share of total world population (percentage points) | 17.79 |

### Enrichment Fields (from API Countries)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Capital | string | Capital city name | New Delhi |
| Region | string | Continental region (6 values: Asia, Africa, Americas, Europe, Oceania, Polar) | Asia |
| Subregion | string | Sub-continental region (22 unique values) | Southern Asia |
| Languages | string | Official/spoken languages, comma-separated | Hindi, English |
| Currencies | string | Official currencies, comma-separated | Indian rupee |

### Notes

- Negative migration values indicate net emigration (more people leaving than arriving)
- Yearly Change and Urban Pop % are stored as raw numbers, not as fractions (e.g. 0.87 means 0.87%, not 87%)
- World Share values sum to approximately 100% across all records
- Languages and Currencies may contain multiple comma-separated values for multilingual/multi-currency countries
- Some small dependencies may have NaN values in certain demographic fields where data was unavailable

## Raw Files

### population_scraped.csv
234 records × 11 columns — cleaned scraped data before merge

### api_countries.csv
250 records × 6 columns — flattened API data before merge (16 more records than scraped data due to territories not listed on Worldometers)
