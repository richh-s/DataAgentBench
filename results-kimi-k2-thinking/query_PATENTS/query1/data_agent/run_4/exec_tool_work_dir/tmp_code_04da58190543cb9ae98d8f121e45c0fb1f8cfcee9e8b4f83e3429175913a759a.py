code = """import json
import re
from collections import defaultdict

# Load level 5 CPC symbols
level5_file = '/tmp/tmpm6q8civg.json'
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in level5_data)
print(f"Loaded {len(level5_symbols)} level 5 CPC symbols")

# Load publication data
pub_file = '/tmp/tmp_2nmiwnj.json'
with open(pub_file, 'r') as f:
    publications = json.load(f)

print(f"Processing {len(publications)} publications...")

# Count patents per CPC group per year
patent_counts = defaultdict(lambda: defaultdict(int))
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
                            # Extract main group symbol (before / or space)
                            group = code.split('/')[0].split()[0]
                            patent_counts[group][year] += 1
                except:
                    continue

print(f"Found {len(patent_counts)} unique CPC groups")
print(f"Year range: {min(years)} to {max(years)}")

# Calculate EMA (smoothing factor 0.2)
alpha = 0.2
cpc_ema = {}

for cpc, yearly_counts in patent_counts.items():
    sorted_years = sorted(yearly_counts.keys())
    if len(sorted_years) < 2:
        continue
    
    ema = {}
    # First year: EMA = actual count
    ema[sorted_years[0]] = float(yearly_counts[sorted_years[0]])
    
    # Subsequent years
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
            # Find year with max EMA
            max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
            if max_year == 2022:
                best_2022_level5.append(cpc)

print(f"Found {len(best_2022_level5)} level 5 CPC groups with peak EMA in 2022")

# Sort and format results
result_codes = sorted(best_2022_level5)

result = {
    'count': len(result_codes),
    'cpc_level5_codes_peak_2022': result_codes
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'error': 'no_publication_files'}, 'var_functions.query_db:48': [{'total_patents': '277813'}], 'var_functions.query_db:50': [], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'error': 'no_files'}, 'var_functions.execute_python:64': {'level5_symbols': []}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
