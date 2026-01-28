code = """import json
import os
import re
from collections import defaultdict

# Load patent data
patents_key = 'var_functions.query_db:42'
if patents_key not in globals():
    print("Patents data key not found")
    exit()

patents_file = globals()[patents_key]
with open(patents_file, 'r') as f:
    patents_data = json.load(f)

print('Loaded', len(patents_data), 'German patents from 2019 second half')

# Extract CPC level 4 codes and filing years
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for patent in patents_data:
    # Extract filing year
    filing_date = patent.get('filing_date', '')
    year_match = re.search(r'(\d{4})', filing_date)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    if year < 2000 or year > 2024:
        continue
    
    # Parse CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_codes = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
    except:
        continue
    
    if not isinstance(cpc_codes, list):
        continue
    
    # Count each CPC level 4 code
    for cpc_entry in cpc_codes:
        if not isinstance(cpc_entry, dict):
            continue
        
        cpc_code = cpc_entry.get('code', '')
        if not cpc_code or len(cpc_code) < 4:
            continue
        
        slash_pos = cpc_code.find('/')
        if slash_pos > 0:
            main_group = cpc_code[:slash_pos]
            if len(main_group) >= 4:
                level4_code = main_group[:4]
                cpc_year_counts[level4_code][year] += 1

print('Found', len(cpc_year_counts), 'CPC level 4 groups')

# Load CPC definitions
cpc_def_key = 'var_functions.query_db:52'
cpc_titles = {}
if cpc_def_key in globals():
    cpc_def_file = globals()[cpc_def_key]
    with open(cpc_def_file, 'r') as f:
        cpc_defs = json.load(f)
    
    for entry in cpc_defs:
        symbol = entry.get('symbol', '')
        title = entry.get('titleFull', '')
        if symbol and title and len(symbol) == 4:
            cpc_titles[symbol] = title

print('Loaded', len(cpc_titles), 'CPC level 4 titles')

# Calculate EMA for each CPC group
ema_results = []
smoothing_factor = 0.1

for cpc_code, year_counts in cpc_year_counts.items():
    # Get counts for years 2000-2024
    years = list(range(2000, 2025))
    counts = [year_counts.get(year, 0) for year in years]
    
    # Calculate EMA
    ema = []
    if counts:
        ema.append(counts[0])
        for i in range(1, len(counts)):
            ema_val = smoothing_factor * counts[i] + (1 - smoothing_factor) * ema[i-1]
            ema.append(ema_val)
    
    # Find best year (highest EMA)
    max_ema = max(ema)
    best_year = years[ema.index(max_ema)]
    
    ema_results.append({
        'cpc_group_code': cpc_code,
        'full_title': cpc_titles.get(cpc_code, 'Title not available'),
        'best_year': best_year,
        'exponential_moving_average': round(max_ema, 2),
        'total_patents': sum(counts)
    })

# Sort by EMA descending
ema_results.sort(key=lambda x: x['exponential_moving_average'], reverse=True)

print('Top 10 CPC groups by EMA:')
for i, result in enumerate(ema_results[:10]):
    print(f"{i+1}. {result['cpc_group_code']} - {result['full_title'][:60]}...")
    print(f"   Best Year: {result['best_year']}, EMA: {result['exponential_moving_average']}, Total: {result['total_patents']}")

# Save results
with open('german_cpc_ema_final.json', 'w') as f:
    json.dump(ema_results, f, indent=2)

result = {
    'status': 'success',
    'total_cpc_groups': len(ema_results),
    'top_groups': ema_results[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'status': 'success', 'cpc_groups': 11, 'total_patents': 6, 'sample_groups': ['B41F', 'B66C', 'E02F', 'B60S', 'F02D']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'status': 'success', 'cpc_groups': 564, 'total_patents': 11644, 'year_range': {'min': 1882, 'max': 2024}}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'status': 'success', 'total_cpc_groups': 11, 'top_groups': 11}, 'var_functions.execute_python:50': {'status': 'success', 'top_cpc_groups': [{'cpc_group_code': 'C04B', 'full_title': 'Title not available', 'best_year': 2015, 'exponential_moving_average': 4.5, 'total_patents_in_dataset': 45}, {'cpc_group_code': 'B29C', 'full_title': 'Title not available', 'best_year': 2007, 'exponential_moving_average': 1.5, 'total_patents_in_dataset': 15}, {'cpc_group_code': 'E02F', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.5, 'total_patents_in_dataset': 6}, {'cpc_group_code': 'B41F', 'full_title': 'Title not available', 'best_year': 2007, 'exponential_moving_average': 0.3, 'total_patents_in_dataset': 3}, {'cpc_group_code': 'F02D', 'full_title': 'Title not available', 'best_year': 2018, 'exponential_moving_average': 0.3, 'total_patents_in_dataset': 3}, {'cpc_group_code': 'C09K', 'full_title': 'Title not available', 'best_year': 2015, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'F42B', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'F41H', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'B66C', 'full_title': 'Title not available', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}, {'cpc_group_code': 'B60S', 'full_title': 'Title not available', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}, {'cpc_group_code': 'Y02T', 'full_title': 'Title not available', 'best_year': 2018, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}]}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
