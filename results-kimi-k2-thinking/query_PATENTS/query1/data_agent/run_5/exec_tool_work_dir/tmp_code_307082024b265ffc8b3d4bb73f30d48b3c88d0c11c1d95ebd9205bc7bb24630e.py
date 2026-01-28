code = """import json
import re
import pandas as pd
import numpy as np

# Load the publication data
file_path = 'file_storage/functions.query_db:14.json'
with open(file_path, 'r') as f:
    publication_data = json.load(f)

# Load level 5 CPC symbols
file_path_cpc5 = 'file_storage/functions.query_db:20.json'
with open(file_path_cpc5, 'r') as f:
    cpc_level5_data = json.load(f)

cpc_level5_symbols = set(item['symbol'] for item in cpc_level5_data)

# Process publication data to extract years and CPC codes
cpc_yearly_counts = {}

# Date parsing regex to extract year
date_pattern = r'(\d{4})'

for record in publication_data:
    # Extract year from publication_date
    pub_date = record.get('publication_date', '')
    year_match = re.search(date_pattern, pub_date)
    if year_match:
        year = int(year_match.group(1))
        # Parse CPC codes
        cpc_str = record.get('cpc', '')
        if cpc_str:
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code', '')
                    if cpc_code:
                        # Extract level 5 group code
                        if '/' in cpc_code:
                            main_part = cpc_code.split('/')[0]
                            match = re.match(r'^([A-Z]+\d+[A-Z]?)', main_part)
                            if match:
                                level5_code = match.group(1)
                            else:
                                continue
                        else:
                            level5_code = cpc_code
                        
                        # Check if this is a valid level 5 code
                        if level5_code in cpc_level5_symbols:
                            if level5_code not in cpc_yearly_counts:
                                cpc_yearly_counts[level5_code] = {}
                            cpc_yearly_counts[level5_code][year] = cpc_yearly_counts[level5_code].get(year, 0) + 1
            except:
                continue

# Get all years present in the data
all_years = set()
for code, yearly_data in cpc_yearly_counts.items():
    all_years.update(yearly_data.keys())

if not all_years:
    print('__RESULT__:')
    print(json.dumps({'error': 'No year data found'}, indent=2))
else:
    all_years = sorted(list(all_years))
    year_range = list(range(min(all_years), max(all_years) + 1))

    # Calculate EMA for each CPC code
    alpha = 0.2
    cpc_best_years = {}

    for cpc_code, yearly_counts in cpc_yearly_counts.items():
        # Initialize EMA
        prev_ema = None
        
        for year in year_range:
            count = yearly_counts.get(year, 0)
            
            if prev_ema is None:
                # First value - use actual count
                ema = count
            else:
                # EMA calculation
                ema = alpha * count + (1 - alpha) * prev_ema
            
            prev_ema = ema
        
        # Find the year with maximum EMA value
        # Since EMA is cumulative, the peak is more likely in recent years with high activity
        # For each year, we need to recalculate forward from the start to get the EMA at that point
        best_ema_value = 0
        best_year = None
        
        for target_year in year_range:
            # Calculate EMA up to this year
            ema_at_year = None
            temp_prev_ema = None
            
            for year in year_range:
                count = yearly_counts.get(year, 0)
                
                if temp_prev_ema is None:
                    temp_ema = count
                else:
                    temp_ema = alpha * count + (1 - alpha) * temp_prev_ema
                
                temp_prev_ema = temp_ema
                
                if year == target_year:
                    ema_at_year = temp_ema
                    break
            
            # Track the best (highest EMA) year
            if ema_at_year is not None and ema_at_year > best_ema_value:
                best_ema_value = ema_at_year
                best_year = target_year
        
        if best_year is not None:
            cpc_best_years[cpc_code] = {
                'best_year': best_year,
                'best_ema_value': best_ema_value
            }

    # Filter for CPC codes whose best year is 2022
    cpc_best_in_2022 = [cpc_code for cpc_code, data in cpc_best_years.items() if data['best_year'] == 2022]

    print('__RESULT__:')
    print(json.dumps({
        'total_cpc_codes_analyzed': len(cpc_best_years),
        'codes_with_best_year_2022': len(cpc_best_in_2022),
        'sample_results_2022': cpc_best_in_2022[:50],
        'all_results_2022': cpc_best_in_2022
    }, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.execute_python:10': {'file_path': 'file_storage/functions.query_db:2.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:12': {'total_records': 10, 'keys_in_record': ['Patents_info', 'cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'sample_cpc_parsed': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}], 'sample_publication_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 277813, 'sample_record': {'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': 'Aug 3rd, 2021'}, 'cpi_codes_sample': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}], 'sample_publication_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_level5_symbols': 677, 'sample_level5_symbols': ['A21B', 'F16C', 'H03L', 'B68F', 'A61N', 'G01N', 'A61D', 'B23G', 'E04D', 'G01T']}, 'var_functions.execute_python:24': {'total_cpc_codes': 175852, 'sample_cpc_data': {'C01B33/00': {'2021': 4, '2007': 1, '2020': 1}, 'C01B35/00': {'2021': 3, '2019': 3, '2022': 1}, 'H01M10/0565': {'2021': 34, '2020': 15, '2006': 11}, 'H01M10/0562': {'2021': 57, '2024': 21, '2015': 9}, 'C01G45/006': {'2021': 3, '2020': 2, '2019': 2}}}, 'var_functions.execute_python:26': {'total_level5_codes_with_data': 669, 'all_years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'year_range': '1837 to 2024', 'sample_level5_data': {'C01B': {'2021': 530, '1975': 37, '2007': 119}, 'H01M': {'2021': 4424, '2020': 3640, '2022': 4350}, 'C01G': {'2021': 102, '2023': 121, '2024': 47}, 'C01P': {'2021': 398, '2022': 438, '1977': 37}, 'Y02E': {'2021': 1577, '2020': 1298, '2022': 1490}, 'F16H': {'2020': 742, '2024': 153, '2008': 276}, 'B29C': {'2021': 2268, '2022': 1838, '2024': 711}, 'C08J': {'2021': 800, '1989': 45, '2000': 82}, 'B32B': {'2021': 3333, '2005': 296, '1989': 83}, 'C09D': {'2021': 798, '1995': 43, '2008': 144}}}}

exec(code, env_args)
