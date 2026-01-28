code = """import json, re
from collections import defaultdict

# Load German patents granted in 2019 with filing dates
patents_path = locals()['var_functions.query_db:72']
with open(patents_path, 'r') as f:
    patents_2019 = json.load(f)

# Load CPC level 4 definitions
cpc_path = locals()['var_functions.query_db:28']
with open(cpc_path, 'r') as f:
    cpc_level4 = json.load(f)

cpc_titles = {item['symbol']: item['titleFull'] for item in cpc_level4}

# Filter for second half 2019 grants (July-December)
second_half_months = ['july 2019', 'august 2019', 'september 2019', 'october 2019', 'november 2019', 'december 2019']
h2_patents = []

for patent in patents_2019:
    grant_date = patent.get('grant_date', '').lower()
    if any(month in grant_date for month in second_half_months):
        h2_patents.append(patent)

print(f"Total patents granted in 2019: {len(patents_2019)}")
print(f"Patents granted in second half 2019: {len(h2_patents)}")

# Group by CPC level 4 and filing year
cpc_filing_years = defaultdict(lambda: defaultdict(int))

for patent in h2_patents:
    # Get filing year
    filing_date = patent.get('filing_date', '')
    year_match = re.search(r'(\d{4})', filing_date)
    if not year_match:
        continue
    
    filing_year = int(year_match.group(1))
    
    # Parse CPC codes
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

print(f"CPC Level 4 groups found: {len(cpc_filing_years)}")

# Calculate exponential moving average (EMA) for each CPC group
alpha = 0.1
cpc_ema_results = []

for cpc_code, year_counts in cpc_filing_years.items():
    if not year_counts:
        continue
    
    all_years = sorted(year_counts.keys())
    if len(all_years) < 2:
        continue  # Need at least 2 years for meaningful EMA trend
    
    # Calculate EMA values
    ema_values = {}
    previous_ema = None
    
    for year in all_years:
        value = year_counts[year]
        
        if previous_ema is None:
            current_ema = value
        else:
            current_ema = alpha * value + (1 - alpha) * previous_ema
        
        ema_values[year] = current_ema
        previous_ema = current_ema
    
    # Find year with highest EMA
    best_year = max(ema_values, key=ema_values.get)
    best_ema = ema_values[best_year]
    
    cpc_ema_results.append({
        'cpc_code': cpc_code,
        'title_full': cpc_titles.get(cpc_code, 'Unknown'),
        'best_year': best_year,
        'best_ema': round(best_ema, 2),
        'best_actual_count': year_counts[best_year],
        'total_patents': sum(year_counts.values()),
        'all_years': dict(year_counts),
        'ema_values': {k: round(v, 2) for k, v in ema_values.items()}
    })

# Sort by best EMA value
sorted_results = sorted(cpc_ema_results, key=lambda x: x['best_ema'], reverse=True)

print(f"\nTop CPC Level 4 Groups by Exponential Moving Average:")
print(f"{'Rank':<6} {'CPC':<6} {'Best Year':<11} {'EMA':<8} {'Count':<7} {'Title'}")
print("-" * 80)

for i, result in enumerate(sorted_results[:15], 1):
    print(f"{i:<6} {result['cpc_code']:<6} {result['best_year']:<11} {result['best_ema']:<8} {result['best_actual_count']:<7} {result['title_full'][:60]}")

final_result = {
    'total_patents_analyzed': len(h2_patents),
    'cpc_groups_evaluated': len(sorted_results),
    'top_cpc_groups': sorted_results[:15]
}

print('\n__RESULT__:')
print(json.dumps(final_result, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_2019_patents': 164, 'second_half_patents': 66, 'sample': {'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'grant_date': 'on October 31st, 2019', 'cpc': '[\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M2230/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3496",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61M1/3693",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [], 'var_functions.execute_python:48': {'processed_patents': 18, 'unique_cpc_groups': 27, 'top_groups': [['C04', 45, 'CEMENTS; CONCRETE; ARTIFICIAL STONE; CERAMICS; REFRACTORIES'], ['H04', 36, 'ELECTRIC COMMUNICATION TECHNIQUE'], ['F02', 26, 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'], ['B29', 20, 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'], ['G02', 12, 'OPTICS'], ['F23', 11, 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'], ['H01', 10, 'ELECTRIC ELEMENTS'], ['A61', 9, 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'], ['Y02', 6, 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'], ['E02', 6, 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:54': {'total_filtered_patents': 6, 'valid_patents': 0, 'unique_cpc_groups': 0, 'filing_years_range': [], 'top_cpc': []}, 'var_functions.execute_python:62': {'total': 11644, 'filtered': 6, 'filing_years': {}, 'grant_years': {'2019': 6}}, 'var_functions.query_db:64': [{'total_patents': '11644'}], 'var_functions.execute_python:68': {'total_h2_2019_patents': 6, 'cpc_groups_analyzed': 0, 'sorted_cpc_groups': []}, 'var_functions.query_db:70': [{'count': '68'}], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
