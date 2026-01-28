code = """import json
import re
import pandas as pd
import numpy as np
from collections import defaultdict

# Load German patents data
german_patents_file = locals()['var_functions.query_db:38']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

print(f'Processing {len(german_patents)} German patents from 2019...')

# Date parsing function
def parse_month(date_str):
    if not date_str:
        return None
    lower = date_str.lower()
    if 'jul' in lower: return 7
    if 'aug' in lower: return 8
    if 'sep' in lower: return 9
    if 'oct' in lower: return 10
    if 'nov' in lower: return 11
    if 'dec' in lower: return 12
    if 'jan' in lower: return 1
    if 'feb' in lower: return 2
    if 'mar' in lower: return 3
    if 'apr' in lower: return 4
    if 'may' in lower: return 5
    if 'jun' in lower: return 6
    return None

# CPC extraction function
def extract_cpc_level4(cpc_data):
    try:
        cpc_list = json.loads(cpc_data)
        codes = []
        for item in cpc_list:
            code = item.get('code', '')
            if code and re.match(r'^[A-HY][0-9]{2}[A-Z][0-9]{2,4}/[0-9]{2,4}$', code):
                codes.append(code)
        return codes
    except:
        return []

# Build monthly counts for Level 4 CPC codes
cpc_monthly = defaultdict(lambda: defaultdict(int))
h2_patents = []

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = parse_month(grant_date)
    
    # Only H2 2019 (July-December)
    if month and month >= 7 and month <= 12:
        cpc_data = patent.get('cpc', '')
        codes = extract_cpc_level4(cpc_data)
        
        for code in codes:
            # Extract group code (level 4 group, e.g., B41F21 from B41F21/102)
            group_code = code.split('/')[0]
            if len(group_code) >= 7:  # Level 4 format
                cpc_monthly[group_code][month] += 1
        
        h2_patents.append(patent)

print(f'H2 2019 patents: {len(h2_patents)}')
print(f'CPC Level 4 groups: {len(cpc_monthly)}')

# Calculate EMA for each CPC group (months 7-12: July-Dec)
alpha = 0.1
months = [7, 8, 9, 10, 11, 12]

ema_results = []
for group_code, monthly_counts in cpc_monthly.items():
    # Build time series
    values = [monthly_counts.get(month, 0) for month in months]
    
    # Calculate EMA
    ema_values = []
    ema_prev = values[0] if values else 0
    
    for value in values:
        ema_current = alpha * value + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find best month (highest EMA)
    max_ema = max(ema_values) if ema_values else 0
    max_month_idx = ema_values.index(max_ema) if ema_values else 0
    best_month = months[max_month_idx]
    
    ema_results.append({
        'cpc_group_code': group_code,
        'max_ema': max_ema,
        'best_month': best_month,
        'best_month_name': ['July', 'August', 'September', 'October', 'November', 'December'][max_month_idx],
        'total_patents': sum(values),
        'ema_values': ema_values,
        'raw_values': values
    })

# Sort by highest EMA
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

print(f'Top CPC groups by EMA: {len(ema_results)}')
print('Sample results:', ema_results[:5])

# Get CPC definitions for top 10 groups
top_groups = [r['cpc_group_code'] for r in ema_results[:10]]
print('Top groups to lookup:', top_groups)

print('__RESULT__:')
print(json.dumps({
    'ema_results': ema_results,
    'top_groups': top_groups,
    'h2_patent_count': len(h2_patents)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}, 'var_functions.execute_python:20': {'pub_count': 5, 'cpc_count': 10, 'sample_pub_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_grant_date': '3rd August 2021'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:46': {'total_cpc': 152, 'total_patents': 34, 'sample_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02M59/102', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'G01D11/24', 'B63B21/50']}, 'var_functions.query_db:52': [{'symbol': 'F02D41/0005', 'titleFull': 'Controlling intake air during deceleration'}, {'symbol': 'F02D41/0007', 'titleFull': 'Controlling intake air for control of turbo-charged or super-charged engines'}, {'symbol': 'F02D41/003', 'titleFull': 'Adding fuel vapours, e.g. drawn from engine fuel reservoir'}, {'symbol': 'F02D41/0047', 'titleFull': 'Controlling exhaust gas recirculation [EGR]'}, {'symbol': 'F02D41/0027', 'titleFull': 'Controlling engines characterised by use of non-liquid fuels, pluralities of fuels, or non-fuel substances added to the combustible mixtures the fuel being gaseous'}, {'symbol': 'B63B21/28', 'titleFull': 'Anchors securing to bed driven in by explosive charge'}, {'symbol': 'B63B21/27', 'titleFull': 'Anchors securing to bed by suction'}, {'symbol': 'B63B21/29', 'titleFull': 'Anchors securing to bed by weight, e.g. flukeless weight anchors'}, {'symbol': 'B63B21/32', 'titleFull': 'Anchors rigid when in use with one fluke'}, {'symbol': 'B63B21/34', 'titleFull': 'Anchors rigid when in use with two or more flukes'}, {'symbol': 'B63B21/44', 'titleFull': 'Anchors pivoting when in use with two or more flukes'}, {'symbol': 'B63B21/40', 'titleFull': 'Anchors pivoting when in use with one fluke'}, {'symbol': 'B63B21/60', 'titleFull': 'Quick releases'}, {'symbol': 'B63B21/663', 'titleFull': 'Fairings'}, {'symbol': 'F02D41/08', 'titleFull': 'Introducing corrections for particular operating conditions for idling'}, {'symbol': 'F02D41/10', 'titleFull': 'Introducing corrections for particular operating conditions for acceleration'}, {'symbol': 'F02D41/047', 'titleFull': 'Taking into account fuel evaporation or wall wetting'}, {'symbol': 'F02D41/12', 'titleFull': 'Introducing corrections for particular operating conditions for deceleration'}, {'symbol': 'F02D41/042', 'titleFull': 'Introducing corrections for particular operating conditions for stopping the engine'}, {'symbol': 'F02D41/045', 'titleFull': 'Detection of accelerating or decelerating state'}]}

exec(code, env_args)
