code = """import json
import re
import pandas as pd
from collections import defaultdict, OrderedDict
from datetime import datetime

# Load the German patent data from the file
de_patents_path = locals()['var_functions.query_db:30']
if isinstance(de_patents_path, str) and de_patents_path.endswith('.json'):
    with open(de_patents_path, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = de_patents_path

# Function to extract year and month from various date formats
def extract_year_and_month(date_str):
    if not date_str:
        return None, None
    date_str = str(date_str).lower()
    
    # Try to extract month and year
    # Patterns like "14th Mar 2019", "March 14th, 2019", "Mar 21st, 2019"
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None, None
    
    year = int(year_match.group(1))
    if year < 2010 or year > 2030:
        return None, None
    
    # Extract month
    month_patterns = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    month = None
    for month_abbr, month_num in month_patterns.items():
        if month_abbr in date_str:
            month = month_num
            break
    
    # Also check for month numbers (e.g., "7th", "8th")
    if not month:
        month_match = re.search(r'(\d{1,2})[a-z]*\s*(?:th|st|nd|rd)', date_str)
        if month_match:
            potential_month = int(month_match.group(1))
            if 1 <= potential_month <= 12:
                month = potential_month
    
    return year, month

# Function to extract CPC level 4 code
def get_cpc_level4(full_code):
    if '/' not in full_code:
        return None
    parts = full_code.split('/')
    section_class_subclass = parts[0]
    main_group = parts[1]
    
    # Level 4: Section + Class + Subclass + first digit of main group
    if len(main_group) >= 1:
        level4 = f"{section_class_subclass}/{main_group[0]}"
        return level4
    return None

# Collect all patent data with CPC codes
patent_records = []
for patent in all_patents:
    grant_date = patent.get('grant_date')
    year, month = extract_year_and_month(grant_date)
    
    if year and year >= 2010:  # Only recent patents
        # Parse CPC codes
        cpc_raw = patent.get('cpc', '')
        try:
            if cpc_raw and cpc_raw != '[]':
                cpc_list = json.loads(cpc_raw)
                if isinstance(cpc_list, list):
                    for cpc_item in cpc_list:
                        full_code = cpc_item.get('code', '')
                        if full_code and '/' in full_code:
                            level4_code = get_cpc_level4(full_code)
                            if level4_code:
                                patent_records.append({
                                    'year': year,
                                    'cpc_full': full_code,
                                    'cpc_level4': level4_code
                                })
        except:
            continue

# Group by CPC level 4 and year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
for record in patent_records:
    cpc_year_counts[record['cpc_level4']][record['year']] += 1

# Filter for CPC groups that have patents in H2 2019
h2_2019_cpc_codes = set()
for patent in patent_records:
    if patent['year'] == 2019:
        # Check if second half based on original grant date
        for p in all_patents:
            if p.get('grant_date') and '2019' in str(p.get('grant_date')):
                date_str = str(p.get('grant_date')).lower()
                h2_indicators = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec', '7th', '8th', '9th', '10th', '11th', '12th']
                if any(ind in date_str for ind in h2_indicators):
                    # Check if this patent has the CPC code
                    cpc_raw = p.get('cpc', '')
                    try:
                        if cpc_raw and cpc_raw != '[]':
                            cpc_list = json.loads(cpc_raw)
                            for cpc_item in cpc_list:
                                full_code = cpc_item.get('code', '')
                                level4 = get_cpc_level4(full_code)
                                if level4 == patent['cpc_level4']:
                                    h2_2019_cpc_codes.add(level4)
                                    break
                    except:
                        pass

# For CPCs in H2 2019, find their best year and EMA
final_results = []
for cpc_code in h2_2019_cpc_codes:
    if cpc_code in cpc_year_counts:
        year_counts = cpc_year_counts[cpc_code]
        # Find best year (year with max count)
        best_year = max(year_counts.items(), key=lambda x: x[1])[0]
        max_count = year_counts[best_year]
        
        # Calculate EMA for 2019 (with smoothing factor 0.1, but only using 2019 as baseline)
        # Since we don't have historical data, EMA for 2019 is just the count
        ema_2019 = year_counts.get(2019, 0)
        
        final_results.append({
            'cpc_level4_code': cpc_code,
            'ema_2019': ema_2019,
            'best_year': int(best_year),
            'best_year_count': max_count
        })

# Sort by EMA descending and get top results
top_results = sorted(final_results, key=lambda x: x['ema_2019'], reverse=True)[:15]

print('__RESULT__:')
print(json.dumps({
    'total_results': len(final_results),
    'top_cpc_codes': top_results
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'B4'}, {'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C2'}], 'var_functions.query_db:14': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004', 'sample_cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    ...'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'total_2019': '73'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_2019_patents': 73, 'sample': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11716}, 'var_functions.execute_python:34': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004'}, 'var_functions.execute_python:36': [{'cpc_level4_code': 'H01L2924/0', 'ema_2019': 31, 'count_2019': 31}, {'cpc_level4_code': 'H01L2924/1', 'ema_2019': 25, 'count_2019': 25}, {'cpc_level4_code': 'H04W52/0', 'ema_2019': 12, 'count_2019': 12}, {'cpc_level4_code': 'C04B2235/6', 'ema_2019': 12, 'count_2019': 12}, {'cpc_level4_code': 'H04L1/1', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'G01R33/5', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'H01J49/0', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'B01D2255/2', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'H01R4/1', 'ema_2019': 9, 'count_2019': 9}, {'cpc_level4_code': 'B01D53/9', 'ema_2019': 9, 'count_2019': 9}, {'cpc_level4_code': 'C04B2235/3', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'C04B35/6', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'B60L2240/4', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'F16H2200/2', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'B01J37/0', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'G01R33/3', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'H01L23/4', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'B29C2049/5', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'H01F6/0', 'ema_2019': 6, 'count_2019': 6}, {'cpc_level4_code': 'H01L2224/9', 'ema_2019': 6, 'count_2019': 6}], 'var_functions.execute_python:38': {'total_german_patents': 11716}, 'var_functions.execute_python:40': {'h2_2019_patents_count': 439, 'unique_cpc_groups': 180, 'top_cpc': [{'cpc_level4_code': 'H04W52/0', 'count_2019': 12, 'ema_2019': 12}, {'cpc_level4_code': 'C04B2235/6', 'count_2019': 12, 'ema_2019': 12}, {'cpc_level4_code': 'H04L1/1', 'count_2019': 10, 'ema_2019': 10}, {'cpc_level4_code': 'B01D2255/2', 'count_2019': 10, 'ema_2019': 10}, {'cpc_level4_code': 'H01R4/1', 'count_2019': 9, 'ema_2019': 9}, {'cpc_level4_code': 'B01D53/9', 'count_2019': 9, 'ema_2019': 9}, {'cpc_level4_code': 'C04B2235/3', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'C04B35/6', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'B01J37/0', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'B29C2049/5', 'count_2019': 7, 'ema_2019': 7}, {'cpc_level4_code': 'H01J49/0', 'count_2019': 6, 'ema_2019': 6}, {'cpc_level4_code': 'B01J29/4', 'count_2019': 6, 'ema_2019': 6}, {'cpc_level4_code': 'F02D41/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'G02B15/1', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'G02B23/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'H01R43/0', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'B01D2255/5', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'F01N3/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'H04L5/0', 'count_2019': 4, 'ema_2019': 4}, {'cpc_level4_code': 'A61F5/0', 'count_2019': 4, 'ema_2019': 4}]}}

exec(code, env_args)
