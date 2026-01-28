code = """import json
import re
from collections import defaultdict

# Load data
patents_path = locals()['var_functions.query_db:44']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

cpc_path = locals()['var_functions.query_db:22']
with open(cpc_path, 'r') as f:
    cpc_definitions = json.load(f)

print(f'Loaded {len(patents_data)} Germany patents')
print(f'Loaded {len(cpc_definitions)} CPC definitions')

# Create CPC mapping and check format
cpc_symbols = set(d['symbol'] for d in cpc_definitions)
print(f'CPC symbols sample (first 20): {list(cpc_symbols)[:20]}')

# Date parsing and CPC extraction
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def parse_date(date_str):
    if not date_str:
        return None, None
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
    if not code:
        return None
    clean = code.split('/')[0].split('.')[0]
    if len(clean) >= 4:
        return clean[:4]
    return None

# Extract CPC codes from 2019 H2 Germany patents
cpc_codes_2019_h2 = defaultdict(int)
cpc_codes_all = defaultdict(lambda: defaultdict(int))
found_sample_patents = []

for i, patent in enumerate(patents_data):
    year, month = parse_date(patent.get('grant_date'))
    if not year:
        continue
    
    # Count CPC codes for all years
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        level4 = get_cpc_level4(code)
        if level4:
            cpc_codes_all[level4][year] += 1
            
            if year == 2019 and month and month >= 7:
                cpc_codes_2019_h2[level4] += 1
                if len(found_sample_patents) < 5:
                    title_data = patent.get('title_localized', '[]')
                    try:
                        titles = [t.get('text', '') for t in json.loads(title_data) if t.get('text')]
                        title = titles[0] if titles else 'No title'
                    except:
                        title = 'No title'
                    
                    found_sample_patents.append({
                        'index': i,
                        'cpc_code': level4,
                        'month': month,
                        'title': title
                    })

print(f'\nCPC codes in 2019 H2: {len(cpc_codes_2019_h2)}')
print(f'All CPC codes across years: {len(cpc_codes_all)}')
print(f'Top CPC codes in 2019 H2: {sorted(cpc_codes_2019_h2.items(), key=lambda x: x[1], reverse=True)[:10]}')

# Check for matches with CPC definitions
cpc_codes_list = list(cpc_codes_2019_h2.keys())
print(f'\nCPC codes from patents (sample 10): {cpc_codes_list[:10]}')

# Check if any matches exist
matches = []
for code in cpc_codes_list:
    if code in cpc_symbols:
        matches.append(code)

print(f'Exact matches with CPC definitions: {len(matches)}')
print(f'Matched codes: {matches}')

# Try partial matching for non-matching codes
non_matches = [c for c in cpc_codes_list if c not in cpc_symbols]
if non_matches:
    print(f'\nNon-matching CPC codes: {len(non_matches)}')
    
    # Try to find similar codes in definitions
    for code in non_matches[:5]:
        similar = [s for s in cpc_symbols if s.startswith(code) or code.startswith(s)]
        print(f'  Code {code}: similar definitions - {similar[:3]}')

# Sample patents found
print(f'\nSample 2019 H2 patents ({len(found_sample_patents)} found):')
for p in found_sample_patents:
    print(f"  Month {p['month']}: {p['cpc_code']} - {p['title'][:60]}")

result = {
    'total_germany_patents': len(patents_data),
    'cpc_codes_2019_h2_count': len(cpc_codes_2019_h2),
    'exact_matches': len(matches),
    'matched_codes': matches,
    'non_matching_codes_count': len(non_matches),
    'sample_patents': found_sample_patents
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}, 'var_functions.execute_python:36': {'results': []}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'top_cpc_codes': []}}

exec(code, env_args)
