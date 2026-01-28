code = """import json, re, os, glob

# First, let's see what files exist
print("Files in /tmp:")
files = glob.glob('/tmp/*')
for f in files:
    if 'tmp' in f and f.endswith('.json'):
        print(f"  {f} ({os.path.getsize(f)} bytes)")

# Process the publications
# Find the most recent publications file
pub_files = sorted([f for f in files if 'tmp' in f and f.endswith('.json') and os.path.getsize(f) > 1000], 
                   key=os.path.getctime, reverse=True)

if pub_files:
    latest_file = pub_files[0]
    print(f"\nUsing file: {latest_file}")
    
    with open(latest_file, 'r') as f:
        publications = json.load(f)
    
    print(f"Loaded {len(publications)} publications")
    
    # Count patents by CPC group and year
    patent_counts = {}
    years = set()
    
    for pub in publications:
        date_str = pub.get('publication_date', '')
        if date_str:
            year_match = re.search(r'(\d{4})', date_str)
            if year_match:
                year = int(year_match.group(1))
                years.add(year)
                
                cpc_str = pub.get('cpc', '')
                if cpc_str:
                    try:
                        cpc_list = json.loads(cpc_str)
                        for item in cpc_list:
                            code = item.get('code', '')
                            if code:
                                group = code.split('/')[0].split()[0]
                                if group not in patent_counts:
                                    patent_counts[group] = {}
                                patent_counts[group][year] = patent_counts[group].get(year, 0) + 1
                    except:
                        pass
    
    print(f"Found {len(patent_counts)} CPC groups")
    print(f"Year range: {sorted(list(years))}")
    
    # Calculate EMA
    alpha = 0.2
    cpc_ema = {}
    
    for cpc, yearly_counts in patent_counts.items():
        sorted_years = sorted(yearly_counts.keys())
        if len(sorted_years) < 2:
            continue
        
        ema = {}
        ema[sorted_years[0]] = float(yearly_counts[sorted_years[0]])
        
        for i in range(1, len(sorted_years)):
            year = sorted_years[i]
            prev_year = sorted_years[i-1]
            ema[year] = alpha * yearly_counts[year] + (1 - alpha) * ema[prev_year]
        
        cpc_ema[cpc] = ema
    
    print(f"Calculated EMA for {len(cpc_ema)} CPC groups")
    
    # Get level 5 symbols
    level5_symbols = [item['symbol'] for item in var_functions.query_db_40]
    level5_set = set(level5_symbols)
    
    # Find CPC at level 5 with best year = 2022
    best_2022 = []
    
    if 2022 in years:
        for cpc, ema_values in cpc_ema.items():
            if cpc in level5_set and 2022 in ema_values:
                max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
                if max_year == 2022:
                    best_2022.append(cpc)
    
    print(f"Level 5 CPC groups with peak in 2022: {len(best_2022)}")
    
    result = {
        'count': len(best_2022),
        'cpc_codes': sorted(best_2022)
    }
else:
    result = {'error': 'no_publication_files_found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'error': 'no_publication_files'}, 'var_functions.query_db:48': [{'total_patents': '277813'}], 'var_functions.query_db:50': [], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
