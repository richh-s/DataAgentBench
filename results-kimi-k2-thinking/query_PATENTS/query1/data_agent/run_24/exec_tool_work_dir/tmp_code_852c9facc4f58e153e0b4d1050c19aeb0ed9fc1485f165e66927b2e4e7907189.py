code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict
import re

# Read publications data
pub_file_path = locals()['var_functions.query_db:42']
with open(pub_file_path, 'r') as f:
    publications = json.load(f)

print("Processing publications...")

# Step 1: Extract level 5 CPC codes and count by year
# Level 5 format: Section(1 letter) + Class(2 digits) + Subclass(1 letter) + Main Group(1-3 digits)
# Examples: "C01B33/00" -> "C01B33", "H01M10/0565" -> "H01M10", "A61K31/00" -> "A61K31"

cpc_year_counts = defaultdict(lambda: defaultdict(int))
invalid_dates = 0
total_processed = 0

for pub in publications:
    # Parse publication date
    try:
        date_str = pub['publication_date']
        year = int(date_str.split(', ')[1])
    except:
        invalid_dates += 1
        continue
    
    # Parse CPC codes JSON
    try:
        cpc_data = json.loads(pub['cpc'])
        for entry in cpc_data:
            full_code = entry['code']
            total_processed += 1
            
            # Extract level 5 code
            if '/' in full_code:
                main_part = full_code.split('/')[0]  # e.g., "C01B33"
                
                # Match pattern: Section(letter) + Class(2 digits) + Subclass(letter) + Main Group(digits)
                # This matches codes like: C01B33, H01M10, A61K31, G06F16
                match = re.match(r'^([A-Z][0-9]{2}[A-Z])([0-9]{1,3})$', main_part)
                if match:
                    subclass = match.group(1)      # e.g., "C01B"
                    main_group = match.group(2)    # e.g., "33"
                    level5_code = subclass + main_group  # e.g., "C01B33"
                    cpc_year_counts[year][level5_code] += 1
                    
    except:
        continue

# Get all years and codes
all_years = sorted(cpc_year_counts.keys())
all_level5_codes = set()
for year_counts in cpc_year_counts.values():
    all_level5_codes.update(year_counts.keys())

print("Year range: {} - {}".format(min(all_years), max(all_years)))
print("Years with data: {}".format(len(all_years)))
print("Invalid dates: {}".format(invalid_dates))
print("Total CPC entries processed: {}".format(total_processed))
print("Unique level 5 CPC codes: {}".format(len(all_level5_codes)))

if len(all_level5_codes) > 0:
    print("Sample codes: {}".format(list(all_level5_codes)[:10]))
    
    # Check if 2022 is in the data
    if 2022 in all_years:
        print("2022 data exists: {} codes".format(len(cpc_year_counts[2022])))
    else:
        print("2022 not found in years. Closest years: {}".format([y for y in all_years if abs(y-2022) <= 2]))

    # Step 2: Create DataFrame
    df_data = []
    for year in all_years:
        row = {}
        for code in all_level5_codes:
            row[code] = cpc_year_counts[year].get(code, 0)
        df_data.append(row)

    df = pd.DataFrame(df_data, index=all_years)
    print("DataFrame shape: {}".format(df.shape))

    # Step 3: Calculate EMA with alpha=0.2 (smoothing factor)
    alpha = 0.2
    ema_df = df.ewm(alpha=alpha, adjust=False).mean()

    # Step 4: Find CPC codes where 2022 has the highest EMA
    codes_best_in_2022 = []
    for code in all_level5_codes:
        if code in ema_df.columns and 2022 in ema_df.index:
            # Find year with maximum EMA for this code
            max_year = ema_df[code].idxmax()
            if max_year == 2022:
                codes_best_in_2022.append(code)

    print("Codes with best year = 2022: {}".format(len(codes_best_in_2022)))
    
    if len(codes_best_in_2022) > 0:
        print("First 10 codes: {}".format(codes_best_in_2022[:10]))
    
    result = codes_best_in_2022
else:
    print("No level 5 codes found!")
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'invalid_dates': 139721, 'valid_entries': 1333969, 'unique_cpc_codes': 143452, 'years': [1837, 1839, 1841, 1842, 1844, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'min_year': 1837, 'max_year': 2024}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 143452, 'codes_best_2022': 12035, 'sample_codes': ['G11B3/5845', 'H03M1/0854', 'A61K2800/546', 'H01L24/29', 'B65B19/223', 'D07B1/062', 'B29D29/00', 'C04B14/10', 'A47C7/16', 'B62D55/062', 'B05D7/544', 'A61C11/00', 'Y10T137/402', 'H10B12/37', 'H02G7/18', 'G06F2209/5022', 'C22C1/1068', 'B60L15/42', 'B32B5/10', 'G11C7/1069'], 'format_distribution': {'subgroup': 100}, 'sample_level5_matches': [], 'level5_symbols_count': 677, 'years_count': 182, 'min_year': 1837, 'max_year': 2024}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:38': ['H04', 'B65', 'B27', 'E01', 'F04', 'F23', 'F17', 'F25', 'B25', 'B30', 'B63', 'B22', 'C30', 'D01', 'B02', 'G07', 'C21', 'B21', 'B43', 'B23', 'B24', 'C07', 'A43', 'B82', 'B61', 'G21', 'G04', 'C09', 'C06', 'F16', 'B08', 'B44', 'B62', 'B03', 'C05', 'C12', 'C22', 'B66', 'B05', 'D06', 'F41', 'F15', 'B01', 'A61', 'B60', 'H01', 'B64', 'C04', 'C25', 'B33', 'D02', 'B29', 'A41', 'D07'], 'var_functions.execute_python:40': 'file_storage/functions.execute_python:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': 'file_storage/functions.execute_python:44.json'}

exec(code, env_args)
