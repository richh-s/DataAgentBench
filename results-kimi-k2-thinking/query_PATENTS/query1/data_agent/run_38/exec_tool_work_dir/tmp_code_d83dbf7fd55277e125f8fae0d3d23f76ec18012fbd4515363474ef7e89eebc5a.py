code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load the full patent data
patent_data_path = locals()['var_functions.query_db:5']
with open(patent_data_path, 'r') as f:
    patent_data = json.load(f)

# Load CPC level 5 symbols
cpc_symbols_path = locals()['var_functions.query_db:8']
with open(cpc_symbols_path, 'r') as f:
    cpc_level5_data = json.load(f)

# Create a set of level 5 CPC symbols
cpc_level5_symbols = set()
for record in cpc_level5_data:
    symbol = record['symbol']
    symbol = symbol.strip()
    cpc_level5_symbols.add(symbol)

print(f"Starting analysis with {len(patent_data)} patents and {len(cpc_level5_symbols)} level 5 CPC symbols")

# Function to parse publication dates
def parse_date(date_str):
    if not date_str:
        return None
    try:
        date_str = date_str.strip().lower()
        
        # Extract year first - look for 4-digit number
        year_match = re.search(r'(\d{4})', date_str)
        if not year_match:
            return None
        year = int(year_match.group(1))
        
        # Extract month
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        
        month = 1  # default
        for month_abbr, month_num in month_map.items():
            if month_abbr in date_str:
                month = month_num
                break
        
        # Extract day
        day_match = re.search(r'(\d{1,2})[a-z]{0,2}\b(?!\d{4})', date_str)
        day = int(day_match.group(1)) if day_match else 1
        
        return datetime(year, month, day).date()
    except:
        return None

# Extract CPC codes and count by year - optimized for memory
cpc_year_counts = defaultdict(lambda: defaultdict(int))
year_range = set()
valid_records = 0
no_cpc = 0

for record in patent_data:
    # Parse date
    pub_date = parse_date(record['publication_date'])
    if not pub_date:
        continue
        
    year = pub_date.year
    year_range.add(year)
    
    # Parse CPC codes
    cpc_str = record['cpc']
    if not cpc_str:
        no_cpc += 1
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        found_level5 = False
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code and len(code) >= 4:
                # Take first 4 characters as the base symbol
                base_symbol = code[:4]
                if base_symbol in cpc_level5_symbols:
                    cpc_year_counts[base_symbol][year] += 1
                    found_level5 = True
        
        if found_level5:
            valid_records += 1
            
    except:
        pass

# Calculate exponential moving average (EMA) for each CPC code
smoothing_factor = 0.2
cpc_best_year_2022 = []

min_year = min(year_range)
max_year = max(year_range)
all_years = list(range(min_year, max_year + 1))

print(f"Processing {len(cpc_year_counts)} CPC codes across years {min_year}-{max_year}")

for cpc_code in list(cpc_year_counts.keys()):
    year_counts = cpc_year_counts[cpc_code]
    
    # Create complete count series for all years
    counts = [year_counts.get(year, 0) for year in all_years]
    
    # Calculate EMA
    ema_values = []
    if counts:
        ema_values.append(float(counts[0]))  # Start with first value
        for i in range(1, len(counts)):
            ema_val = smoothing_factor * counts[i] + (1 - smoothing_factor) * ema_values[i-1]
            ema_values.append(ema_val)
    
    # Find year with highest EMA
    if ema_values:
        max_ema_idx = ema_values.index(max(ema_values))
        max_ema_year = all_years[max_ema_idx]
        max_ema_value = ema_values[max_ema_idx]
        
        # Check if the best year is 2022
        if max_ema_year == 2022:
            cpc_best_year_2022.append({
                'cpc_code': cpc_code,
                'max_ema_value': max_ema_value,
                'max_ema_year': max_ema_year,
                'year_counts_2020_2024': {year: year_counts.get(year, 0) for year in range(2020, 2025)}
            })

# Sort by EMA value (descending)
cpc_best_year_2022_sorted = sorted(cpc_best_year_2022, key=lambda x: x['max_ema_value'], reverse=True)

