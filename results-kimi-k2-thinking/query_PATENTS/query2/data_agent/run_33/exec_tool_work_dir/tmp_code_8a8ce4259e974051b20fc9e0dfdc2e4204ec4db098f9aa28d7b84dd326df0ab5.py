code = """import json
import os
import re
from collections import defaultdict

# Load the patent data
def load_json_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        return json.load(f)

# Get file paths
patents_key = 'var_functions.query_db:42'
cpc_def_key = 'var_functions.query_db:46'

patents_file = globals().get(patents_key) if patents_key in globals() else None
cpc_def_file = globals().get(cpc_def_key) if cpc_def_key in globals() else None

if not patents_file or not os.path.exists(patents_file):
    print('ERROR: Patents data file not found')
    result = {'status': 'error', 'message': 'Patents file not found'}
else:
    patents_data = load_json_file(patents_file)
    print('Loaded', len(patents_data), 'patents')
    
    # Extract CPC level 4 codes and filing years
    cpc_year_counts = defaultdict(lambda: defaultdict(int))
    
    for patent in patents_data:
        # Extract filing year
        filing_date = patent.get('filing_date', '')
        year_match = re.search(r'(\d{4})', filing_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        # Skip invalid years
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
        
        # Process each CPC code
        for cpc_entry in cpc_codes:
            if not isinstance(cpc_entry, dict):
                continue
            
            cpc_code = cpc_entry.get('code', '')
            if not cpc_code or len(cpc_code) < 4:
                continue
            
            # Find main group (before slash)
            slash_pos = cpc_code.find('/')
            if slash_pos > 0:
                main_group = cpc_code[:slash_pos]
                # Level 4 code: first 4 characters
                if len(main_group) >= 4:
                    level4_code = main_group[:4]
                    cpc_year_counts[level4_code][year] += 1
    
    print('Found', len(cpc_year_counts), 'CPC level 4 groups')
    
    # Calculate exponential moving averages
    ema_results = {}
    smoothing_factor = 0.1
    
    for cpc_code, year_counts in cpc_year_counts.items():
        # Get all years with data (2000-2024)
        years = list(range(2000, 2025))
        counts = [year_counts.get(year, 0) for year in years]
        
        # Calculate EMA
        ema = []
        if counts:
            ema.append(counts[0])
            for i in range(1, len(counts)):
                ema_val = smoothing_factor * counts[i] + (1 - smoothing_factor) * ema[i-1]
                ema.append(ema_val)
        
        # Find year with highest EMA
        max_ema_idx = ema.index(max(ema))
        best_year = years[max_ema_idx]
        max_ema_value = ema[max_ema_idx]
        
        ema_results[cpc_code] = {
            'best_year': best_year,
            'max_ema': max_ema_value,
            'total_patents': sum(counts)
        }
    
    # Sort by max EMA value and get top 20
    sorted_results = sorted(ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)[:20]
    
    print('Top CPC groups by EMA:')
    for i, (code, data) in enumerate(sorted_results):
        print(f"{i+1}. {code}: EMA={data['max_ema']:.2f}, Best Year={data['best_year']}, Total Patents={data['total_patents']}")
    
    # Load CPC definitions if available
    cpc_titles = {}
    if cpc_def_file and os.path.exists(cpc_def_file):
        cpc_defs = load_json_file(cpc_def_file)
        print('Loaded', len(cpc_defs), 'CPC definitions')
        
        for entry in cpc_defs:
            symbol = entry.get('symbol', '')
            title = entry.get('titleFull', '')
            if symbol and title:
                cpc_titles[symbol] = title
    
    # Prepare final results
    final_results = []
    for cpc_code, data in sorted_results:
        full_title = cpc_titles.get(cpc_code, 'Title not available')
        final_results.append({
            'cpc_group_code': cpc_code,
            'full_title': full_title,
            'best_year': data['best_year'],
            'exponential_moving_average': round(data['max_ema'], 2),
            'total_patents_in_dataset': data['total_patents']
        })
    
    # Save final results
    with open('german_cpc_ema_results.json', 'w') as f:
        json.dump(final_results, f, indent=2)
    
    result = {
        'status': 'success',
        'top_cpc_groups': final_results
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'status': 'success', 'cpc_groups': 11, 'total_patents': 6, 'sample_groups': ['B41F', 'B66C', 'E02F', 'B60S', 'F02D']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'status': 'success', 'cpc_groups': 564, 'total_patents': 11644, 'year_range': {'min': 1882, 'max': 2024}}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'status': 'success', 'total_cpc_groups': 11, 'top_groups': 11}}

exec(code, env_args)
