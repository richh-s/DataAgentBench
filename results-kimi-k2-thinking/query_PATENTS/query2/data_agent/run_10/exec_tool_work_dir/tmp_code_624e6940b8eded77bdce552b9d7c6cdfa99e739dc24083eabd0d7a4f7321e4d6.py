code = """import json, os, re
from datetime import datetime

# Load all German patents
all_patents_file = locals()['var_functions.query_db:66']
with open(all_patents_file, 'r') as f:
    all_german_patents = json.load(f)

# Load H2 2019 patents
h2_patents_file = locals()['var_functions.query_db:70']
with open(h2_patents_file, 'r') as f:
    h2_2019_patents = json.load(f)

print('Total German patents: %d' % len(all_german_patents))
print('H2 2019 patents: %d' % len(h2_2019_patents))

# Date parsing
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

# Extract CPC level 4 counts by year for all German patents
cpc4_yearly_counts = {}
years = set()

for p in all_german_patents:
    grant_date = parse_date(p.get('grant_date', ''))
    if grant_date and 2015 <= grant_date.year <= 2020:
        year = grant_date.year
        years.add(year)
        
        if year not in cpc4_yearly_counts:
            cpc4_yearly_counts[year] = {}
        
        cpc_data = p.get('cpc', '')
        codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
        for code in codes:
            m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
            if m:
                cpc4 = m.group(1) + '/00'
                cpc4_yearly_counts[year][cpc4] = cpc4_yearly_counts[year].get(cpc4, 0) + 1

# Get CPC level 4 codes that appear in H2 2019 patents
h2_cpc4_codes = set()
for p in h2_2019_patents:
    cpc_data = p.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_data)
    for code in codes:
        m = re.match(r'^([A-Z]\d{2}[A-Z]\d)/\d+', code)
        if m:
            h2_cpc4_codes.add(m.group(1) + '/00')

print('Total years: %s' % sorted(years))
print('H2 2019 CPC4 codes: %d' % len(h2_cpc4_codes))

# Calculate EMA for each CPC4 code (smoothing factor 0.1)
ema_results = {}
sorted_years = sorted(years)

for cpc4 in h2_cpc4_codes:
    # Get time series for this CPC4 code
    yearly_values = []
    for year in sorted_years:
        count = cpc4_yearly_counts.get(year, {}).get(cpc4, 0)
        yearly_values.append(count)
    
    # Calculate EMA
    alpha = 0.1
    ema_values = []
    ema_prev = yearly_values[0] if yearly_values else 0
    ema_values.append(ema_prev)
    
    for i in range(1, len(yearly_values)):
        ema_current = alpha * yearly_values[i] + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find year with highest EMA
    if ema_values:
        max_ema_idx = ema_values.index(max(ema_values))
        best_year = sorted_years[max_ema_idx]
        ema_results[cpc4] = {
            'best_year': best_year,
            'max_ema': ema_values[max_ema_idx],
            'yearly_counts': dict(zip(sorted_years, yearly_values)),
            'ema_values': dict(zip(sorted_years, ema_values))
        }

print('CPC4 groups with EMA calculated: %d' % len(ema_results))
print('Sample result:')
for i, (cpc4, data) in enumerate(ema_results.items()):
    if i < 3:
        print('  %s: best year %d, max EMA %.2f' % (cpc4, data['best_year'], data['max_ema']))

result = {
    'h2_cpc4_count': len(h2_cpc4_codes),
    'years_analyzed': sorted_years,
    'ema_calculated': len(ema_results),
    'sample_results': [(k, v['best_year'], v['max_ema']) for k, v in list(ema_results.items())[:5]]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:78': {'patents_h2_2019': 16, 'years': [2015, 2016, 2017, 2018, 2019, 2020]}}

exec(code, env_args)
