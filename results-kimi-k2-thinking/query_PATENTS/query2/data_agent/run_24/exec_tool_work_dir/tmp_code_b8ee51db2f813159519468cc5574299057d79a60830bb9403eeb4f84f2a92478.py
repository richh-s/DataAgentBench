code = """import json
import re

# Load the CPC definitions result
cpc_file = var_functions.query_db:48
with open(cpc_file, 'r') as f:
    cpc_defs = json.load(f)

# Load the EMA analysis results
ema_key = 'var_functions.execute_python:44'
top_groups_data = globals()[ema_key]

top_groups = top_groups_data['top_ema_groups']
print("Top 10 CPC groups by EMA:", [g['cpc_group_code'] for g in top_groups])

# Extract level 4 group titles from CPC definitions
# For each symbol like "C04B35/053", the level 4 group is "C04B35"

group_titles = {}
for group_info in top_groups:
    group_code = group_info['cpc_group_code']
    group_titles[group_code] = "Title not found"  # default
    
    # Look for the base group in CPC definitions
    for entry in cpc_defs:
        symbol = entry['symbol']
        # Check if this matches our group (e.g., "C04B35/..." matches "C04B35")
        if symbol.startswith(group_code + '/') or symbol == group_code:
            group_titles[group_code] = entry['titleFull']
            break

# Create final results
final_results = []
for group_info in top_groups:
    group_code = group_info['cpc_group_code']
    final_results.append({
        'cpc_group_code': group_code,
        'title_full': group_titles[group_code],
        'best_year': group_info['best_year'],
        'max_exponential_moving_average': round(group_info['max_ema'], 2),
        'patents_in_h2_2019': group_info['h2_2019_count']
    })

print("\nFinal Results:")
for r in final_results:
    print(f"{r['cpc_group_code']}: {r['title_full'][:60]}... - Best Year: {r['best_year']}, Max EMA: {r['max_exponential_moving_average']}")

print("\n" + "="*80)
print("CPC TECHNOLOGY AREAS IN GERMANY WITH HIGHEST EMA")
print("="*80)
for i, result in enumerate(final_results, 1):
    print(f"{i}. CPC Group: {result['cpc_group_code']}")
    print(f"   Full Title: {result['title_full']}")
    print(f"   Best Year: {result['best_year']}")
    print(f"   Max EMA (α=0.1): {result['max_exponential_moving_average']}")
    print(f"   Patents in H2 2019: {result['patents_in_h2_2019']}")
    print()

output = {
    'total_cpc_groups_analyzed': len(top_groups),
    'results': final_results
}

print("__RESULT__:")
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, {'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'cpc': '[\n  {\n    "code": "F02D41/3005",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M65/005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02D41/20",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '5th of December, 2019'}, {'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '22nd of August, 2019'}, {'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'September the 19th, 2019'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '17th of October, 2019'}], 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_groups': 10, 'top_groups': [['F02M59', 8], ['F02D41', 5], ['B41F21', 2], ['F02M55', 2], ['F04B53', 2], ['B41F22', 1], ['F02M65', 1], ['G01D11', 1], ['B23K1', 1], ['B63B21', 1]], 'cpc_details': {'B41F21': {'code': 'B41F21', 'title': None}, 'B41F22': {'code': 'B41F22', 'title': None}, 'F02D41': {'code': 'F02D41', 'title': None}, 'F02M65': {'code': 'F02M65', 'title': None}, 'F02M59': {'code': 'F02M59', 'title': None}, 'F02M55': {'code': 'F02M55', 'title': None}, 'F04B53': {'code': 'F04B53', 'title': None}, 'G01D11': {'code': 'G01D11', 'title': None}, 'B23K1': {'code': 'B23K1', 'title': None}, 'B63B21': {'code': 'B63B21', 'title': None}}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:24': {'h2_2019_patents': 34, 'total_groups': 68, 'top_groups': [['H04W52', 12], ['C04B35', 12], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['Y02T10', 4]]}, 'var_functions.query_db:26': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': {'h2_2019_groups': 68, 'top_ema_groups': [{'cpc_group_code': 'Y02T10', 'best_year': 2021, 'max_ema': 5.666824204272428, 'h2_2019_count': 4}, {'cpc_group_code': 'F02D41', 'best_year': 2019, 'max_ema': 3.855928136814618, 'h2_2019_count': 9}, {'cpc_group_code': 'H01L23', 'best_year': 2024, 'max_ema': 3.7195126984113056, 'h2_2019_count': 3}, {'cpc_group_code': 'C04B35', 'best_year': 2019, 'max_ema': 3.5256148415074953, 'h2_2019_count': 12}, {'cpc_group_code': 'H01R13', 'best_year': 2013, 'max_ema': 2.8868890139948955, 'h2_2019_count': 1}, {'cpc_group_code': 'B29C45', 'best_year': 2007, 'max_ema': 2.4935963447224703, 'h2_2019_count': 2}, {'cpc_group_code': 'B60W30', 'best_year': 2023, 'max_ema': 2.480651495851129, 'h2_2019_count': 1}, {'cpc_group_code': 'H01J49', 'best_year': 2023, 'max_ema': 1.7185400000000004, 'h2_2019_count': 10}, {'cpc_group_code': 'G01N27', 'best_year': 2008, 'max_ema': 1.5988955945421695, 'h2_2019_count': 1}, {'cpc_group_code': 'F16C33', 'best_year': 2014, 'max_ema': 1.4369763885014006, 'h2_2019_count': 3}]}, 'var_functions.query_db:46': [], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
