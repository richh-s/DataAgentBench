code = """import json
import re
from collections import defaultdict
import math

# Load German patents data for 2019 second half
file_path_2019 = locals()['var_functions.query_db:22']
with open(file_path_2019, 'r') as f:
    german_patents_2019 = json.load(f)

# Query variable for 2015 data
file_path_2015 = locals()['var_functions.query_db:50']
with open(file_path_2015, 'r') as f:
    german_patents_2015 = json.load(f)

# Helper functions
def extract_cpc_codes(cpc_json):
    try:
        return [item['code'] for item in json.loads(cpc_json)]
    except:
        return []

def extract_year_from_date(date_str):
    try:
        match = re.search(r'(\d{4})', date_str)
        return int(match.group(1)) if match else None
    except:
        return None

def get_cpc_level_4(code):
    match = re.match(r'^([A-Z]\d{2}[A-Z])', code)
    return match.group(1) if match else None

# Collect data for multiple years
years_to_analyze = [2015, 2016, 2017, 2018, 2019]
patent_counts = defaultdict(lambda: defaultdict(int))

def process_patents_batch(patents_batch):
    for patent in patents_batch:
        grant_date = patent['grant_date']
        year = extract_year_from_date(grant_date)
        if year in years_to_analyze:
            cpc_codes = extract_cpc_codes(patent['cpc'])
            for cpc_code in cpc_codes:
                level4_code = get_cpc_level_4(cpc_code)
                if level4_code:
                    patent_counts[level4_code][year] += 1

process_patents_batch(german_patents_2019)
process_patents_batch(german_patents_2015)

# Calculate EMA for each CPC group
alpha = 0.1
ema_results = defaultdict(dict)

for cpc_code in patent_counts:
    # Get sorted years
    sorted_years = sorted(patent_counts[cpc_code].keys())
    if not sorted_years:
        continue
    
    # Initialize EMA
    ema = None
    
    for year in sorted_years:
        count = patent_counts[cpc_code][year]
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        ema_results[cpc_code][year] = ema

# Find best year for each CPC (year with highest EMA)
best_years = {}
for cpc_code in ema_results:
    best_year = max(ema_results[cpc_code].keys(), 
                   key=lambda y: ema_results[cpc_code][y])
    best_years[cpc_code] = {
        'year': best_year,
        'ema_value': ema_results[cpc_code][best_year],
        'raw_count': patent_counts[cpc_code][best_year]
    }

# Sort by EMA value to find highest
sorted_cpc = sorted(best_years.items(), 
                   key=lambda x: x[1]['ema_value'], 
                   reverse=True)

output = {
    'total_cpc_codes': len(sorted_cpc),
    'top_10_cpc': sorted_cpc[:10],
    'sample_data': dict(list(patent_counts.items())[:3])
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total': '277813'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B04B",\n  "B04C"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B04', 'synonyms': '[]', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'titlePart': '[\n  "CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B23B",\n  "B23C",\n  "B23D",\n  "B23F",\n  "B23G",\n  "B23H",\n  "B23K",\n  "B23P",\n  "B23Q"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B23', 'synonyms': '[]', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'titlePart': '[\n  "MACHINE TOOLS",\n  "METAL-WORKING NOT OTHERWISE PROVIDED FOR"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B30B"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B30', 'synonyms': '[]', 'titleFull': 'PRESSES', 'titlePart': '[\n  "PRESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B21B",\n  "B21C",\n  "B21D",\n  "B21F",\n  "B21G",\n  "B21H",\n  "B21J",\n  "B21K",\n  "B21L"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B21', 'synonyms': '[]', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'titlePart': '[\n  "MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL",\n  "PUNCHING METAL"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B25B",\n  "B25C",\n  "B25D",\n  "B25F",\n  "B25G",\n  "B25H",\n  "B25J"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B25', 'synonyms': '[]', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'titlePart': '[\n  "HAND TOOLS",\n  "PORTABLE POWER-DRIVEN TOOLS",\n  "MANIPULATORS"\n]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'total_records': 0, 'first_record': None}, 'var_functions.execute_python:32': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.execute_python:30', '__builtins__', 'json'], 'keys_with_query': ['var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22'], 'total_records': 0}, 'var_functions.execute_python:36': {'total_german_patents': 39, 'sample_patent': 'f'}, 'var_functions.execute_python:40': {'variable_type': "<class 'str'>", 'is_string': True, 'is_list': False, 'length': 39, 'preview': 'file_storage/functions.query_db:22.json'}, 'var_functions.execute_python:42': {'total_german_patents': 18, 'sample_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'first_3_grant_dates': ['dated 21st November 2019', '5th of December, 2019', '22nd of August, 2019']}, 'var_functions.execute_python:48': {'total_patents': 18, 'cpc_count': 40, 'years': [2019], 'sample': {'B41F': {'2019': 3}, 'F02D': {'2019': 8}}}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
