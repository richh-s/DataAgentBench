code = """import json
import pandas as pd
import numpy as np

# Load the CPC level 5 symbols
level5_symbols_var = locals()['var_functions.query_db:38']
if isinstance(level5_symbols_var, str):
    with open(level5_symbols_var, 'r') as f:
        level5_symbols_data = json.load(f)
else:
    level5_symbols_data = level5_symbols_var

# Create a set of level 5 symbols for fast lookup
level5_symbols = set(record['symbol'] for record in level5_symbols_data)
print('Loaded ' + str(len(level5_symbols)) + ' level 5 CPC symbols')

# Load the raw publication data
publication_data_var = locals()['var_functions.query_db:6']
if isinstance(publication_data_var, str):
    with open(publication_data_var, 'r') as f:
        publication_data = json.load(f)
else:
    publication_data = publication_data_var

print('Loaded ' + str(len(publication_data)) + ' publication records')

# Function to extract year from natural language date
import re
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group())
    return None

# Process data more carefully, handling the CPC parsing
cpc_year_counts = {}
valid_records = 0
all_years = set()
sample_cpc_codes = []

for i, record in enumerate(publication_data):
    if not isinstance(record, dict):
        continue
        
    cpc_str = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    year = extract_year(pub_date)
    
    if not year or not cpc_str:
        continue
    
    try:
        # Parse the CPC JSON string
        cpc_list = json.loads(cpc_str)
        for item in cpc_list:
            if isinstance(item, dict) and 'code' in item:
                full_code = item['code']
                
                # Extract the level 5 code (need to handle patterns like C01B33/00 -> C01B, H01M10/0565 -> H01M)
                # Level 5 codes are typically section + class + subclass (4 chars for subclass)
                # Patterns like: C01B, H01M, G06F, etc.
                
                # Remove any subgroup after /
                if '/' in full_code:
                    main_part = full_code.split('/')[0]
                else:
                    main_part = full_code
                
                # Try to find the level 5 symbol by progressively shortening the string
                level5_code = None
                for j in range(len(main_part), 3, -1):  # Try lengths from full down to 4
                    candidate = main_part[:j]
                    if candidate in level5_symbols:
                        level5_code = candidate
                        break
                
                if level5_code:
                    if len(sample_cpc_codes) < 10:
                        sample_cpc_codes.append((full_code, level5_code))
                    
                    valid_records += 1
                    all_years.add(year)
                    key = (level5_code, year)
                    cpc_year_counts[key] = cpc_year_counts.get(key, 0) + 1
                    
    except Exception as e:
        continue

print('Processed ' + str(valid_records) + ' valid CPC/year entries')
if all_years:
    print('Years range: ' + str(min(all_years)) + ' to ' + str(max(all_years)))
else:
    print('No years found')
    
print('Sample CPC mappings (full -> level5):')
for mapping in sample_cpc_codes[:5]:
    print('  ' + mapping[0] + ' -> ' + mapping[1])

# Get recent years for analysis
recent_years = sorted([y for y in all_years if y >= 2010]) if all_years else []
print('Recent years for analysis: ' + str(len(recent_years)))

# Show distribution of CPC codes found in data
unique_level5_in_data = set(k[0] for k in cpc_year_counts.keys())
print('Unique level 5 CPC codes found in publications: ' + str(len(unique_level5_in_data)))

# If we have data, calculate EMA
if valid_records > 0 and recent_years:
    # Calculate EMA for each level 5 CPC code
    alpha = 0.2
    cpc_ema_data = {}
    
    for cpc_code in unique_level5_in_data:
        # Get all counts for this CPC code
        yearly_counts = {}
        for year in recent_years:
            yearly_counts[year] = cpc_year_counts.get((cpc_code, year), 0)
        
        # Calculate EMA
        ema_by_year = {}
        prev_ema = None
        
        for year in sorted(recent_years):
            count = yearly_counts[year]
            
            if prev_ema is None:
                ema = count
            else:
                ema = alpha * count + (1 - alpha) * prev_ema
            
            ema_by_year[year] = ema
            prev_ema = ema
        
        cpc_ema_data[cpc_code] = ema_by_year
    
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
    
    print('Best CPC per year (sample):')
    for year in sorted(best_cpc_per_year.keys())[-5:]:
        data = best_cpc_per_year[year]
        print('  ' + str(year) + ': ' + data['cpc_code'] + ' (EMA: ' + str(round(data['ema'], 2)) + ')')
    
    # Find CPC codes whose best year is 2022
    best_year_2022_cpcs = []
    for cpc_code, ema_by_year in cpc_ema_data.items():
        max_ema = -1
        best_year = None
        for year, ema in ema_by_year.items():
            if ema > max_ema:
                max_ema = ema
                best_year = year
        
        if best_year == 2022:
            best_year_2022_cpcs.append(cpc_code)
    
    print('CPC codes with best year 2022: ' + str(len(best_year_2022_cpcs)))
    if best_year_2022_cpcs:
        print('Sample CPC codes with best year 2022: ' + str(best_year_2022_cpcs[:10]))
    
    result = {
        'valid_entries_processed': valid_records,
        'unique_level5_codes_found': len(unique_level5_in_data),
        'recent_years_count': len(recent_years),
        'sample_mappings': sample_cpc_codes[:10],
        'best_cpc_per_year_sample': {str(k): v for k, v in list(best_cpc_per_year.items())[-5:]},
        'cpc_best_year_2022': best_year_2022_cpcs,
        'years_available': list(sorted(all_years))[-10:] if all_years else []
    }
else:
    result = {
        'valid_entries_processed': valid_records,
        'unique_level5_codes_found': len(unique_level5_in_data),
        'recent_years_count': len(recent_years),
        'sample_mappings': sample_cpc_codes[:10],
        'cpc_year_counts_sample': dict(list(cpc_year_counts.items())[:10]),
        'years_available': list(sorted(all_years))[-10:] if all_years else [],
        'error': 'No EMA data calculated'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'level5_symbols_count': 677, 'years': [1837, 1839, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'sample_cpc_counts': {'C01B33|2021': 57, 'C01B35|2021': 6, 'H01M10|2021': 1288, 'C01G45|2021': 10, 'C01P2002|2021': 86}}, 'var_functions.execute_python:28': {'total_cpc_codes': 9947, 'level5_cpc_with_ema': 0, 'recent_years_count': 15, 'best_cpc_per_year': {}, 'sample_cpc_ema': {}}, 'var_functions.query_db:30': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': 'Aug 3rd, 2021'}], 'var_functions.query_db:34': [{'symbol': 'A62B', 'level': '5.0', 'titleFull': 'DEVICES, APPARATUS OR METHODS FOR LIFE-SAVING'}, {'symbol': 'A63G', 'level': '5.0', 'titleFull': 'MERRY-GO-ROUNDS; SWINGS; ROCKING-HORSES; CHUTES; SWITCHBACKS; SIMILAR DEVICES FOR PUBLIC AMUSEMENT'}, {'symbol': 'A63K', 'level': '5.0', 'titleFull': 'RACING; RIDING SPORTS; EQUIPMENT OR ACCESSORIES THEREFOR'}, {'symbol': 'A63B', 'level': '5.0', 'titleFull': 'APPARATUS FOR PHYSICAL TRAINING, GYMNASTICS, SWIMMING, CLIMBING, OR FENCING; BALL GAMES; TRAINING EQUIPMENT'}, {'symbol': 'A63J', 'level': '5.0', 'titleFull': 'DEVICES FOR THEATRES, CIRCUSES, OR THE LIKE; CONJURING APPLIANCES OR THE LIKE'}, {'symbol': 'A63C', 'level': '5.0', 'titleFull': 'SKATES; SKIS; ROLLER SKATES; DESIGN OR LAYOUT OF COURTS, RINKS OR THE LIKE'}, {'symbol': 'A63D', 'level': '5.0', 'titleFull': 'BOWLING GAMES, e.g. SKITTLES, BOCCE OR BOWLS; INSTALLATIONS THEREFOR; BAGATELLE OR SIMILAR GAMES; BILLIARDS'}, {'symbol': 'A63F', 'level': '5.0', 'titleFull': 'CARD, BOARD, OR ROULETTE GAMES; INDOOR GAMES USING SMALL MOVING PLAYING BODIES; VIDEO GAMES; GAMES NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'C25D', 'level': '5.0', 'titleFull': 'PROCESSES FOR THE ELECTROLYTIC OR ELECTROPHORETIC PRODUCTION OF COATINGS; ELECTROFORMING; APPARATUS THEREFOR'}, {'symbol': 'A63H', 'level': '5.0', 'titleFull': 'TOYS, e.g. TOPS, DOLLS, HOOPS OR BUILDING BLOCKS'}, {'symbol': 'A99Z', 'level': '5.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B01J', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL PROCESSES, e.g. CATALYSIS OR COLLOID CHEMISTRY; THEIR RELEVANT APPARATUS'}, {'symbol': 'B01B', 'level': '5.0', 'titleFull': 'BOILING; BOILING APPARATUS ; EVAPORATION; EVAPORATION APPARATUS'}, {'symbol': 'B01D', 'level': '5.0', 'titleFull': 'SEPARATION'}, {'symbol': 'B01L', 'level': '5.0', 'titleFull': 'CHEMICAL OR PHYSICAL LABORATORY APPARATUS FOR GENERAL USE'}, {'symbol': 'B01F', 'level': '5.0', 'titleFull': 'MIXING, e.g. DISSOLVING, EMULSIFYING OR DISPERSING'}, {'symbol': 'B02C', 'level': '5.0', 'titleFull': 'CRUSHING, PULVERISING, OR DISINTEGRATING IN GENERAL; MILLING GRAIN'}, {'symbol': 'B02B', 'level': '5.0', 'titleFull': 'PREPARING GRAIN FOR MILLING; REFINING GRANULAR FRUIT TO COMMERCIAL PRODUCTS BY WORKING THE SURFACE'}, {'symbol': 'B03B', 'level': '5.0', 'titleFull': 'SEPARATING SOLID MATERIALS USING LIQUIDS OR USING PNEUMATIC TABLES OR JIGS'}, {'symbol': 'B03D', 'level': '5.0', 'titleFull': 'FLOTATION; DIFFERENTIAL SEDIMENTATION'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'valid_entries_processed': 0, 'unique_level5_codes_found': 0, 'recent_years_count': 0, 'sample_mappings': [], 'cpc_year_counts_sample': {}, 'years_available': []}}

exec(code, env_args)
