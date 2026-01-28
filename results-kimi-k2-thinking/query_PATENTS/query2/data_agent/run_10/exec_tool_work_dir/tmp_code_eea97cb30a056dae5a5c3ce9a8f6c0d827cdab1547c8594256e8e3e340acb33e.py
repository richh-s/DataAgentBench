code = """import json
import os
import re
from datetime import datetime

# Load the data
data_file = var_functions.query_db:30
print('Data file:', data_file)

# Load German patents from 2019
german_patents_2019 = []
with open(data_file, 'r') as f:
    german_patents_2019 = json.load(f)

print('Total German patents with 2019 grant dates:', len(german_patents_2019))
print('\nFirst few entries:')
for i, patent in enumerate(german_patents_2019[:3]):
    print(f"{i+1}. {patent['Patents_info'][:80]}...")
    print(f"   Grant: {patent['grant_date']}")
    print(f"   CPC codes: {patent['cpc'][:100]}...")
    
# Try to parse dates
months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def parse_date(date_str):
    if not date_str:
        return None
    
    date_str_lower = date_str.lower()
    
    # Try pattern: "14th Mar 2019"
    match = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', date_str_lower)
    if match:
        try:
            day = int(match.group(1))
            month_str = match.group(2)[:3]
            year = int(match.group(3))
            month = months.get(month_str)
            if month:
                return datetime(year, month, day)
        except:
            pass
    
    # Try pattern: "March 21st, 2019" or "Mar 21st 2019"
    match = re.search(r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', date_str_lower)
    if match:
        try:
            month_str = match.group(1)[:3]
            day = int(match.group(2))
            year = int(match.group(3))
            month = months.get(month_str)
            if month:
                return datetime(year, month, day)
        except:
            pass
    
    return None

# Filter for second half of 2019
patents_h2_2019 = []
for patent in german_patents_2019:
    grant_date = parse_date(patent['grant_date'])
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        patents_h2_2019.append(patent)

print(f'\nPatents granted in second half of 2019: {len(patents_h2_2019)}')

# Extract CPC codes and create level 4 groups
cpc_level4_counts = {}
all_cpc_codes = []

for patent in patents_h2_2019:
    cpc_data = patent['cpc']
    try:
        cpc_list = json.loads(cpc_data)
        for item in cpc_list:
            code = item.get('code', '')
            if code:
                all_cpc_codes.append(code)
                # Extract level 4: format like G06F9/45533 -> G06F9/00
                level4_match = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if level4_match:
                    level4 = level4_match.group(1) + '/00'
                    cpc_level4_counts[level4] = cpc_level4_counts.get(level4, 0) + 1
    except:
        # Fallback regex extraction
        code_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
        for code in code_matches:
            all_cpc_codes.append(code)
            level4_match = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if level4_match:
                level4 = level4_match.group(1) + '/00'
                cpc_level4_counts[level4] = cpc_level4_counts.get(level4, 0) + 1

print(f'Unique CPC codes: {len(set(all_cpc_codes))}')
print(f'Level 4 CPC groups: {len(cpc_level4_counts)}')
print('\nTop 10 Level 4 CPC groups:')
sorted_groups = sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)
for group, count in sorted_groups[:10]:
    print(f'  {group}: {count}')

result = {
    'patents_h2_2019': len(patents_h2_2019),
    'unique_cpc_codes': len(set(all_cpc_codes)),
    'level4_groups': len(cpc_level4_counts),
    'top_level4': sorted_groups[:20]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
