code = """import json
import re
from collections import defaultdict

# Load datasets
patents_path = locals()['var_functions.query_db:44']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

cpc_path = locals()['var_functions.query_db:22']
with open(cpc_path, 'r') as f:
    cpc_definitions = json.load(f)

# Build mappings
cpc_titles = {d['symbol']: d.get('titleFull', '') for d in cpc_definitions}
cpc_symbols = set(cpc_titles.keys())

print('Patents: ' + str(len(patents_data)) + ', CPC defs: ' + str(len(cpc_symbols)))

# Date & CPC parsing
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def parse_date(date_str):
    if not date_str:
        return None, None
    patterns = [r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})', r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})']
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            month_str = match.group(2) if match.group(1).isdigit() else match.group(1)
            year = int(match.group(3))
            for key, val in month_map.items():
                if month_str.lower().startswith(key.lower()):
                    return year, val
    return None, None

def extract_cpc_level4(code):
    if not code:
        return None
    clean = code.split('/')[0].split('.')[0]
    return clean[:4] if len(clean) >= 4 else None

# Count CPC codes for Germany patents across all years
cpc_yearly = defaultdict(lambda: defaultdict(int))
cpc_2019_h2 = defaultdict(int)
h2_2019_count = 0

for patent in patents_data:
    year, month = parse_date(patent.get('grant_date', ''))
    if not year:
        continue
    
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        level4 = extract_cpc_level4(code)
        if level4:
            cpc_yearly[level4][year] += 1
            if year == 2019 and month and month >= 7:
                cpc_2019_h2[level4] += 1
    
    if year == 2019 and month and month >= 7:
        h2_2019_count += 1

print('Germany patents 2019 H2: ' + str(h2_2019_count))
print('CPC codes in 2019 H2: ' + str(len(cpc_2019_h2)))
print('Top 10 CPC codes: ' + str(sorted(cpc_2019_h2.items(), key=lambda x: x[1], reverse=True)[:10]))
print('Sample CPC codes from patents: ' + str(list(cpc_2019_h2.keys())[:10]))

# Find CPC codes present in definitions
matching_cpc_codes = []
for code in cpc_2019_h2.keys():
    if code in cpc_symbols:
        matching_cpc_codes.append(code)

print('Exact matches with CPC definitions: ' + str(len(matching_cpc_codes)))

# Calculate EMA and find best year for matching codes
def calc_ema(values, alpha=0.1):
    if not values:
        return []
    result = [values[0]]
    for v in values[1:]:
        result.append(alpha * v + (1 - alpha) * result[-1])
    return result

results = []
for cpc_code in matching_cpc_codes:
    yearly_data = cpc_yearly[cpc_code]
    sorted_years = sorted(yearly_data.keys())
    patent_counts = [yearly_data[y] for y in sorted_years]
    
    ema_values = calc_ema(patent_counts, alpha=0.1)
    idx = ema_values.index(max(ema_values))
    best_year = sorted_years[idx]
    
    # Get title
    title = cpc_titles.get(cpc_code, '')
    
    # Get representative patent title from 2019 H2
    rep_title = ''
    for patent in patents_data:
        y, m = parse_date(patent.get('grant_date', ''))
        if y == 2019 and m and m >= 7:
            cpcs = [extract_cpc_level4(c.get('code', '')) for c in json.loads(patent.get('cpc', '[]'))]
            if cpc_code in cpcs:
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
        'title_full': title,
        'representative_title': rep_title,
        'best_year': best_year,
        'patents_in_best_year': yearly_data[best_year],
        'ema_value': ema_values[idx],
        'patents_2019_h2': cpc_2019_h2[cpc_code]
    })

# Sort by EMA
top_results = sorted(results, key=lambda x: x['ema_value'], reverse=True)[:10]

print('\\nTOP CPC CODES BY EMA:')
for i, r in enumerate(top_results, 1):
    print(str(i) + '. ' + r['cpc_code'])
    print('   Full Title: ' + r['title_full'])
    print('   Best Year: ' + str(r['best_year']))
    print('   Patents in Best Year: ' + str(r['patents_in_best_year']))
    print('   EMA: ' + str(round(r['ema_value'], 2)))
    print('   2019 H2 Patents: ' + str(r['patents_2019_h2']))
    if r['representative_title']:
        print('   Sample Patent: ' + r['representative_title'][:80])
    print()

output = {'top_cpc_codes': top_results}
print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}, 'var_functions.execute_python:36': {'results': []}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'top_cpc_codes': []}}

exec(code, env_args)
