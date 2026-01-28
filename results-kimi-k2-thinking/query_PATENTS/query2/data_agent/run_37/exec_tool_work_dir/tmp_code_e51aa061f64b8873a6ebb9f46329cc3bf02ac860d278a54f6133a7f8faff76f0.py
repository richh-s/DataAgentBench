code = """import json
import re
from collections import defaultdict

# Load patents data
patents_path = locals()['var_functions.query_db:14']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

# Load CPC definitions
cpc_path = locals()['var_functions.query_db:22']
with open(cpc_path, 'r') as f:
    cpc_definitions = json.load(f)

# Create CPC title mapping
cpc_titles = {d['symbol']: d.get('titleFull', '') for d in cpc_definitions}

# Date parsing
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def parse_date(date_str):
    if not date_str: return None, None
    patterns = [r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})', r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})']
    for pattern in patterns:
        if (match := re.search(pattern, date_str, re.IGNORECASE)):
            month_str = match.group(2) if match.group(1).isdigit() else match.group(1)
            year = int(match.group(3))
            for key, val in month_map.items():
                if month_str.lower().startswith(key.lower()):
                    return year, val
    return None, None

def get_cpc_level4(code):
    if not code: return None
    clean = code.split('/')[0].split('.')[0]
    return clean[:4] if len(clean) >= 4 else None

# Process patents
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
germany_h2_2019_cpcs = defaultdict(int)

for patent in patents_data:
    # Check Germany patent
    patents_info = patent.get('Patents_info', '')
    if not ('DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info):
        continue
    
    # Parse grant date
    year, month = parse_date(patent.get('grant_date'))
    if not year: continue
    
    # Extract CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        level4 = get_cpc_level4(code)
        if not level4: continue
        
        # Count all years for EMA
        cpc_yearly_counts[level4][year] += 1
        
        # Track 2019 H2 specifically
        if year == 2019 and month and month >= 7:
            germany_h2_2019_cpcs[level4] += 1

# Calculate EMA for CPC codes in 2019 H2
def calc_ema(values, alpha=0.1):
    if not values: return []
    ema = [values[0]]
    for v in values[1:]:
        ema.append(alpha * v + (1 - alpha) * ema[-1])
    return ema

results = []
for cpc_code in germany_h2_2019_cpcs:
    if cpc_code not in cpc_titles:
        continue
    
    yearly_data = cpc_yearly_counts[cpc_code]
    if 2019 not in yearly_data:
        continue
    
    # Prepare yearly data for EMA
    sorted_years = sorted(yearly_data.keys())
    values = [yearly_data[y] for y in sorted_years]
    
    # Calculate EMA
    ema_values = calc_ema(values, alpha=0.1)
    
    # Find best year (highest EMA)
    max_ema_idx = ema_values.index(max(ema_values))
    best_year = sorted_years[max_ema_idx]
    
    # Get a representative title (first one found)
    rep_title = ''
    for patent in patents_data:
        pi = patent.get('Patents_info', '')
        if not ('DE-' in pi or ' from DE,' in pi): continue
        y, m = parse_date(patent.get('grant_date'))
        if y == 2019 and cpc_code in [get_cpc_level4(c.get('code', '')) for c in json.loads(patent.get('cpc', '[]'))]:
            title_data = patent.get('title_localized', '[]')
            try:
                titles = [t.get('text', '') for t in json.loads(title_data) if t.get('text')]
                if titles:
                    rep_title = titles[0]
                    break
            except:
                pass
    
    results.append({
        'cpc_code': cpc_code,
        'title_full': cpc_titles[cpc_code],
        'representative_title': rep_title,
        'best_year': best_year,
        'patents_in_best_year': yearly_data[best_year],
        'ema_value': ema_values[max_ema_idx],
        'patents_2019_h2': germany_h2_2019_cpcs[cpc_code]
    })

# Sort by EMA value
top_results = sorted(results, key=lambda x: x['ema_value'], reverse=True)

print('CPC Technology Areas in Germany with Highest EMA for 2019 H2 Patents:')
print('========================================================================')
for i, r in enumerate(top_results[:10], 1):
    print(f"{i}. CPC Code: {r['cpc_code']}")
    print(f"   Full Title: {r['title_full']}")
    print(f"   Best Year: {r['best_year']}")
    print(f"   Patents in Best Year: {r['patents_in_best_year']}")
    print(f"   EMA Value: {r['ema_value']:.2f}")
    print(f"   Patents in 2019 H2: {r['patents_2019_h2']}")
    if r['representative_title']:
        print(f"   Representative Patent Title: {r['representative_title']}")
    print()

output = {'results': top_results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}}

exec(code, env_args)
