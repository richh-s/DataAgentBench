code = """import json
import pandas as pd
import numpy as np
import re
import os

# Load the dataset
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse CPC codes and extract years
parsed_data = []
for record in data:
    try:
        date_str = record['publication_date']
        year_match = re.search(r'(\d{4})', date_str)
        if year_match:
            year = int(year_match.group(1))
            
            cpc_str = record['cpc']
            if cpc_str and cpc_str != 'null' and cpc_str != '[]':
                try:
                    cpc_list = json.loads(cpc_str)
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code', '')
                        if code:
                            # Extract level 5 group (A + 2 digits + letter)
                            group_match = re.match(r'^([A-Z]\d{2}[A-Z])', code)
                            if group_match:
                                level5_group = group_match.group(1)
                                parsed_data.append({
                                    'year': year,
                                    'cpc_group': level5_group
                                })
                except json.JSONDecodeError:
                    continue
    except Exception:
        continue

df = pd.DataFrame(parsed_data)
print(f"Total parsed records: {len(df)}")
print(f"Year range: {df['year'].min()} to {df['year'].max()}")
print(f"Unique CPC groups: {df['cpc_group'].nunique()}")

# Get yearly counts per CPC group
yearly_counts = df.groupby(['year', 'cpc_group']).size().reset_index(name='count')
print(f"Yearly counts shape: {yearly_counts.shape}")

# Create a complete grid of all years and CPC groups
all_years = sorted(yearly_counts['year'].unique())
all_groups = sorted(yearly_counts['cpc_group'].unique())

print(f"All years: {min(all_years)} to {max(all_years)} ({len(all_years)} years)")
print(f"All groups: {len(all_groups)} groups")

# Pivot to get counts per group per year (fill missing with 0)
pivot_df = yearly_counts.pivot(index='cpc_group', columns='year', values='count').fillna(0)

# Calculate EMA for each group with smoothing factor 0.2
alpha = 0.2
ema_results = {}

for group in all_groups:
    if group in pivot_df.index:
        # Get counts for this group in chronological order
        counts = [pivot_df.loc[group, year] if year in pivot_df.columns else 0 for year in all_years]
        
        # Calculate EMA
        ema_values = []
        ema = None
        for count in counts:
            if ema is None:
                ema = count  # Initialize with first value
            else:
                ema = alpha * count + (1 - alpha) * ema
            ema_values.append(ema)
        
        # Find the year with maximum EMA
        max_ema_idx = np.argmax(ema_values)
        max_ema_year = all_years[max_ema_idx]
        max_ema_value = ema_values[max_ema_idx]
        
        ema_results[group] = {
            'best_year': int(max_ema_year),
            'max_ema': float(max_ema_value),
            'ema_by_year': {int(year): float(ema) for year, ema in zip(all_years, ema_values)}
        }

print(f"Calculated EMA for {len(ema_results)} groups")

# Filter groups whose best year is 2022
groups_best_in_2022 = [group for group, data in ema_results.items() if data['best_year'] == 2022]
print(f"Groups with best year 2022: {len(groups_best_in_2022)}")

# Sort by max EMA value (descending) to get highest EMA groups
groups_2022_sorted = sorted(groups_best_in_2022, key=lambda g: ema_results[g]['max_ema'], reverse=True)

print("Top 10 groups with best year 2022:")
for i, group in enumerate(groups_2022_sorted[:10]):
    print(f"{i+1}. {group}: EMA = {ema_results[group]['max_ema']:.2f}")

# Return the final result
result = {
    'total_groups_analyzed': len(all_groups),
    'groups_best_year_2022': len(groups_best_in_2022),
    'top_groups_2022': groups_2022_sorted[:50],  # Top 50 for reference
    'all_groups_2022': groups_best_in_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:22': {'total_records': 277813, 'parsed_records': 2681388, 'year_range': [1837, 2024], 'top_groups_by_year': {'1837': {'cpc_group': 'B26F', 'count': 1}, '1839': {'cpc_group': 'B02B', 'count': 2}, '1841': {'cpc_group': 'A47L', 'count': 2}, '1842': {'cpc_group': 'Y10T', 'count': 3}, '1843': {'cpc_group': 'B43K', 'count': 1}, '1844': {'cpc_group': 'F03B', 'count': 2}, '1845': {'cpc_group': 'B05B', 'count': 1}, '1846': {'cpc_group': 'B23G', 'count': 1}, '1847': {'cpc_group': 'B65G', 'count': 2}, '1848': {'cpc_group': 'B60K', 'count': 1}, '1849': {'cpc_group': 'B44B', 'count': 1}, '1850': {'cpc_group': 'F04B', 'count': 1}, '1851': {'cpc_group': 'A23N', 'count': 1}, '1852': {'cpc_group': 'B29C', 'count': 1}, '1853': {'cpc_group': 'Y10T', 'count': 2}, '1854': {'cpc_group': 'A01D', 'count': 1}, '1855': {'cpc_group': 'B21D', 'count': 1}, '1856': {'cpc_group': 'A47L', 'count': 1}, '1857': {'cpc_group': 'A47C', 'count': 1}, '1858': {'cpc_group': 'B65H', 'count': 3}, '1859': {'cpc_group': 'B30B', 'count': 2}, '1860': {'cpc_group': 'Y10S', 'count': 4}, '1861': {'cpc_group': 'Y10T', 'count': 5}, '1862': {'cpc_group': 'Y10T', 'count': 4}, '1863': {'cpc_group': 'Y10S', 'count': 6}, '1864': {'cpc_group': 'Y10T', 'count': 6}, '1865': {'cpc_group': 'A01C', 'count': 2}, '1866': {'cpc_group': 'Y10T', 'count': 7}, '1867': {'cpc_group': 'Y10T', 'count': 9}, '1868': {'cpc_group': 'Y10T', 'count': 5}, '1869': {'cpc_group': 'C02F', 'count': 3}, '1870': {'cpc_group': 'Y10T', 'count': 14}, '1871': {'cpc_group': 'Y10T', 'count': 11}, '1872': {'cpc_group': 'B29C', 'count': 6}, '1873': {'cpc_group': 'B29C', 'count': 4}, '1874': {'cpc_group': 'E05B', 'count': 3}, '1875': {'cpc_group': 'A47D', 'count': 6}, '1876': {'cpc_group': 'Y10T', 'count': 14}, '1877': {'cpc_group': 'B29C', 'count': 10}, '1878': {'cpc_group': 'Y10T', 'count': 7}, '1879': {'cpc_group': 'Y10T', 'count': 14}, '1880': {'cpc_group': 'Y10T', 'count': 15}, '1881': {'cpc_group': 'Y10T', 'count': 15}, '1882': {'cpc_group': 'Y10T', 'count': 19}, '1883': {'cpc_group': 'Y10T', 'count': 26}, '1884': {'cpc_group': 'Y10T', 'count': 26}, '1885': {'cpc_group': 'Y10T', 'count': 25}, '1886': {'cpc_group': 'Y10T', 'count': 15}, '1887': {'cpc_group': 'Y10T', 'count': 13}, '1888': {'cpc_group': 'Y10T', 'count': 16}, '1889': {'cpc_group': 'Y10T', 'count': 13}, '1890': {'cpc_group': 'Y10T', 'count': 40}, '1891': {'cpc_group': 'Y10T', 'count': 20}, '1892': {'cpc_group': 'Y10T', 'count': 51}, '1893': {'cpc_group': 'Y10T', 'count': 13}, '1894': {'cpc_group': 'Y10T', 'count': 23}, '1895': {'cpc_group': 'Y10T', 'count': 11}, '1896': {'cpc_group': 'Y10T', 'count': 12}, '1897': {'cpc_group': 'Y10T', 'count': 11}, '1898': {'cpc_group': 'Y10T', 'count': 4}, '1899': {'cpc_group': 'Y10T', 'count': 8}, '1900': {'cpc_group': 'H01L', 'count': 101}, '1901': {'cpc_group': 'C25B', 'count': 6}, '1902': {'cpc_group': 'Y10S', 'count': 6}, '1903': {'cpc_group': 'B65G', 'count': 4}, '1904': {'cpc_group': 'Y10T', 'count': 11}, '1905': {'cpc_group': 'C07C', 'count': 9}, '1906': {'cpc_group': 'Y10T', 'count': 10}, '1907': {'cpc_group': 'Y10T', 'count': 9}, '1908': {'cpc_group': 'Y10T', 'count': 20}, '1909': {'cpc_group': 'F16B', 'count': 10}, '1910': {'cpc_group': 'Y10T', 'count': 12}, '1911': {'cpc_group': 'C25B', 'count': 6}, '1912': {'cpc_group': 'Y10T', 'count': 22}, '1913': {'cpc_group': 'Y10T', 'count': 27}, '1914': {'cpc_group': 'Y10T', 'count': 72}, '1915': {'cpc_group': 'Y10T', 'count': 60}, '1916': {'cpc_group': 'Y10T', 'count': 44}, '1917': {'cpc_group': 'Y10T', 'count': 28}, '1918': {'cpc_group': 'Y10T', 'count': 16}, '1919': {'cpc_group': 'Y10T', 'count': 20}, '1920': {'cpc_group': 'Y10T', 'count': 12}, '1921': {'cpc_group': 'Y10T', 'count': 32}, '1922': {'cpc_group': 'Y10T', 'count': 40}, '1923': {'cpc_group': 'Y10T', 'count': 82}, '1924': {'cpc_group': 'B65D', 'count': 20}, '1925': {'cpc_group': 'Y10T', 'count': 66}, '1926': {'cpc_group': 'Y10T', 'count': 60}, '1927': {'cpc_group': 'Y10T', 'count': 58}, '1928': {'cpc_group': 'Y10T', 'count': 34}, '1929': {'cpc_group': 'Y10T', 'count': 34}, '1930': {'cpc_group': 'B60N', 'count': 12}, '1931': {'cpc_group': 'Y10T', 'count': 78}, '1932': {'cpc_group': 'Y10T', 'count': 86}, '1933': {'cpc_group': 'Y10T', 'count': 52}, '1934': {'cpc_group': 'Y10T', 'count': 74}, '1935': {'cpc_group': 'Y10T', 'count': 62}, '1936': {'cpc_group': 'Y10T', 'count': 96}, '1937': {'cpc_group': 'Y10T', 'count': 84}, '1938': {'cpc_group': 'Y10T', 'count': 130}, '1939': {'cpc_group': 'Y10T', 'count': 138}, '1940': {'cpc_group': 'Y10T', 'count': 98}, '1941': {'cpc_group': 'Y10T', 'count': 144}, '1942': {'cpc_group': 'Y10T', 'count': 84}, '1943': {'cpc_group': 'Y10T', 'count': 40}, '1944': {'cpc_group': 'Y10T', 'count': 110}, '1945': {'cpc_group': 'Y10T', 'count': 116}, '1946': {'cpc_group': 'C10M', 'count': 101}, '1947': {'cpc_group': 'Y10T', 'count': 62}, '1948': {'cpc_group': 'Y10T', 'count': 64}, '1949': {'cpc_group': 'Y10T', 'count': 50}, '1950': {'cpc_group': 'Y10T', 'count': 118}, '1951': {'cpc_group': 'Y10T', 'count': 106}, '1952': {'cpc_group': 'Y10T', 'count': 166}, '1953': {'cpc_group': 'Y10T', 'count': 134}, '1954': {'cpc_group': 'C10M', 'count': 228}, '1955': {'cpc_group': 'Y10T', 'count': 92}, '1956': {'cpc_group': 'Y10T', 'count': 88}, '1957': {'cpc_group': 'C10M', 'count': 178}, '1958': {'cpc_group': 'Y10T', 'count': 155}, '1959': {'cpc_group': 'Y10T', 'count': 152}, '1960': {'cpc_group': 'Y10T', 'count': 146}, '1961': {'cpc_group': 'Y10T', 'count': 106}, '1962': {'cpc_group': 'C10M', 'count': 128}, '1963': {'cpc_group': 'Y10T', 'count': 114}, '1964': {'cpc_group': 'C10M', 'count': 225}, '1965': {'cpc_group': 'Y10T', 'count': 220}, '1966': {'cpc_group': 'C10M', 'count': 337}, '1967': {'cpc_group': 'C10M', 'count': 189}, '1968': {'cpc_group': 'Y10T', 'count': 181}, '1969': {'cpc_group': 'Y10T', 'count': 215}, '1970': {'cpc_group': 'Y10T', 'count': 232}, '1971': {'cpc_group': 'Y10T', 'count': 294}, '1972': {'cpc_group': 'C10M', 'count': 314}, '1973': {'cpc_group': 'Y10T', 'count': 302}, '1974': {'cpc_group': 'Y10T', 'count': 452}, '1975': {'cpc_group': 'Y10T', 'count': 411}, '1976': {'cpc_group': 'Y10T', 'count': 427}, '1977': {'cpc_group': 'Y10T', 'count': 364}, '1978': {'cpc_group': 'Y10T', 'count': 422}, '1979': {'cpc_group': 'C07D', 'count': 292}, '1980': {'cpc_group': 'Y10T', 'count': 362}, '1981': {'cpc_group': 'Y10T', 'count': 380}, '1982': {'cpc_group': 'Y10T', 'count': 424}, '1983': {'cpc_group': 'Y10T', 'count': 428}, '1984': {'cpc_group': 'Y10T', 'count': 468}, '1985': {'cpc_group': 'Y10T', 'count': 466}, '1986': {'cpc_group': 'Y10T', 'count': 410}, '1987': {'cpc_group': 'Y10T', 'count': 566}, '1988': {'cpc_group': 'Y10T', 'count': 574}, '1989': {'cpc_group': 'Y10T', 'count': 584}, '1990': {'cpc_group': 'Y10T', 'count': 520}, '1991': {'cpc_group': 'Y10T', 'count': 528}, '1992': {'cpc_group': 'Y10T', 'count': 591}, '1993': {'cpc_group': 'Y10T', 'count': 488}, '1994': {'cpc_group': 'Y10T', 'count': 609}, '1995': {'cpc_group': 'Y10T', 'count': 669}, '1996': {'cpc_group': 'Y10T', 'count': 744}, '1997': {'cpc_group': 'Y10T', 'count': 683}, '1998': {'cpc_group': 'A61K', 'count': 806}, '1999': {'cpc_group': 'A61K', 'count': 1046}, '2000': {'cpc_group': 'H01L', 'count': 1450}, '2001': {'cpc_group': 'H01L', 'count': 1707}, '2002': {'cpc_group': 'H01L', 'count': 2196}, '2003': {'cpc_group': 'H01L', 'count': 2170}, '2004': {'cpc_group': 'H01L', 'count': 2951}, '2005': {'cpc_group': 'H01L', 'count': 2526}, '2006': {'cpc_group': 'H01L', 'count': 3575}, '2007': {'cpc_group': 'H01L', 'count': 3545}, '2008': {'cpc_group': 'H01L', 'count': 4994}, '2009': {'cpc_group': 'H01L', 'count': 5982}, '2010': {'cpc_group': 'H01L', 'count': 4474}, '2011': {'cpc_group': 'H01L', 'count': 4099}, '2012': {'cpc_group': 'H01L', 'count': 3636}, '2013': {'cpc_group': 'H01L', 'count': 3487}, '2014': {'cpc_group': 'H01L', 'count': 4811}, '2015': {'cpc_group': 'H01L', 'count': 6704}, '2016': {'cpc_group': 'A61K', 'count': 7322}, '2017': {'cpc_group': 'A61K', 'count': 7894}, '2018': {'cpc_group': 'A61K', 'count': 8577}, '2019': {'cpc_group': 'H01L', 'count': 7587}, '2020': {'cpc_group': 'H01L', 'count': 10200}, '2021': {'cpc_group': 'A61K', 'count': 11053}, '2022': {'cpc_group': 'H01L', 'count': 8733}, '2023': {'cpc_group': 'H01L', 'count': 6777}, '2024': {'cpc_group': 'H01L', 'count': 4298}}}}

exec(code, env_args)
