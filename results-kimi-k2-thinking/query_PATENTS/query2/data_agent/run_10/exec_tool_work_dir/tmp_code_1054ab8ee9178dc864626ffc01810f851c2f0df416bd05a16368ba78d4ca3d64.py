code = """import json, re
from datetime import datetime

all_patents_file = locals()['var_functions.query_db:66']
h2_patents_file = locals()['var_functions.query_db:70']

with open(all_patents_file, 'r') as f:
    all_german_patents = json.load(f)
with open(h2_patents_file, 'r') as f:
    h2_2019_patents = json.load(f)

print('Loaded data: %d total, %d H2 2019' % (len(all_german_patents), len(h2_2019_patents)))

months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s or not isinstance(s, str):
        return None
    s = s.lower()
    for pat, idx_day, idx_mon, idx_year in [(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', 1, 2, 3), (r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', 2, 1, 3)]:
        m = re.search(pat, s)
        if m:
            try:
                day = int(m.group(idx_day))
                mon = months.get(m.group(idx_mon)[:3], 0)
                year = int(m.group(idx_year))
                return datetime(year, mon, day) if mon else None
            except:
                pass
    return None

# Build CPC4 yearly counts for 2015-2020
years = list(range(2015, 2021))
cpc4_by_year = {y: {} for y in years}

for p in all_german_patents:
    d = parse_date(p.get('grant_date', ''))
    if d and 2015 <= d.year <= 2020:
        cpc = p.get('cpc', '')
        for code in re.findall(r'"code":\s*"([^"]+)"', cpc):
            m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if m:
                cpc4 = m.group(1) + '/00'
                cpc4_by_year[d.year][cpc4] = cpc4_by_year[d.year].get(cpc4, 0) + 1

# Get CPC4 codes from H2 2019 patents
h2_cpc4 = set()
for p in h2_2019_patents:
    for code in re.findall(r'"code":\s*"([^"]+)"', p.get('cpc', '')):
        m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
        if m:
            h2_cpc4.add(m.group(1) + '/00')

print('Years: %s, H2 CPC4 codes: %d' % (sorted([y for y in years if cpc4_by_year[y]]), len(h2_cpc4)))

# Calculate EMA for each CPC4 code
ema_results = {}
alpha = 0.1
for cpc4 in h2_cpc4:
    counts = [cpc4_by_year[y].get(cpc4, 0) for y in years]
    emas = []
    prev = counts[0] if counts else 0
    emas.append(prev)
    for i in range(1, len(counts)):
        cur = alpha * counts[i] + (1 - alpha) * prev
        emas.append(cur)
        prev = cur
    max_idx = emas.index(max(emas))
    ema_results[cpc4] = {'best_year': years[max_idx], 'max_ema': emas[max_idx], 'counts': dict(zip(years, counts))}

print('EMA calculated for %d codes' % len(ema_results))

# Get CPC definitions from database
cpc4_list = list(ema_results.keys())
print('Need definitions for %d CPC4 codes' % len(cpc4_list))
result = {'cpc4_codes': cpc4_list[:50], 'ema_sample': [(k, v['best_year'], round(v['max_ema'], 2)) for k, v in list(ema_results.items())[:10]]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:78': {'patents_h2_2019': 16, 'years': [2015, 2016, 2017, 2018, 2019, 2020]}}

exec(code, env_args)
