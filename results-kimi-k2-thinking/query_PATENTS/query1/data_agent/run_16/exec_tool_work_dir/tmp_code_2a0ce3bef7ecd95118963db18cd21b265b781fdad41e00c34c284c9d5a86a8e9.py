code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the patent data
patent_file = locals()['var_functions.query_db:4']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Load the CPC level 5 data
cpc_file = locals()['var_functions.query_db:11']
with open(cpc_file, 'r') as f:
    cpc_level5 = json.load(f)

# Create set of valid level 5 CPC codes for fast lookup
level5_codes = {item['symbol'] for item in cpc_level5}

# Function to parse publication date
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    if not date_str or date_str == '':
        return None
    try:
        # Format: "Aug 3rd, 2021" or "Oct 6th, 2020"
        parts = date_str.split()
        if len(parts) >= 3:
            month = parts[0]
            year = parts[-1]
            if month in month_map and year.isdigit():
                return int(year)
    except:
        pass
    return None

# Extract CPC codes and years from patents
patent_records = []
for patent in patent_data:
    pub_date = patent.get('publication_date', '')
    year = parse_date(pub_date)
    if not year:
        continue
    
    cpc_str = patent.get('cpc', '')
    if not cpc_str or cpc_str == '':
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                # Extract group part (before the / for subclasses, or the main group)
                if '/' in code:
                    group_part = code.split('/')[0]
                else:
                    group_part = code
                
                # Check if it's a level 5 group
                if group_part in level5_codes:
                    patent_records.append({
                        'cpc_group': group_part,
                        'year': year,
                        'full_code': code
                    })
    except:
        continue

print('__RESULT__:')
print(json.dumps({
    'total_patents_processed': len(patent_data),
    'valid_records': len(patent_records),
    'sample_records': patent_records[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
