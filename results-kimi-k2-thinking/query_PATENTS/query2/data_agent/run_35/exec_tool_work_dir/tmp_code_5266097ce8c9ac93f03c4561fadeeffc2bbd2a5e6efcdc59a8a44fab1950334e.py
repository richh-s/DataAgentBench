code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Load patents data
patents_file = locals()['var_functions.query_db:9']
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

# Load CPC definitions
cpc_file = locals()['var_functions.query_db:26']
with open(cpc_file, 'r') as f:
    cpc_definitions = json.load(f)

# Extract Germany patents and their CPC codes for 2017-2021
germany_patents = []

for row in patents_data:
    patents_info = str(row['Patents_info'])
    if 'DE-' not in patents_info:
        continue
    
    grant_date_str = str(row['grant_date'])
    if not grant_date_str or grant_date_str == 'None':
        continue
    
    # Extract year
    year_match = re.search(r'20\d{2}', grant_date_str)
    if year_match:
        year = int(year_match.group())
        if 2017 <= year <= 2021:
            # Extract month
            month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date_str, re.IGNORECASE)
            if month_match:
                month_str = month_match.group(1).capitalize()
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                }
                month_num = month_map.get(month_str, 0)
                
                # For 2019, only use second half
                if (year == 2019 and month_num >= 7) or (year != 2019):
                    # Extract CPC codes
                    cpc_str = str(row['cpc'])
                    if cpc_str and cpc_str != 'None':
                        try:
                            cpc_list = json.loads(cpc_str)
                            for cpc_item in cpc_list:
                                if isinstance(cpc_item, dict) and 'code' in cpc_item:
                                    cpc_code = cpc_item['code']
                                    if '/' in cpc_code:
                                        group_part = cpc_code.split('/')[0]
                                        if len(group_part) >= 4:
                                            level_4_group = group_part[:4]
                                            germany_patents.append({
                                                'year': year,
                                                'month': month_num,
                                                'cpc_level4': level_4_group,
                                                'cpc_full': cpc_code
                                            })
                        except:
                            pass

# Create DataFrame
df_patents = pd.DataFrame(germany_patents)

# Count patents per year per CPC level 4 group
yearly_counts = df_patents.groupby(['year', 'cpc_level4']).size().reset_index(name='count')

# Pivot to get years as columns
cpc_matrix = yearly_counts.pivot(index='cpc_level4', columns='year', values='count').fillna(0)

# Ensure we have all years from 2017-2021
for year in range(2017, 2022):
    if year not in cpc_matrix.columns:
        cpc_matrix[year] = 0

cpc_matrix = cpc_matrix[sorted(cpc_matrix.columns)]

print('CPC-level4 groups:', len(cpc_matrix))
print('Years:', cpc_matrix.columns.tolist())

# Calculate Exponential Moving Average (EMA) for each CPC group
# Using smoothing factor alpha = 0.1 (span = 2/alpha - 1 = 19)
alpha = 0.1
span = int(2/alpha - 1)

def calc_ema(series):
    return series.ewm(alpha=alpha, adjust=False).mean()

# Calculate EMA for each CPC group across years
ema_results = {}
for cpc_group in cpc_matrix.index:
    counts = cpc_matrix.loc[cpc_group, 2017:2021].values
    ema = calc_ema(pd.Series(counts))
    max_ema = ema.max()
    max_year_index = ema.idxmax()
    # Convert index to actual year (0-based index + 2017)
    max_year = 2017 + max_year_index if pd.notna(max_year_index) else None
    
    ema_results[cpc_group] = {
        'max_ema': max_ema,
        'max_ema_year': max_year,
        'ema_values': ema.tolist(),
        'original_counts': counts.tolist()
    }

# Sort by max EMA and get top 10
top_10_cpc = sorted(ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)[:10]

print('Top 10 CPC groups by EMA:')
for i, (cpc, data) in enumerate(top_10_cpc, 1):
    print(f"{i}. {cpc}: Max EMA = {data['max_ema']:.2f} in {data['max_ema_year']}")

# Get CPC definitions for top groups
cpc_def_dict = {d['symbol']: d['titleFull'] for d in cpc_definitions if d['symbol'] and d['titleFull']}

# For level 4 groups, we need to find the general group title
# The CPC symbols in the definitions are more specific, so we'll find the best match
final_results = []

