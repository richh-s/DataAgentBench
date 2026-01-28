code = """import json, re
from collections import defaultdict

patents_path = locals()['var_functions.query_db:50']
with open(patents_path) as f:
    all_patents = json.load(f)

second_half = ['july 2019', 'august 2019', 'september 2019', 'october 2019', 'november 2019', 'december 2019']
filtered = []
for p in all_patents:
    if any(month in p.get('grant_date','').lower() for month in second_half):
        filtered.append(p)

grant_years = defaultdict(int)
filing_years = defaultdict(int)
for patent in filtered:
    # Filing year
    filing_date = patent.get('filing_date', '')
    if filing_date:
        m = re.search(r'(\d{4})', filing_date)
        if m:
            filing_years[int(m.group(1))] += 1
    
    # Grant year
    grant_date = patent.get('grant_date', '')
    if grant_date:
        m = re.search(r'(\d{4})', grant_date)
        if m:
            grant_years[int(m.group(1))] += 1

print('Total German patents:', len(all_patents))
print('Second half 2019 patents:', len(filtered))
print('Filing years found:', len(filing_years))
print('Grant years found:', len(grant_years))
if filing_years:
    print('Filing year range:', min(filing_years.keys()), '-', max(filing_years.keys()))
if grant_years:
    print('Grant year range:', min(grant_years.keys()), '-', max(grant_years.keys()))

result = {
    'total': len(all_patents),
    'filtered': len(filtered),
    'filing_years': dict(filing_years),
    'grant_years': dict(grant_years)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [], 'var_functions.execute_python:48': {'processed_patents': 18, 'unique_cpc_groups': 27, 'top_groups': [['C04', 45, 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'], ['H04', 36, 'ELECTRIC COMMUNICATION TECHNIQUE'], ['F02', 26, 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'], ['B29', 20, 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'], ['G02', 12, 'OPTICS'], ['F23', 11, 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'], ['H01', 10, 'ELECTRIC ELEMENTS'], ['A61', 9, 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'], ['Y02', 6, 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'], ['E02', 6, 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': {'total_filtered_patents': 6, 'valid_patents': 0, 'unique_cpc_groups': 0, 'filing_years_range': [], 'top_cpc': []}}

exec(code, env_args)
