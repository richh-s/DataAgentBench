code = """import json
import re
from datetime import datetime

file_path = locals()['var_function-call-18415164886367726200']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str: return None
    s = date_str.lower().replace(',', '').replace('dated', '').replace('on', '').replace('the', '').strip()
    s = re.sub(r'(?<=\d)(st|nd|rd|th)', '', s)
    formats = ["%d %b %Y", "%Y %b %d", "%d %B %Y", "%Y %B %d", "%Y %m %d"]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None

def is_h2_2019(d):
    if not d: return False
    return d.year == 2019 and d.month >= 7

valid_patents = []
for p in data:
    info = p.get('Patents_info', '')
    
    # Filter Country: Germany or DE code
    is_de = False
    if 'germany' in info.lower():
        is_de = True
    elif re.search(r'\bfrom DE\b', info) or re.search(r'\(no\. DE-', info) or re.search(r'publication (no\.|number) DE-', info):
        is_de = True
    
    if not is_de:
        continue

    g_date = parse_date(p.get('grant_date'))
    if not is_h2_2019(g_date):
        continue
    
    f_date = parse_date(p.get('filing_date'))
    if not f_date:
        continue
    
    cpc_json = p.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_json)
    except:
        continue
    
    codes = set()
    for item in cpcs:
        code = item.get('code', '')
        if len(code) >= 3:
            codes.add(code[:3])
            
    if codes:
        valid_patents.append({
            'year': f_date.year,
            'cpcs': list(codes)
        })

# Aggregate
counts = {} 
years_in_data = set()
for p in valid_patents:
    y = p['year']
    years_in_data.add(y)
    for c in p['cpcs']:
        if c not in counts:
            counts[c] = {}
        counts[c][y] = counts[c].get(y, 0) + 1

if not counts:
    print('__RESULT__:')
    print(json.dumps([]))
    exit()

min_year = min(years_in_data)
max_year = max(years_in_data)
sorted_years = sorted(range(min_year, max_year + 1))

alpha = 0.1
cpc_emas = {}

for cpc, year_counts in counts.items():
    ema_series = {}
    current_ema = None
    for y in sorted_years:
        cnt = year_counts.get(y, 0)
        if current_ema is None:
            current_ema = cnt
        else:
            current_ema = alpha * cnt + (1 - alpha) * current_ema
        ema_series[y] = current_ema
    cpc_emas[cpc] = ema_series

# Identify winners for each year
winners = set()
for y in sorted_years:
    best_cpc = None
    max_val = -1
    for cpc, series in cpc_emas.items():
        val = series.get(y, 0)
        if val > max_val:
            max_val = val
            best_cpc = cpc
    if best_cpc:
        winners.add(best_cpc)

final_list = []
for cpc in winners:
    series = cpc_emas[cpc]
    best_y = None
    max_v = -1
    for y, v in series.items():
        if v > max_v:
            max_v = v
            best_y = y
    
    final_list.append({
        "code": cpc,
        "best_year": best_y
    })

print('__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_function-call-13721774658737760568': 'file_storage/function-call-13721774658737760568.json', 'var_function-call-9307426392161200507': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_function-call-18415164886367725303': [{'symbol': 'B99', 'level': '4.0'}, {'symbol': 'B29', 'level': '4.0'}, {'symbol': 'B33', 'level': '4.0'}, {'symbol': 'C22', 'level': '4.0'}, {'symbol': 'D99', 'level': '4.0'}, {'symbol': 'F28', 'level': '4.0'}, {'symbol': 'B', 'level': '2.0'}, {'symbol': 'H', 'level': '2.0'}, {'symbol': 'Y', 'level': '2.0'}, {'symbol': 'D', 'level': '2.0'}, {'symbol': 'F', 'level': '2.0'}, {'symbol': 'E', 'level': '2.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'G', 'level': '2.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A45', 'level': '4.0'}, {'symbol': 'A24', 'level': '4.0'}, {'symbol': 'A61', 'level': '4.0'}, {'symbol': 'A63', 'level': '4.0'}, {'symbol': 'A22', 'level': '4.0'}], 'var_function-call-18415164886367726200': 'file_storage/function-call-18415164886367726200.json', 'var_function-call-1805589570488599833': [{'code': 'G01', 'best_year': 2008, 'max_ema': 1}]}

exec(code, env_args)
