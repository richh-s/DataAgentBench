code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict

# Load German patents data
german_patents_file = locals()['var_functions.query_db:34']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

print(f'Loaded {len(german_patents)} German patents')

# Function to parse various date formats
def parse_grant_date(date_str):
    if not date_str:
        return None
    
    try:
        # Remove "dated" and other prefixes
        date_str = re.sub(r'^dated\s+', '', date_str, flags=re.IGNORECASE)
        date_str = re.sub(r'^on\s+', '', date_str, flags=re.IGNORECASE)
        
        # Try to extract month and year
        month_match = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*', date_str, re.IGNORECASE)
        year_match = re.search(r'(2019)', date_str)
        
        if month_match and year_match:
            month_name = month_match.group(1).lower()
            year = int(year_match.group(1))
            
            month_map = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
            }
            
            month = month_map.get(month_name)
            if month and year == 2019:
                return month
        return None
    except:
        return None

# Filter patents granted in second half of 2019 (July-December)
h2_2019_patents = []
for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = parse_grant_date(grant_date)
    if month and month >= 7:  # July to December
        h2_2019_patents.append(patent)

print(f'Patents granted in H2 2019: {len(h2_2019_patents)}')

# Extract CPC codes from level 4 (format: XX99/99 or XX99/9999)
cpc_level4_map = {}  # Maps CPC code to patents
cpc_patterns = [
    r'([A-HY]\d{2}[A-Z]\d{2}/\d{2})',  # XX99/99 format
    r'([A-HY]\d{2}[A-Z]\d{2}/\d{4})'   # XX99/9999 format  
]

for patent in h2_2019_patents:
    cpc_data = patent.get('cpc', '')
    if not cpc_data:
        continue
        
    try:
        # Parse the CPC JSON array
        cpc_list = json.loads(cpc_data)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code:
                continue
                
            # Match level 4 CPC codes
            for pattern in cpc_patterns:
                match = re.match(pattern, code)
                if match:
                    level4_code = match.group(1)
                    if level4_code not in cpc_level4_map:
                        cpc_level4_map[level4_code] = []
                    cpc_level4_map[level4_code].append(patent)
                    break
                    
    except json.JSONDecodeError:
        # Fallback: try to extract from string
        for pattern in cpc_patterns:
            matches = re.findall(pattern, cpc_data)
            for match in matches:
                if match not in cpc_level4_map:
                    cpc_level4_map[match] = []
                cpc_level4_map[match].append(patent)

print(f'Found {len(cpc_level4_map)} level 4 CPC codes in H2 2019')
print('Sample CPC codes:', list(cpc_level4_map.keys())[:10])

# Save results for next step
result = {
    'cpc_level4_map': cpc_level4_map,
    'total_patents': len(h2_2019_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}, 'var_functions.execute_python:20': {'pub_count': 5, 'cpc_count': 10, 'sample_pub_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_grant_date': '3rd August 2021'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
