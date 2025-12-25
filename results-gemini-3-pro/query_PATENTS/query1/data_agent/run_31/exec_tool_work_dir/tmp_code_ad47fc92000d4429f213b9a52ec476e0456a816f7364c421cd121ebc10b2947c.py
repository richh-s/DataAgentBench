code = """import json
import pandas as pd
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-8605716924548816221'], 'r') as f:
    l5_data = json.load(f)
    # Extract symbols
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-15653579714414806466'], 'r') as f:
    patent_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits starting with 19 or 20
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

# Process data
counts = {} # Key: (cpc_code, year), Value: count

for entry in patent_data:
    year = extract_year(entry.get('filing_date'))
    if year is None:
        continue
    
    cpc_field = entry.get('cpc')
    if not cpc_field:
        continue
    
    try:
        cpc_list = json.loads(cpc_field)
    except:
        continue
        
    # Extract unique Level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Assuming Level 5 codes are 4 chars (Subclass), e.g., "A01B"
        # We check if the prefix of the code matches any Level 5 code.
        # Since Level 5 codes are 4 chars, we take the first 4 chars.
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    for pc in patent_codes:
        key = (pc, year)
        counts[key] = counts.get(key, 0) + 1

# Convert to DataFrame
df = pd.DataFrame([{'cpc': k[0], 'year': k[1], 'count': v} for k, v in counts.items()])

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Fill missing years
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Pivot to have years as index and cpc as columns
    df_pivot = df.pivot(index='year', columns='cpc', values='count').reindex(all_years).fillna(0)
    
    # Calculate EMA
    # Formula: EMA_t = alpha * x_t + (1-alpha) * EMA_{t-1}
    # Pandas ewm function: adjust=False corresponds to the recursive formula
    # alpha = 0.2
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year for each CPC
    best_years = ema_df.idxmax()
    
    # Filter for 2022
    target_cpcs = best_years[best_years == 2022].index.tolist()
    
    print('__RESULT__:')
    print(json.dumps(target_cpcs))"""

env_args = {'var_function-call-8605716924548816221': 'file_storage/function-call-8605716924548816221.json', 'var_function-call-3390649654093091550': [{'COUNT(*)': '277813'}], 'var_function-call-15653579714414806466': 'file_storage/function-call-15653579714414806466.json'}

exec(code, env_args)
