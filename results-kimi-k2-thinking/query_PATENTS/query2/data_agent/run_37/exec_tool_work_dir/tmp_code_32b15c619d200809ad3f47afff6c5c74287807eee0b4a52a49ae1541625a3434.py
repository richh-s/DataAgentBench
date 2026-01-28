code = """import json
import re
from collections import defaultdict

# Load data
patents_path = locals()['var_functions.query_db:14']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

cpc_path = locals()['var_functions.query_db:22']
with open(cpc_path, 'r') as f:
    cpc_definitions = json.load(f)

print(f'Patents: {len(patents_data)}')
print(f'CPC defs: {len(cpc_definitions)}')

# Date parsing
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def parse_date(date_str):
    if not date_str:
        return None, None
    patterns = [r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})', r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})', r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})']
    match = None
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            break
    if not match:
        return None, None
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
    return clean[:4] if len(clean) >= 4 else None

# Process Germany patents 2019 H2
h2_2019_patents = []
cpc_level4_counts = defaultdict(int)

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if not ('DE-' in patents_info or ' from DE,' in patents_info):
        continue
    
    year, month = parse_date(patent.get('grant_date'))
    if year == 2019 and month and month >= 7:
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data)
        except:
            continue
        
        patent_cpcs = []
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            level4 = get_cpc_level4(code)
            if level4:
                patent_cpcs.append(level4)
                cpc_level4_counts[level4] += 1
        
        if patent_cpcs:
            h2_2019_patents.append({
                'cpc': patent_cpcs,
                'patent_info': patents_info[:80]
            })

print(f'2019 H2 Germany patents: {len(h2_2019_patents)}')
print(f'CPC level4 codes found: {len(cpc_level4_counts)}')
print(f'Top CPC codes: {sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)[:10]}')

# Build CPC symbol match mapping
cpc_def_symbols = set(d['symbol'] for d in cpc_definitions)
print(f'\nSample CPC definition symbols: {list(cpc_def_symbols)[:20]}')
print(f'\nSample patent CPC codes: {list(cpc_level4_counts.keys())[:20]}')

# Find precise matches
exact_matches = {code: count for code, count in cpc_level4_counts.items() if code in cpc_def_symbols}
print(f'\nExact matches: {len(exact_matches)}')

# If no exact matches, try different matching strategies
if not exact_matches:
    # Strategy 1: Find definitions that start with patent code pattern
    prefix_matches = {}
    for code, count in cpc_level4_counts.items():
        for symbol in cpc_def_symbols:
            if code.startswith(symbol):
                prefix_matches[code] = (count, symbol)
                break
    
    print(f'Prefix matches: {len(prefix_matches)}')
    print(f'Prefix sample: {list(prefix_matches.items())[:10]}')
    
    # Strategy 2: Find patent codes that start with definition symbol
    suffix_matches = {}
    for symbol in cpc_def_symbols:
        matching_codes = [code for code in cpc_level4_counts.keys() if code.startswith(symbol)]
        if matching_codes:
            total = sum(cpc_level4_counts[c] for c in matching_codes)
            suffix_matches[symbol] = (total, matching_codes)
    
    print(f'Suffix matches (using definition symbols): {len(suffix_matches)}')
    print(f'Suffix sample: {list(suffix_matches.items())[:10]}')

# Final result
output = {
    'h2_2019_patents_count': len(h2_2019_patents),
    'cpc_level4_codes_extracted': len(cpc_level4_counts),
    'top_cpc_codes': sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)[:15],
    'exact_cpc_matches': len(exact_matches),
    'exact_match_codes': list(exact_matches.keys())[:10]
}

print('\n__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}, 'var_functions.execute_python:36': {'results': []}}

exec(code, env_args)
