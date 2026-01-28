code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict

# Load German patents from 2019
german_patents_file = locals()['var_functions.query_db:38']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

print(f'Loaded {len(german_patents)} German patents from 2019')

# Function to parse grant date and extract month/year
def parse_grant_date_month(date_str):
    if not date_str:
        return None
    
    try:
        # Remove prefixes like "dated", "on"
        date_str = re.sub(r'^dated\s+', '', date_str, flags=re.IGNORECASE)
        date_str = re.sub(r'^on\s+', '', date_str, flags=re.IGNORECASE)
        
        # Match month names
        month_match = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*', date_str, re.IGNORECASE)
        year_match = re.search(r'(2019)', date_str)
        
        if month_match and year_match:
            month_name = month_match.group(1).lower()
            month_map = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
            }
            month = month_map.get(month_name)
            if month:
                return month
        return None
    except:
        return None

# Function to extract level 4 CPC codes (XX99/99 or XX99/9999 format)
def extract_cpc_level4(cpc_data):
    try:
        # Parse CPC JSON
        cpc_list = json.loads(cpc_data)
        level4_codes = []
        pattern = r'^[A-HY]\d{2}[A-Z]\d{2,4}/\d{2,4}$'
        
        for item in cpc_list:
            code = item.get('code', '')
            if code:
                # Match pattern for level 4
                if re.match(pattern, code):
                    # Get the group part before /
                    group_part = code.split('/')[0]
                    if len(group_part) >= 7:  # E.g., B41F21
                        level4_codes.append(code)
        return level4_codes
    except:
        return []

# Process patents - filter for H2 2019 and extract CPC codes
cpc_patent_counts = defaultdict(lambda: defaultdict(int))  # cpc_code -> month -> count
h2_patents = []

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = parse_grant_date_month(grant_date)
    
    # Filter for H2 2019 (July-December)
    if month and month >= 7:
        cpc_data = patent.get('cpc', '')
        level4_codes = extract_cpc_level4(cpc_data)
        
        for cpc_code in level4_codes:
            cpc_patent_counts[cpc_code][month] += 1
        
        h2_patents.append(patent)

print(f'Patents granted in H2 2019: {len(h2_patents)}')
print(f'CPC level 4 codes found: {len(cpc_patent_counts)}')
print('Sample CPC codes:', list(cpc_patent_counts.keys())[:10])

# Display monthly counts for each CPC code
cpc_monthly_data = []
for cpc_code, month_counts in cpc_patent_counts.items():
    for month, count in month_counts.items():
        cpc_monthly_data.append({
            'cpc_code': cpc_code,
            'month': month,
            'count': count,
            'year': 2019
        })

df_monthly = pd.DataFrame(cpc_monthly_data)
if not df_monthly.empty:
    print('\nMonthly patent counts for each CPC (Level 4):')
    print(df_monthly.head(10))
    
print('__RESULT__:')
print(json.dumps({
    'total_cpc_level4': len(cpc_patent_counts),
    'total_h2_patents': len(h2_patents),
    'sample_cpc_codes': list(cpc_patent_counts.keys())[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}, 'var_functions.execute_python:20': {'pub_count': 5, 'cpc_count': 10, 'sample_pub_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_grant_date': '3rd August 2021'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
