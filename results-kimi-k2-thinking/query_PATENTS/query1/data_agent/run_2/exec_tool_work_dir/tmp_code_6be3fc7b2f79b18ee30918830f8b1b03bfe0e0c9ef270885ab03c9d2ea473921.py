code = """import json
import re
from collections import defaultdict, Counter

# Load data
filepath = locals()['var_functions.query_db:32']
with open(filepath, 'r') as f:
    raw_data = json.load(f)

# Efficiently count CPC codes per year using dictionaries
cpc_yearly = defaultdict(Counter)
years = set()

for record in raw_data:
    pub_date = record.get('publication_date', '')
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
        years.add(year)
        
        cpc_str = record.get('cpc', '[]')
        cpc_list = json.loads(cpc_str)
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code and '/' in code:
                cpc_yearly[code][year] += 1

# Calculate EMA for each CPC code
alpha = 0.2
best_2022 = []
min_year = min(years)

for code, yearly_counts in cpc_yearly.items():
    # Need at least 2 years of data
    if len(yearly_counts) < 2:
        continue
    
    # Sort years and calculate EMA
    sorted_years = sorted(yearly_counts.items())
    ema = sorted_years[0][1]
    max_ema = ema
    max_ema_year = sorted_years[0][0]
    
    for year, count in sorted_years[1:]:
        ema = alpha * count + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            max_ema_year = year
    
    # Check if best year is 2022
    if max_ema_year == 2022:
        best_2022.append((code, max_ema))

# Sort by EMA descending
best_2022.sort(key=lambda x: x[1], reverse=True)
result = [code for code, ema in best_2022]

print(f'Years in data: {min(years)}-{max(years)}')
print(f'Total unique CPC level 5 codes: {len(cpc_yearly)}')
print(f'Codes with best year 2022: {len(result)}')

if result:
    print(f'Top 5 codes: {result[:5]}')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A61K9/06', 'A61K45/06', 'G06N3/08', 'G06N20/00', 'G02B6/3897', 'A61K31/675', 'C07D471/04', 'C07D401/14', 'A61K47/60', 'H04L69/326', 'A61B5/7267', 'G06T2207/10024', 'G06T7/90', 'A61P29/00', 'A61P35/00', 'A61P43/00', 'A61P3/10', 'A61P31/14', 'A61P25/16', 'A61P25/28', 'G06F3/011', 'A61P3/04', 'A61K47/26', 'A61P9/12', 'A61P9/10', 'A61P1/00', 'A61K31/606', 'A61K47/02', 'H01M10/613', 'G02F1/294', 'A61P9/04', 'A61P11/06', 'A61K9/2059', 'A61P3/00', 'A61P17/00', 'A61P25/20', 'A61P15/10', 'A61P25/06', 'A61P25/14', 'A61P13/12', 'A61P15/00', 'A61P13/10', 'A61P15/08', 'A61K47/12', 'A61K9/4866', 'A61P11/16', 'A61P13/00', 'A61P27/16', 'A61P25/30', 'A61P25/22', 'A61P25/24', 'A61P7/02', 'A61P37/06', 'A61P3/06', 'A61P9/02', 'H04J11/0079', 'A61P9/06', 'A61P9/00', 'C08G18/7671', 'H04N7/185', 'H04N23/51', 'H04W88/18', 'B60W2556/50'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
