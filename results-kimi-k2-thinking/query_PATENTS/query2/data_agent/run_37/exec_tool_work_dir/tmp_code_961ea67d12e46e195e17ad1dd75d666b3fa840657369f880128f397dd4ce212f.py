code = """import json
import re
from collections import defaultdict

# Read the data
patents_path = locals()['var_functions.query_db:14']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

def parse_grant_date(date_str):
    if not date_str:
        return None, None
    
    patterns = [
        r'(\d{1,2})(?:st|nd|rd|th)?\s+of?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th),?\s+(20\d{2})',
        r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+),?\s+(20\d{2})',
        r'([A-Za-z]+)\s+(\d{1,2}),?\s+(20\d{2})',
        r'dated\s+(\d{1,2})(?:st|nd|rd|th)\s+([A-Za-z]+)\s+(20\d{2})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            if pattern.count('([A-Za-z]+)') == 1:
                if match.group(1).isdigit():
                    month_str = match.group(2)
                    year = int(match.group(3))
                else:
                    month_str = match.group(1)
                    year = int(match.group(3))
            else:
                month_str = match.group(1)
                year = int(match.group(3))
            
            month = None
            for key, val in month_map.items():
                if month_str.lower().startswith(key.lower()):
                    month = val
                    break
            
            if month and year:
                return year, month
    
    return None, None

def get_cpc_level4(code):
    if not code:
        return None
    # Extract first 4 characters (letters + digits)
    # Format examples: G06F9/45533 -> G06F, A61D1/00 -> A61D, B41F21/102 -> B41F
    # We need to extract exactly 4 characters after cleaning
    clean = code.split('/')[0].split('.')[0]
    if len(clean) >= 4:
        return clean[:4]
    return None

# Extract CPC codes from 2019 H2 Germany patents
cpc_codes_sample = set()
germany_2019_h2_info = []

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if not ('DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info):
        continue
    
    grant_date_str = patent.get('grant_date')
    year, month = parse_grant_date(grant_date_str)
    
    if year == 2019 and month and month >= 7:
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data)
        except:
            continue
        
        codes = []
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            level4 = get_cpc_level4(code)
            if level4:
                cpc_codes_sample.add(level4)
                codes.append(level4)
        
        # Get title
        title_data = patent.get('title_localized', '[]')
        try:
            title_list = json.loads(title_data)
            titles = [t.get('text', '') for t in title_list if t.get('text')]
            title = titles[0] if titles else 'No title'
        except:
            title = 'No title'
        
        germany_2019_h2_info.append({
            'month': month,
            'cpc_codes': codes,
            'title': title,
            'grant_date': grant_date_str
        })

print('Sample patents from 2019 H2 in Germany:')
for i, p in enumerate(germany_2019_h2_info[:5]):
    print(str(i+1) + '. Month ' + str(p['month']) + ': ' + p['title'][:60])
    print('   CPC: ' + str(p['cpc_codes']))
    print('   Date: ' + str(p['grant_date']))

print('\nAll CPC Level 4 codes from 2019 H2 Germany patents:')
print(sorted(cpc_codes_sample))

# Check CPC definitions
with open(locals()['var_functions.query_db:22'], 'r') as f:
    cpc_defs = json.load(f)

cpc_def_symbols = set(cpc_def['symbol'] for cpc_def in cpc_defs)
print('\nTotal CPC level 4 definitions available: ' + str(len(cpc_def_symbols)))
print('Sample CPC definitions: ' + str(list(cpc_def_symbols)[:10]))

# Find intersections
intersection = cpc_codes_sample.intersection(cpc_def_symbols)
print('\nMatching CPC codes: ' + str(len(intersection)))
print('Matches: ' + str(sorted(intersection)))

# Get CPC codes not found
not_found = cpc_codes_sample - cpc_def_symbols
if not_found:
    print('\nCPC codes NOT in definitions: ' + str(sorted(not_found)))

output = {
    'germany_patents_2019_h2': len(germany_2019_h2_info),
    'cpc_codes_from_h2_patents': len(cpc_codes_sample),
    'matching_cpc_definitions': len(intersection),
    'non_matching_cpc': len(not_found),
    'all_cpc_codes': sorted(list(cpc_codes_sample)),
    'matching_cpc_codes': sorted(list(intersection)),
    'non_matching_cpc_codes': sorted(list(not_found)) if not_found else []
}

print('\n__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}, 'var_functions.execute_python:32': {'germany_patents_total': 1339, 'germany_patents_2019_h2': 19, 'cpc_codes_evaluated': 0, 'top_cpc_codes': []}}

exec(code, env_args)
