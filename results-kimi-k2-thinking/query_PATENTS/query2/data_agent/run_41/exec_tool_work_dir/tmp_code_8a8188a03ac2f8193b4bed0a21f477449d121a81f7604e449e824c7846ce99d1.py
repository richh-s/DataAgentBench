code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict

# Load the previous results
prev_file = locals()['var_functions.execute_python:46']
with open(prev_file, 'r') as f:
    analysis_data = json.load(f)

# Reconstruct the cpc_counts structure from the monthly data
cpc_counts = defaultdict(lambda: defaultdict(int))

# We need to recalculate this from the original data
german_patents_file = locals()['var_functions.query_db:38']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

# Simple month extraction
def get_month(date_str):
    if not date_str:
        return None
    lower = date_str.lower()
    if 'jul' in lower: return 7
    if 'aug' in lower: return 8
    if 'sep' in lower: return 9
    if 'oct' in lower: return 10
    if 'nov' in lower: return 11
    if 'dec' in lower: return 12
    return None

# Extract level 4 CPC codes
def get_cpc_codes(cpc_data):
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

# Build monthly counts for each CPC
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = get_month(grant_date)
    
    if month and month >= 7:  # H2 2019
        cpc_data = patent.get('cpc', '')
        codes = get_cpc_codes(cpc_data)
        
        for code in codes:
            cpc_monthly_counts[code][month] += 1

# Calculate Exponential Moving Average (EMA) for each CPC code
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
# Using smoothing factor α = 0.1
alpha = 0.1

ema_results = []
months = list(range(7, 13))  # July to December 2019

for cpc_code, monthly_counts in cpc_monthly_counts.items():
    # Build time series (monthly counts)
    values = [monthly_counts.get(month, 0) for month in months]
    
    # Calculate EMA
    ema_values = []
    ema_prev = values[0] if values else 0  # Initialize with first value
    
    for value in values:
        ema_current = alpha * value + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find month with highest EMA
    max_ema = max(ema_values)
    max_month_idx = ema_values.index(max_ema)
    max_month = months[max_month_idx]
    
    ema_results.append({
        'cpc_code': cpc_code,
        'max_ema': max_ema,
        'best_month': max_month,
        'ema_values': ema_values,
        'raw_values': values
    })

# Sort by max EMA value (descending) to get highest EMAs
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)

# Get CPC definitions for the top CPC codes
top_cpc_codes = [result['cpc_code'].split('/')[0] for result in ema_results[:20]]
print('Top CPC codes to lookup:', top_cpc_codes)

print('__RESULT__:')
print(json.dumps({
    'ema_results': ema_results[:20],  # Top 20 by EMA
    'top_cpc_symbols': top_cpc_codes,
    'total_cpc_analyzed': len(cpc_monthly_counts)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}, 'var_functions.execute_python:20': {'pub_count': 5, 'cpc_count': 10, 'sample_pub_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_grant_date': '3rd August 2021'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:46': {'total_cpc': 152, 'total_patents': 34, 'sample_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02M59/102', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'G01D11/24', 'B63B21/50']}}

exec(code, env_args)
