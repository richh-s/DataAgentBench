code = """import json
import re
from datetime import datetime

# Load German patents data
all_patents_file = locals()['var_functions.query_db:66']
h2_2019_patents_file = locals()['var_functions.query_db:70']

with open(all_patents_file, 'r') as f:
    all_german_patents = json.load(f)

with open(h2_2019_patents_file, 'r') as f:
    h2_2019_patents = json.load(f)

print('Total German patents: %d' % len(all_german_patents))
print('H2 2019 patents: %d' % len(h2_2019_patents))

# Date parsing setup
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def parse_date(s):
    if not s or not isinstance(s, str):
        return None
    s = s.lower()
    p1 = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+(\w{3,})\s+(\d{4})', s)
    if p1:
        try:
            day, mon_str, year = int(p1.group(1)), p1.group(2)[:3], int(p1.group(3))
            mon = months.get(mon_str, 0)
            return datetime(year, mon, day) if mon else None
        except:
            pass
    p2 = re.search(r'(\w{3,})\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', s)
    if p2:
        try:
            day, mon_str, year = int(p2.group(2)), p2.group(1)[:3], int(p2.group(3))
            mon = months.get(mon_str, 0)
            return datetime(year, mon, day) if mon else None
        except:
            pass
    return None

# Build historical CPC4 counts (2015-2020)
years = range(2015, 2021)
cpc4_by_year = {year: {} for year in years}

for p in all_german_patents:
    grant_date = parse_date(p.get('grant_date', ''))
    if grant_date and 2015 <= grant_date.year <= 2020:
        year = grant_date.year
        cpc_data = p.get('cpc', '')
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
        for code in codes:
            m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if m:
                cpc4 = m.group(1) + '/00'
                cpc4_by_year[year][cpc4] = cpc4_by_year[year].get(cpc4, 0) + 1

# Get CPC4 codes from H2 2019 patents
h2_cpc4_codes = set()
for p in h2_2019_patents:
    cpc_data = p.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
    for code in codes:
        m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
        if m:
            h2_cpc4_codes.add(m.group(1) + '/00')

print('Years with data: %s' % [y for y in years if cpc4_by_year[y]])
print('CPC4 codes in H2 2019: %d' % len(h2_cpc4_codes))

# Calculate EMA for each CPC4 code (smoothing factor 0.1)
ema_results = {}

for cpc4 in h2_cpc4_codes:
    # Get yearly counts for this CPC4
    yearly_counts = [cpc4_by_year[year].get(cpc4, 0) for year in years]
    
    # Calculate EMA
    alpha = 0.1
    ema_values = []
    ema_prev = yearly_counts[0] if yearly_counts else 0
    ema_values.append(ema_prev)
    
    for i in range(1, len(yearly_counts)):
        ema_current = alpha * yearly_counts[i] + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find best year (highest EMA)
    if ema_values:
        max_idx = ema_values.index(max(ema_values))
        best_year = years[max_idx]
        ema_results[cpc4] = {
            'best_year': best_year,
            'max_ema': ema_values[max_idx],
            'yearly_counts': dict(zip(years, yearly_counts)),
            'ema_values': dict(zip(years, ema_values))
        }

print('EMA calculated for %d CPC4 codes' % len(ema_results))

# Get CPC4 codes with highest EMA (top 20)
top_ema_cpc4 = sorted(ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)[:20]

print('Top 5 CPC4 codes by EMA:')
for code, data in top_ema_cpc4[:5]:
    print('  %s: best year %d, EMA %.2f' % (code, data['best_year'], data['max_ema']))

# Prepare final data structure
cpc4_codes_for_query = [code for code, _ in top_ema_cpc4]

result = {
    'h2_2019_patents_total': len(h2_2019_patents),
    'cpc4_codes_count': len(h2_cpc4_codes),
    'cpc4_with_ema': len(ema_results),
    'top_cpc4_codes': cpc4_codes_for_query,
    'detailed_results': ema_results
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:78': {'patents_h2_2019': 16, 'years': [2015, 2016, 2017, 2018, 2019, 2020]}}

exec(code, env_args)
