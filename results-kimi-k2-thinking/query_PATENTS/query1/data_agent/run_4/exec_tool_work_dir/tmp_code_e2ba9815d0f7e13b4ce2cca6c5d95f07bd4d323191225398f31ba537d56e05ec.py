code = """import json, re, os

# Process the publications data from query_db_52 file
file_path = '/tmp/tmpf7s0i7n4.json'

print('Loading publications data...')
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f'Processing {len(publications)} publications...')

# Count patents by CPC group and year
patent_counts = {}
years = set()

for pub in publications:
    date_str = pub.get('publication_date', '')
    if date_str:
        year_match = re.findall(r'(\d{4})', date_str)
        if year_match:
            year = int(year_match[0])
            years.add(year)
            
            cpc_str = pub.get('cpc', '')
            if cpc_str:
                try:
                    cpc_list = json.loads(cpc_str)
                    for item in cpc_list:
                        code = item.get('code', '')
                        if code:
                            # Extract main CPC symbol (before / or space)
                            group = code.split('/')[0].split()[0]
                            if group not in patent_counts:
                                patent_counts[group] = {}
                            patent_counts[group][year] = patent_counts[group].get(year, 0) + 1
                except:
                    pass

print(f'Found {len(patent_counts)} unique CPC groups')
print(f'Year range: {min(years)} to {max(years)}')

# Calculate EMA for each CPC group
alpha = 0.2
cpc_ema = {}

for cpc, yearly_counts in patent_counts.items():
    sorted_years = sorted(yearly_counts.keys())
    if len(sorted_years) < 2:
        continue
    
    ema = {}
    # First year EMA is just the count
    ema[sorted_years[0]] = float(yearly_counts[sorted_years[0]])
    
    # Calculate EMA for subsequent years
    for i in range(1, len(sorted_years)):
        year = sorted_years[i]
        prev_year = sorted_years[i-1]
        ema[year] = alpha * yearly_counts[year] + (1 - alpha) * ema[prev_year]
    
    cpc_ema[cpc] = ema

print(f'Calculated EMA for {len(cpc_ema)} CPC groups')

# Get level 5 CPC symbols from the database
level5_symbols = [item['symbol'] for item in var_functions.query_db_40]
level5_set = set(level5_symbols)

print(f'Found {len(level5_set)} level 5 CPC symbols')

# Find CPC groups at level 5 with best year = 2022
best_2022_level5 = []

if 2022 in years:
    for cpc, ema_values in cpc_ema.items():
        if cpc in level5_set and 2022 in ema_values:
            max_year = max(ema_values.keys(), key=lambda y: ema_values[y])
            if max_year == 2022:
                best_2022_level5.append(cpc)

print(f'CPC level 5 groups with peak EMA in 2022: {len(best_2022_level5)}')
print('Sample codes:', best_2022_level5[:20])

result = {
    'total_patents_processed': len(publications),
    'cpc_groups_analyzed': len(cpc_ema),
    'level5_groups_with_peak_2022': len(best_2022_level5),
    'cpc_codes': best_2022_level5
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:26': {'status': 'no_data'}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'error': 'no_publication_files'}, 'var_functions.query_db:48': [{'total_patents': '277813'}], 'var_functions.query_db:50': [], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
