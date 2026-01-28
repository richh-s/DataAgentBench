code = """import json
from collections import defaultdict

# Load the German patents data from our previous query
all_patents_path = locals()['var_functions.query_db:50']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print(f"Total German patents in database: {len(all_patents)}")

# Check data structure - what date fields are actually populated?
sample_patent = all_patents[0] if all_patents else {}
print(f"Sample patent keys: {list(sample_patent.keys())}")
print(f"Sample data:")
for key in ['Patents_info', 'grant_date', 'publication_date', 'filing_date', 'priority_date']:
    if key in sample_patent:
        print(f"  {key}: {sample_patent[key]}")

# Count patents by grant year to see data distribution
grant_years = defaultdict(int)
for patent in all_patents:
    grant_date = patent.get('grant_date', '')
    if grant_date:
        # Extract year from grant_date
        import re
        year_match = re.search(r'(\d{4})', grant_date)
        if year_match:
            year = int(year_match.group(1))
            grant_years[year] += 1

print(f"\nPatents by grant year (top 10):")
sorted_years = sorted(grant_years.items(), key=lambda x: x[1], reverse=True)
for year, count in sorted_years[:10]:
    print(f"  {year}: {count}")

result = {
    'total_patents': len(all_patents),
    'years_with_data': len(grant_years),
    'year_range': f"{min(grant_years.keys())} - {max(grant_years.keys())}" if grant_years else None,
    'top_years': sorted_years[:5]
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [], 'var_functions.execute_python:48': {'processed_patents': 18, 'unique_cpc_groups': 27, 'top_groups': [['C04', 45, 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'], ['H04', 36, 'ELECTRIC COMMUNICATION TECHNIQUE'], ['F02', 26, 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'], ['B29', 20, 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'], ['G02', 12, 'OPTICS'], ['F23', 11, 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'], ['H01', 10, 'ELECTRIC ELEMENTS'], ['A61', 9, 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'], ['Y02', 6, 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'], ['E02', 6, 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': {'total_filtered_patents': 6, 'valid_patents': 0, 'unique_cpc_groups': 0, 'filing_years_range': [], 'top_cpc': []}}

exec(code, env_args)
