code = """import json
import re
from datetime import datetime

# Load German patents with 2019 grants
storage_key = 'var_functions.query_db:70'
german_patents_2019 = locals()[storage_key]

print('Loaded %d patents' % len(german_patents_2019))

# Date parsing
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s:
        return None
    s = s.lower()
    p1 = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', s)
    if p1:
        try:
            day = int(p1.group(1))
            mon = months.get(p1.group(2)[:3], 0)
            year = int(p1.group(3))
            return datetime(year, mon, day) if mon else None
        except:
            return None
    p2 = re.search(r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', s)
    if p2:
        try:
            day = int(p2.group(2))
            mon = months.get(p2.group(1)[:3], 0)
            year = int(p2.group(3))
            return datetime(year, mon, day) if mon else None
        except:
            return None
    return None

# Filter H2 2019
h2_2019 = [p for p in german_patents_2019 if (lambda d: d and d.year == 2019 and d.month >= 7)(parse_date(p.get('grant_date', '')))]

print('H2 2019 patents: %d' % len(h2_2019))

# Extract CPC level 4 codes
cpc4_in_h2 = {}
for p in h2_2019:
    cpc = p.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc)
    for code in codes:
        m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
        if m:
            level4 = m.group(1) + '/00'
            cpc4_in_h2[level4] = cpc4_in_h2.get(level4, 0) + 1

print('CPC4 codes in H2: %d' % len(cpc4_in_h2))
print('Top 5:', list(cpc4_in_h2.items())[:5])

result = {'h2_patents': len(h2_2019), 'cpc4_codes': list(cpc4_in_h2.keys()), 'top_cpc4': sorted(cpc4_in_h2.items(), key=lambda x: x[1], reverse=True)[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
