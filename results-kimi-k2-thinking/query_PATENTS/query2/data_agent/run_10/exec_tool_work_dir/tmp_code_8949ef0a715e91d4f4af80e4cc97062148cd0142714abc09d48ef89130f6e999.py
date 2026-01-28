code = """import json
import os
import re
from datetime import datetime

# Load data from storage
data = locals()['var_functions.query_db:40']
print('Data type:', type(data))
print('Data length:', len(data) if isinstance(data, list) else 'Not a list')

# The data should be a list of patent records
patents_2019_h2 = []

months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s:
        return None
    s = s.lower()
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', s)
    if m:
        day = int(m.group(1))
        month = months.get(m.group(2)[:3], 0)
        year = int(m.group(3))
        return datetime(year, month, day) if month else None
    return None

# Filter patents for H2 2019
for p in data:
    grant_date = parse_date(p.get('grant_date', ''))
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        patents_2019_h2.append(p)

print('H2 2019 patents found:', len(patents_2019_h2))

# Count CPC codes at level 4
cpc4_counts = {}
all_cpc = []

for p in patents_2019_h2:
    cpc = p.get('cpc', '')
    try:
        cpc_list = json.loads(cpc)
        for item in cpc_list:
            code = item.get('code', '')
            if code:
                all_cpc.append(code)
                m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if m:
                    cpc4 = m.group(1) + '/00'
                    cpc4_counts[cpc4] = cpc4_counts.get(cpc4, 0) + 1
    except:
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc)
        for code in codes:
            all_cpc.append(code)
            m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if m:
                cpc4 = m.group(1) + '/00'
                cpc4_counts[cpc4] = cpc4_counts.get(cpc4, 0) + 1

result = {
    'h2_2019_patents': len(patents_2019_h2),
    'unique_cpc': len(set(all_cpc)),
    'cpc4_groups': len(cpc4_counts),
    'top_cpc4': sorted(cpc4_counts.items(), key=lambda x: x[1], reverse=True)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
