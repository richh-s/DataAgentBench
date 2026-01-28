code = """import json
import pandas as pd
import numpy as np

# Load the CPC level 5 and year counts data
level5_symbols_var = locals()['var_functions.query_db:24']
if isinstance(level5_symbols_var, str):
    with open(level5_symbols_var, 'r') as f:
        level5_symbols_data = json.load(f)
else:
    level5_symbols_data = level5_symbols_var

# Extract all level 5 CPC symbols
level5_symbols = [record['symbol'] for record in level5_symbols_data]

# Load CPC year counts data
cpc_analysis_var = locals()['var_functions.execute_python:22']
if isinstance(cpc_analysis_var, str):
    with open(cpc_analysis_var, 'r') as f:
        cpc_analysis = json.load(f)
else:
    cpc_analysis = cpc_analysis_var

# Parse CPC year counts from string format {code|year: count}
cpc_year_counts_raw = cpc_analysis['cpc_year_counts']
years = cpc_analysis['years']

# Build a proper data structure: cpc -> year -> count
cpc_yearly_counts = {}
for key, count in cpc_year_counts_raw.items():
    try:
        code, year = key.split('|')
        year = int(year)
        if code not in cpc_yearly_counts:
            cpc_yearly_counts[code] = {}
        cpc_yearly_counts[code][year] = count
    except:
        continue

print('Total CPC codes found: ' + str(len(cpc_yearly_counts)))

# Focus on recent years (2010-2024) for EMA calculation
recent_years = [y for y in years if y >= 2010]
print('Recent years for analysis: ' + str(recent_years[:8]) + '...' + str(recent_years[-3:]))

# Calculate EMA for each CPC code with smoothing factor 0.2
alpha = 0.2
cpc_ema_data = {}

for cpc_code in cpc_yearly_counts.keys():
    # Filter for only level 5 groups (main group codes without subgroup)
    if cpc_code not in level5_symbols:
        continue
    
    ema_values = []
    ema_by_year = {}
    prev_ema = None
    
    for year in sorted(recent_years):
        # Get count for this year, default to 0
        count = cpc_yearly_counts[cpc_code].get(year, 0)
        
        if prev_ema is None:
            # First EMA is just the first value
            ema = count
        else:
            # EMA formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
            ema = alpha * count + (1 - alpha) * prev_ema
        
        ema_values.append(ema)
        ema_by_year[year] = ema
        prev_ema = ema
    
    if ema_values:  # Only store if we have data
        cpc_ema_data[cpc_code] = ema_by_year

print('CPC codes with EMA data: ' + str(len(cpc_ema_data)))

# Find the CPC with highest EMA for each year
best_cpc_per_year = {}
for year in recent_years:
    max_ema = -1
    best_cpc = None
    
    for cpc_code, ema_by_year in cpc_ema_data.items():
        if year in ema_by_year:
            if ema_by_year[year] > max_ema:
                max_ema = ema_by_year[year]
                best_cpc = cpc_code
    
    if best_cpc:
        best_cpc_per_year[year] = {
            'cpc_code': best_cpc,
            'ema': max_ema
        }

print('Best CPC per recent year:')
for year in sorted(best_cpc_per_year.keys())[-5:]:
    data = best_cpc_per_year[year]
    print('  ' + str(year) + ': ' + data['cpc_code'] + ' (EMA: ' + str(round(data['ema'], 2)) + ')')

result = {
    'total_cpc_codes': len(cpc_yearly_counts),
    'level5_cpc_with_ema': len(cpc_ema_data),
    'recent_years_count': len(recent_years),
    'best_cpc_per_year': best_cpc_per_year,
    'sample_cpc_ema': {code: dict(list(ema_by_year.items())[-3:]) for code, ema_by_year in list(cpc_ema_data.items())[:3]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_symbols_count': 677, 'years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'sample_cpc_counts': {'C01B33|2021': 57, 'C01B35|2021': 6, 'H01M10|2021': 1288, 'C01G45|2021': 10, 'C01P2002|2021': 86}}}

exec(code, env_args)
