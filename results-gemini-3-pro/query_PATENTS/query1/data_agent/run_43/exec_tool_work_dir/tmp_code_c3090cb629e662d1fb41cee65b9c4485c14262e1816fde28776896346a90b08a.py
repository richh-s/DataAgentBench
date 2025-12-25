code = """import json
import pandas as pd
import re

# Load Level 5 symbols
with open(locals()['var_function-call-14887408148356226124'], 'r') as f:
    level5_data = json.load(f)

# Extract symbols into a set for fast lookup
level5_symbols = set(item['symbol'] for item in level5_data)

# Load publication data
with open(locals()['var_function-call-14887408148356225641'], 'r') as f:
    pub_data = json.load(f)

# Process publication data
cpc_filings = []

for entry in pub_data:
    date_str = entry.get('filing_date', '')
    cpc_json = entry.get('cpc', '[]')
    
    # Extract Year
    # Look for 4 digits in the range 1900-2024
    match = re.search(r'(19|20)\d{2}', date_str)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract codes
    # We need to map full code (e.g. C01B33/00) to Level 5 symbol (e.g. C01B)
    # The Level 5 symbols seem to be 4 characters.
    # Let's extract unique 4-char prefixes from the cpc codes in this patent
    # and filter by level5_symbols
    
    codes_in_patent = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                codes_in_patent.add(prefix)
    
    for code in codes_in_patent:
        cpc_filings.append({'year': year, 'cpc': code})

# Create DataFrame
df = pd.DataFrame(cpc_filings)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Count filings per CPC per Year
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    # We need a continuous year range for EMA calculation to handle years with 0 filings
    # Although EMA normally updates only on observations, "moving average each year" implies a time series.
    # If a year has 0 filings, the count is 0, and EMA decays.
    
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = pd.DataFrame({'year': range(min_year, max_year + 1)})
    
    results = []
    
    # Unique CPCs
    unique_cpcs = counts['cpc'].unique()
    
    alpha = 0.2
    
    for cpc in unique_cpcs:
        # Get data for this CPC
        cpc_data = counts[counts['cpc'] == cpc].merge(all_years, on='year', how='right').fillna({'count': 0, 'cpc': cpc}).sort_values('year')
        
        # Calculate EMA
        # Pandas ewm: adjust=False means: y_t = (1-alpha)*y_{t-1} + alpha*x_t
        # This matches the formula EMA_t = alpha * Count_t + (1 - alpha) * EMA_{t-1}
        # We need to specify the initial value. Pandas ewm by default uses the first value as the initial EMA?
        # "When adjust=False, weighted averages are calculated recursively as: y0=x0; yt=(1-alpha)y_{t-1} + alpha x_t"
        # This seems correct for standard EMA.
        
        cpc_data['ema'] = cpc_data['count'].ewm(alpha=alpha, adjust=False).mean()
        
        # Find best year
        best_year_row = cpc_data.loc[cpc_data['ema'].idxmax()]
        best_year = int(best_year_row['year'])
        max_ema = best_year_row['ema']
        
        if best_year == 2022:
            results.append(cpc)
            
    # Sort results for consistency
    results.sort()
    
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-1774117398355901906': ['publicationinfo'], 'var_function-call-1774117398355902325': ['cpc_definition'], 'var_function-call-14887408148356226124': 'file_storage/function-call-14887408148356226124.json', 'var_function-call-14887408148356225641': 'file_storage/function-call-14887408148356225641.json'}

exec(code, env_args)
