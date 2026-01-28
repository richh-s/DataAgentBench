code = """import json
import re
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Load the data
de_patents_path = locals()['var_functions.query_db:30']
if isinstance(de_patents_path, str) and de_patents_path.endswith('.json'):
    with open(de_patents_path, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = de_patents_path

# Function to extract year from grant_date (multiple formats)
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4-digit year patterns
    year_match = re.search(r'(\d{4})', str(date_str))
    if year_match:
        year = int(year_match.group(1))
        return year if 1900 <= year <= 2030 else None
    return None

# Extract data for patents with grant dates
patent_data = []
for patent in all_patents:
    grant_date = patent.get('grant_date')
    year = extract_year(grant_date)
    
    if year and year >= 2010:  # Recent enough
        # Parse CPC codes
        cpc_raw = patent.get('cpc', '')
        try:
            if cpc_raw and cpc_raw != '[]':
                cpc_list = json.loads(cpc_raw)
                if isinstance(cpc_list, list):
                    for cpc_item in cpc_list:
                        code = cpc_item.get('code', '')
                        if code:
                            patent_data.append({
                                'year': year,
                                'cpc_code': code,
                                'grant_date': grant_date
                            })
        except:
            # Skip invalid CPC data
            pass

# Filter for 2019 second half (July-December)
h2_2019_patents = []
for p in patent_data:
    if p['year'] == 2019:
        # Look for month indicators in grant_date for second half of year
        date_str = p['grant_date'].lower()
        # Common patterns for H2 months
        h2_indicators = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec',
                        '7th', '8th', '9th', '10th', '11th', '12th']
        if any(indicator in date_str for indicator in h2_indicators):
            h2_2019_patents.append(p)

# Group by CPC level 4 codes
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for patent in h2_2019_patents:
    full_code = patent['cpc_code']
    # Get level 4 code (first 4 characters of main class + first 4 of subclass)
    # Format: Section (1 char), Class (2-3 chars), Subclass (1 letter), Main group (1-4 digits)
    # Level 4 typically means: Section + Class + Subclass + first digit of main group
    if len(full_code) >= 7:  # e.g., G06F9/45533
        parts = full_code.split('/')
        if len(parts) == 2:
            section_class_subclass = parts[0]  # e.g., G06F9
            main_group = parts[1]  # e.g., 45533
            
            # Get first 4 characters (level 4)
            level4_code = f"{section_class_subclass}/{main_group[0]}"
            cpc_year_counts[level4_code][2019] += 1

# Calculate exponential moving average with smoothing factor 0.1
# For simplicity, we'll just use the 2019 count as the EMA since we only have one year
results = []
for cpc_code, year_counts in cpc_year_counts.items():
    ema = year_counts[2019]  # EMA with only one data point
    results.append({
        'cpc_level4_code': cpc_code,
        'ema_2019': ema,
        'count_2019': year_counts[2019]
    })

# Sort by EMA (count) descending
top_results = sorted(results, key=lambda x: x['ema_2019'], reverse=True)[:20]

print('__RESULT__:')
print(json.dumps(top_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'B4'}, {'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C2'}], 'var_functions.query_db:14': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004', 'sample_cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    ...'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'total_2019': '73'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_2019_patents': 73, 'sample': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11716}, 'var_functions.execute_python:34': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004'}}

exec(code, env_args)