for cpc_group, ema_data in top_10_cpc:
    # Find definition - look for exact level 4 or parent
    title = "Title not found"
    
    # Try to find exact match first
    for def_item in cpc_definitions:
        symbol = def_item['symbol']
        if symbol and len(symbol) >= 4 and symbol[:4] == cpc_group:
            title = def_item['titleFull']
            break
    
    # If still not found, look for parent groups
    if title == "Title not found":
        for def_item in cpc_definitions:
            symbol = def_item['symbol']
            if symbol and len(symbol) >= 4 and symbol.startswith(cpc_group[:3]):
                title = def_item['titleFull']
                break
    
    final_results.append({
        'cpc_group_code': cpc_group,
        'title': title,
        'best_year': ema_data['max_ema_year'],
        'max_ema': round(ema_data['max_ema'], 2)
    })

print('\nFinal Results:')
for i, result in enumerate(final_results, 1):
    print(f"{i}. {result['cpc_group_code']}: {result['title']}")
    print(f"   Best Year: {result['best_year']}, Max EMA: {result['max_ema']}")

print('__RESULT__:')
print(json.dumps(final_results[:10], indent=2))"""

env_args = {'var_functions.list_db:2': ['publicationinfo'], 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'count': 0, 'sample': []}, 'var_functions.execute_python:12': {'total_records': 3838, 'germany_patents_found': 50, 'sample_germany': [{'info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:14': {'germany_patents_second_half_2019': 0, 'sample': []}, 'var_functions.execute_python:16': {'sample_dates_2019': [{'patent_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date_raw': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date_raw': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'second_half_count': 24, 'sample_second_half': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date_raw': 'dated 21st November 2019', 'month': 11, 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date_raw': '5th of December, 2019', 'month': 12, 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'patent_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date_raw': '22nd of August, 2019', 'month': 8, 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}, 'var_functions.execute_python:18': {'total_records': 252, 'unique_level4_groups': 49, 'sample_records': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F21/102', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F22/00', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_full': 'B41F21/00', 'cpc_level4': 'B41F', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_full': 'F02D41/3005', 'cpc_level4': 'F02D', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_full': 'F02D41/20', 'cpc_level4': 'F02D', 'year': 2019}], 'cpc_level4_list': ['B60R', 'F04B', 'F42B', 'F24B', 'Y10T', 'E02F', 'A61L', 'E05B', 'B23K', 'A43B', 'B29C', 'G01N', 'Y02T', 'F02M', 'G07C', 'F02D', 'A61B', 'H01F', 'G01D', 'B64D', 'F41H', 'A47J', 'Y02E', 'H01H', 'F23N', 'A21C', 'C09K', 'H02J', 'G01F', 'B63B', 'B29D', 'H04L', 'B60W', 'B66C', 'Y02D', 'A61F', 'F23L', 'B60S', 'F02N', 'F23B', 'H04W', 'F02P', 'B41F', 'F16H', 'H01J', 'B60K', 'G02B', 'H01R', 'C04B']}, 'var_functions.execute_python:22': {'total_patents': 252, 'years': [2019], 'unique_cpc_level4': 49, 'yearly_counts_sample': [{'year': 2019, 'cpc_level4': 'A21C', 'count': 1}, {'year': 2019, 'cpc_level4': 'A43B', 'count': 5}, {'year': 2019, 'cpc_level4': 'A47J', 'count': 1}, {'year': 2019, 'cpc_level4': 'A61B', 'count': 5}, {'year': 2019, 'cpc_level4': 'A61F', 'count': 6}, {'year': 2019, 'cpc_level4': 'A61L', 'count': 2}, {'year': 2019, 'cpc_level4': 'B23K', 'count': 1}, {'year': 2019, 'cpc_level4': 'B29C', 'count': 19}, {'year': 2019, 'cpc_level4': 'B29D', 'count': 1}, {'year': 2019, 'cpc_level4': 'B41F', 'count': 3}], 'cpc_level4_list': ['A21C', 'A43B', 'A47J', 'A61B', 'A61F', 'A61L', 'B23K', 'B29C', 'B29D', 'B41F', 'B60K', 'B60R', 'B60S', 'B60W', 'B63B', 'B64D', 'B66C', 'C04B', 'C09K', 'E02F']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
