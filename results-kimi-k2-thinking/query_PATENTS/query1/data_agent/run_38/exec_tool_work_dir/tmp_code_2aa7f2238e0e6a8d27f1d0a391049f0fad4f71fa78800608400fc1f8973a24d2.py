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

print(f"Loaded {len(cpc_level5_symbols)} level 5 CPC symbols")

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

# Extract CPC codes and count by year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
year_range = set()

valid_processed = 0
skipped_no_level5 = 0

cpc_symbol_pattern = re.compile(r'^([A-HY]\d{2}[A-Z])')

for record in patent_data:
    # Parse date
    pub_date = parse_date(record['publication_date'])
    if not pub_date:
        continue
        
    year = pub_date.year
    year_range.add(year)
    valid_processed += 1
    
    # Parse CPC codes
    cpc_str = record['cpc']
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        found_level5 = False
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if not code:
                continue
                
            # Extract the base level 5 code (first 4 characters before any digits)
            match = cpc_symbol_pattern.match(code)
            if match:
                base_symbol = match.group(1)
                if base_symbol in cpc_level5_symbols:
                    cpc_year_counts[base_symbol][year] += 1
                    found_level5 = True
        
        if not found_level5:
            skipped_no_level5 += 1
            
    except Exception as e:
        continue

# Calculate statistics
min_year = min(year_range) if year_range else 0
max_year = max(year_range) if year_range else 0

result = {
    'valid_processed': valid_processed,
    'year_range': f"{min_year} to {max_year}",
    'unique_cpc_codes_found': len(cpc_year_counts),
    'skipped_no_level5': skipped_no_level5,
    'sample_cpc_counts': {k: dict(v) for k, v in list(cpc_year_counts.items())[:5]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.execute_python:14': {'sample_dates': [[0, 'Aug 3rd, 2021'], [1, 'Oct 6th, 2020'], [2, 'Sep 21st, 2021'], [3, '2020, April 7th'], [4, 'Mar 23rd, 2021'], [5, 'March 2nd, 2021'], [6, '2021, November 9th'], [7, '30th June 2020'], [8, '2021 on Mar 16th'], [9, '9th Nov 2021']], 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'total_patents': 277813, 'total_level5_symbols': 677, 'sample_level5_symbols': ['C30B', 'B63C', 'C01P', 'A01N', 'A23G', 'B60V', 'D21B', 'G10L', 'H02N', 'F03G']}, 'var_functions.execute_python:18': {'total_processed': 192752, 'invalid_dates': 85061, 'no_cpc': 0, 'unique_cpc_codes': 0, 'sample_counts': {}}, 'var_functions.execute_python:22': {'total_processed': 276015, 'valid_processed': 276015, 'unique_level5_symbols': 677, 'found_level5_codes': 0, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10', 'C01P2002/76', 'H01M10/0525', 'H01M2004/028', 'H01M4/1315', 'H01M2004/021', 'H01M4/525', 'C01B33/00', 'H01M4/1315', 'H01M4/525', 'H01M4/505'], 'sample_level5_symbols': ['A45F', 'C12M', 'G04G', 'D21C', 'B68C', 'B25D', 'B64G', 'C07H', 'G07C', 'F16L']}}

exec(code, env_args)
