code = """import json
import re
from collections import defaultdict
import math

# Load German patents data
file_path = locals()['var_functions.query_db:22']
with open(file_path, 'r') as f:
    german_patents = json.load(f)

# Helper function to extract CPC codes and parse grant dates
def extract_cpc_codes(cpc_json):
    """Extract CPC codes from JSON string"""
    try:
        # Clean up the string and parse as JSON
        cpc_list = json.loads(cpc_json)
        return [item['code'] for item in cpc_list]
    except:
        return []

def extract_year_from_date(date_str):
    """Extract year from grant date string"""
    try:
        # Look for 4-digit year in the string
        match = re.search(r'(\d{4})', date_str)
        if match:
            return int(match.group(1))
    except:
        pass
    return None

def get_cpc_level_4(code):
    """Extract CPC code at level 4 (XXNN format)"""
    # CPC codes can be like: B41F21/102, G06F9/45533, etc.
    # Level 4 is the main class portion: B41F, G06F, etc.
    match = re.match(r'^([A-Z]\d{2}[A-Z])', code)
    if match:
        return match.group(1)
    return None

# Process the data
patent_counts = defaultdict(lambda: defaultdict(int))  # cpc_level4 -> year -> count
all_years = set()
all_cpc_codes = set()

for patent in german_patents:
    grant_date = patent['grant_date']
    year = extract_year_from_date(grant_date)
    if not year:
        continue
    
    cpc_codes = extract_cpc_codes(patent['cpc'])
    for cpc_code in cpc_codes:
        level4_code = get_cpc_level_4(cpc_code)
        if level4_code:
            patent_counts[level4_code][year] += 1
            all_years.add(year)
            all_cpc_codes.add(level4_code)

# Sort years for EMA calculation
sorted_years = sorted(list(all_years))

print('__RESULT__:')
print(json.dumps({
    'total_patents_processed': len(german_patents),
    'cpc_level4_codes_found': len(all_cpc_codes),
    'years_found': sorted_years,
    'sample_counts': dict(list(patent_counts.items())[:3])
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total': '277813'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B04B",\n  "B04C"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B04', 'synonyms': '[]', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'titlePart': '[\n  "CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B23B",\n  "B23C",\n  "B23D",\n  "B23F",\n  "B23G",\n  "B23H",\n  "B23K",\n  "B23P",\n  "B23Q"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B23', 'synonyms': '[]', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'titlePart': '[\n  "MACHINE TOOLS",\n  "METAL-WORKING NOT OTHERWISE PROVIDED FOR"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B30B"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B30', 'synonyms': '[]', 'titleFull': 'PRESSES', 'titlePart': '[\n  "PRESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B21B",\n  "B21C",\n  "B21D",\n  "B21F",\n  "B21G",\n  "B21H",\n  "B21J",\n  "B21K",\n  "B21L"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B21', 'synonyms': '[]', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'titlePart': '[\n  "MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL",\n  "PUNCHING METAL"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B25B",\n  "B25C",\n  "B25D",\n  "B25F",\n  "B25G",\n  "B25H",\n  "B25J"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B25', 'synonyms': '[]', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'titlePart': '[\n  "HAND TOOLS",\n  "PORTABLE POWER-DRIVEN TOOLS",\n  "MANIPULATORS"\n]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'total_records': 0, 'first_record': None}, 'var_functions.execute_python:32': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.execute_python:30', '__builtins__', 'json'], 'keys_with_query': ['var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', 'var_functions.query_db:12', 'var_functions.query_db:14', 'var_functions.query_db:16', 'var_functions.query_db:18', 'var_functions.query_db:20', 'var_functions.query_db:22'], 'total_records': 0}, 'var_functions.execute_python:36': {'total_german_patents': 39, 'sample_patent': 'f'}, 'var_functions.execute_python:40': {'variable_type': "<class 'str'>", 'is_string': True, 'is_list': False, 'length': 39, 'preview': 'file_storage/functions.query_db:22.json'}, 'var_functions.execute_python:42': {'total_german_patents': 18, 'sample_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'first_3_grant_dates': ['dated 21st November 2019', '5th of December, 2019', '22nd of August, 2019']}}

exec(code, env_args)
