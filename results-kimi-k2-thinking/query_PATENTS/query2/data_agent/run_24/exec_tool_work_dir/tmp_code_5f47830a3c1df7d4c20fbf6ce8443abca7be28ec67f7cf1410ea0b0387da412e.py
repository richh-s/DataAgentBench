code = """import json, re
from collections import defaultdict

# Access the results using proper variable names
file_key = 'var_functions.query_db:40'
result_file_path = globals()[file_key]

with open(result_file_path, 'r') as f:
    all_patents = json.load(f)

print("Loaded {} patents".format(len(all_patents)))

# First, let's just identify all relevant CPC groups and their yearly counts
yearly_group_counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r'(\d{4})')

code_pattern = re.compile(r'^[A-Z]\d{2}[A-Z]\d{2}$')

for p in all_patents:
    date = p.get('grant_date', '')
    m = year_pattern.search(date)
    if m:
        year = int(m.group(1))
        try:
            cpc_list = json.loads(p['cpc'])
            for entry in cpc_list:
                code = entry.get('code', '')
                if '/' in code:
                    group = code.split('/')[0]
                    if code_pattern.match(group):
                        yearly_group_counts[year][group] += 1
        except:
            pass

# Filter for H2 2019
h2_2019_groups = defaultdict(int)
for p in all_patents:
    date = p.get('grant_date', '').lower()
    if '2019' in date and any(m in date for m in ['jul','aug','sep','oct','nov','dec']):
        try:
            cpc_list = json.loads(p['cpc'])
            for entry in cpc_list:
                code = entry.get('code', '')
                if '/' in code:
                    group = code.split('/')[0]
                    if code_pattern.match(group):
                        h2_2019_groups[group] += 1
        except:
            pass

print("H2 2019 groups count: {}".format(len(h2_2019_groups)))
print("Year range: {} to {}".format(min(yearly_group_counts.keys()), max(yearly_group_counts.keys())))

# Calculate EMA for groups in H2 2019
alpha = 0.1
results = []

candidates = list(h2_2019_groups.items())
for group, count_2019 in candidates:
    if count_2019 == 0:
        continue
    
    years = sorted(yearly_group_counts.keys())
    ema_prev = 0
    max_ema = 0
    best_year = None
    
    for year in years:
        count = yearly_group_counts[year].get(group, 0)
        ema = alpha * count + (1 - alpha) * ema_prev
        
        if ema > max_ema:
            max_ema = ema
            best_year = year
        
        ema_prev = ema
    
    results.append({
        'cpc_group_code': group,
        'best_year': best_year,
        'max_ema': max_ema,
        'h2_2019_count': count_2019
    })

top_results = sorted(results, key=lambda x: x['max_ema'], reverse=True)[:10]
print("Top by EMA: {}".format(top_results))

print("__RESULT__:")
print(json.dumps({
    'h2_2019_groups': len(h2_2019_groups),
    'top_ema_groups': top_results
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_groups': 10, 'top_groups': [['F02M59', 8], ['F02D41', 5], ['B41F21', 2], ['F02M55', 2], ['F04B53', 2], ['B41F22', 1], ['F02M65', 1], ['G01D11', 1], ['B23K1', 1], ['B63B21', 1]], 'cpc_details': {'B41F21': {'code': 'B41F21', 'title': None}, 'B41F22': {'code': 'B41F22', 'title': None}, 'F02D41': {'code': 'F02D41', 'title': None}, 'F02M65': {'code': 'F02M65', 'title': None}, 'F02M59': {'code': 'F02M59', 'title': None}, 'F02M55': {'code': 'F02M55', 'title': None}, 'F04B53': {'code': 'F04B53', 'title': None}, 'G01D11': {'code': 'G01D11', 'title': None}, 'B23K1': {'code': 'B23K1', 'title': None}, 'B63B21': {'code': 'B63B21', 'title': None}}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': {'h2_2019_patents': 34, 'total_groups': 68, 'top_groups': [['H04W52', 12], ['C04B35', 12], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['Y02T10', 4]]}, 'var_functions.query_db:26': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
