code = """import json
import re
from collections import defaultdict

# Load German patents from query result
result_file = var_functions.query_db:16
with open(result_file, 'r') as f:
    all_patents = json.load(f)

print("Loaded {} German patents".format(len(all_patents)))

# Group patents by grant year and count CPC groups
patents_by_year = defaultdict(list)
cpc_counts_by_year = defaultdict(lambda: defaultdict(int))

year_pattern = re.compile(r'(\d{4})')

for patent in all_patents:
    grant_date = patent.get('grant_date', '')
    year_match = year_pattern.search(grant_date)
    if year_match:
        year = int(year_match.group(1))
        patents_by_year[year].append(patent)
        
        # Count CPC groups for this patent
        try:
            cpc_list = json.loads(patent['cpc'])
            for entry in cpc_list:
                code = entry.get('code', '')
                if '/' in code:
                    group = code.split('/')[0]
                    # Validate level 4 format (e.g., H04W52)
                    if re.match(r'^[A-Z]\d{2}[A-Z]\d{2}$', group):
                        cpc_counts_by_year[year][group] += 1
        except:
            continue

# Show year range
years = sorted(cpc_counts_by_year.keys())
print("Year range: {} to {}".format(min(years), max(years)))

# Calculate EMA for each CPC group
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
alpha = 0.1

# Initialize EMA tracking
group_ema_history = defaultdict(dict)  # group -> year -> EMA value
group_best_year = {}  # group -> (best_year, max_ema)

for group in set(group for year_data in cpc_counts_by_year.values() for group in year_data.keys()):
    prev_ema = 0
    max_ema = 0
    best_year = None
    
    for year in sorted(years):
        current_count = cpc_counts_by_year[year].get(group, 0)
        
        # Calculate EMA
        ema = alpha * current_count + (1 - alpha) * prev_ema
        group_ema_history[group][year] = ema
        
        # Track best year
        if ema > max_ema:
            max_ema = ema
            best_year = year
            
        prev_ema = ema
    
    group_best_year[group] = {
        'best_year': best_year,
        'max_ema': max_ema,
        'recent_ema': prev_ema  # Most recent EMA (last year)
    }

# Filter groups that have patents in H2 2019 (from previous analysis)
h2_2019_top_groups = ['H04W52', 'C04B35', 'H01J49', 'F02D41', 'H04W72', 'F02M59', 'B29C49', 'G02B15', 'G02B23', 'Y02T10']

# Get top groups by max EMA
sorted_groups = sorted(group_best_year.items(), key=lambda x: x[1]['max_ema'], reverse=True)
top_10_groups = [(group, data) for group, data in sorted_groups[:10] if group in h2_2019_top_groups]

# If we don't have 10 groups from H2 2019, get top by EMA from all groups
top_10_groups = [(group, data) for group, data in sorted_groups[:10]]

print("Top 10 groups by max EMA:")
for i, (group, data) in enumerate(top_10_groups, 1):
    print("{}. {}: Best year {}, Max EMA {:.2f}, Recent EMA {:.2f}".format(
        i, group, data['best_year'], data['max_ema'], data['recent_ema']))

# Prepare result for next step (getting titles)
result = {
    'selected_groups': [
        {
            'cpc_group_code': group,
            'best_year': data['best_year'],
            'max_ema': data['max_ema'],
            'recent_ema': data['recent_ema']
        }
        for group, data in top_10_groups
    ]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_groups': 10, 'top_groups': [['F02M59', 8], ['F02D41', 5], ['B41F21', 2], ['F02M55', 2], ['F04B53', 2], ['B41F22', 1], ['F02M65', 1], ['G01D11', 1], ['B23K1', 1], ['B63B21', 1]], 'cpc_details': {'B41F21': {'code': 'B41F21', 'title': None}, 'B41F22': {'code': 'B41F22', 'title': None}, 'F02D41': {'code': 'F02D41', 'title': None}, 'F02M65': {'code': 'F02M65', 'title': None}, 'F02M59': {'code': 'F02M59', 'title': None}, 'F02M55': {'code': 'F02M55', 'title': None}, 'F04B53': {'code': 'F04B53', 'title': None}, 'G01D11': {'code': 'G01D11', 'title': None}, 'B23K1': {'code': 'B23K1', 'title': None}, 'B63B21': {'code': 'B63B21', 'title': None}}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': {'h2_2019_patents': 34, 'total_groups': 68, 'top_groups': [['H04W52', 12], ['C04B35', 12], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['Y02T10', 4]]}, 'var_functions.query_db:26': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
