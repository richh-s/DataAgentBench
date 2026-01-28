code = """import json, os, re
from datetime import datetime

# Load German patents 2019 grants data
data_key = 'var_functions.query_db:70'
file_path = locals()[data_key]
german_patents_2019 = json.loads(open(file_path).read())

print('Loaded %d German patents with 2019 grants' % len(german_patents_2019))

# Parse dates function
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s:
        return None
    s = s.lower()
    patterns = [
        (r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', lambda m: (int(m.group(1)), months.get(m.group(2)[:3],0), int(m.group(3)))),
        (r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', lambda m: (int(m.group(2)), months.get(m.group(1)[:3],0), int(m.group(3)))),
    ]
    for pat, ext in patterns:
        m = re.search(pat, s)
        if m:
            day, mon, year = ext(m)
            if mon > 0:
                try:
                    return datetime(year, mon, day)
                except:
                    pass
    return None

# Get all German patents for historical data
all_german_patents = json.loads(open(locals()['var_functions.query_db:66']).read())
print('Loaded %d all German patents' % len(all_german_patents))

# Filter patents from 2015-2020 and extract CPC level 4 counts
cpc4_yearly = {}
patents_h2_2019 = []

for p in all_german_patents:
    grant_date = parse_date(p.get('grant_date', ''))
    if grant_date:
        year = grant_date.year
        if 2015 <= year <= 2020:
            # Extract CPC codes
            cpc_data = p.get('cpc', '')
            codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
            for code in codes:
                m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
                if m:
                    cpc4 = m.group(1) + '/00'
                    if year not in cpc4_yearly:
                        cpc4_yearly[year] = {}
                    cpc4_yearly[year][cpc4] = cpc4_yearly[year].get(cpc4, 0) + 1
            
            # Check if H2 2019
            if year == 2019 and grant_date.month >= 7:
                patents_h2_2019.append(p)

print('H2 2019 patents: %d' % len(patents_h2_2019))
print('Years with data: %s' % sorted(cpc4_yearly.keys()))

result = {'patents_h2_2019': len(patents_h2_2019), 'years': sorted(cpc4_yearly.keys())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
