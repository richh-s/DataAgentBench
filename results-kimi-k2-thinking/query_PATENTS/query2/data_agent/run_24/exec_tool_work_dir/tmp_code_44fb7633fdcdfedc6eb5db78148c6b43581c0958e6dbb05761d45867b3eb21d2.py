code = """import json
import re
from collections import defaultdict

# Load the CPC definitions for our top groups
result_file = var_functions.query_db:30
with open(result_file, 'r') as f:
    cpc_definitions = json.load(f)

# Load the H2 2019 analysis
h2_2019_key = 'var_functions.execute_python:24'
h2_2019_data = globals()[h2_2019_key]

top_groups = h2_2019_data['top_groups']
print("Top CPC groups in H2 2019: {}".format(top_groups))

# Extract the level 4 group titles from CPC definitions
group_titles = {}
for group, count in top_groups:
    # Look for the group symbol in CPC definitions
    for def_entry in cpc_definitions:
        symbol = def_entry['symbol']
        # Check if this is the main group (not a subgroup)
        if symbol == group or symbol.startswith(group + '/'):
            # The title for the main group is usually the base symbol
            if '/' not in symbol or symbol == group:
                group_titles[group] = def_entry['titleFull']
                break

# For groups we didn't find, try alternative queries
missing_groups = [g for g, _ in top_groups if g not in group_titles]
print("Missing groups: {}".format(missing_groups))

# Prepare final results with the data we have
final_results = []
for group, count in top_groups:
    title = group_titles.get(group, "Title not found in database")
    final_results.append({
        'cpc_group_code': group,
        'title_full': title,
        'patent_count_h2_2019': count,
        'best_year': 2019
    })

print("\nFinal results:")
print(json.dumps(final_results, indent=2))

result_summary = {
    'total_cpc_groups_analyzed': len(top_groups),
    'results': final_results
}

print("__RESULT__:")
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_groups': 10, 'top_groups': [['F02M59', 8], ['F02D41', 5], ['B41F21', 2], ['F02M55', 2], ['F04B53', 2], ['B41F22', 1], ['F02M65', 1], ['G01D11', 1], ['B23K1', 1], ['B63B21', 1]], 'cpc_details': {'B41F21': {'code': 'B41F21', 'title': None}, 'B41F22': {'code': 'B41F22', 'title': None}, 'F02D41': {'code': 'F02D41', 'title': None}, 'F02M65': {'code': 'F02M65', 'title': None}, 'F02M59': {'code': 'F02M59', 'title': None}, 'F02M55': {'code': 'F02M55', 'title': None}, 'F04B53': {'code': 'F04B53', 'title': None}, 'G01D11': {'code': 'G01D11', 'title': None}, 'B23K1': {'code': 'B23K1', 'title': None}, 'B63B21': {'code': 'B63B21', 'title': None}}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': {'h2_2019_patents': 34, 'total_groups': 68, 'top_groups': [['H04W52', 12], ['C04B35', 12], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['Y02T10', 4]]}, 'var_functions.query_db:26': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
