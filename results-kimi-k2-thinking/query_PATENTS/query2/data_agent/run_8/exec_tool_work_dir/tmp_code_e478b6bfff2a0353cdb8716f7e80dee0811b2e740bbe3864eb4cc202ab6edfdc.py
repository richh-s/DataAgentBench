code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:2']

# Load the full results from the query
with open(file_path, 'r') as f:
    patents_2019 = json.load(f)

# Function to parse grant dates in various formats
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    date_str = date_str.strip()
    patterns = [
        (r'(\d{1,2})\w{2} (\w+) (\d{4})', lambda m: (m.group(2), m.group(1), m.group(3))),
        (r'(\w+) (\d{1,2})\w{2}, (\d{4})', lambda m: (m.group(1), m.group(2), m.group(3))),
    ]
    month_map = {
        'Jan': 1, 'January': 1, 'Feb': 2, 'February': 2, 'Mar': 3, 'March': 3,
        'Apr': 4, 'April': 4, 'May': 5, 'Jun': 6, 'June': 6, 'Jul': 7, 'July': 7,
        'Aug': 8, 'August': 8, 'Sep': 9, 'September': 9, 'Oct': 10, 'October': 10,
        'Nov': 11, 'November': 11, 'Dec': 12, 'December': 12
    }
    for pattern, extractor in patterns:
        match = re.match(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                month_str, day_str, year_str = extractor(match)
                month_num = month_map.get(month_str.strip())
                if month_num:
                    return datetime(int(year_str), month_num, int(day_str))
            except:
                continue
    return None

# Extract Germany patents from second half 2019
patents_de_h2 = []
for patent in patents_2019:
    parsed_date = parse_grant_date(patent['grant_date'])
    if parsed_date and parsed_date.year == 2019 and parsed_date.month >= 7:
        patents_info = patent['Patents_info']
        if 'DE-' in patents_info or ' from DE,' in patents_info or patents_info.startswith('DE'):
            patents_de_h2.append({
                'patents_info': patents_info,
                'grant_date': patent['grant_date'],
                'parsed_date': parsed_date,
                'cpc_json': patent['cpc']
            })

print('Germany patents H2 2019:', len(patents_de_h2))

# Parse CPC codes (JSON-like string to list)
all_cpc_entries = []
for patent in patents_de_h2:
    try:
        cpc_list = json.loads(patent['cpc_json'])
        for cpc_entry in cpc_list:
            cpc_code = cpc_entry.get('code', '')
            if cpc_code:
                all_cpc_entries.append({
                    'cpc_code': cpc_code,
                    'full_cpc_entry': cpc_entry,
                    'grant_date': patent['grant_date'],
                    'parsed_date': patent['parsed_date']
                })
    except:
        continue

print('Total CPC entries:', len(all_cpc_entries))

# Extract level 4 CPC codes (format: X99Y/9999 or X99Y/999 or X99Y/99 or X99Y/9)
# We need the group code at level 4 which is like G06F9/45533 -> G06F9/455 (level 4)
cpc_level4_entries = []
for entry in all_cpc_entries:
    cpc_code = entry['cpc_code']
    # Split by '/' to separate main group from subgroup
    if '/' in cpc_code:
        main_group, subgroup = cpc_code.split('/', 1)
        # For level 4, we take the first 3 digits of subgroup if available
        if len(subgroup) >= 3:
            level4_subgroup = subgroup[:3]
            level4_code = f"{main_group}/{level4_subgroup}"
        else:
            level4_code = cpc_code
        
        cpc_level4_entries.append({
            'cpc_level4_code': level4_code,
            'cpc_full_code': cpc_code,
            **entry  # Include all existing fields
        })

print('CPC Level 4 entries:', len(cpc_level4_entries))

# Group by Level 4 CPC code and count by year
from collections import defaultdict, Counter

# Since all are from 2019, we'll create yearly data
yearly_counts = defaultdict(int)
for entry in cpc_level4_entries:
    yearly_counts[entry['cpc_level4_code']] += 1

# Get unique CPC level 4 codes
cpc_level4_codes = list(set(entry['cpc_level4_code'] for entry in cpc_level4_entries))
print('Unique CPC Level 4 codes:', len(cpc_level4_codes))
print('Sample codes:', cpc_level4_codes[:10])

result = {
    'total_german_patents_h2_2019': len(patents_de_h2),
    'total_cpc_entries': len(all_cpc_entries),
    'total_cpc_level4_entries': len(cpc_level4_entries),
    'unique_cpc_level4_codes': len(cpc_level4_codes),
    'sample_codes': cpc_level4_codes[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}}

exec(code, env_args)
