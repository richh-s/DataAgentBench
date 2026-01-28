code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict
import re

# Load the file paths
file_path_all = locals()['var_functions.query_db:20']  # All DE patents
file_path_2019 = locals()['var_functions.query_db:8']  # 2019 second half DE patents

# Load all DE patent data
with open(file_path_all, 'r') as f:
    de_patents_all = json.load(f)

# Load 2019 second half data
with open(file_path_2019, 'r') as f:
    de_patents_2019 = json.load(f)

print('Loaded ' + str(len(de_patents_all)) + ' total DE patents')
print('Loaded ' + str(len(de_patents_2019)) + ' 2019 second half DE patents')

# Extract CPC level 4 codes from 2019 second half patents
codes_2019_level4 = set()
for patent in de_patents_2019:
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                level4 = code.split('/')[0]
                codes_2019_level4.add(level4)
    except:
        continue

print('CPC Level 4 groups from 2019 second half: ' + str(len(codes_2019_level4)))

# Build historical data for these CPC groups
year_pattern = r'(\d{4})'
historical_data = []

for patent in de_patents_all:
    grant_date = patent.get('grant_date', '')
    if not grant_date:
        continue
    
    # Extract year
    year_match = re.search(year_pattern, grant_date)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Extract CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                level4 = code.split('/')[0]
                if level4 in codes_2019_level4:
                    historical_data.append({
                        'year': year,
                        'cpc_group': level4,
                        'full_code': code
                    })
    except:
        continue

print('Historical records for 2019 CPC groups: ' + str(len(historical_data)))

# Create DataFrame
df = pd.DataFrame(historical_data)
print('Year range: ' + str(df['year'].min()) + ' to ' + str(df['year'].max()))

# Group by year and CPC group
grouped = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
print('Year-group combinations: ' + str(len(grouped)))

# Get years with data for each group
group_years = grouped.groupby('cpc_group')['year'].apply(list).to_dict()

# Prepare for EMA calculation
# For each CPC group, create a complete time series from first to last year
results = []
smoothing = 0.1

for cpc_group in codes_2019_level4:
    group_data = grouped[grouped['cpc_group'] == cpc_group]
    if group_data.empty:
        continue
    
    years = sorted(group_data['year'].tolist())
    if len(years) < 2:
        continue
    
    year_counts = dict(zip(group_data['year'], group_data['count']))
    
    # Create complete time series
    all_years = list(range(min(years), max(years) + 1))
    yearly_counts = []
    
    for year in all_years:
        yearly_counts.append(year_counts.get(year, 0))
    
    # Calculate EMA
    ema_values = []
    ema_prev = yearly_counts[0]  # Initialize with first value
    ema_values.append(ema_prev)
    
    for i in range(1, len(yearly_counts)):
        ema_current = smoothing * yearly_counts[i] + (1 - smoothing) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find best year (highest EMA in 2019 or earlier)
    valid_years = [y for y in all_years if y <= 2019]
    valid_ema = [ema_values[all_years.index(y)] for y in valid_years]
    
    if valid_ema:
        best_ema = max(valid_ema)
        best_year = valid_years[valid_ema.index(best_ema)]
        
        # Get full title for best code (one with highest count in best year)
        best_year_data = df[(df['cpc_group'] == cpc_group) & (df['year'] == best_year)]
        if not best_year_data.empty:
            most_common_code = best_year_data['full_code'].value_counts().index[0]
        else:
            most_common_code = cpc_group + '/00'  # fallback
        
        results.append({
            'cpc_group': cpc_group,
            'best_year': best_year,
            'best_ema': best_ema,
            'full_code': most_common_code,
            'years_active': len([y for y in yearly_counts if y > 0])
        })

# Sort by best EMA
top_results = sorted(results, key=lambda x: x['best_ema'], reverse=True)[:10]

