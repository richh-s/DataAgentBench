code = """import json
import os
from collections import defaultdict

# Access the file paths correctly
patents_path = locals()['var_functions.query_db:36']
cpc_path = locals()['var_functions.query_db:28']

# Load patents data
with open(patents_path, 'r') as f:
    patents = json.load(f)

# Load CPC level 4 definitions  
with open(cpc_path, 'r') as f:
    cpc_level4 = json.load(f)

# Create mapping: symbol -> title for level 4
cpc_titles = {}
for item in cpc_level4:
    cpc_titles[item['symbol']] = item['titleFull']

# Extract level 4 groups from CPC codes
def extract_level4_code(full_code):
    """Extract level 4 code from full CPC code."""
    if not full_code or '/' not in full_code:
        return None
    
    main_part = full_code.split('/')[0]
    
    # Try different lengths to find a match in cpc_titles
    for length in range(len(main_part), 1, -1):
        test_code = main_part[:length]
        if test_code in cpc_titles:
            return test_code
    
    return None

# Count CPC codes by level 4 group
cpc_counts = defaultdict(int)
processed_patents = 0

for patent in patents:
    processed_patents += 1
    
    # Parse CPC field (it's a JSON string)
    cpc_field = patent.get('cpc', '[]')
    if cpc_field and cpc_field != '[]':
        try:
            cpc_list = json.loads(cpc_field)
            
            for cpc_item in cpc_list:
                full_code = cpc_item.get('code', '')
                level4_code = extract_level4_code(full_code)
                
                if level4_code:
                    cpc_counts[level4_code] += 1
        except:
            continue

# Get top CPC groups
top_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]

result = {
    'processed_patents': processed_patents,
    'unique_cpc_groups': len(cpc_counts),
    'top_groups': [(code, count, cpc_titles.get(code, 'Unknown')) for code, count in top_cpc]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': []}

exec(code, env_args)
