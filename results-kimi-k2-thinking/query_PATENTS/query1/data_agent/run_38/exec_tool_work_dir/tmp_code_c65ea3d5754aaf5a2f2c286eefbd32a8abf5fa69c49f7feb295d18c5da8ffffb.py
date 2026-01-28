code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load the full patent data
patent_data_path = locals()['var_functions.query_db:5']
with open(patent_data_path, 'r') as f:
    patent_data = json.load(f)

# Function to parse publication dates
def parse_date(date_str):
    if not date_str:
        return None
    try:
        date_str = date_str.strip()
        patterns = [
            r'(\w+)[,.\s]*(\d{1,2})[a-zA-Z]{0,2}[,\s]*(\d{4})',  # "Aug 3rd, 2021" or "March 2nd, 2021"
            r'(\d{4})[,\s]*(\w+)[,.\s]*(\d{1,2})',                # "2020, April 7th"
            r'(\d{1,2})[a-zA-Z]{0,2}[,.\s]*(\w+)[,.\s]*(\d{4})', # "30th June 2020"
            r'(\d{1,2})\s+(\w+)\s+(\d{4})',                      # "9th Nov 2021"
        ]
        
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        
        for pattern in patterns:
            match = re.search(pattern, date_str.lower())
            if match:
                parts = list(match.groups())
                # Find year, month, day
                for part in parts:
                    if part.isdigit() and len(part) == 4:
                        year = int(part)
                    elif part.isdigit():
                        day = int(part)
                    elif part[:3] in month_map:
                        month = month_map[part[:3]]
                
                if 'year' in locals() and 'month' in locals() and 'day' in locals():
                    return datetime(year, month, day).date()
    except:
        pass
    return None

# Extract CPC codes at level 5 and count by year
cpc_year_counts = defaultdict(lambda: defaultdict(int))

cpc_code_pattern = re.compile(r'^[A-HY]\d{2}[A-Z]$')

total_processed = 0
invalid_dates = 0
no_cpc = 0

for record in patent_data:
    # Parse date
    pub_date = parse_date(record['publication_date'])
    if not pub_date:
        invalid_dates += 1
        continue
    
    year = pub_date.year
    
    # Parse CPC codes
    cpc_str = record['cpc']
    if not cpc_str:
        no_cpc += 1
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                # Check if this is a level 5 CPC code based on the pattern
                # Extract the first part before '/' if it exists
                base_code = code.split('/')[0]
                
                # Should be in format like A01B, A01C, etc. (section + 2 digits + letter)
                if cpc_code_pattern.match(base_code):
                    cpc_year_counts[base_code][year] += 1
    except:
        pass
    
    total_processed += 1

print('__RESULT__:')
print(json.dumps({
    'total_processed': total_processed,
    'invalid_dates': invalid_dates,
    'no_cpc': no_cpc,
    'unique_cpc_codes': len(cpc_year_counts),
    'sample_counts': {k: dict(v) for k, v in list(cpc_year_counts.items())[:5]}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.execute_python:14': {'sample_dates': [[0, 'Aug 3rd, 2021'], [1, 'Oct 6th, 2020'], [2, 'Sep 21st, 2021'], [3, '2020, April 7th'], [4, 'Mar 23rd, 2021'], [5, 'March 2nd, 2021'], [6, '2021, November 9th'], [7, '30th June 2020'], [8, '2021 on Mar 16th'], [9, '9th Nov 2021']], 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'total_patents': 277813, 'total_level5_symbols': 677, 'sample_level5_symbols': ['C30B', 'B63C', 'C01P', 'A01N', 'A23G', 'B60V', 'D21B', 'G10L', 'H02N', 'F03G']}}

exec(code, env_args)
