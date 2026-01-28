code = """import json
import os
import re
from datetime import datetime

# Access German patents with 2019 grants from storage
german_patents_2019 = []
storage_data = locals()['var_functions.query_db:58']

if isinstance(storage_data, str) and '.json' in storage_data:
    with open(storage_data, 'r') as f:
        german_patents_2019 = json.load(f)
else:
    german_patents_2019 = storage_data

print('Loaded %d German patents with 2019 grants' % len(german_patents_2019))

# Parse dates and filter for H2 2019
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s:
        return None
    s = s.lower()
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', s)
    if m:
        day, mon_str, year = int(m.group(1)), m.group(2)[:3], int(m.group(3))
        mon = months.get(mon_str, 0)
        return datetime(year, mon, day) if mon else None
    m = re.search(r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', s)
    if m:
        day, mon_str, year = int(m.group(2)), m.group(1)[:3], int(m.group(3))
        mon = months.get(mon_str, 0)
        return datetime(year, mon, day) if mon else None
    return None

# Filter patents for H2 2019
patents_h2 = []
for p in german_patents_2019:
    date = parse_date(p.get('grant_date', ''))
    if date and date.year == 2019 and date.month >= 7:
        patents_h2.append(p)

print('H2 2019 patents: %d' % len(patents_h2))

# Extract and count CPC level 4 codes by year
cpc_by_year = {}
for p in german_patents_2019:
    grant_date = parse_date(p.get('grant_date', ''))
    if grant_date and grant_date.year >= 2015:
        year = grant_date.year
        if year not in cpc_by_year:
            cpc_by_year[year] = {}
        
        cpc_data = p.get('cpc', '')
        try:
            cpc_list = json.loads(cpc_data)
            for item in cpc_list:
                code = item.get('code', '')
                if code:
                    m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                    if m:
                        level4 = m.group(1) + '/00'
                        cpc_by_year[year][level4] = cpc_by_year[year].get(level4, 0) + 1
        except:
            codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
            for code in codes:
                m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if m:
                    level4 = m.group(1) + '/00'
                    cpc_by_year[year][level4] = cpc_by_year[year].get(level4, 0) + 1

# Get level 4 CPC codes from H2 2019
h2_cpc4 = set()
for p in patents_h2:
    cpc_data = p.get('cpc', '')
    try:
        cpc_list = json.loads(cpc_data)
        for item in cpc_list:
            code = item.get('code', '')
            if code:
                m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if m:
                    h2_cpc4.add(m.group(1) + '/00')
    except:
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
        for code in codes:
            m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if m:
                h2_cpc4.add(m.group(1) + '/00')

print('Level 4 CPC codes in H2 2019: %d' % len(h2_cpc4))
print('Sample codes:', list(h2_cpc4)[:10])

result = {
    'h2_2019_patents': len(patents_h2),
    'h2_cpc4_codes': list(h2_cpc4),
    'years_with_data': sorted(cpc_by_year.keys()),
    'sample_year_counts': {k: len(v) for k, v in list(cpc_by_year.items())[:3]}
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
