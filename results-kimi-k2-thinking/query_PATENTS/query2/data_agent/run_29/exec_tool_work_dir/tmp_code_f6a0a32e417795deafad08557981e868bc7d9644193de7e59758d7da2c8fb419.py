code = """import json
import pandas as pd
import re
import os

# Access the full dataset
# We need to find the most complete data source
var_candidates = [var for var in locals().keys() if 'query_db' in var]
print(f"Candidate variables: {var_candidates}")

# Find the variable with the most data
data = []
source_var = None
for var in var_candidates:
    try:
        var_value = locals()[var]
        if isinstance(var_value, list):
            if len(var_value) > len(data):
                data = var_value
                source_var = var
                print(f"Using {var} with {len(var_value)} records")
        elif isinstance(var_value, str) and '.json' in var_value:
            if os.path.exists(var_value):
                with open(var_value, 'r') as f:
                    loaded_data = json.load(f)
                if len(loaded_data) > len(data):
                    data = loaded_data
                    source_var = var
                    print(f"Using {var} from file with {len(loaded_data)} records")
    except:
        continue

print(f"Final dataset: {len(data)} records from {source_var}")

# Debug: Check grant dates
grant_dates = [r.get('grant_date', '') for r in data[:20]]
print(f"Sample grant dates: {grant_dates}")

# Function to extract month from grant_date
def extract_month(grant_date):
    date_str = grant_date.lower()
    if any(month in date_str for month in ['jul', 'jul.', 'july', 'jul,', 'jul/', 'jul1']):
        return 7
    elif any(month in date_str for month in ['aug', 'aug.', 'august']):
        return 8
    elif any(month in date_str for month in ['sep', 'sep.', 'sept', 'sept.', 'september']):
        return 9
    elif any(month in date_str for month in ['oct', 'oct.', 'october']):
        return 10
    elif any(month in date_str for month in ['nov', 'nov.', 'november']):
        return 11
    elif any(month in date_str for month in ['dec', 'dec.', 'december']):
        return 12
    else:
        return None

# Filter for second half of 2019 (July-December)
second_half_patents = []
for record in data:
    grant_date = record.get('grant_date', '')
    month = extract_month(grant_date)
    if month and month >= 7:  # July to December
        second_half_patents.append(record)

print(f"Patents in second half of 2019: {len(second_half_patents)}")

# Extract CPC level 4 codes and count patents
cpc_level4_counts = {}
cpc_full_codes = {}

for record in second_half_patents:
    cpc_field = record.get('cpc', '[]')
    if cpc_field and cpc_field != '[]':
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_item in cpc_list:
                full_code = cpc_item.get('code', '')
                if full_code and '/' in full_code:
                    level4_code = full_code.split('/')[0]
                    # CPC level 4 typically has 6-7 characters (e.g., B41F21, F02D41)
                    # Take first 6 characters for consistency
                    level4_key = level4_code[:6]
                    
                    cpc_level4_counts[level4_key] = cpc_level4_counts.get(level4_key, 0) + 1
                    
                    # Store one full code per level4 for reference
                    if level4_key not in cpc_full_codes:
                        cpc_full_codes[level4_key] = full_code
        except Exception as e:
            continue

print(f"Unique CPC level 4 groups: {len(cpc_level4_counts)}")
print(f"Top 10 CPC groups: {sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)[:10]}")

# Since we only have data for 2019, the EMA calculation is simplified:
# EMA for 2019 = actual count for 2019 (as there's no prior history)
# The "best year" for each CPC group is 2019 as it's the only year

# Prepare results for CPC definition lookup
cpc_results = []
for level4, count in sorted(cpc_level4_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
    cpc_results.append({
        'cpc_level4_code': level4,
        'full_cpc_code': cpc_full_codes.get(level4, ''),
        'patent_count_2019': count,
        'ema_2019': count,  # Since no historical data, EMA = actual count
        'best_year': 2019
    })

print(f"Prepared {len(cpc_results)} CPC groups for title lookup")

# Save results to a file for export
with open('/tmp/cpc_analysis_results.json', 'w') as f:
    json.dump({
        'analysis_summary': {
            'total_patents_second_half_2019': len(second_half_patents),
            'total_unique_cpc_level4': len(cpc_level4_counts),
            'top_cpc_groups': cpc_results[:10]
        },
        'all_cpc_groups': cpc_results
    }, f, indent=2)

print('Analysis complete, results saved to file')
print('__RESULT__:')
print(json.dumps({
    'status': 'analysis_complete',
    'patents_second_half_2019': len(second_half_patents),
    'unique_cpc_groups': len(cpc_level4_counts),
    'top_groups_sample': cpc_results[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': 'July 8th, 2019'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '8th April 2019'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019, May 30th'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd May 2019'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Nov 14th'}], 'var_functions.query_db:2': [{'total_patents': '68'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'error': 'No CPC data found'}, 'var_functions.query_db:14': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.execute_python:16': {'status': 'ready_to_query'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'status': 'success', 'record_count': 0}, 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.execute_python:30': {'status': 'complete', 'records': 10, 'sample_cpc_counts': {'G06F9': 2, 'A61D1': 1, 'A61B17': 5, 'E21B33': 2, 'G01S13': 1, 'G01S5': 1, 'F41G3': 1, 'F41H13': 1, 'G01S19': 5, 'F25B23': 1, 'F24D17': 2, 'F25B24': 1, 'Y02B10': 1, 'F24D22': 2, 'Y02B30': 2, 'G01N33': 4, 'A61K20': 4, 'A61K39': 3, 'G01N23': 1, 'C07K14': 2, 'B60P1': 1, 'B61D3': 4, 'Y02T30': 1, 'F16K17': 1, 'F16L43': 1}}}

exec(code, env_args)
