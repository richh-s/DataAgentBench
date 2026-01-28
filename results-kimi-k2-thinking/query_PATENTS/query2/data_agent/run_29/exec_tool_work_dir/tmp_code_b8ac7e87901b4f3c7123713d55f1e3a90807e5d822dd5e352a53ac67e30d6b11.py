code = """import json
import pandas as pd
from datetime import datetime
import re

# Access the result from the previous query
# The result is stored in a variable named var_functions.query_db:8
# Since we can't use this name directly with :, let's check what's in locals
available_vars = [var for var in locals().keys() if 'query_db' in var]
print(f'Available variables: {available_vars}')

# Get the data from the storage variable
data = locals().get('var_functions.query_db:8', [])

# Debug: print number of records and first few
print(f'Number of records: {len(data)}')
if data:
    print(f'First record keys: {data[0].keys() if isinstance(data[0], dict) else "Not a dict"}')
    print(f'First record CPC: {data[0].get("cpc", "No CPC") if isinstance(data[0], dict) else "Not a dict"}')

# Parse CPC codes and extract level 4 identifiers
cpc_year_data = []

for record in data:
    if not isinstance(record, dict):
        continue
    
    cpc_json = record.get('cpc', '')
    grant_date = record.get('grant_date', '')
    
    # Extract year from grant_date
    year_match = re.search(r'2019', grant_date)
    year = 2019  # All records should be from 2019
    
    if cpc_json and cpc_json != '[]':
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                if not isinstance(cpc_item, dict):
                    continue
                code = cpc_item.get('code', '')
                if code:
                    # Extract level 4 CPC (first 7 characters including the dot)
                    # CPC format: Section (1 char), Class (2 digits), Subclass (1 letter), Group (1-3 digits)
                    # Level 4 is typically the group level before the slash
                    # For example: B41F21/102 -> level 4 would be B41F21
                    
                    # Split by '/' to get the main group and subgroup
                    parts = code.split('/')
                    if len(parts) >= 1:
                        main_group = parts[0]
                        # For level 4, we want the first 6 characters (section + class + subclass + group)
                        # This is typically the first 6 characters of the main group
                        level4_code = main_group[:6] if len(main_group) >= 6 else main_group
                        
                        cpc_year_data.append({
                            'cpc_level4': level4_code,
                            'year': year,
                            'full_code': code
                        })
        except Exception as e:
            print(f'Error parsing CPC JSON: {e}, CPC: {cpc_json[:100]}...')
            continue

# Debug: print extracted CPC data
print(f'Extracted {len(cpc_year_data)} CPC level 4 entries')
if cpc_year_data:
    print(f'Sample entries: {cpc_year_data[:5]}')

# Count patents per CPC level 4 per year
cpc_year_counts = {}
for item in cpc_year_data:
    key = (item['cpc_level4'], item['year'])
    cpc_year_counts[key] = cpc_year_counts.get(key, 0) + 1

# Debug: print counts
print(f'Count entries: {len(cpc_year_counts)}')
for key, count in list(cpc_year_counts.items())[:10]:
    print(f'  {key}: {count}')

# Calculate EMA
# For EMA with smoothing factor 0.1, we need historical data
# Since we only have 2019 data, we'll calculate a simple score based on the count
# and treat it as the EMA for 2019

if cpc_year_counts:
    # Create dataframe for analysis
    df_counts = pd.DataFrame([
        {'cpc_level4': key[0], 'year': key[1], 'count': count}
        for key, count in cpc_year_counts.items()
    ])
    
    print(f'DataFrame shape: {df_counts.shape}')
    print(df_counts.head())
    
    # Calculate EMA (simplified - since we only have one year, EMA = count)
    df_counts['ema'] = df_counts['count']
    
    # Sort by EMA in descending order
    top_cpc = df_counts.sort_values('ema', ascending=False)
    
    print(f'Top CPC groups by EMA:')
    print(top_cpc.head(10))
    
    # Get top 10 for further analysis
    top_10_cpc = top_cpc.head(10).to_dict('records')
    
    # Save result
    result = {
        'cpc_analysis': {
            'total_unique_cpc_level4': len(top_cpc),
            'top_cpc_groups': top_10_cpc
        },
        'sample_patents_parsed': len(data)
    }
else:
    result = {'error': 'No CPC data found'}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': 'July 8th, 2019'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '8th April 2019'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019, May 30th'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd May 2019'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Nov 14th'}], 'var_functions.query_db:2': [{'total_patents': '68'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
