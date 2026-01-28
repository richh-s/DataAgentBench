code = """import json
import re
import pandas as pd
import numpy as np
from collections import defaultdict, Counter

# Load publication data
pub_file = locals()['var_functions.query_db:12']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print('Processing data...')

# Extract CPC group counts per year (focusing on level 5 = 4-char groups)
group_year_counts = defaultdict(lambda: defaultdict(int))
year_group_counts = defaultdict(lambda: defaultdict(int))

for item in pub_data:
    pub_date = item.get('publication_date', '')
    if not pub_date:
        continue
        
    year_match = re.search(r'(\d{4})', pub_date)
    if not year_match:
        continue
        
    year = int(year_match.group(1))
    if year < 2010 or year > 2023:  # Focus on recent years
        continue
    
    cpc_str = item.get('cpc', '[]')
    if not cpc_str or cpc_str == '[]':
        continue
        
    try:
        cpc_list = json.loads(cpc_str)
        for cpc in cpc_list:
            full_code = cpc.get('code', '')
            if not full_code:
                continue
            # Extract level 5 group (first 4 chars before slash)
            if '/' in full_code:
                group = full_code.split('/')[0][:4]
                if len(group) == 4:  # Valid level 5 group
                    group_year_counts[group][year] += 1
                    year_group_counts[year][group] += 1
    except:
        continue

years = sorted(year_group_counts.keys())
groups = sorted(group_year_counts.keys())

print(f'Years: {years}')
print(f'Groups: {len(groups)}')
print(f'Year 2022 groups: {len(year_group_counts[2022])}')

# Create count matrix
matrix = []
for group in groups:
    row = [group_year_counts[group].get(year, 0) for year in years]
    matrix.append(row)

matrix_df = pd.DataFrame(matrix, index=groups, columns=years)

# Calculate EMA (α=0.2)
α = 0.2
ema_matrix = []
for i, group in enumerate(groups):
    values = matrix_df.iloc[i].values
    ema = [values[0]]
    for j in range(1, len(values)):
        ema.append(α * values[j] + (1-α) * ema[-1])
    ema_matrix.append(ema)

ema_df = pd.DataFrame(ema_matrix, index=groups, columns=years)

# For each year, find top 10% groups by EMA
top_groups_per_year = {}
for year in years:
    year_ema = ema_df[year].sort_values(ascending=False)
    top_n = max(1, int(len(year_ema) * 0.1))
    top_groups = set(year_ema.head(top_n).index)
    top_groups_per_year[year] = top_groups

# Find groups whose best year is 2022 and were top performers that year
groups_best_2022 = []
for group in groups:
    group_ema = ema_df.loc[group]
    best_year = group_ema.idxmax()
    if best_year == 2022 and group in top_groups_per_year[2022]:
        groups_best_2022.append(group)

# Filter to only level 5 groups (already are, but verify)
result = {
    'count': len(groups_best_2022),
    'groups': sorted(groups_best_2022)
}

print('Groups with best year 2022:', len(groups_best_2022))
if groups_best_2022:
    print('Sample:', groups_best_2022[:10])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'count': 0, 'groups': []}, 'var_functions.execute_python:26': {'years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'top_years': {'2018': 16293, '2021': 16079, '2022': 16012, '2023': 14217, '2017': 13795}, 'cpc_total': 2685154, 'samples': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10']}}

exec(code, env_args)
