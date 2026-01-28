code = """import json
import os
import re
from collections import defaultdict

# Get the data file path
result_key = 'var_functions.query_db:42'
result_file = None
if result_key in globals():
    result_file = globals()[result_key]

if not result_file or not os.path.exists(result_file):
    print('ERROR: Could not find data file')
    result = {'status': 'error', 'message': 'Data file not found'}
else:
    print('Loading data from:', result_file)
    
    with open(result_file, 'r') as f:
        patents_data = json.load(f)
    
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
        
        # Skip years before 2000 or after 2024 (data quality)
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
    
    # Calculate exponential moving averages for each CPC group
    ema_results = {}
    smoothing_factor = 0.1
    
    for cpc_code, year_counts in cpc_year_counts.items():
        # Get all years with data (2000-2024)
        years = list(range(2000, 2025))
        counts = [year_counts.get(year, 0) for year in years]
        
        # Calculate EMA
        ema = []
        if counts:
            # Initialize with first value
            ema.append(counts[0])
            # Calculate EMA for subsequent years
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
            'ema_values': list(zip(years, ema))
        }
    
    # Sort by max EMA value
    sorted_results = sorted(ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)
    
    # Save results
    output_file = 'cpc_ema_results.json'
    with open(output_file, 'w') as f:
        json.dump({
            'total_cpc_groups': len(cpc_year_counts),
            'top_cpc_groups': sorted_results[:50]  # Top 50
        }, f, indent=2)
    
    print('Top 5 CPC groups by EMA:')
    for i in range(min(5, len(sorted_results))):
        cpc_code, data = sorted_results[i]
        print(f"{i+1}. {cpc_code}: EMA={data['max_ema']:.2f} in year {data['best_year']}")
    
    result = {
        'status': 'success',
        'total_cpc_groups': len(cpc_year_counts),
        'top_groups': len(sorted_results)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'status': 'success', 'cpc_groups': 11, 'total_patents': 6, 'sample_groups': ['B41F', 'B66C', 'E02F', 'B60S', 'F02D']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'status': 'success', 'cpc_groups': 564, 'total_patents': 11644, 'year_range': {'min': 1882, 'max': 2024}}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
