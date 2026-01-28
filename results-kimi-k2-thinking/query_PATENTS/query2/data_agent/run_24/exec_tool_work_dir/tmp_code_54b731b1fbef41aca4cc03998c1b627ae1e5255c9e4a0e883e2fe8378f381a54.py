code = """import json
import re

# Load German patents data
result_file = var_functions.query_db:40
with open(result_file, 'r') as f:
    all_patents = json.load(f)

print("Loaded {} German patents".format(len(all_patents)))

# Filter for H2 2019 patents
h2_2019_patents = []
for patent in all_patents:
    grant_date = patent.get('grant_date', '').lower()
    # Check for 2019 and second half months
    if '2019' in grant_date and any(month in grant_date for month in ['jul','aug','sep','oct','nov','dec']):
        h2_2019_patents.append(patent)

print("Found {} patents granted in H2 2019".format(len(h2_2019_patents)))

# Extract CPC level 4 groups
cpc_groups_count = {}
for patent in h2_2019_patents:
    try:
        cpc_list = json.loads(patent['cpc'])
        for entry in cpc_list:
            code = entry.get('code', '')
            # Extract level 4 group (before /)
            if '/' in code:
                group = code.split('/')[0]
                # Validate format (4 characters then digits)
                if re.match(r'^[A-Z]\d{2}[A-Z]\d{2}$', group):
                    cpc_groups_count[group] = cpc_groups_count.get(group, 0) + 1
    except:
        continue

print("Unique level 4 CPC groups in H2 2019: {}".format(len(cpc_groups_count)))
top_groups = sorted(cpc_groups_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 groups:", top_groups)

# For EMA calculation, we need historical patent counts by year for these groups
# Let's collect patent counts by year for all German patents
yearly_counts = {}
year_pattern = re.compile(r'(\d{4})')

def extract_group(code):
    if '/' in code:
        group = code.split('/')[0]
        if re.match(r'^[A-Z]\d{2}[A-Z]\d{2}$', group):
            return group
    return None

# Collect all relevant CPC groups (at least those in H2 2019)
all_groups = set(cpc_groups_count.keys())

# Build yearly patent counts for each group
for patent in all_patents:
    grant_date = patent.get('grant_date', '')
    year_match = year_pattern.search(grant_date)
    if year_match:
        year = int(year_match.group(1))
        if year not in yearly_counts:
            yearly_counts[year] = {}
        
        try:
            cpc_list = json.loads(patent['cpc'])
            for entry in cpc_list:
                code = entry.get('code', '')
                group = extract_group(code)
                if group and group in all_groups:
                    yearly_counts[year][group] = yearly_counts[year].get(group, 0) + 1
        except:
            continue

# Calculate EMA for each group
alpha = 0.1
results = []

for group in all_groups:
    years = sorted(yearly_counts.keys())
    ema_prev = 0
    max_ema = 0
    best_year = None
    
    for year in years:
        count = yearly_counts[year].get(group, 0)
        ema = alpha * count + (1 - alpha) * ema_prev
        
        if ema > max_ema:
            max_ema = ema
            best_year = year
            
        ema_prev = ema
    
    # Only include groups present in H2 2019
    if cpc_groups_count.get(group, 0) > 0:
        results.append({
            'cpc_group_code': group,
            'max_ema': max_ema,
            'best_year': best_year,
            'h2_2019_count': cpc_groups_count[group]
        })

# Sort by max EMA
top_results = sorted(results, key=lambda x: x['max_ema'], reverse=True)[:10]
print("Top groups by EMA: {}".format(top_results))

print("__RESULT__:")
print(json.dumps({
    'h2_2019_patents': len(h2_2019_patents),
    'unique_cpc_groups': len(cpc_groups_count),
    'top_ema_groups': top_results
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_groups': 10, 'top_groups': [['F02M59', 8], ['F02D41', 5], ['B41F21', 2], ['F02M55', 2], ['F04B53', 2], ['B41F22', 1], ['F02M65', 1], ['G01D11', 1], ['B23K1', 1], ['B63B21', 1]], 'cpc_details': {'B41F21': {'code': 'B41F21', 'title': None}, 'B41F22': {'code': 'B41F22', 'title': None}, 'F02D41': {'code': 'F02D41', 'title': None}, 'F02M65': {'code': 'F02M65', 'title': None}, 'F02M59': {'code': 'F02M59', 'title': None}, 'F02M55': {'code': 'F02M55', 'title': None}, 'F04B53': {'code': 'F04B53', 'title': None}, 'G01D11': {'code': 'G01D11', 'title': None}, 'B23K1': {'code': 'B23K1', 'title': None}, 'B63B21': {'code': 'B63B21', 'title': None}}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': {'h2_2019_patents': 34, 'total_groups': 68, 'top_groups': [['H04W52', 12], ['C04B35', 12], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['Y02T10', 4]]}, 'var_functions.query_db:26': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
