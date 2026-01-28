code = """import json, re
from collections import defaultdict

all_patents_path = locals()['var_functions.query_db:50']
cpc_path = locals()['var_functions.query_db:28']

with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

with open(cpc_path, 'r') as f:
    cpc_level4 = json.load(f)

cpc_titles = {}
for item in cpc_level4:
    cpc_titles[item['symbol']] = item['titleFull']

second_half_patterns = ['july 2019', 'august 2019', 'september 2019', 'october 2019', 'november 2019', 'december 2019']
filtered_patents = []
for patent in all_patents:
    grant_date = patent.get('grant_date', '').lower()
    if any(month in grant_date for month in second_half_patterns):
        filtered_patents.append(patent)

filing_year_pattern = re.compile(r'(\d{4})')
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
valid_patents = 0
no_filing_date = 0

for patent in filtered_patents:
    filing_date = patent.get('filing_date', '')
    if not filing_date:
        no_filing_date += 1
        continue
    
    year_match = filing_year_pattern.search(filing_date)
    if year_match:
        filing_year = int(year_match.group(1))
        valid_patents += 1
        
        cpc_field = patent.get('cpc', '[]')
        if cpc_field and cpc_field != '[]':
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_item in cpc_list:
                    full_code = cpc_item.get('code', '')
                    if full_code and '/' in full_code:
                        main_part = full_code.split('/')[0]
                        for length in range(len(main_part), 1, -1):
                            test_code = main_part[:length]
                            if test_code in cpc_titles:
                                cpc_yearly_counts[test_code][filing_year] += 1
                                break
            except:
                continue

all_years = set()
for cpc_code, year_data in cpc_yearly_counts.items():
    all_years.update(year_data.keys())
sorted_years = sorted(list(all_years))

all_cpc_counts = {}
for cpc_code, year_data in cpc_yearly_counts.items():
    total = sum(year_data.values())
    all_cpc_counts[cpc_code] = total

top_cpc = sorted(all_cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]

result = {
    'total_filtered_patents': len(filtered_patents),
    'valid_patents': valid_patents,
    'unique_cpc_groups': len(cpc_yearly_counts),
    'filing_years_range': [min(sorted_years), max(sorted_years)] if sorted_years else [],
    'top_cpc': [(code, total, cpc_titles.get(code, 'Unknown')) for code, total in top_cpc[:5]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [], 'var_functions.execute_python:48': {'processed_patents': 18, 'unique_cpc_groups': 27, 'top_groups': [['C04', 45, 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'], ['H04', 36, 'ELECTRIC COMMUNICATION TECHNIQUE'], ['F02', 26, 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'], ['B29', 20, 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'], ['G02', 12, 'OPTICS'], ['F23', 11, 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'], ['H01', 10, 'ELECTRIC ELEMENTS'], ['A61', 9, 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'], ['Y02', 6, 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'], ['E02', 6, 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
