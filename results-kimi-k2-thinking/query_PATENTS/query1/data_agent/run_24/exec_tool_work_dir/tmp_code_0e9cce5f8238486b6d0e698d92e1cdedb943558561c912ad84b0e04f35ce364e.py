code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Read the data files
pub_file_path = locals()['var_functions.query_db:14']
cpc_file_path = locals()['var_functions.query_db:18']

with open(pub_file_path, 'r') as f:
    publications = json.load(f)

with open(cpc_file_path, 'r') as f:
    level5_codes = json.load(f)

# Create a set of level 5 codes for fast lookup
level5_symbols = set([item['symbol'] for item in level5_codes])

print(f"Total publications: {len(publications)}")
print(f"Number of level 5 CPC codes: {len(level5_symbols)}")
print(f"Sample level 5 codes: {list(level5_symbols)[:10]}")

# Parse CPC codes and extract years
cpc_year_counts = {}
invalid_dates = 0
valid_entries = 0

for pub in publications:
    # Parse publication date
    try:
        date_str = pub['publication_date']
        year = int(date_str.split(', ')[1])
    except:
        invalid_dates += 1
        continue
    
    # Parse CPC codes
    try:
        cpc_data = json.loads(pub['cpc'])
        for cpc_entry in cpc_data:
            cpc_code = cpc_entry['code']
            # Count by year and CPC code
            if year not in cpc_year_counts:
                cpc_year_counts[year] = {}
            cpc_year_counts[year][cpc_code] = cpc_year_counts[year].get(cpc_code, 0) + 1
            valid_entries += 1
    except:
        continue

# Get all unique CPC codes and years
all_cpc_codes = set()
all_years = sorted(cpc_year_counts.keys())
for year, counts in cpc_year_counts.items():
    all_cpc_codes.update(counts.keys())

print(f"Years: {all_years[:5]}...{all_years[-5:]}")
print(f"Total unique CPC codes: {len(all_cpc_codes)}")
print(f"Valid entries: {valid_entries}")

# Calculate Exponential Moving Average (EMA) for each CPC code
# EMA formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
alpha = 0.2

# Create a DataFrame with years as rows and CPC codes as columns
df_data = []
for year in all_years:
    row = {}
    for cpc in all_cpc_codes:
        row[cpc] = cpc_year_counts.get(year, {}).get(cpc, 0)
    df_data.append(row)

df = pd.DataFrame(df_data, index=all_years)

print(f"DataFrame shape: {df.shape}")
print(f"DataFrame index (years): {df.index.tolist()[:10]}...{df.index.tolist()[-10:]}")

# Calculate EMA for each CPC code (column)
ema_df = df.ewm(alpha=alpha, adjust=False).mean()

print(f"EMA DataFrame shape: {ema_df.shape}")

# For each CPC code, find the year with the highest EMA
cpc_best_years = {}
for cpc_code in all_cpc_codes:
    if cpc_code in ema_df.columns:
        max_year = ema_df[cpc_code].idxmax()
        max_ema = ema_df[cpc_code].max()
        cpc_best_years[cpc_code] = {'year': max_year, 'ema': max_ema}

# Filter for CPC codes where best year is 2022
cpc_best_2022 = {code: info for code, info in cpc_best_years.items() if info['year'] == 2022}

print(f"CPC codes with best year = 2022: {len(cpc_best_2022)}")

# Filter to only include level 5 CPC codes
# Level 5 codes should be in format like "A01B1/00" (subclass/group/subgroup)
# Let's check the actual format of our CPC codes
sample_codes = list(all_cpc_codes)[:20]
print(f"Sample CPC codes: {sample_codes}")

# Check if any of our codes are level 5
level5_matches = []
for code in sample_codes:
    # Check if the base symbol (first part) is in level5_symbols
    base_symbol = code.split('/')[0] if '/' in code else code
    base_symbol = ''.join([c for c in base_symbol if not c.isdigit()])
    if base_symbol in level5_symbols:
        level5_matches.append(code)

print(f"Sample level 5 matches: {level5_matches[:10]}")

# Analyze what level the codes in our database actually are
# Let's group by format
def get_format(code):
    if '/' in code:
        return 'subgroup'
    elif any(c.isdigit() for c in code):
        return 'group'
    else:
        return 'subclass'

formats = {}
for code in list(all_cpc_codes)[:100]:  # Sample first 100
    fmt = get_format(code)
    formats[fmt] = formats.get(fmt, 0) + 1

print(f"Format distribution (sample): {formats}")

# Save intermediate results
result = {
    'total_cpc_codes': len(all_cpc_codes),
    'codes_best_2022': len(cpc_best_2022),
    'sample_codes': sample_codes,
    'format_distribution': formats,
    'sample_level5_matches': level5_matches[:10],
    'level5_symbols_count': len(level5_symbols),
    'years_count': len(all_years),
    'min_year': min(all_years),
    'max_year': max(all_years)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'invalid_dates': 139721, 'valid_entries': 1333969, 'unique_cpc_codes': 143452, 'years': [1837, 1839, 1841, 1842, 1844, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'min_year': 1837, 'max_year': 2024}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