result = {
    'total_cpc_codes_analyzed': len(cpc_year_counts),
    'cpc_codes_with_best_year_2022': len(cpc_best_year_2022),
    'top_cpc_codes_2022': [item['cpc_code'] for item in cpc_best_year_2022_sorted[:20]],
    'all_cpc_codes_2022': [item['cpc_code'] for item in cpc_best_year_2022_sorted]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.execute_python:14': {'sample_dates': [[0, 'Aug 3rd, 2021'], [1, 'Oct 6th, 2020'], [2, 'Sep 21st, 2021'], [3, '2020, April 7th'], [4, 'Mar 23rd, 2021'], [5, 'March 2nd, 2021'], [6, '2021, November 9th'], [7, '30th June 2020'], [8, '2021 on Mar 16th'], [9, '9th Nov 2021']], 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'total_patents': 277813, 'total_level5_symbols': 677, 'sample_level5_symbols': ['C30B', 'B63C', 'C01P', 'A01N', 'A23G', 'B60V', 'D21B', 'G10L', 'H02N', 'F03G']}, 'var_functions.execute_python:18': {'total_processed': 192752, 'invalid_dates': 85061, 'no_cpc': 0, 'unique_cpc_codes': 0, 'sample_counts': {}}, 'var_functions.execute_python:22': {'total_processed': 276015, 'valid_processed': 276015, 'unique_level5_symbols': 677, 'found_level5_codes': 0, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10', 'C01P2002/76', 'H01M10/0525', 'H01M2004/028', 'H01M4/1315', 'H01M2004/021', 'H01M4/525', 'C01B33/00', 'H01M4/1315', 'H01M4/525', 'H01M4/505'], 'sample_level5_symbols': ['A45F', 'C12M', 'G04G', 'D21C', 'B68C', 'B25D', 'B64G', 'C07H', 'G07C', 'F16L']}, 'var_functions.execute_python:24': {'valid_processed': 276015, 'year_range': '1837 to 2024', 'unique_cpc_codes_found': 669, 'skipped_no_level5': 0, 'sample_cpc_counts': {'C01B': {'2021': 530, '1975': 37, '2007': 119, '2022': 443, '2009': 317, '2017': 443, '2002': 251, '1976': 29, '2020': 435, '1972': 31, '1977': 26, '2008': 98, '2013': 309, '1988': 91, '1971': 18, '1966': 31, '1991': 40, '1967': 24, '1968': 10, '2018': 412, '1931': 8, '1970': 32, '2005': 132, '1985': 16, '1996': 25, '1979': 45, '2012': 337, '1978': 23, '2023': 408, '1999': 45, '2010': 234, '2016': 227, '2024': 178, '2001': 83, '1993': 36, '1995': 61, '2014': 289, '2015': 612, '2019': 307, '1994': 109, '2006': 195, '1982': 34, '1986': 10, '1989': 36, '1984': 22, '1959': 6, '1983': 28, '2011': 203, '1969': 21, '2003': 132, '1973': 22, '1998': 33, '2000': 83, '1990': 32, '1974': 30, '1964': 16, '1961': 19, '1960': 10, '2004': 128, '1997': 58, '1987': 39, '1946': 2, '1963': 14, '1942': 4, '1900': 2, '1965': 18, '1980': 23, '1981': 26, '1909': 1, '1952': 1, '1937': 4, '1992': 27, '1926': 2, '1930': 2, '1914': 3, '1903': 1, '1941': 3, '1908': 2, '1933': 7, '1955': 6, '1956': 2, '1936': 6, '1929': 1, '1962': 1, '1921': 2, '1958': 2, '1935': 6, '1925': 1, '1905': 6, '1862': 1, '1932': 4, '1934': 3, '1917': 1, '1939': 1, '1876': 1}, 'H01M': {'2021': 4424, '2020': 3640, '2022': 4350, '2024': 2496, '2023': 4147, '2010': 982, '1997': 63, '2007': 691, '1998': 152, '2001': 271, '2002': 354, '2017': 2686, '2016': 2208, '2018': 3141, '1973': 37, '2004': 582, '2006': 1011, '2011': 1037, '2012': 1052, '2014': 2111, '2019': 2884, '1994': 57, '2008': 764, '1915': 4, '1974': 48, '1985': 51, '1986': 59, '1984': 69, '1990': 78, '1983': 77, '1975': 19, '2003': 413, '2009': 925, '2013': 1058, '2015': 2155, '1980': 38, '1989': 75, '1992': 40, '2005': 417, '1967': 5, '1977': 11, '1995': 65, '1987': 26, '1951': 2, '1958': 17, '1979': 30, '1982': 47, '1999': 130, '1988': 64, '1981': 18, '2000': 283, '1991': 17, '1976': 44, '1940': 6, '1941': 4, '1952': 6, '1917': 2, '1971': 52, '1996': 83, '1968': 23, '1993': 72, '1964': 5, '1937': 6, '1902': 1, '1972': 16, '1966': 4, '1963': 1, '1928': 8, '1950': 2, '1939': 2, '1954': 10, '1921': 3, '1969': 14, '1924': 4, '1955': 8, '1970': 7, '1949': 14, '1962': 6, '1914': 4, '1926': 2, '1960': 5, '1918': 1, '1957': 4, '1978': 6, '1892': 2, '1934': 2, '1959': 2, '1965': 31, '1942': 2, '1943': 1, '1961': 2, '1874': 2, '1909': 2}, 'C01G': {'2021': 102, '2023': 121, '2024': 47, '1976': 13, '2012': 51, '2018': 97, '2013': 85, '1982': 16, '2006': 114, '1965': 6, '1984': 4, '2019': 94, '1998': 2, '1978': 6, '2016': 79, '2011': 50, '2022': 152, '2020': 110, '2009': 39, '1948': 2, '1977': 29, '1972': 4, '1959': 3, '2007': 28, '2003': 16, '2015': 61, '2017': 96, '2001': 13, '1989': 12, '1986': 10, '1987': 13, '2014': 47, '1995': 4, '2004': 10, '2010': 54, '2000': 8, '1993': 12, '2005': 23, '1969': 7, '1974': 11, '1867': 1, '1990': 5, '1991': 14, '2008': 22, '1996': 8, '1938': 2, '1963': 6, '2002': 15, '1970': 6, '1994': 5, '1971': 2, '1961': 3, '1968': 2, '1964': 2, '1992': 14, '1975': 2, '1997': 31, '1947': 1, '1981': 7, '1988': 21, '1942': 2, '1923': 1, '1900': 4, '1980': 8, '1983': 4, '1958': 5, '1973': 7, '1967': 6, '1954': 1, '1950': 4, '1951': 1, '1962': 4, '1935': 1}, 'C01P': {'2021': 398, '2022': 438, '1977': 37, '2024': 168, '1976': 50, '2012': 106, '2016': 301, '1995': 50, '2013': 172, '1971': 7, '1968': 3, '1902': 1, '2006': 146, '1983': 16, '1970': 2, '2019': 282, '2005': 150, '1985': 5, '1998': 67, '1979': 9, '2020': 314, '2011': 155, '1994': 5, '2023': 281, '2018': 294, '2010': 212, '1993': 42, '2009': 137, '1984': 6, '1964': 6, '1972': 4, '2017': 348, '1991': 69, '2007': 135, '2003': 42, '2015': 207, '2008': 58, '2001': 58, '1989': 30, '2014': 57, '2000': 49, '2002': 136, '1990': 16, '1969': 25, '1997': 47, '1933': 4, '1996': 64, '1916': 2, '1980': 26, '1986': 37, '1973': 16, '1999': 61, '1987': 31, '1963': 6, '1992': 36, '2004': 25, '1981': 9, '1959': 2, '1974': 6, '1988': 48, '1900': 1, '1978': 7, '1982': 12, '1958': 14, '1950': 6, '1967': 7, '1965': 1, '1951': 1, '1975': 1, '1942': 8}, 'Y02E': {'2021': 1577, '2020': 1298, '2022': 1490, '2024': 586, '2023': 1551, '2005': 190, '2011': 582, '1980': 68, '1997': 82, '2010': 548, '2016': 956, '2003': 218, '2007': 273, '2018': 1301, '1972': 23, '1971': 18, '1996': 87, '1982': 98, '1979': 61, '1977': 40, '1976': 73, '1994': 82, '1981': 77, '2019': 1104, '1998': 78, '1967': 17, '1995': 84, '1985': 63, '1984': 100, '1990': 81, '2001': 152, '2015': 948, '2002': 165, '2017': 1105, '1986': 83, '1987': 78, '1973': 39, '1975': 52, '1991': 72, '2013': 645, '2004': 197, '2006': 269, '2012': 613, '2014': 837, '2009': 420, '2008': 368, '1988': 84, '1978': 57, '1974': 30, '1919': 2, '2000': 143, '1983': 87, '1993': 63, '1992': 65, '1989': 81, '1970': 12, '1999': 106, '1968': 20, '1966': 17, '1961': 8, '1962': 9, '1936': 2, '1969': 23, '1965': 13, '1911': 1, '1940': 3, '1907': 4, '1941': 1, '1952': 2, '1917': 1, '1958': 6, '1944': 2, '1964': 7, '1924': 3, '1937': 1, '1876': 2, '1905': 1, '1929': 1, '1959': 8, '1957': 2, '1931': 7, '1915': 3, '1963': 7, '1928': 2, '1942': 2, '1950': 1, '1939': 1, '1954': 1, '1930': 1, '1900': 5, '1882': 3, '1955': 1, '1913': 2, '1949': 3, '1951': 1, '1922': 2, '1914': 4, '1953': 1, '1881': 1, '1918': 1, '1892': 2, '1935': 2, '1934': 1, '1932': 3, '1946': 1, '1889': 2, '1925': 2, '1921': 1, '1890': 2, '1844': 2, '1884': 2, '1948': 1, '1960': 2, '1926': 1, '1858': 3, '1874': 1, '1909': 1, '1866': 2, '1923': 2}}}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json'}

exec(code, env_args)
