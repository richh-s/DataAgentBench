code = """import json
import re
import pandas as pd
import numpy as np

# Load Level 5 Codes
with open('var_function-call-5635872423012651359.json', 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load Patent Data
# Since the file might be large, reading it all into memory might be okay if it's < 1GB.
# The previous step indicated ~277k records. 
with open('var_function-call-3527882799012816558.json', 'r') as f:
    patents = json.load(f)

# Process Data
data = []
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for p in patents:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract Year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique Level 5 codes for this patent
    # Using 4-char prefix as proxy for level 5 as established
    p_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                p_codes.add(prefix)
    
    for code in p_codes:
        data.append({'year': year, 'code': code})

df = pd.DataFrame(data)

# Aggregate counts
df_counts = df.groupby(['code', 'year']).size().reset_index(name='count')

# Calculate EMA
results = []
codes = df_counts['code'].unique()

for code in codes:
    sub = df_counts[df_counts['code'] == code].sort_values('year')
    min_year = sub['year'].min()
    max_year = sub['year'].max()
    
    # Reindex to include all years (fill 0)
    full_idx = pd.RangeIndex(start=min_year, stop=2023, step=1) # Up to 2022
    # Wait, query implies checking if best year IS 2022. So we must have data/EMA up to 2022.
    # What if max_year < 2022? We should extend to 2022 with 0 counts to see if EMA drops.
    # What if max_year > 2022? We should check up to max_year.
    # Let's extend to max(2022, max_year).
    
    end_year = max(2022, max_year)
    full_idx = pd.RangeIndex(start=min_year, stop=end_year + 1, step=1)
    
    sub = sub.set_index('year').reindex(full_idx, fill_value=0).rename_axis('year').reset_index()
    
    # Calculate EMA
    # alpha = 0.2
    sub['ema'] = sub['count'].ewm(alpha=0.2, adjust=False).mean()
    
    # Find Best Year
    best_year_idx = sub['ema'].idxmax()
    best_year = sub.loc[best_year_idx, 'year']
    
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11333700863713924145': 'file_storage/function-call-11333700863713924145.json', 'var_function-call-11333700863713924824': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-5635872423012651359': 'file_storage/function-call-5635872423012651359.json', 'var_function-call-4292733715298409796': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-18005061453345551091': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'A41D', 'level': '5.0', 'titleFull': 'OUTERWEAR; PROTECTIVE GARMENTS; ACCESSORIES'}], 'var_function-call-5617066391461986581': [], 'var_function-call-2737902941994605580': [{'count(*)': '277813'}], 'var_function-call-3527882799012816558': 'file_storage/function-call-3527882799012816558.json'}

exec(code, env_args)
