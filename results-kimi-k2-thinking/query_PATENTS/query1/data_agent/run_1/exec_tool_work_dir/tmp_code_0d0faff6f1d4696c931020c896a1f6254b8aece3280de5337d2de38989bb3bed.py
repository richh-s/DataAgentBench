code = """import json, re
from collections import defaultdict

# Get file paths from storage
pub_data_path = locals()['var_functions.query_db:6']
cpc_def_path = locals()['var_functions.query_db:5']

# Read data
with open(pub_data_path, 'r') as f:
    publications = json.load(f)

with open(cpc_def_path, 'r') as f:
    cpc_level_info = json.load(f)

# Get level 5 CPC symbols
cpc_level5_symbols = set(item['symbol'] for item in cpc_level_info)

# Count CPC codes by year
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    # Parse year
    m = re.search(r'(\d{4})', pub['publication_date'])
    if not m: continue
    year = int(m.group(1))
    
    # Parse CPC codes
    cpc_str = pub['cpc']
    if not cpc_str: continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for entry in cpc_list:
            code = entry['code']
            group = code.split('/')[0]
            if group in cpc_level5_symbols:
                cpc_yearly_counts[group][year] += 1
    except: continue

# Calculate EMA
def calculate_ema(yearly_counts, alpha=0.2):
    if len(yearly_counts) < 2: return None, {}
    years = sorted(yearly_counts.keys())
    ema = {}
    prev = None
    for y in years:
        count = yearly_counts[y]
        if prev is None:
            prev = count
        else:
            prev = alpha * count + (1-alpha) * prev
        ema[y] = prev
    best = max(ema, key=ema.get)
    return best, ema

# Find CPC codes with best year = 2022
cpc_best_2022 = []
for code, counts in cpc_yearly_counts.items():
    best_year, ema_data = calculate_ema(counts)
    if best_year == 2022:
        cpc_best_2022.append(code)

result = json.dumps(sorted(cpc_best_2022))
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'B21L', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A47F', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}, {'symbol': 'A45D', 'level': '5.0'}, {'symbol': 'A45B', 'level': '5.0'}, {'symbol': 'A46D', 'level': '5.0'}, {'symbol': 'A46B', 'level': '5.0'}, {'symbol': 'A47L', 'level': '5.0'}, {'symbol': 'B22C', 'level': '5.0'}, {'symbol': 'A47D', 'level': '5.0'}, {'symbol': 'A47G', 'level': '5.0'}, {'symbol': 'A47K', 'level': '5.0'}, {'symbol': 'A47H', 'level': '5.0'}, {'symbol': 'A47B', 'level': '5.0'}, {'symbol': 'A47C', 'level': '5.0'}, {'symbol': 'A47J', 'level': '5.0'}, {'symbol': 'A61M', 'level': '5.0'}, {'symbol': 'A61K', 'level': '5.0'}, {'symbol': 'A61B', 'level': '5.0'}, {'symbol': 'A61C', 'level': '5.0'}, {'symbol': 'A61F', 'level': '5.0'}, {'symbol': 'A61L', 'level': '5.0'}, {'symbol': 'A61J', 'level': '5.0'}, {'symbol': 'A61G', 'level': '5.0'}, {'symbol': 'A61Q', 'level': '5.0'}, {'symbol': 'A61P', 'level': '5.0'}, {'symbol': 'B60V', 'level': '5.0'}, {'symbol': 'A61H', 'level': '5.0'}, {'symbol': 'A61D', 'level': '5.0'}, {'symbol': 'A61N', 'level': '5.0'}, {'symbol': 'A62C', 'level': '5.0'}, {'symbol': 'A62D', 'level': '5.0'}, {'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}, {'symbol': 'B02B', 'level': '5.0'}, {'symbol': 'B03B', 'level': '5.0'}, {'symbol': 'B03D', 'level': '5.0'}, {'symbol': 'B03C', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
