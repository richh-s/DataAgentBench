code = """import json
import re
from collections import defaultdict

# Load patent data
patents_file = locals()['var_functions.query_db:20']
with open(patents_file, 'r') as f:
    patents_2019 = json.load(f)

# Load CPC definitions
cpc_file = locals()['var_functions.query_db:28']
with open(cpc_file, 'r') as f:
    cpc_level4 = json.load(f)

# Create mapping for level 4 CPC codes
cpc_titles = {cpc['symbol']: cpc['titleFull'] for cpc in cpc_level4}

# Process patents: extract CPC codes and filter for Germany + second half 2019
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
month_patterns = {month.lower(): month for month in second_half_months}

cpc_counts_by_year = defaultdict(int)
yearly_cpc_data = defaultdict(lambda: defaultdict(int))

second_half_patents = []

for patent in patents_2019:
    # Check for Germany in Patents_info
    patents_info = patent.get('Patents_info', '')
    if 'DE-' not in patents_info:
        continue
    
    # Check grant date for second half 2019
    grant_date = patent.get('grant_date', '')
    is_second_half = False
    date_lower = grant_date.lower()
    
    for month_lower, month in month_patterns.items():
        if month_lower in date_lower:
            is_second_half = True
            break
    
    if not is_second_half:
        continue
    
    second_half_patents.append(patent)
    
    # Parse CPC codes (they're JSON strings, not actual JSON)
    cpc_field = patent.get('cpc', '[]')
    if cpc_field and cpc_field != '[]':
        try:
            # Clean and parse the JSON-like string
            cpc_clean = cpc_field.replace('\n', '').strip()
            cpc_data = json.loads(cpc_clean)
            
            # Extract level 4 codes (first 3-4 characters before any /)
            # E.g., "A61P31/22" -> level 4 is "A61P"
            for cpc_item in cpc_data:
                full_code = cpc_item.get('code', '')
                if full_code and '/' in full_code:
                    parts = full_code.split('/')
                    class_part = parts[0]
                    
                    # For level 4, we take the main class + subclass letter + number
                    # E.g., A61P -> A61 is main class, P is subclass
                    # For level 4 grouping, we want codes like A61P, G06F, etc.
                    if len(class_part) >= 3:
                        # Look up the level 4 symbol that matches
                        level4_code = None
                        for i in range(len(class_part), 0, -1):
                            test_code = class_part[:i]
                            if test_code in cpc_titles:
                                level4_code = test_code
                                break
                        
                        if level4_code:
                            cpc_counts_by_year[level4_code] += 1
                            yearly_cpc_data[2019][level4_code] += 1
        except Exception as e:
            print(f"Error parsing CPC for patent {patents_info[:50]}: {e}")

print(f"Total Germany patents in second half 2019: {len(second_half_patents)}")
print(f"Unique CPC level 4 codes: {len(cpc_counts_by_year)}")
print(f"Top 5 CPC codes: {sorted(cpc_counts_by_year.items(), key=lambda x: x[1], reverse=True)[:5]}")

result = {
    'total_second_half_patents': len(second_half_patents),
    'unique_level4_cpcs': len(cpc_counts_by_year),
    'top_five': sorted(cpc_counts_by_year.items(), key=lambda x: x[1], reverse=True)[:5]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
