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

# Function to parse publication dates more flexibly
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
total_processed = 0
valid_processed = 0

# Check the actual format of CPC codes in the data
sample_codes = []

for i, record in enumerate(patent_data):
    pub_date = parse_date(record['publication_date'])
    if not pub_date:
        continue
        
    year = pub_date.year
    valid_processed += 1
    
    # Parse CPC codes
    cpc_str = record['cpc']
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                if len(sample_codes) < 20:
                    sample_codes.append(code)
                # Extract base code (before /)
                base_code = code.split('/')[0]
                if base_code in cpc_level5_symbols:
                    cpc_year_counts[base_code][year] += 1
    except:
        pass
    
    total_processed += 1

result_data = {
    'total_processed': total_processed,
    'valid_processed': valid_processed,
    'unique_level5_symbols': len(cpc_level5_symbols),
    'found_level5_codes': len(cpc_year_counts),
    'sample_cpc_codes': sample_codes,
    'sample_level5_symbols': list(cpc_level5_symbols)[:10]
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.execute_python:14': {'sample_dates': [[0, 'Aug 3rd, 2021'], [1, 'Oct 6th, 2020'], [2, 'Sep 21st, 2021'], [3, '2020, April 7th'], [4, 'Mar 23rd, 2021'], [5, 'March 2nd, 2021'], [6, '2021, November 9th'], [7, '30th June 2020'], [8, '2021 on Mar 16th'], [9, '9th Nov 2021']], 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'total_patents': 277813, 'total_level5_symbols': 677, 'sample_level5_symbols': ['C30B', 'B63C', 'C01P', 'A01N', 'A23G', 'B60V', 'D21B', 'G10L', 'H02N', 'F03G']}, 'var_functions.execute_python:18': {'total_processed': 192752, 'invalid_dates': 85061, 'no_cpc': 0, 'unique_cpc_codes': 0, 'sample_counts': {}}}

exec(code, env_args)
