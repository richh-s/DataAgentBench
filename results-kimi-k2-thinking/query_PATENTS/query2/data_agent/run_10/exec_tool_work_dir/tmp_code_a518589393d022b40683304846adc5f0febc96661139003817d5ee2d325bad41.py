code = """import json, os, re
from datetime import datetime

# Directly load the JSON data from the variable
# Based on the query result, we know it's a JSON file containing patent data

temp_file = '/tmp/' + [f for f in os.listdir('/tmp') if f.endswith('.json') and 'query_db' in f][0]
with open(temp_file, 'r') as f:
    german_patents_2019 = json.load(f)

print('Loaded %d German patents from 2019' % len(german_patents_2019))

# Parse dates
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(date_str):
    if not date_str: return None
    date_str_lower = date_str.lower()
    
    # Try various patterns
    patterns = [
        (r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', lambda m: (int(m.group(1)), months.get(m.group(2)[:3],0), int(m.group(3)))),
        (r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', lambda m: (int(m.group(2)), months.get(m.group(1)[:3],0), int(m.group(3)))),
    ]
    
    for pattern, extractor in patterns:
        match = re.search(pattern, date_str_lower)
        if match:
            day, month, year = extractor(match)
            if month > 0:
                try:
                    return datetime(year, month, day)
                except:
                    pass
    return None

# Get patents from second half 2019
patents_h2_2019 = []
for patent in german_patents_2019:
    grant_date = parse_date(patent.get('grant_date',''))
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        patents_h2_2019.append(patent)

print('Second half 2019 patents: %d' % len(patents_h2_2019))

# Extract CPC codes at level 4
cpc_level4_counts = {}
all_cpc = []

for patent in patents_h2_2019:
    cpc_data = patent.get('cpc','')
    try:
        cpc_list = json.loads(cpc_data)
        for item in cpc_list:
            code = item.get('code','')
            if code:
                all_cpc.append(code)
                match = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if match:
                    level4 = match.group(1) + '/00'
                    cpc_level4_counts[level4] = cpc_level4_counts.get(level4, 0) + 1
    except:
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
        for code in codes:
            all_cpc.append(code)
            match = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if match:
                level4 = match.group(1) + '/00'
                cpc_level4_counts[level4] = cpc_level4_counts.get(level4, 0) + 1

result = {
    'patents_h2_2019': len(patents_h2_2019),
    'unique_cpc': len(set(all_cpc)),
    'level4_groups': len(cpc_level4_counts),
    'top_level4': sorted(cpc_level4_counts.items(), key=lambda x:x[1], reverse=True)[:15]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
