code = """import json
import re
from collections import defaultdict

# Read the data
patents_path = locals()['var_functions.query_db:14']
with open(patents_path, 'r') as f:
    patents_data = json.load(f)

# Month mapping
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
    base = code.split('/')[0].split('.')[0]
    if len(base) >= 4:
        return base[:4]
    return None

# Count Germany patents by year
germany_patents = []
germany_patents_2019_h2 = []

for i, patent in enumerate(patents_data):
    patents_info = patent.get('Patents_info', '')
    
    if not ('DE-' in patents_info or ' from DE,' in patents_info or 'Germany' in patents_info):
        continue
    
    grant_date_str = patent.get('grant_date')
    year, month = parse_grant_date(grant_date_str)
    
    if not year:
        continue
    
    germany_patents.append({
        'index': i,
        'year': year,
        'month': month,
        'grant_date': grant_date_str,
        'patents_info': patents_info[:50]
    })
    
    if year == 2019 and month and month >= 7:
        germany_patents_2019_h2.append({
            'index': i,
            'month': month,
            'patents_info': patents_info[:50]
        })

print(f"Total Germany patents: {len(germany_patents)}")
print(f"Germany patents 2019 H2: {len(germany_patents_2019_h2)}")

if germany_patents_2019_h2:
    print(f"Sample 2019 H2 patents:")
    for p in germany_patents_2019_h2[:3]:
        print(f"  Month {p['month']}: {p['patents_info']}...")

# Check CPC codes in these patents
cpc_codes_found = defaultdict(int)
months_found = defaultdict(int)

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if not ('DE-' in patents_info or ' from DE,' in patents_info):
        continue
    
    grant_date_str = patent.get('grant_date')
    year, month = parse_grant_date(grant_date_str)
    
    if year == 2019 and month and month >= 7:
        months_found[month] += 1
        
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data)
        except:
            continue
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            level4 = get_cpc_level4(code)
            if level4:
                cpc_codes_found[level4] += 1

print(f"\nCPC level 4 codes found: {len(cpc_codes_found)}")
print(f"Months distribution: {dict(months_found)}")
print(f"Top 10 CPC codes: {list(cpc_codes_found.items())[:10]}")

# Check CPC definitions existence
with open(locals()['var_functions.query_db:22'], 'r') as f:
    cpc_defs = json.load(f)

cpc_def_symbols = set(cpc_def['symbol'] for cpc_def in cpc_defs)
matching_codes = [code for code in cpc_codes_found.keys() if code in cpc_def_symbols]

print(f"\nMatching CPC codes in definitions: {len(matching_codes)}")
print(f"Sample matches: {matching_codes[:5]}")

output = {
    'germany_patents_total': len(germany_patents),
    'germany_patents_2019_h2': len(germany_patents_2019_h2),
    'cpc_level4_codes_found': len(cpc_codes_found),
    'cpc_codes_matched_in_definitions': len(matching_codes),
    'months_distribution': dict(months_found),
    'sample_cpc_codes': dict(list(cpc_codes_found.items())[:10])
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 50, 'germany_patents_h2_2019': 19}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_germany_patents': 11644, 'germany_patents_h2_2019': 19}, 'var_functions.execute_python:18': {'cpc_codes_count': 33, 'sample_codes': ['B41F', 'F02D', 'F02M', 'F04B', 'B63B', 'B66C', 'E02F', 'B60S', 'Y02T', 'A47J']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_cpc_codes_evaluated': 33, 'top_cpc_codes': []}}

exec(code, env_args)
