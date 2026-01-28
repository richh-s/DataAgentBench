code = """import json
import pandas as pd
import re

# Load data from file
filepath = locals()['var_functions.query_db:32']
with open(filepath, 'r') as f:
    raw_data = json.load(f)

# Use dict for efficient counting
cpc_year_counts = {}
min_year, max_year = float('inf'), float('-inf')

for record in raw_data:
    pub_date = record.get('publication_date', '')
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
        min_year, max_year = min(min_year, year), max(max_year, year)
        
        cpc_str = record.get('cpc', '[]')
        for cpc in json.loads(cpc_str):
            code = cpc.get('code', '')
            if code and '/' in code:
                key = (code, year)
                cpc_year_counts[key] = cpc_year_counts.get(key, 0) + 1

# Build DataFrame efficiently
data = [{'cpc_level5': k[0], 'year': k[1], 'count': v} 
        for k, v in cpc_year_counts.items()]
counts_df = pd.DataFrame(data)

# Calculate EMA for each CPC code
alpha = 0.2
best_2022_codes = []

for code in counts_df['cpc_level5'].unique():
    group = counts_df[counts_df['cpc_level5'] == code].sort_values('year')
    if len(group) < 2:
        continue
    
    # Calculate EMA
    ema = group.iloc[0]['count']
    max_ema, max_year = ema, group.iloc[0]['year']
    
    for _, row in group.iloc[1:].iterrows():
        ema = alpha * row['count'] + (1 - alpha) * ema
        if ema > max_ema:
            max_ema, max_year = ema, row['year']
    
    if max_year == 2022:
        best_2022_codes.append((code, max_ema))

# Sort by EMA and extract codes
result = [code for code, _ in sorted(best_2022_codes, key=lambda x: x[1], reverse=True)]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A61K9/06', 'A61K45/06', 'G06N3/08', 'G06N20/00', 'G02B6/3897', 'A61K31/675', 'C07D471/04', 'C07D401/14', 'A61K47/60', 'H04L69/326', 'A61B5/7267', 'G06T2207/10024', 'G06T7/90', 'A61P29/00', 'A61P35/00', 'A61P43/00', 'A61P3/10', 'A61P31/14', 'A61P25/16', 'A61P25/28', 'G06F3/011', 'A61P3/04', 'A61K47/26', 'A61P9/12', 'A61P9/10', 'A61P1/00', 'A61K31/606', 'A61K47/02', 'H01M10/613', 'G02F1/294', 'A61P9/04', 'A61P11/06', 'A61K9/2059', 'A61P3/00', 'A61P17/00', 'A61P25/20', 'A61P15/10', 'A61P25/06', 'A61P25/14', 'A61P13/12', 'A61P15/00', 'A61P13/10', 'A61P15/08', 'A61K47/12', 'A61K9/4866', 'A61P11/16', 'A61P13/00', 'A61P27/16', 'A61P25/30', 'A61P25/22', 'A61P25/24', 'A61P7/02', 'A61P37/06', 'A61P3/06', 'A61P9/02', 'H04J11/0079', 'A61P9/06', 'A61P9/00', 'C08G18/7671', 'H04N7/185', 'H04N23/51', 'H04W88/18', 'B60W2556/50'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
