import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned/enriched_countries.csv')
print(df.columns.tolist())

# 1. Population by Region
pop_by_region = df.groupby('Region')['Population 2026'].sum().sort_values(ascending=False)
print(pop_by_region)

plt.figure(figsize=(10, 6))
pop_by_region.plot(kind='bar', color='steelblue')
plt.title('Total Population by Region (2026)')
plt.ylabel('Population (Billions)')
plt.xlabel('Region')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('docs/01_population_by_region.png', dpi=150)
plt.show()
print('Chart saved')

# 2. Top 10 most populous with enrichment
top10 = df.nlargest(10, 'Population 2026')[['Country', 'Population 2026', 'Capital', 'Region', 'Languages', 'Currencies']]
print(top10.to_string(index=False))

# 3. Fertility Rate vs Median Age by Region
fig, ax = plt.subplots(figsize=(10, 6))

regions = df['Region'].dropna().unique()
colors = ['steelblue', 'coral', 'seagreen', 'goldenrod', 'mediumpurple']

for region, color in zip(regions, colors):
    subset = df[df['Region'] == region]
    ax.scatter(subset['Median Age'], subset['Fert. Rate'], 
               label=region, color=color, alpha=0.6)

ax.set_xlabel('Median Age')
ax.set_ylabel('Fertility Rate')
ax.set_title('Fertility Rate vs Median Age by Region (2026)')
ax.legend()
plt.tight_layout()
plt.savefig('docs/03_fertility_vs_median_age.png', dpi=150)
plt.show()
print('Chart saved')

# 4. Average Urban Pop % by Subregion
urban_by_sub = df.groupby('Subregion')['Urban Pop %'].mean().sort_values(ascending=True)

plt.figure(figsize=(10, 8))
urban_by_sub.plot(kind='barh', color='steelblue')
plt.title('Average Urban Population % by Subregion (2026)')
plt.xlabel('Urban Population %')
plt.ylabel('')
plt.tight_layout()
plt.savefig('docs/04_urban_pop_by_subregion.png', dpi=150)
plt.show()
print('Chart saved')

# 5. Migration patterns by Region
mig_by_region = df.groupby('Region')['Migrants (net)'].sum().sort_values()

plt.figure(figsize=(10, 6))
colors = ['coral' if x < 0 else 'steelblue' for x in mig_by_region.values]
mig_by_region.plot(kind='barh', color=colors)
plt.title('Net Migration by Region (2026)')
plt.xlabel('Net Migrants')
plt.ylabel('')
plt.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('docs/05_migration_by_region.png', dpi=150)
plt.show()
print('Chart saved')



