code = """import json
import numpy as np
from collections import defaultdict

# Get the file path from previous query
file_path = locals()['var_functions.query_db:5']

with open(file_path, 'r') as f:
    data = json.load(f)

# Count filings per CPC code per year
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for record in data:
    # Extract year
    import re
    year_match = re.search(r'(\d{4})', record['publication_date'])
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    if year < 1900 or year > 2023:
        continue
    
    # Extract CPC codes (level 5)
    try:
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            # Pattern for level 5: H01M10/05, A61K31/00, etc.
            # Section(1) + Class(2) + Subclass(optional letter) + Main group + / + Subgroup(2 digits)
            if re.match(r'^[A-Z][0-9]{2}[A-Z]?[0-9]+/[0-9]{2}$', code):
                cpc_year_counts[code][year] += 1
    except:
        continue

# Calculate EMA for each CPC code
smoothing = 0.2
cpc_with_best_year_2022 = []

for cpc, year_counts in cpc_year_counts.items():
    years = list(range(1900, 2024))
    values = [year_counts.get(year, 0) for year in years]
    
    # Calculate EMA
    ema_values = []
    first_nonzero = next((v for v in values if v > 0), 0)
    if first_nonzero == 0:
        continue
    
    ema_prev = first_nonzero
    ema_values.append(ema_prev)
    
    for i in range(1, len(values)):
        ema_current = smoothing * values[i] + (1 - smoothing) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    # Find year with max EMA
    max_idx = np.argmax(ema_values)
    if years[max_idx] == 2022:
        cpc_with_best_year_2022.append(cpc)

# Limit to top results and format
result_cpc_codes = sorted(cpc_with_best_year_2022)[:100]  # Take first 100 sorted codes

print(f'Total CPC level 5 codes peaked in 2022: {len(cpc_with_best_year_2022)}')
print('Sample codes (first 20):')
for code in result_cpc_codes[:20]:
    print(f'  {code}')

output = {
    'total_codes': len(cpc_with_best_year_2022),
    'sample_codes': result_cpc_codes[:50]  # Return first 50
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:9': ['cpc_definition'], 'var_functions.execute_python:14': {'num_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:16': {'num_cpc_codes': 70324, 'num_years': 186, 'cpc_sample': ['C01B33/00', 'C01B35/00', 'H01M10/05', 'C01G45/00', 'C01P2002/76', 'Y02E60/10', 'H01M2004/02', 'H01M4/13', 'H01M4/52', 'H01M4/50'], 'years_sample': [1837, 1839, 1841, 1842, 1843]}, 'var_functions.execute_python:18': {'num_candidates': 171, 'sample_cpc': ['C01P2002/76', 'B29C70/48', 'B32B27/34', 'B32B2255/02', 'B32B27/10', 'B32B2307/50', 'B32B5/18', 'A01K2267/03', 'A61P7/00', 'A61P1/16']}, 'var_functions.execute_python:20': {'peaked_in_2022': 2664, 'codes': ['C01P2002/76', 'B29C70/48', 'B32B27/34', 'B32B2255/02', 'B32B27/10', 'B32B2307/50', 'B32B5/18', 'A01K2267/03', 'A61P7/00', 'A61P1/16', 'A61P3/00', 'A23L33/12', 'A61P13/12', 'C12N7/00', 'G10L25/63', 'C12N15/85', 'C07K2319/02', 'A61K45/06', 'A61K38/00', 'B60Y2200/92']}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'symbol': 'B04', 'level': '4.0'}, {'symbol': 'B23', 'level': '4.0'}, {'symbol': 'B30', 'level': '4.0'}, {'symbol': 'B21', 'level': '4.0'}, {'symbol': 'B25', 'level': '4.0'}, {'symbol': 'B99', 'level': '4.0'}, {'symbol': 'B29', 'level': '4.0'}, {'symbol': 'B33', 'level': '4.0'}, {'symbol': 'C22', 'level': '4.0'}, {'symbol': 'D99', 'level': '4.0'}], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}]}

exec(code, env_args)
