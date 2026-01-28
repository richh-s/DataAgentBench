code = """import json
import re
import os
import glob

# Check what files exist in /tmp
print("Files in /tmp:")
all_files = glob.glob('/tmp/*')
json_files = [f for f in all_files if f.endswith('.json')]
for f in sorted(json_files, key=os.path.getctime, reverse=True)[:10]:
    print(f"  {f} ({os.path.getsize(f)} bytes)")

# Load level 5 CPC symbols
level5_file = None
for f in json_files:
    if 'cpc' in f.lower() or 'level' in f.lower() or any(x in open(f).read(1000).lower() for x in ['symbol', 'level']):
        level5_file = f
        break

if not level5_file:
    # Try the most recent files
    for f in sorted(json_files, key=os.path.getctime, reverse=True)[:5]:
        try:
            with open(f, 'r') as file:
                content = json.load(file)
            if isinstance(content, list) and len(content) > 0 and 'symbol' in str(content[0]):
                level5_file = f
                break
        except:
            continue

print(f"\nUsing level5 file: {level5_file}")

if level5_file:
    with open(level5_file, 'r') as f:
        level5_data = json.load(f)
    level5_symbols = set(item.get('symbol') or item['symbol'] for item in level5_data)
    print(f"Loaded {len(level5_symbols)} level 5 CPC symbols")
    print(f"Sample: {sorted(list(level5_symbols))[:10]}")
else:
    level5_symbols = set()
    print("No level 5 symbols found")

# Find publication data file
pub_file = None
for f in sorted(json_files, key=os.path.getctime, reverse=True):
    if f != level5_file:
        try:
            with open(f, 'r') as file:
                content = json.load(file)
            if isinstance(content, list) and len(content) > 0 and 'publication_date' in str(content[0]):
                pub_file = f
                break
        except:
            continue

print(f"\nUsing publication file: {pub_file}")

if pub_file and level5_symbols:
    with open(pub_file, 'r') as f:
        publications = json.load(f)
    
    print(f"Processing {len(publications)} publications...")
    
    # Count patents per CPC group per year
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
                        continue
    
    print(f"Found {len(patent_counts)} unique CPC groups")
    print(f"Year range: {min(years)} to {max(years)}")
    
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
    
    # Find level 5 CPC groups with peak EMA in 2022
    best_2022_level5 = []
    
    if 2022 in years:
        for cpc, ema_values in cpc_ema.items():
            if cpc in level5_symbols and 2022 in ema_values:
                max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
                if max_year == 2022:
                    best_2022_level5.append(cpc)
    
    print(f"Found {len(best_2022_level5)} level 5 CPC groups with peak EMA in 2022")
    
    result = {
        'count': len(best_2022_level5),
        'cpc_codes': sorted(best_2022_level5)
    }
else:
    result = {'error': 'missing_data', 'level5_symbols': len(level5_symbols), 'pub_file': pub_file is not None}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'error': 'no_publication_files'}, 'var_functions.query_db:48': [{'total_patents': '277813'}], 'var_functions.query_db:50': [], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'error': 'no_files'}, 'var_functions.execute_python:64': {'level5_symbols': []}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
