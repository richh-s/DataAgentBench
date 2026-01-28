code = """import json
import re
import pandas as pd
from collections import defaultdict

# Load German patents data
de_patents_path = locals()['var_functions.query_db:30']
if isinstance(de_patents_path, str) and de_patents_path.endswith('.json'):
    with open(de_patents_path, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = de_patents_path

# Load CPC definitions
cpc_defs_path = locals()['var_functions.query_db:56']
if isinstance(cpc_defs_path, str) and cpc_defs_path.endswith('.json'):
    with open(cpc_defs_path, 'r') as f:
        cpc_definitions = json.load(f)
else:
    cpc_definitions = cpc_defs_path

# Create CPC title lookup
cpc_title_lookup = {item['symbol']: item['titleFull'] for item in cpc_definitions}

# Function to extract year and month
def extract_year_and_month(date_str):
    if not date_str:
        return None, None
    date_str = str(date_str).lower()
    
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None, None
    
    year = int(year_match.group(1))
    if year < 2010 or year > 2030:
        return None, None
    
    month_patterns = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    month = None
    for month_abbr, month_num in month_patterns.items():
        if month_abbr in date_str:
            month = month_num
            break
    
    if not month:
        month_match = re.search(r'(\d{1,2})[a-z]*\s*(?:th|st|nd|rd)', date_str)
        if month_match:
            potential_month = int(month_match.group(1))
            if 1 <= potential_month <= 12:
                month = potential_month
    
    return year, month

# Function to get CPC level 4 code
def get_cpc_level4(full_code):
    if '/' not in full_code:
        return None
    parts = full_code.split('/')
    section_class_subclass = parts[0]
    main_group = parts[1]
    
    if len(main_group) >= 1:
        level4 = f"{section_class_subclass}/{main_group[0]}"
        return level4
    return None

# Collect patent data
patent_records = []
h2_2019_patents = []

for patent in all_patents:
    grant_date = patent.get('grant_date')
    year, month = extract_year_and_month(grant_date)
    
    if year and year >= 2010:
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
                                    'cpc_level4': level4_code
                                })
                                
                                # Track H2 2019
                                if year == 2019 and month and month >= 7:
                                    h2_2019_patents.append(level4_code)
        except:
            continue

# Group by CPC level 4 and year
cpc_year_counts = defaultdict(lambda: defaultdict(int))
for record in patent_records:
    cpc_year_counts[record['cpc_level4']][record['year']] += 1

# Find CPC codes in H2 2019
h2_2019_codes = set(h2_2019_patents)

# Calculate EMA and best year for each CPC code in H2 2019
final_results = []
for cpc_code in h2_2019_codes:
    if cpc_code in cpc_year_counts:
        year_counts = cpc_year_counts[cpc_code]
        
        # Get 2019 count (EMA base)
        count_2019 = year_counts.get(2019, 0)
        
        # Find best year
        best_year = max(year_counts.items(), key=lambda x: x[1]) if year_counts else (2019, 0)
        
        # Get full CPC level 4 symbol (formatted)
        formatted_symbol = cpc_code[0:-1] + '0' + cpc_code[-1] if len(cpc_code.split('/')[1]) == 1 else cpc_code
        
        final_results.append({
            'cpc_level4_code': formatted_symbol,
            'ema_2019': count_2019,
            'best_year': best_year[0],
            'best_year_count': best_year[1],
            'title_full': cpc_title_lookup.get(formatted_symbol, 'Title not found')
        })

# Sort by EMA descending and get top 10
top_10 = sorted(final_results, key=lambda x: x['ema_2019'], reverse=True)[:10]

print('__RESULT__:')
print(json.dumps({
    'total_cpc_codes_in_h2_2019': len(h2_2019_codes),
    'top_10_cpc_codes': top_10
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'B4'}, {'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C1'}, {'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'kind_code': 'C2'}], 'var_functions.query_db:14': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004', 'sample_cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    ...'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'total_2019': '73'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_2019_patents': 73, 'sample': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11716}, 'var_functions.execute_python:34': {'total_records': 11716, 'sample_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_grant_date': 'dated 7th October 2004'}, 'var_functions.execute_python:36': [{'cpc_level4_code': 'H01L2924/0', 'ema_2019': 31, 'count_2019': 31}, {'cpc_level4_code': 'H01L2924/1', 'ema_2019': 25, 'count_2019': 25}, {'cpc_level4_code': 'H04W52/0', 'ema_2019': 12, 'count_2019': 12}, {'cpc_level4_code': 'C04B2235/6', 'ema_2019': 12, 'count_2019': 12}, {'cpc_level4_code': 'H04L1/1', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'G01R33/5', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'H01J49/0', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'B01D2255/2', 'ema_2019': 10, 'count_2019': 10}, {'cpc_level4_code': 'H01R4/1', 'ema_2019': 9, 'count_2019': 9}, {'cpc_level4_code': 'B01D53/9', 'ema_2019': 9, 'count_2019': 9}, {'cpc_level4_code': 'C04B2235/3', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'C04B35/6', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'B60L2240/4', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'F16H2200/2', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'B01J37/0', 'ema_2019': 8, 'count_2019': 8}, {'cpc_level4_code': 'G01R33/3', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'H01L23/4', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'B29C2049/5', 'ema_2019': 7, 'count_2019': 7}, {'cpc_level4_code': 'H01F6/0', 'ema_2019': 6, 'count_2019': 6}, {'cpc_level4_code': 'H01L2224/9', 'ema_2019': 6, 'count_2019': 6}], 'var_functions.execute_python:38': {'total_german_patents': 11716}, 'var_functions.execute_python:40': {'h2_2019_patents_count': 439, 'unique_cpc_groups': 180, 'top_cpc': [{'cpc_level4_code': 'H04W52/0', 'count_2019': 12, 'ema_2019': 12}, {'cpc_level4_code': 'C04B2235/6', 'count_2019': 12, 'ema_2019': 12}, {'cpc_level4_code': 'H04L1/1', 'count_2019': 10, 'ema_2019': 10}, {'cpc_level4_code': 'B01D2255/2', 'count_2019': 10, 'ema_2019': 10}, {'cpc_level4_code': 'H01R4/1', 'count_2019': 9, 'ema_2019': 9}, {'cpc_level4_code': 'B01D53/9', 'count_2019': 9, 'ema_2019': 9}, {'cpc_level4_code': 'C04B2235/3', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'C04B35/6', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'B01J37/0', 'count_2019': 8, 'ema_2019': 8}, {'cpc_level4_code': 'B29C2049/5', 'count_2019': 7, 'ema_2019': 7}, {'cpc_level4_code': 'H01J49/0', 'count_2019': 6, 'ema_2019': 6}, {'cpc_level4_code': 'B01J29/4', 'count_2019': 6, 'ema_2019': 6}, {'cpc_level4_code': 'F02D41/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'G02B15/1', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'G02B23/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'H01R43/0', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'B01D2255/5', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'F01N3/2', 'count_2019': 5, 'ema_2019': 5}, {'cpc_level4_code': 'H04L5/0', 'count_2019': 4, 'ema_2019': 4}, {'cpc_level4_code': 'A61F5/0', 'count_2019': 4, 'ema_2019': 4}]}, 'var_functions.execute_python:42': {'total_results': 250, 'top_cpc_codes': [{'cpc_level4_code': 'H01L2924/0', 'ema_2019': 31, 'best_year': 2019, 'best_year_count': 31}, {'cpc_level4_code': 'H01L2924/1', 'ema_2019': 25, 'best_year': 2019, 'best_year_count': 25}, {'cpc_level4_code': 'C04B2235/6', 'ema_2019': 12, 'best_year': 2019, 'best_year_count': 12}, {'cpc_level4_code': 'H04W52/0', 'ema_2019': 12, 'best_year': 2019, 'best_year_count': 12}, {'cpc_level4_code': 'B01D2255/2', 'ema_2019': 10, 'best_year': 2019, 'best_year_count': 10}, {'cpc_level4_code': 'H04L1/1', 'ema_2019': 10, 'best_year': 2019, 'best_year_count': 10}, {'cpc_level4_code': 'G01R33/5', 'ema_2019': 10, 'best_year': 2019, 'best_year_count': 10}, {'cpc_level4_code': 'H01J49/0', 'ema_2019': 10, 'best_year': 2019, 'best_year_count': 10}, {'cpc_level4_code': 'H01R4/1', 'ema_2019': 9, 'best_year': 2019, 'best_year_count': 9}, {'cpc_level4_code': 'B01D53/9', 'ema_2019': 9, 'best_year': 2019, 'best_year_count': 9}, {'cpc_level4_code': 'B01J37/0', 'ema_2019': 8, 'best_year': 2019, 'best_year_count': 8}, {'cpc_level4_code': 'C04B2235/3', 'ema_2019': 8, 'best_year': 2013, 'best_year_count': 8}, {'cpc_level4_code': 'C04B35/6', 'ema_2019': 8, 'best_year': 2019, 'best_year_count': 8}, {'cpc_level4_code': 'B60L2240/4', 'ema_2019': 8, 'best_year': 2018, 'best_year_count': 10}, {'cpc_level4_code': 'F16H2200/2', 'ema_2019': 8, 'best_year': 2019, 'best_year_count': 8}]}, 'var_functions.execute_python:44': {'total_patents_available': 11716, 'data_source': "<class 'list'>"}, 'var_functions.query_db:48': [], 'var_functions.query_db:50': [{'symbol': 'B01D2255/102', 'titleFull': 'Platinum group metals'}, {'symbol': 'B01D2255/104', 'titleFull': 'Silver'}, {'symbol': 'B01D2255/106', 'titleFull': 'Gold'}, {'symbol': 'B01D2255/202', 'titleFull': 'Alkali metals'}, {'symbol': 'B01D2255/209', 'titleFull': 'Other metals'}, {'symbol': 'B01D2255/206', 'titleFull': 'Rare earth metals'}, {'symbol': 'B01D2255/207', 'titleFull': 'Transition metals'}, {'symbol': 'B01D2255/204', 'titleFull': 'Alkaline earth metals'}, {'symbol': 'B01D2255/405', 'titleFull': 'Spinels'}, {'symbol': 'B01D2255/402', 'titleFull': 'Perovskites'}, {'symbol': 'B01D2255/407', 'titleFull': 'Zr-Ce mixed oxides'}, {'symbol': 'B01D2255/502', 'titleFull': 'Beta zeolites'}, {'symbol': 'B01D2255/504', 'titleFull': 'ZSM 5 zeolites'}, {'symbol': 'B01D2255/705', 'titleFull': 'Ligands for metal-organic catalysts'}, {'symbol': 'B01D2255/707', 'titleFull': 'Additives or dopants'}, {'symbol': 'B01D2255/702', 'titleFull': 'Carbon'}, {'symbol': 'B01D2255/806', 'titleFull': 'Electrocatalytic'}, {'symbol': 'B01D2255/804', 'titleFull': 'Enzymatic'}, {'symbol': 'B01D2255/802', 'titleFull': 'Photocatalytic'}, {'symbol': 'B01D2255/808', 'titleFull': 'Hydrolytic'}, {'symbol': 'B01D2255/92', 'titleFull': 'Dimensions'}, {'symbol': 'B01D2255/902', 'titleFull': 'Multilayered catalyst'}, {'symbol': 'B01D2255/911', 'titleFull': 'NH3-storage component incorporated in the catalyst'}, {'symbol': 'B01D2255/905', 'titleFull': 'Catalysts having a gradually changing coating'}, {'symbol': 'B01D2255/909', 'titleFull': 'H2-storage component incorporated in the catalyst'}, {'symbol': 'B01D2255/904', 'titleFull': 'Multiple catalysts'}, {'symbol': 'B01D2255/912', 'titleFull': 'HC-storage component incorporated in the catalyst'}, {'symbol': 'B01D2255/903', 'titleFull': 'Multi-zoned catalysts'}, {'symbol': 'B01D2255/908', 'titleFull': 'O2-storage component incorporated in the catalyst'}, {'symbol': 'B01D2255/91', 'titleFull': 'NOx-storage component incorporated in the catalyst'}, {'symbol': 'B01D2255/906', 'titleFull': 'Catalyst dispersed in the gas'}, {'symbol': 'B01D2255/915', 'titleFull': 'Catalyst supported on particulate filters'}, {'symbol': 'B01J37/0018', 'titleFull': 'Addition of a binding agent or of material, later completely removed among others as result of heat treatment, leaching or washing,(e.g. forming of pores; protective layer, desintegrating by heat)'}, {'symbol': 'B01J37/0027', 'titleFull': 'Powdering'}, {'symbol': 'B01J37/0063', 'titleFull': 'Granulating'}, {'symbol': 'B60L2240/30', 'titleFull': 'Parking brake position'}, {'symbol': 'B60L2240/14', 'titleFull': 'Acceleration'}, {'symbol': 'B60L2240/24', 'titleFull': 'Steering angle'}, {'symbol': 'B60L2240/34', 'titleFull': 'Cabin temperature'}, {'symbol': 'B60L2240/32', 'titleFull': 'Driving direction'}, {'symbol': 'B60L2240/36', 'titleFull': 'Temperature of vehicle components or parts'}, {'symbol': 'B60L2240/26', 'titleFull': 'Vehicle weight'}, {'symbol': 'B60L2240/12', 'titleFull': 'Speed'}, {'symbol': 'B60L2240/22', 'titleFull': 'Yaw angle'}, {'symbol': 'B60L2240/28', 'titleFull': 'Door position'}, {'symbol': 'B60L2240/50', 'titleFull': 'Drive Train control parameters related to clutches'}, {'symbol': 'B60L2240/42', 'titleFull': 'Drive Train control parameters related to electric machines'}, {'symbol': 'B60L2240/46', 'titleFull': 'Drive Train control parameters related to wheels'}, {'symbol': 'B60L2240/52', 'titleFull': 'Drive Train control parameters related to converters'}, {'symbol': 'B60L2240/48', 'titleFull': 'Drive Train control parameters related to transmissions'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'symbol': 'C04B2235/30', 'titleFull': 'Constituents and secondary phases not being of a fibrous nature'}, {'symbol': 'B01D53/90', 'titleFull': 'Injecting reactants'}, {'symbol': 'B01D2255/20', 'titleFull': 'Metals or compounds thereof'}, {'symbol': 'B60L2240/40', 'titleFull': 'Drive Train control parameters'}, {'symbol': 'C04B2235/60', 'titleFull': 'Aspects relating to the preparation, properties or mechanical treatment of green bodies or pre-forms'}, {'symbol': 'F16H2200/20', 'titleFull': 'Transmissions using gears with orbital motion'}, {'symbol': 'G01R33/50', 'titleFull': 'NMR imaging systems based on the determination of relaxation times, e.g. T1 measurement by IR sequences; T2 measurement by multiple-echo sequences'}, {'symbol': 'B01J37/00', 'titleFull': 'Processes, in general, for preparing catalysts; Processes, in general, for activation of catalysts'}, {'symbol': 'H01J49/00', 'titleFull': 'Particle spectrometers or separator tubes'}, {'symbol': 'H04L1/00', 'titleFull': 'Arrangements for detecting or preventing errors in the information received'}, {'symbol': 'H04W52/00', 'titleFull': 'Power management, e.g. TPC [Transmission Power Control], power saving or power classes'}, {'symbol': 'H01R4/10', 'titleFull': 'Electrically-conductive connections between two or more conductive members in direct contact, i.e. touching one another; Means for effecting or maintaining such contact; Electrically-conductive connections having two or more spaced connecting locations for conductors and using contact members penetrating insulation effected solely by twisting, wrapping, bending, crimping, or other permanent deformation'}], 'var_functions.query_db:56': [{'symbol': 'C04B2235/30', 'titleFull': 'Constituents and secondary phases not being of a fibrous nature'}, {'symbol': 'G01R33/50', 'titleFull': 'NMR imaging systems based on the determination of relaxation times, e.g. T1 measurement by IR sequences; T2 measurement by multiple-echo sequences'}, {'symbol': 'B01J37/00', 'titleFull': 'Processes, in general, for preparing catalysts; Processes, in general, for activation of catalysts'}, {'symbol': 'H01J49/00', 'titleFull': 'Particle spectrometers or separator tubes'}, {'symbol': 'B01D53/90', 'titleFull': 'Injecting reactants'}, {'symbol': 'H04L1/00', 'titleFull': 'Arrangements for detecting or preventing errors in the information received'}, {'symbol': 'H04W52/00', 'titleFull': 'Power management, e.g. TPC [Transmission Power Control], power saving or power classes'}, {'symbol': 'H01R4/10', 'titleFull': 'Electrically-conductive connections between two or more conductive members in direct contact, i.e. touching one another; Means for effecting or maintaining such contact; Electrically-conductive connections having two or more spaced connecting locations for conductors and using contact members penetrating insulation effected solely by twisting, wrapping, bending, crimping, or other permanent deformation'}, {'symbol': 'B01D2255/20', 'titleFull': 'Metals or compounds thereof'}, {'symbol': 'B60L2240/40', 'titleFull': 'Drive Train control parameters'}, {'symbol': 'C04B2235/60', 'titleFull': 'Aspects relating to the preparation, properties or mechanical treatment of green bodies or pre-forms'}, {'symbol': 'F16H2200/20', 'titleFull': 'Transmissions using gears with orbital motion'}]}

exec(code, env_args)
