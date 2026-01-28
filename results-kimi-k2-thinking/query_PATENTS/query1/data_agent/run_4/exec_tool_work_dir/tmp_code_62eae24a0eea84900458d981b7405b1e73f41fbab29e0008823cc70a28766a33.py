code = """import json, re, os, glob

# Load all publications data
pub_files = glob.glob('/tmp/tmp*.json')
pub_files.sort(key=os.path.getctime, reverse=True)

if not pub_files:
    print('No publication files found')
    result = {'error': 'no_publication_files'}
else:
    latest_file = pub_files[0]
    with open(latest_file, 'r') as f:
        publications = json.load(f)
    
    print(f'Loaded {len(publications)} publications from {latest_file}')
    
    # Count patents by CPC group and year
    patent_counts = {}
    years = set()
    
    for pub in publications:
        date_str = pub.get('publication_date', '')
        if date_str:
            year_match = re.search(r'\d{4}', date_str)
            if year_match:
                year = int(year_match.group())
                years.add(year)
                cpc_str = pub.get('cpc', '')
                if cpc_str:
                    try:
                        cpc_list = json.loads(cpc_str)
                        for item in cpc_list:
                            code = item.get('code', '')
                            if code:
                                # Extract main group (before / or space)
                                group = code.split('/')[0].split()[0]
                                if group not in patent_counts:
                                    patent_counts[group] = {}
                                patent_counts[group][year] = patent_counts[group].get(year, 0) + 1
                    except:
                        pass
    
    print(f'Found {len(patent_counts)} CPC groups')
    print(f'Year range: {sorted(years)}')
    
    # Calculate EMA (smoothing factor 0.2)
    alpha = 0.2
    cpc_ema = {}
    
    for cpc, yearly_counts in patent_counts.items():
        sorted_years = sorted(yearly_counts.keys())
        if len(sorted_years) < 2:
            continue
        
        ema_values = {}
        # First EMA = first year's count
        ema_values[sorted_years[0]] = float(yearly_counts[sorted_years[0]])
        
        # Calculate subsequent EMAs
        for i, year in enumerate(sorted_years[1:], 1):
            prev_year = sorted_years[i-1]
            ema_values[year] = alpha * yearly_counts[year] + (1 - alpha) * ema_values[prev_year]
        
        cpc_ema[cpc] = ema_values
    
    print(f'Calculated EMA for {len(cpc_ema)} CPC groups')
    
    # Load CPC level 5 symbols
    level5_symbols = var_functions.query_db_40
    level5_set = set(item['symbol'] for item in level5_symbols)
    print(f'Found {len(level5_set)} level 5 CPC symbols')
    
    # Find CPC groups with best year = 2022
    best_2022_level5 = []
    
    if 2022 in years:
        for cpc, ema_values in cpc_ema.items():
            # Check if CPC is level 5 (exact match in level5_set)
            if cpc in level5_set:
                # Find year with max EMA
                max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
                if max_year == 2022:
                    best_2022_level5.append(cpc)
    
    print(f'CPC level 5 groups with best year 2022: {len(best_2022_level5)}')
    print(f'Sample: {best_2022_level5[:20]}')
    
    result = {
        'count': len(best_2022_level5),
        'cpc_codes': best_2022_level5
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
