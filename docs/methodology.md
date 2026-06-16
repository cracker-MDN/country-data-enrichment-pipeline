# Methodology

## Objective

Build a two-source data pipeline that combines web-scraped population data with API-sourced country metadata to enable regional analysis that neither source could support alone.

## Source Selection

**Worldometers** was chosen for population data because it provides a well-structured HTML table with 11 demographic fields across 234 countries and dependencies. The table is scrapable without authentication.

**API Countries** (apicountries.com) was chosen for enrichment because it returns JSON with no authentication required, includes region/subregion classification (which Worldometers lacks), and provides structured language and currency data.

The original plan used the REST Countries API v3.1, but this was deprecated during development. The pipeline was adapted to use API Countries as an alternative — a real-world example of handling external dependency changes.

## Scraping Approach

The scraping script sends a GET request with a User-Agent header to avoid potential blocking. BeautifulSoup parses the HTML, finds the first `<table>` tag, then iterates through `<tr>` rows extracting `<td>` cell text. The header row (`<th>` cells) provides column names for the DataFrame.

## API Approach

The API returns a JSON array of 250 country objects. Each object contains nested data structures — languages and currencies are lists of dictionaries. These are flattened into comma-separated strings (e.g. "Pashto, Uzbek, Turkmen") for DataFrame compatibility and clean CSV export.

## Data Cleaning

Four issues required cleaning in the scraped data:

1. **Garbled minus signs** — Unicode character â\x88\x92 (a malformed UTF-8 minus sign) replaced with standard hyphen-minus
2. **Commas in numbers** — stripped to enable numeric conversion
3. **Percentage signs** — stripped to enable numeric conversion
4. **Column name encoding** — Â² replaced with ² in column headers

All numeric columns converted using `pd.to_numeric()` with `errors='coerce'` to handle any remaining edge cases gracefully.

## Merge Strategy

A left join preserves all 234 scraped records while attaching API enrichment where available. Country names differ between sources in three predictable ways: shortened names (e.g. "United States" vs "United States of America"), encoding differences (e.g. "CÃ´te d'Ivoire" vs "Ivory Coast"), and convention differences (e.g. "St. Vincent & Grenadines" vs "Saint Vincent and the Grenadines").

A 37-entry mapping dictionary was built manually by comparing the unmatched scraped names against the full API name list. This achieved 100% record linkage (0 unmatched after mapping). Fuzzy matching was considered but rejected — the mismatches were systematic and predictable, making an explicit mapping more transparent and reproducible.

## Analysis Design

Five analyses were chosen to demonstrate that the API enrichment enables insights impossible from the scraped data alone. All five use the Region or Subregion fields (from the API) as grouping variables, combined with population metrics (from scraping). This validates the enrichment pipeline's purpose.
