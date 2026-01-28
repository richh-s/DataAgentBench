code = """import json

# Read the CPC definition data to understand levels
file_path = locals()['var_functions.query_db:26']
with open(file_path, 'r') as f:
    cpc_levels = json.load(f)

# Build a set of valid level 5 CPC codes from the definition database
level5_codes = set()
cpc_level_map = {}

for entry in cpc_levels:
    symbol = entry['symbol']
    level = float(entry['level'])
    cpc_level_map[symbol] = level
    
    # Check if this is at level 5
    if level == 5.0:
        level5_codes.add(symbol)

# Read the CPC codes with best year 2022
file_path = locals()['var_functions.execute_python:21']
with open(file_path, 'r') as f:
    cpc_best_2022 = json.load(f)

print('Number of CPC codes with best year 2022:', len(cpc_best_2022))
print('Number of level 5 codes in definition DB:', len(level5_codes))
print('Sample level 5 codes:', list(level5_codes)[:10])

# Find intersection: CPC codes that are both in level5_codes and have best year 2022
valid_cpc_codes = []
for cpc in cpc_best_2022:
    # Check if this exact CPC code is at level 5 in the definition database
    if cpc in level5_codes:
        valid_cpc_codes.append(cpc)
    else:
        # Also check if any parent code is at level 5
        # For codes like H01M10/0525, check parents H01M10, H01M, etc.
        parts = cpc.split('/')
        if len(parts) == 2:
            main_part = parts[0]
            # Check different lengths to find level 5 parent
            for i in range(len(main_part), 0, -1):
                parent = main_part[:i]
                if parent in level5_codes:
                    valid_cpc_codes.append(parent)
                    break

# Remove duplicates and return
valid_cpc_codes = list(set(valid_cpc_codes))
print('Number of valid level 5 CPC codes with best year 2022:', len(valid_cpc_codes))
print('Sample codes:', valid_cpc_codes[:10])
print('__RESULT__:')
print(json.dumps(valid_cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_cpc_codes': 143452, 'cpc_best_year_2022_count': 12036, 'level5_cpc_best_year_2022_count': 12036, 'sample_level5_cpc_2022': ['C01P2002/76', 'H01M10/0525', 'F16H2200/2007', 'F16H2200/2041', 'B29C70/48', 'C09D175/08', 'B32B27/34', 'B32B2260/021', 'B32B2307/50', 'B32B27/302']}, 'var_functions.execute_python:21': 'file_storage/functions.execute_python:21.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': [{'symbol': 'H01M10/0525', 'level': '10.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
