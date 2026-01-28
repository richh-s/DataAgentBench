code = """import json
import re
from datetime import datetime
import pandas as pd
import numpy as np

# Load the publication data
file_path = 'file_storage/functions.query_db:14.json'
with open(file_path, 'r') as f:
    publication_data = json.load(f)

# Load level 5 CPC symbols
file_path_cpc5 = 'file_storage/functions.query_db:20.json'
with open(file_path_cpc5, 'r') as f:
    cpc_level5_data = json.load(f)

cpc_level5_symbols = set(item['symbol'] for item in cpc_level5_data)

# Process publication data to extract years and CPC codes
cpc_yearly_counts = {}

# Date parsing regex to extract year
date_pattern = r'(\d{4})'

for record in publication_data:
    # Extract year from publication_date
    pub_date = record.get('publication_date', '')
    year_match = re.search(date_pattern, pub_date)
    if year_match:
        year = int(year_match.group(1))
        # Parse CPC codes
        cpc_str = record.get('cpc', '')
        if cpc_str:
            try:
                cpc_list = json.loads(cpc_str)
                for cpc_item in cpc_list:
                    cpc_code = cpc_item.get('code', '')
                    if cpc_code:
                        # Extract level 5 group code (main group, before the slash)
                        # For example, "C01B33/00" -> "C01B"
                        # But also handle codes like "A01B" which are already level 5
                        if '/' in cpc_code:
                            # Extract the main group part before slash
                            main_part = cpc_code.split('/')[0]
                            # Extract letters + first digits (e.g., "C01B" from "C01B33")
                            # This matches the pattern: letters followed by digits
                            match = re.match(r'^([A-Z]+\d+[A-Z]?)', main_part)
                            if match:
                                level5_code = match.group(1)
                            else:
                                continue
                        else:
                            # Already a top-level code, check if it's in our level 5 set
                            level5_code = cpc_code
                        
                        # Check if this is a valid level 5 code
                        if level5_code in cpc_level5_symbols:
                            # Initialize nested dict if needed
                            if level5_code not in cpc_yearly_counts:
                                cpc_yearly_counts[level5_code] = {}
                            # Count filings per year for each CPC code
                            cpc_yearly_counts[level5_code][year] = cpc_yearly_counts[level5_code].get(year, 0) + 1
            except:
                continue

# Get all years present in the data
all_years = set()
for code, yearly_data in cpc_yearly_counts.items():
    all_years.update(yearly_data.keys())

all_years = sorted(list(all_years))

print('__RESULT__:')
print(json.dumps({
    'total_level5_codes_with_data': len(cpc_yearly_counts),
    'all_years': all_years,
    'year_range': f"{min(all_years)} to {max(all_years)}" if all_years else "No data",
    'sample_level5_data': {k: dict(list(v.items())[:3]) for k, v in list(cpc_yearly_counts.items())[:10]}
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.execute_python:10': {'file_path': 'file_storage/functions.query_db:2.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:12': {'total_records': 10, 'keys_in_record': ['Patents_info', 'cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'sample_cpc_parsed': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}], 'sample_publication_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 277813, 'sample_record': {'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': 'Aug 3rd, 2021'}, 'cpi_codes_sample': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}], 'sample_publication_date': 'Aug 3rd, 2021'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_level5_symbols': 677, 'sample_level5_symbols': ['A21B', 'F16C', 'H03L', 'B68F', 'A61N', 'G01N', 'A61D', 'B23G', 'E04D', 'G01T']}, 'var_functions.execute_python:24': {'total_cpc_codes': 175852, 'sample_cpc_data': {'C01B33/00': {'2021': 4, '2007': 1, '2020': 1}, 'C01B35/00': {'2021': 3, '2019': 3, '2022': 1}, 'H01M10/0565': {'2021': 34, '2020': 15, '2006': 11}, 'H01M10/0562': {'2021': 57, '2024': 21, '2015': 9}, 'C01G45/006': {'2021': 3, '2020': 2, '2019': 2}}}}

exec(code, env_args)
