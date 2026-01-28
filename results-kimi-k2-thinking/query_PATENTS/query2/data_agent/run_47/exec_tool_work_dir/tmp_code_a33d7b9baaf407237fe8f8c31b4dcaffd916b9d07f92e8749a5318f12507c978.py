code = """import json, re
from collections import defaultdict

# Load German patents data
patents_path = locals()['var_functions.query_db:50']
with open(patents_path, 'r') as f:
    all_patents = json.load(f)

# Load CPC level 4 definitions
cpc_path = locals()['var_functions.query_db:28']
with open(cpc_path, 'r') as f:
    cpc_level4 = json.load(f)

cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_level4}

# Filter patents granted in second half of 2019
second_half_patterns = ['july 2019', 'august 2019', 'september 2019', 'october 2019', 'november 2019', 'december 2019']
h2_2019_patents = []

for patent in all_patents:
    grant_date = patent.get('grant_date', '').lower()
    if any(month in grant_date for month in second_half_patterns):
        h2_2019_patents.append(patent)

print(f"Total German patents: {len(all_patents)}")
print(f"Patents granted in H2 2019: {len(h2_2019_patents)}")

# Group by CPC level 4 and track filing years
cpc_filing_years = defaultdict(lambda: defaultdict(int))
filing_years = set()

for patent in h2_2019_patents:
    # Get filing year
    filing_date = patent.get('filing_date', '')
    if not filing_date:
        continue
    
    year_match = re.search(r'(\d{4})', filing_date)
    if not year_match:
        continue
    
    filing_year = int(year_match.group(1))
    filing_years.add(filing_year)
    
    # Parse CPC codes and extract level 4
    cpc_field = patent.get('cpc', '[]')
    if not cpc_field or cpc_field == '[]':
        continue
    
    try:
        cpc_list = json.loads(cpc_field)
        for cpc_item in cpc_list:
            full_code = cpc_item.get('code', '')
            if not full_code or '/' not in full_code:
                continue
            
            main_part = full_code.split('/')[0]
            # Find matching level 4 code
            for length in range(len(main_part), 1, -1):
                test_code = main_part[:length]
                if test_code in cpc_titles:
                    cpc_filing_years[test_code][filing_year] += 1
                    break
    except:
        continue

print(f"\nCPC Level 4 groups found: {len(cpc_filing_years)}")
print(f"Filing years: {sorted(list(filing_years))}")

# Calculate totals and find best year for each CPC
cpc_summary = []
for cpc_code, year_counts in cpc_filing_years.items():
    total = sum(year_counts.values())
    best_year = max(year_counts, key=year_counts.get) if year_counts else None
    best_year_count = year_counts.get(best_year, 0) if best_year else 0
    
    cpc_summary.append({
        'code': cpc_code,
        'title': cpc_titles.get(cpc_code, 'Unknown'),
        'total_patents': total,
        'best_year': best_year,
        'best_year_count': best_year_count,
        'yearly_breakdown': dict(year_counts)
    })

# Sort by total patents
sorted_cpc = sorted(cpc_summary, key=lambda x: x['total_patents'], reverse=True)

print(f"\nTop CPC Level 4 groups:")
for i, cpc in enumerate(sorted_cpc[:10], 1):
    print(f"{i}. {cpc['code']}: {cpc['total_patents']} patents")
    print(f"   {cpc['title'][:80]}")
    print(f"   Best year: {cpc['best_year']} ({cpc['best_year_count']} patents)")

result = {
    'total_h2_2019_patents': len(h2_2019_patents),
    'cpc_groups_analyzed': len(cpc_filing_years),
    'sorted_cpc_groups': sorted_cpc
}

print('\n__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [], 'var_functions.execute_python:48': {'processed_patents': 18, 'unique_cpc_groups': 27, 'top_groups': [['C04', 45, 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'], ['H04', 36, 'ELECTRIC COMMUNICATION TECHNIQUE'], ['F02', 26, 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'], ['B29', 20, 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'], ['G02', 12, 'OPTICS'], ['F23', 11, 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'], ['H01', 10, 'ELECTRIC ELEMENTS'], ['A61', 9, 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'], ['Y02', 6, 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'], ['E02', 6, 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': {'total_filtered_patents': 6, 'valid_patents': 0, 'unique_cpc_groups': 0, 'filing_years_range': [], 'top_cpc': []}, 'var_functions.execute_python:62': {'total': 11644, 'filtered': 6, 'filing_years': {}, 'grant_years': {'2019': 6}}, 'var_functions.query_db:64': [{'total_patents': '11644'}]}

exec(code, env_args)