print('Top 10 CPC groups by EMA:')
for r in top_results:
    print('  ' + r['cpc_group'] + ' (2019: ' + str([y for y in all_years if y == 2019]) + ' EMA=' + str(round(r['best_ema'], 2)) + ')')

result = {
    'candidates': len(results),
    'top_groups': top_results
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': 'July 8th, 2019', 'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '8th April 2019', 'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019, May 30th', 'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'grant_date': '22nd May 2019', 'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'grant_date': '2019 on Nov 14th', 'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'total_patents': 34, 'total_cpc_codes': 313, 'unique_cpc_codes': 201, 'cpc_level4_groups': 115, 'top_groups': [['C04B2235', 32], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['F02M59', 8], ['A61F5', 6]]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_patents': 11644, 'patent_cpc_records': 26277, 'cpc_groups': 3740, 'year_range': [1882, 2024], 'year_group_combinations': 9135, 'data_preview': [{'cpc_level4': 'A01B15', 'year': 1921, 'count': 1}, {'cpc_level4': 'A01B17', 'year': 1921, 'count': 1}, {'cpc_level4': 'A01B3', 'year': 1952, 'count': 1}, {'cpc_level4': 'A01B3', 'year': 2014, 'count': 1}, {'cpc_level4': 'A01B35', 'year': 1928, 'count': 1}, {'cpc_level4': 'A01B59', 'year': 1928, 'count': 1}, {'cpc_level4': 'A01B59', 'year': 2016, 'count': 1}, {'cpc_level4': 'A01B63', 'year': 1952, 'count': 1}, {'cpc_level4': 'A01B63', 'year': 2005, 'count': 1}, {'cpc_level4': 'A01B73', 'year': 2009, 'count': 1}]}, 'var_functions.execute_python:24': {'cpc_level4_codes_2019': ['H01F27', 'A43B13', 'G01L23', 'H01L23', 'H01H2009', 'H03L7', 'H04W72', 'B64D11', 'C04B35', 'F04B53', 'B29C2045', 'F04D29', 'B29C2049', 'H01R2201', 'B60W30', 'B29D99', 'H01L2924', 'G01D11', 'F41H11', 'B60S9', 'C04B40', 'G02B5', 'C09K11', 'F02N2200', 'A61L2', 'A61B90', 'B23K1', 'F16H2200', 'B66C23', 'H04L1', 'H04L5', 'G01F23', 'B60N2', 'H01J49', 'B41F22', 'F02D2200', 'Y02E20', 'G01M1', 'F02N2300', 'G07C9', 'F02D13', 'B60K6', 'F16D2023', 'H02J1', 'E05B19', 'A61B2090', 'F02D15', 'F05D2260', 'G02B23', 'H01R24', 'F02D35', 'F02D41', 'B29C45', 'G01L27', 'E02F9', 'F02M65', 'E02F3', 'B60R16', 'Y02D30', 'F23B50', 'F02P3', 'G02B21', 'C04B2235', 'F02M55', 'F05D2270', 'H02J7', 'Y02T10', 'F42B3', 'F02M59', 'A21C9', 'G08B17', 'B60K17', 'B60K23', 'F16F15', 'H01L25', 'G02B26', 'B63B21', 'F23B60', 'G01N2021', 'F16H37', 'F23L15', 'H01F38', 'G02B13', 'H04W76', 'A61B1', 'B29C49', 'A47J37', 'B29C2949', 'Y10T70', 'F02D2250', 'F02P15', 'G08B19', 'H04W52', 'G02B15', 'F16C33', 'H01H9', 'H04L7', 'H01R13', 'G01N27', 'B41F21', 'F16D2011', 'F16D27', 'F16H3', 'H01R35', 'F02N11', 'B60N2205', 'A43B17', 'F23N1', 'B62D21', 'A43B7', 'F01D5', 'F23L1', 'B62D25', 'A61F5', 'F24B5'], 'count': 115}}

exec(code, env_args)
