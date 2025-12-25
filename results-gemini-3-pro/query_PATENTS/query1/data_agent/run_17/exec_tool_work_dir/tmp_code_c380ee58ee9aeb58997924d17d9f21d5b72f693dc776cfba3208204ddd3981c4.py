code = """import json
import pandas as pd
import re

# Load Level 5 CPC Codes
with open(locals()['var_function-call-15598239778960788131'], 'r') as f:
    cpc_def_data = json.load(f)
level5_codes = set(item['symbol'] for item in cpc_def_data)

# Load Publication Data
with open(locals()['var_function-call-2589434273534193107'], 'r') as f:
    pub_data = json.load(f)

# Process Data
counts = {} # (year, code) -> count

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in pub_data:
    # Parse Year
    f_date = row.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    cpc_str = row.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract codes and count
    # We only care about unique codes per patent? Or total occurrences?
    # Usually patent filings count the patent once per code.
    # So if a patent has C01B twice, it counts once for C01B?
    # Usually yes. "patent filings".
    
    seen_in_patent = set()
    for item in cpc_list:
        full_code = item.get('code', '')
        if len(full_code) >= 4:
            prefix = full_code[:4]
            if prefix in level5_codes:
                if prefix not in seen_in_patent:
                    seen_in_patent.add(prefix)
                    counts[(year, prefix)] = counts.get((year, prefix), 0) + 1

# Convert to DataFrame
data = [{'year': k[0], 'code': k[1], 'count': v} for k, v in counts.items()]
df = pd.DataFrame(data)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Pivot
    df_pivot = df.pivot(index='year', columns='code', values='count').fillna(0)
    
    # Fill missing years in the range
    min_year = df_pivot.index.min()
    max_year = df_pivot.index.max()
    full_range = range(min_year, max_year + 1)
    df_pivot = df_pivot.reindex(full_range, fill_value=0)
    
    # Calculate EMA
    # smoothing factor alpha = 0.2
    # ewm(alpha=0.2, adjust=False) matches EMA formula: y_t = alpha * x_t + (1-alpha) * y_{t-1}
    # adjust=False is important for the recursive definition starting with mean of first periods or similar?
    # Standard EMA usually assumes infinite history or starts with first value.
    # Pandas ewm(alpha=0.2, adjust=False) uses x_0 for y_0.
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year
    best_years = ema_df.idxmax()
    
    # Filter for 2022
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-15598239778960788131': 'file_storage/function-call-15598239778960788131.json', 'var_function-call-15598239778960788336': [{'count(*)': '277813'}], 'var_function-call-2589434273534193107': 'file_storage/function-call-2589434273534193107.json'}

exec(code, env_args)
