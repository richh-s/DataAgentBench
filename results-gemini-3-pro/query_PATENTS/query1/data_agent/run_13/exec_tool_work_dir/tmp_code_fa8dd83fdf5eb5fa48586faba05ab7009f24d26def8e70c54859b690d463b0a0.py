code = """import json
import pandas as pd
import re

# Load the data
with open(locals()['var_function-call-10323089701006148132'], 'r') as f:
    data = json.load(f)

# Extract year and CPC codes
records = []
for entry in data:
    f_date = entry.get('filing_date', '')
    cpc_json = entry.get('cpc', '[]')
    
    # Extract year
    # Look for 4 digits starting with 19 or 20
    match = re.search(r'(19|20)\d{2}', f_date)
    if match:
        year = int(match.group(0))
    else:
        continue # Skip if no valid year found
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_json)
        # Extract codes
        codes = [item['code'] for item in cpc_list if 'code' in item]
        for code in codes:
            records.append({'year': year, 'cpc': code})
    except:
        continue

df = pd.DataFrame(records)

# Count per year per CPC
if not df.empty:
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # Pivot to have years as columns or iterate
    # We need to calculate EMA over the full range of years for each CPC
    
    # Get range of years
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Pivot
    pivot_df = counts.pivot(index='cpc', columns='year', values='count').fillna(0)
    
    # Reindex to include all years in range (if gaps exist)
    pivot_df = pivot_df.reindex(columns=all_years, fill_value=0)
    
    # Calculate EMA
    # Formula: EMA_t = alpha * count_t + (1-alpha) * EMA_{t-1}
    # Initial EMA: The first value (or 0?)
    # "exponential moving average of patent filings each year"
    # Typically, pandas ewm can handle this. 
    # pandas.DataFrame.ewm(alpha=0.2, adjust=False).mean()
    # adjust=False corresponds to: y_t = (1-alpha)*y_{t-1} + alpha*x_t
    # which matches the standard EMA formula often used.
    
    ema_df = pivot_df.T.ewm(alpha=0.2, adjust=False).mean().T
    
    # Find best year
    best_years = ema_df.idxmax(axis=1)
    
    # Filter for best year == 2022
    target_cpc = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_cpc))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-15599228345113843070': 'file_storage/function-call-15599228345113843070.json', 'var_function-call-10323089701006148132': 'file_storage/function-call-10323089701006148132.json'}

exec(code, env_args)
