code = """import json
import re

# Load data
patents_data = []
cpc_definitions = []

with open(locals()['var_functions.query_db:44'], 'r') as f:
    patents_data = json.load(f)

with open(locals()['var_functions.query_db:22'], 'r') as f:
    cpc_definitions = json.load(f)

# Create CPC symbol set
cpc_symbols = set()
for d in cpc_definitions:
    cpc_symbols.add(d['symbol'])

print('Data loaded: patents=' + str(len(patents_data)) + ', cpc_defs=' + str(len(cpc_symbols)))

# Define month mapping
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
             'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6,
             'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

# Parse date function
def parse_date(date_str):
    if not date_str:
        return None, None
    patterns = [
        r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})',
        r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})'
    ]
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            month_str = match.group(2) if match.group(1).isdigit() else match.group(1)
            year = int(match.group(3))
            for key, val in month_map.items():
                if month_str.lower().startswith(key.lower()):
                    return year, val
    return None, None

# Extract CPC level 4 code
def extract_level4(code):
    if not code:
        return None
    parts = code.split('/')
    if not parts:
        return None
    clean = parts[0].split('.')[0]
    return clean[:4] if len(clean) >= 4 else None

# Process patents
cpc_patent_codes = set()
for patent in patents_data:
    year, month = parse_date(patent.get('grant_date', ''))
    if not (year == 2019 and month and month >= 7):
        continue
    
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
    except:
        continue
    
    for item in cpc_list:
        code = item.get('code', '')
        level4 = extract_level4(code)
        if level4:
            cpc_patent_codes.add(level4)

print('CPC codes from 2019 H2 patents: ' + str(len(cpc_patent_codes)))
print('Sample codes: ' + str(sorted(list(cpc_patent_codes))[:15]))
print('Sample definition symbols: ' + str(sorted(list(cpc_symbols))[:15]))

# Find matches
matches = []
for code in cpc_patent_codes:
    if code in cpc_symbols:
        matches.append(code)

print('\nExact matches: ' + str(len(matches)))
print('Matched: ' + str(matches))

result = {
    'patent_cpc_codes': len(cpc_patent_codes),
    'cpc_definitions': len(cpc_symbols),
    'exact_matches': len(matches),
    'matched_codes': matches,
    'all_patent_codes': sorted(list(cpc_patent_codes)),
    'sample_definitions': sorted(list(cpc_symbols))[:20]
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}, 'var_functions.execute_python:36': {'results': []}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'top_cpc_codes': []}, 'var_functions.execute_python:50': {'top_cpc_codes': []}}

exec(code, env_args)
