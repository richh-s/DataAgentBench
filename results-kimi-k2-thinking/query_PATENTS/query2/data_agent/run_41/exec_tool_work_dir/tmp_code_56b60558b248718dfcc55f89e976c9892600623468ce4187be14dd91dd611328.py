code = """import json
import pandas as pd
import numpy as np
import re
from collections import defaultdict

# Load German patents from 2019
german_patents_file = locals()['var_functions.query_db:38']
with open(german_patents_file, 'r') as f:
    german_patents = json.load(f)

print(f'Analyzing {len(german_patents)} German patents...')

# Date and CPC parsing functions
def parse_month(date_str):
    if not date_str: return None
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    for abbr, num in months.items():
        if abbr in date_str.lower():
            return num
    return None

def extract_cpc_level4(cpc_data):
    try:
        cpc_list = json.loads(cpc_data)
        codes = []
        for item in cpc_list:
            code = item.get('code', '')
            if code and re.match(r'^[A-HY]\d{2}[A-Z]\d{2,4}/\d{2,4}$', code):
                codes.append(code.split('/')[0])  # Get group code
        return list(set(codes))
    except:
        return []

# Build monthly counts for H2 2019
cpc_monthly = defaultdict(lambda: defaultdict(int))
for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    month = parse_month(grant_date)
    if month and 7 <= month <= 12:
        codes = extract_cpc_level4(patent.get('cpc', ''))
        for code in codes:
            cpc_monthly[code][month] += 1

# Calculate EMAs (smoothing factor = 0.1)
alpha = 0.1
months = [7, 8, 9, 10, 11, 12]
month_names = ['July', 'August', 'September', 'October', 'November', 'December']

ema_results = []
for group_code, monthly_counts in cpc_monthly.items():
    values = [monthly_counts.get(m, 0) for m in months]
    ema_values = []
    ema_prev = values[0]
    for val in values:
        ema_current = alpha * val + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    max_ema = max(ema_values)
    best_idx = ema_values.index(max_ema)
    
    ema_results.append({
        'cpc_group_code': group_code,
        'max_ema': max_ema,
        'best_month': months[best_idx],
        'best_month_name': month_names[best_idx],
        'total_patents': sum(values),
        'monthly_values': values
    })

# Sort by highest EMA
ema_results.sort(key=lambda x: x['max_ema'], reverse=True)
top_10 = ema_results[:10]

# Load CPC definitions for group codes (query complete symbols)
groups_to_lookup = [r['cpc_group_code'] for r in top_10]
print('Looking up CPC definitions for:', groups_to_lookup[:5])

# Create final results
final_results = []
for r in top_10:
    final_results.append({
        'rank': len(final_results) + 1,
        'cpc_group_code': r['cpc_group_code'],
        'highest_ema': round(r['max_ema'], 2),
        'best_year': 2019,
        'best_month': r['best_month_name'],
        'title_full': f"Definition for {r['cpc_group_code']} (look up in CPC database)",
        'total_patents_h2_2019': r['total_patents']
    })

print('\nTop CPC Technology Areas in Germany (H2 2019) by EMA:')
print('=' * 70)
for r in final_results:
    print(f"Rank {r['rank']}: {r['cpc_group_code']}")
    print(f"  Highest EMA: {r['highest_ema']}")
    print(f"  Best Month: {r['best_month']} 2019")
    print(f"  Total Patents: {r['total_patents_h2_2019']}")
    print()

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}, 'var_functions.execute_python:20': {'pub_count': 5, 'cpc_count': 10, 'sample_pub_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'sample_grant_date': '3rd August 2021'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:46': {'total_cpc': 152, 'total_patents': 34, 'sample_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02M59/102', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'G01D11/24', 'B63B21/50']}, 'var_functions.query_db:52': [{'symbol': 'F02D41/0005', 'titleFull': 'Controlling intake air during deceleration'}, {'symbol': 'F02D41/0007', 'titleFull': 'Controlling intake air for control of turbo-charged or super-charged engines'}, {'symbol': 'F02D41/003', 'titleFull': 'Adding fuel vapours, e.g. drawn from engine fuel reservoir'}, {'symbol': 'F02D41/0047', 'titleFull': 'Controlling exhaust gas recirculation [EGR]'}, {'symbol': 'F02D41/0027', 'titleFull': 'Controlling engines characterised by use of non-liquid fuels, pluralities of fuels, or non-fuel substances added to the combustible mixtures the fuel being gaseous'}, {'symbol': 'B63B21/28', 'titleFull': 'Anchors securing to bed driven in by explosive charge'}, {'symbol': 'B63B21/27', 'titleFull': 'Anchors securing to bed by suction'}, {'symbol': 'B63B21/29', 'titleFull': 'Anchors securing to bed by weight, e.g. flukeless weight anchors'}, {'symbol': 'B63B21/32', 'titleFull': 'Anchors rigid when in use with one fluke'}, {'symbol': 'B63B21/34', 'titleFull': 'Anchors rigid when in use with two or more flukes'}, {'symbol': 'B63B21/44', 'titleFull': 'Anchors pivoting when in use with two or more flukes'}, {'symbol': 'B63B21/40', 'titleFull': 'Anchors pivoting when in use with one fluke'}, {'symbol': 'B63B21/60', 'titleFull': 'Quick releases'}, {'symbol': 'B63B21/663', 'titleFull': 'Fairings'}, {'symbol': 'F02D41/08', 'titleFull': 'Introducing corrections for particular operating conditions for idling'}, {'symbol': 'F02D41/10', 'titleFull': 'Introducing corrections for particular operating conditions for acceleration'}, {'symbol': 'F02D41/047', 'titleFull': 'Taking into account fuel evaporation or wall wetting'}, {'symbol': 'F02D41/12', 'titleFull': 'Introducing corrections for particular operating conditions for deceleration'}, {'symbol': 'F02D41/042', 'titleFull': 'Introducing corrections for particular operating conditions for stopping the engine'}, {'symbol': 'F02D41/045', 'titleFull': 'Detection of accelerating or decelerating state'}], 'var_functions.execute_python:54': {'ema_results': [{'cpc_group_code': 'C04B2235', 'max_ema': 3.2, 'best_month': 12, 'best_month_name': 'December', 'total_patents': 32, 'ema_values': [0.0, 0.0, 0.0, 0.0, 0.0, 3.2], 'raw_values': [0, 0, 0, 0, 0, 32]}, {'cpc_group_code': 'B29C2045', 'max_ema': 2.0, 'best_month': 7, 'best_month_name': 'July', 'total_patents': 2, 'ema_values': [2.0, 1.8, 1.62, 1.4580000000000002, 1.3122000000000003, 1.1809800000000004], 'raw_values': [2, 0, 0, 0, 0, 0]}, {'cpc_group_code': 'H01H2009', 'max_ema': 2.0, 'best_month': 7, 'best_month_name': 'July', 'total_patents': 2, 'ema_values': [2.0, 1.8, 1.62, 1.4580000000000002, 1.3122000000000003, 1.1809800000000004], 'raw_values': [2, 0, 0, 0, 0, 0]}, {'cpc_group_code': 'B29C2049', 'max_ema': 0.9, 'best_month': 8, 'best_month_name': 'August', 'total_patents': 9, 'ema_values': [0.0, 0.9, 0.81, 0.7290000000000001, 0.6561000000000001, 0.5904900000000002], 'raw_values': [0, 9, 0, 0, 0, 0]}, {'cpc_group_code': 'H01R2201', 'max_ema': 0.2, 'best_month': 12, 'best_month_name': 'December', 'total_patents': 2, 'ema_values': [0.0, 0.0, 0.0, 0.0, 0.0, 0.2], 'raw_values': [0, 0, 0, 0, 0, 2]}, {'cpc_group_code': 'F02N2200', 'max_ema': 0.2, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 2, 'ema_values': [0.0, 0.0, 0.0, 0.2, 0.18000000000000002, 0.16200000000000003], 'raw_values': [0, 0, 0, 2, 0, 0]}, {'cpc_group_code': 'F02N2300', 'max_ema': 0.2, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 2, 'ema_values': [0.0, 0.0, 0.0, 0.2, 0.18000000000000002, 0.16200000000000003], 'raw_values': [0, 0, 0, 2, 0, 0]}, {'cpc_group_code': 'F16H2200', 'max_ema': 0.2, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 2, 'ema_values': [0.0, 0.0, 0.0, 0.2, 0.18000000000000002, 0.16200000000000003], 'raw_values': [0, 0, 0, 2, 0, 0]}, {'cpc_group_code': 'F05D2270', 'max_ema': 0.1, 'best_month': 11, 'best_month_name': 'November', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.0, 0.1, 0.09000000000000001], 'raw_values': [0, 0, 0, 0, 1, 0]}, {'cpc_group_code': 'F05D2260', 'max_ema': 0.1, 'best_month': 11, 'best_month_name': 'November', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.0, 0.1, 0.09000000000000001], 'raw_values': [0, 0, 0, 0, 1, 0]}, {'cpc_group_code': 'B29C2949', 'max_ema': 0.1, 'best_month': 8, 'best_month_name': 'August', 'total_patents': 1, 'ema_values': [0.0, 0.1, 0.09000000000000001, 0.08100000000000002, 0.07290000000000002, 0.06561000000000002], 'raw_values': [0, 1, 0, 0, 0, 0]}, {'cpc_group_code': 'A61B2090', 'max_ema': 0.1, 'best_month': 8, 'best_month_name': 'August', 'total_patents': 1, 'ema_values': [0.0, 0.1, 0.09000000000000001, 0.08100000000000002, 0.07290000000000002, 0.06561000000000002], 'raw_values': [0, 1, 0, 0, 0, 0]}, {'cpc_group_code': 'G01N2021', 'max_ema': 0.1, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.1, 0.09000000000000001, 0.08100000000000002], 'raw_values': [0, 0, 0, 1, 0, 0]}, {'cpc_group_code': 'F02D2250', 'max_ema': 0.1, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.1, 0.09000000000000001, 0.08100000000000002], 'raw_values': [0, 0, 0, 1, 0, 0]}, {'cpc_group_code': 'F02D2200', 'max_ema': 0.1, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.1, 0.09000000000000001, 0.08100000000000002], 'raw_values': [0, 0, 0, 1, 0, 0]}, {'cpc_group_code': 'F16D2023', 'max_ema': 0.1, 'best_month': 8, 'best_month_name': 'August', 'total_patents': 1, 'ema_values': [0.0, 0.1, 0.09000000000000001, 0.08100000000000002, 0.07290000000000002, 0.06561000000000002], 'raw_values': [0, 1, 0, 0, 0, 0]}, {'cpc_group_code': 'F16D2011', 'max_ema': 0.1, 'best_month': 8, 'best_month_name': 'August', 'total_patents': 1, 'ema_values': [0.0, 0.1, 0.09000000000000001, 0.08100000000000002, 0.07290000000000002, 0.06561000000000002], 'raw_values': [0, 1, 0, 0, 0, 0]}, {'cpc_group_code': 'B60N2205', 'max_ema': 0.1, 'best_month': 10, 'best_month_name': 'October', 'total_patents': 1, 'ema_values': [0.0, 0.0, 0.0, 0.1, 0.09000000000000001, 0.08100000000000002], 'raw_values': [0, 0, 0, 1, 0, 0]}], 'top_groups': ['C04B2235', 'B29C2045', 'H01H2009', 'B29C2049', 'H01R2201', 'F02N2200', 'F02N2300', 'F16H2200', 'F05D2270', 'F05D2260'], 'h2_patent_count': 34}, 'var_functions.query_db:56': [], 'var_functions.query_db:58': [], 'var_functions.query_db:74': [{'symbol': 'H01H2009/164', 'titleFull': 'Indicators for switching condition, e.g. "on" or "off" comprising light emitting elements the light emitting elements being incorporated in and movable with the operating part'}, {'symbol': 'H01H2009/184', 'titleFull': 'Illumination of symbols by using laser light'}, {'symbol': 'H01H2009/183', 'titleFull': 'Provisions for enhancing the contrast between the illuminated symbol and the background or between juxtaposed symbols'}, {'symbol': 'B29C2045/0074', 'titleFull': 'Joining parts moulded in separate cavities inserting a heating tool inside the mould'}, {'symbol': 'B29C2045/0063', 'titleFull': 'Joining parts moulded in separate cavities facing before assembling, i.e. bringing the parts opposite to each other before assembling'}], 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
