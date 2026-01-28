code = """import json, re
from collections import defaultdict

# Load level 5 groups
level5_file = locals()['var_functions.query_db:16']
with open(level5_file, 'r') as f:
    level5_data = json.load(f)

level5_symbols = set([row['symbol'] for row in level5_data])

# Load patent publication data
pub_file = locals()['var_functions.query_db:6']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

# Count patents per level5 group per year
counts = defaultdict(int)
year_regex = re.compile(r'(\d{4})$')

for row in pub_data:
    date_str = row.get('publication_date', '')
    m = year_regex.search(date_str)
    if not m:
        continue
    year = int(m.group(1))
    cpc_str = row.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        continue
    for item in cpc_list:
        code = item.get('code')
        if not code:
            continue
        # Extract group (first 4 chars), if length>=4
        if len(code) >= 4:
            group = code[:4]
            if group in level5_symbols:
                counts[(group, year)] += 1

# Determine years present
years = sorted(set(year for _, year in counts.keys()))

# Compute EMA for each group
alpha = 0.2
best_year_per_group = {}
for group in level5_symbols:
    # Build series of counts for each year (0 if missing)
    series = [counts.get((group, y), 0) for y in years]
    ema = None
    best_ema = None
    best_y = None
    for idx, val in enumerate(series):
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_y = years[idx]
    best_year_per_group[group] = best_y

# Filter groups whose best year is 2022
selected_groups = [g for g, y in best_year_per_group.items() if y == 2022]

print('__RESULT__:')
print(json.dumps(selected_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': ['D02G', 'E02B', 'B25B', 'B24B', 'B60R', 'B01L', 'G01L', 'A42B', 'C01F', 'F23G', 'F28G', 'B60T', 'F16C', 'C07C', 'A61H', 'B60G', 'C04B', 'B61K', 'B64C', 'A43D', 'B22F', 'C23G', 'E03F', 'F01M', 'B66C', 'G07G', 'B21F', 'C08K', 'A47F', 'B64U', 'B64B', 'H01S', 'D07B', 'A47C', 'G21F', 'G05B', 'E01H', 'A61D', 'B21J', 'E04H', 'C21D', 'H03M', 'A61K', 'B44F', 'B61G', 'C10J', 'C07G', 'B02B', 'G01P', 'C01P', 'C21C', 'B02C', 'F21W', 'B31F', 'B07B', 'B29C', 'F01K', 'A45D', 'B63B', 'F01C', 'C01D', 'B25H', 'F16K', 'B06B', 'H02N', 'B27C', 'G01N', 'A01B', 'G11C', 'C12Q', 'B62K', 'E03B', 'B05D', 'A43B', 'F25B', 'G06F', 'B32B', 'B27H', 'B31C', 'A61P', 'B62B', 'A21C', 'C08F', 'H01G', 'B05B', 'C22C', 'F16J', 'C12M', 'B27G', 'A41H', 'B05C', 'G03B', 'E01D', 'H01R', 'D06F', 'F03D', 'F24V', 'B60H', 'F15B', 'G10H', 'H01B', 'G09B', 'A01N', 'B64F', 'C09K', 'D01F', 'F04F', 'G01D', 'D03J', 'B22D', 'A01K', 'B23C', 'C12Y', 'G08B', 'B65H', 'G01G', 'B28D', 'G09F', 'E21D', 'H04R', 'B44C', 'E05B', 'B60B', 'E21B', 'D06M', 'C08H', 'B82Y', 'B29L', 'H01L', 'B64D', 'H04S', 'G01B', 'G03F', 'A23K', 'B01F', 'B24C', 'C08G', 'G01F', 'H04N', 'B23K', 'G02B', 'B07C', 'C12L', 'H04W', 'C09D', 'A61B', 'F17C', 'B30B', 'H01Q', 'F03B', 'B61L', 'A41D', 'A41B', 'A21B', 'Y04S', 'G02C', 'A41C', 'A44C', 'B60N', 'F24T', 'B24D', 'A61L', 'G16B', 'G01M', 'C05C', 'C05F', 'C09C', 'F03H', 'G21K', 'B03B', 'A47J', 'A47G', 'F16B', 'B43L', 'B60L', 'D01D', 'C06B'], 'var_functions.query_db:12': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}, {'symbol': 'A01K2227/106', 'level': '9.0'}, {'symbol': 'A01K2227/706', 'level': '9.0'}, {'symbol': 'A01K2227/703', 'level': '9.0'}, {'symbol': 'A01K2267/025', 'level': '9.0'}, {'symbol': 'A01K2267/0393', 'level': '9.0'}, {'symbol': 'A01K2267/0331', 'level': '9.0'}, {'symbol': 'A01K2267/0306', 'level': '9.0'}, {'symbol': 'A01K2267/035', 'level': '9.0'}, {'symbol': 'A01K2267/0337', 'level': '9.0'}, {'symbol': 'A01K85/1813', 'level': '9.0'}, {'symbol': 'A01K85/1821', 'level': '9.0'}, {'symbol': 'A01K85/1833', 'level': '9.0'}, {'symbol': 'A01K85/1843', 'level': '9.0'}, {'symbol': 'A01K85/1877', 'level': '9.0'}, {'symbol': 'A23C2210/204', 'level': '9.0'}], 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
