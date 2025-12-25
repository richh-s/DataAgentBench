code = """import json
import pandas as pd
import re
import os

# Load Level 5 symbols
# path is in var_function-call-14221353990165595785
with open(locals()['var_function-call-14221353990165595785'], 'r') as f:
    l5_data = json.load(f)
l5_symbols = set(item['symbol'] for item in l5_data)

# Load filing data
# path is in var_function-call-5101753233622392342
with open(locals()['var_function-call-5101753233622392342'], 'r') as f:
    filing_data = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Process data
counts = {} # year -> cpc_code -> count

for row in filing_data:
    f_date = row.get('filing_date')
    cpc_json = row.get('cpc')
    
    if not f_date or not cpc_json:
        continue
        
    # Extract year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Find Level 5 codes for this patent
    patent_l5_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Try to match Level 5 symbols
        # Level 5 symbols are 4 chars (e.g. A01B)
        # Patent code: "A01B 1/00" or "A01B1/00"
        # Extract first 4 chars
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in l5_symbols:
                patent_l5_codes.add(subclass)
    
    # Aggregate
    if year not in counts:
        counts[year] = {}
    
    for code in patent_l5_codes:
        counts[year][code] = counts[year].get(code, 0) + 1

# Create DataFrame
df = pd.DataFrame(counts).T # Rows=Years, Cols=CPCs
df = df.sort_index()
df = df.fillna(0)

# Calculate EMA
ema_df = df.ewm(alpha=0.2, adjust=False).mean()

# Find best year for each CPC
best_years = ema_df.idxmax()

# Filter for 2022
target_year = 2022
result_codes = best_years[best_years == target_year].index.tolist()

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-2958369783092376': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-2958369783091725': [{'count': '677'}], 'var_function-call-2958369783095170': 'file_storage/function-call-2958369783095170.json', 'var_function-call-2958369783094519': [{'count(*)': '277813'}], 'var_function-call-7981512775900057419': [{'level': '2.0', 'min': 'A', 'max': 'Y', 'count': '9'}, {'level': '4.0', 'min': 'A01', 'max': 'Y10', 'count': '137'}, {'level': '5.0', 'min': 'A01B', 'max': 'Y10T', 'count': '677'}, {'level': '7.0', 'min': 'A01B1/00', 'max': 'Y10T83/00', 'count': '9816'}, {'level': '8.0', 'min': 'A01B1/02', 'max': 'Y10T83/97', 'count': '48384'}, {'level': '9.0', 'min': 'A01B1/022', 'max': 'Y10T83/96', 'count': '70250'}, {'level': '10.0', 'min': 'A01B1/225', 'max': 'Y10T83/9498', 'count': '62585'}, {'level': '11.0', 'min': 'A01B3/421', 'max': 'Y10T83/949', 'count': '35084'}, {'level': '12.0', 'min': 'A01B3/4215', 'max': 'Y10T83/9486', 'count': '17632'}, {'level': '13.0', 'min': 'A01D2034/6843', 'max': 'Y10T83/9341', 'count': '8015'}, {'level': '14.0', 'min': 'A01D2034/6825', 'max': 'Y10T83/9338', 'count': '3649'}, {'level': '15.0', 'min': 'A47J31/4446', 'max': 'Y10T83/656', 'count': '1521'}, {'level': '16.0', 'min': 'A61B17/7028', 'max': 'Y10T70/7616', 'count': '1223'}, {'level': '17.0', 'min': 'A61K47/6823', 'max': 'Y10T70/761', 'count': '720'}, {'level': '18.0', 'min': 'G01N2333/96444', 'max': 'Y10T70/5473', 'count': '485'}, {'level': '19.0', 'min': 'H01L21/32137', 'max': 'H01L2224/45984', 'count': '621'}], 'var_function-call-14221353990165595785': 'file_storage/function-call-14221353990165595785.json', 'var_function-call-5101753233622392342': 'file_storage/function-call-5101753233622392342.json'}

exec(code, env_args)
