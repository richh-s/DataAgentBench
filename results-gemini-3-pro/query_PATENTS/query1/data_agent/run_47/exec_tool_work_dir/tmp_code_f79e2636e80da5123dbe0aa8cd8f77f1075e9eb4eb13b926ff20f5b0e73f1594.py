code = """import json
import re

# Access the stored file paths
path_cpc_defs = locals()['var_function-call-1274391543131154232']
path_pub_info = locals()['var_function-call-1274391543131155253']

# Load Level 5 CPCs
with open(path_cpc_defs, 'r') as f:
    cpc_def_list = json.load(f)
valid_cpcs = set(item['symbol'] for item in cpc_def_list)

# Load Publication Data
with open(path_pub_info, 'r') as f:
    pub_data = json.load(f)

counts = {} # cpc -> year -> count
all_years = set()

# Process data
for row in pub_data:
    # Extract Year
    date_str = row.get('filing_date')
    if not date_str or not isinstance(date_str, str):
        continue
    
    # Regex for year (19xx or 20xx)
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    # Extract CPCs
    cpc_raw = row.get('cpc')
    if not cpc_raw or not isinstance(cpc_raw, str):
        continue
    
    try:
        cpc_list = json.loads(cpc_raw)
    except json.JSONDecodeError:
        continue
        
    if not isinstance(cpc_list, list):
        continue

    # Get unique valid Level 5 codes for this patent
    patent_cpcs = set()
    for entry in cpc_list:
        code = entry.get('code')
        if code and isinstance(code, str) and len(code) >= 4:
            symbol = code[:4]
            if symbol in valid_cpcs:
                patent_cpcs.add(symbol)
    
    # Aggregate
    for cpc in patent_cpcs:
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA and find best year
# Determine global max year to ensure we cover up to 2022 if data exists
global_max = max(all_years) if all_years else 0
# If data goes only to 2021, then no CPC can have best year 2022 (unless we extrapolate, but we shouldn't).
# Assuming data covers 2022.

matching_cpcs = []

for cpc, year_map in counts.items():
    if not year_map:
        continue
        
    start_year = min(year_map.keys())
    
    # Initialize EMA
    # First data point
    ema = float(year_map[start_year])
    max_ema = ema
    best_year = start_year
    
    # Iterate through all subsequent years up to global_max
    # We fill zeros for missing years
    for y in range(start_year + 1, global_max + 1):
        count = year_map.get(y, 0)
        ema = 0.2 * count + 0.8 * ema
        
        # Check if this is the new best (strictly greater or >=? "highest" usually implies strictly or first? 
        # But float comparison... let's just use > or >=. If equal, later year is "best"? 
        # Usually peaks are distinct. I'll use >.
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        matching_cpcs.append(cpc)

print("__RESULT__:")
print(json.dumps(matching_cpcs))"""

env_args = {'var_function-call-11820737813391212427': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-11820737813391208476': 'file_storage/function-call-11820737813391208476.json', 'var_function-call-18359320766515546987': [{'level': '2.0', 'sample_symbol': 'A', 'cnt': '9'}, {'level': '4.0', 'sample_symbol': 'A01', 'cnt': '137'}, {'level': '5.0', 'sample_symbol': 'A01B', 'cnt': '677'}, {'level': '7.0', 'sample_symbol': 'A01B1/00', 'cnt': '9816'}, {'level': '8.0', 'sample_symbol': 'A01B1/02', 'cnt': '48384'}, {'level': '9.0', 'sample_symbol': 'A01B1/022', 'cnt': '70250'}, {'level': '10.0', 'sample_symbol': 'A01B1/225', 'cnt': '62585'}, {'level': '11.0', 'sample_symbol': 'A01B3/421', 'cnt': '35084'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215', 'cnt': '17632'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843', 'cnt': '8015'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825', 'cnt': '3649'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446', 'cnt': '1521'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028', 'cnt': '1223'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823', 'cnt': '720'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444', 'cnt': '485'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137', 'cnt': '621'}], 'var_function-call-8333227560207613729': [{'len': '4', 'count': '677'}], 'var_function-call-1274391543131154232': 'file_storage/function-call-1274391543131154232.json', 'var_function-call-1274391543131155253': 'file_storage/function-call-1274391543131155253.json'}

exec(code, env_args)
