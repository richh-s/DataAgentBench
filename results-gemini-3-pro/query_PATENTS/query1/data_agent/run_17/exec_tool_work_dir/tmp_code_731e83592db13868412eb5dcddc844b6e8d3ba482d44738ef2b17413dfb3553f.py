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

counts = {} # (year, code) -> count
year_pattern = re.compile(r'\d{4}')

for row in pub_data:
    # Parse Year
    f_date = row.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(str(f_date))
    if not match:
        continue
    year = int(match.group(0))
    
    if year < 1900 or year > 2025:
        continue

    # Parse CPC
    cpc_str = row.get('cpc', '')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
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
if not counts:
    print("__RESULT__:")
    print("[]")
else:
    data = [{'year': k[0], 'code': k[1], 'count': v} for k, v in counts.items()]
    df = pd.DataFrame(data)
    
    # Pivot
    df_pivot = df.pivot(index='year', columns='code', values='count').fillna(0)
    
    # Fill missing years in the range
    min_year = df_pivot.index.min()
    max_year = df_pivot.index.max()
    full_range = range(min_year, max_year + 1)
    df_pivot = df_pivot.reindex(full_range, fill_value=0)
    
    # Calculate EMA
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year
    best_years = ema_df.idxmax()
    
    # Filter for 2022
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-15598239778960788131': 'file_storage/function-call-15598239778960788131.json', 'var_function-call-15598239778960788336': [{'count(*)': '277813'}], 'var_function-call-2589434273534193107': 'file_storage/function-call-2589434273534193107.json', 'var_function-call-6086116679698044266': [], 'var_function-call-15912156190639610316': {'level5_sample': ['F16J', 'F16P', 'F16D', 'F16S', 'F16K', 'F16L', 'F16H', 'F16C', 'F16F', 'F16N'], 'total_level5': 677, 'years_found': [], 'sample_cpcs': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10'], 'matches_in_sample': 2648}, 'var_function-call-3896557571543607071': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019']}

exec(code, env_args)
