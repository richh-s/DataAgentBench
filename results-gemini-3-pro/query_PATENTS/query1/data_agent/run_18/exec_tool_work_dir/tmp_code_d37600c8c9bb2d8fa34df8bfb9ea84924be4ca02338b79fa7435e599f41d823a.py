code = """import json
import re
from collections import Counter

# Load Level 5 symbols
with open(locals()['var_function-call-5087905462925890411'], 'r') as f:
    l5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in l5_data)

# Load Publications
with open(locals()['var_function-call-10591805906603829324'], 'r') as f:
    pubs_data = json.load(f)

stats = {}
stats['total_l5'] = len(level5_symbols)
stats['total_pubs'] = len(pubs_data)

year_pattern = re.compile(r'\b((?:19|20)\d{2})\b')
years_found = []
valid_cpcs_count = 0
dates_parsed = 0
sample_cpc_codes = []

for i, pub in enumerate(pubs_data):
    f_date = pub.get('filing_date')
    cpc_str = pub.get('cpc')
    
    if not f_date or not cpc_str:
        continue
    
    # Check date
    y_matches = year_pattern.findall(f_date)
    if y_matches:
        year = int(y_matches[-1])
        years_found.append(year)
        dates_parsed += 1
    else:
        continue
        
    # Check CPC
    try:
        cpc_list = json.loads(cpc_str)
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                subclass = code[:4]
                if len(sample_cpc_codes) < 10:
                    sample_cpc_codes.append(subclass)
                if subclass in level5_symbols:
                    valid_cpcs_count += 1
    except:
        pass

stats['dates_parsed'] = dates_parsed
stats['valid_cpcs_occurrences'] = valid_cpcs_count
if years_found:
    stats['min_year'] = min(years_found)
    stats['max_year'] = max(years_found)
    stats['year_dist'] = Counter(years_found).most_common(5)

stats['sample_cpc_found'] = sample_cpc_codes
stats['sample_l5'] = list(level5_symbols)[:10]

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-7068108288998237179': [{'filing_date': 'dated 5th March 2019', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-7068108288998238214': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-11289752396498631167': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}], 'var_function-call-3767859603655167710': [{'level': '7.0', 'symbol': 'C13B50/00'}, {'level': '8.0', 'symbol': 'H04Q2213/296'}, {'level': '7.0', 'symbol': 'C13B40/00'}, {'level': '7.0', 'symbol': 'C13B99/00'}, {'level': '7.0', 'symbol': 'C13B45/00'}, {'level': '7.0', 'symbol': 'C21B3/00'}, {'level': '7.0', 'symbol': 'A01B59/00'}, {'level': '8.0', 'symbol': 'H10N89/02'}, {'level': '7.0', 'symbol': 'A01B19/00'}, {'level': '8.0', 'symbol': 'B21D7/04'}], 'var_function-call-5087905462925890411': 'file_storage/function-call-5087905462925890411.json', 'var_function-call-16861969253203945337': [{'COUNT(*)': '277813'}], 'var_function-call-10591805906603829324': 'file_storage/function-call-10591805906603829324.json', 'var_function-call-10128769687173690775': []}

exec(code, env_args)
