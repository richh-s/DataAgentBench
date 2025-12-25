code = """import json
import re
import pandas as pd

# Load level 5 symbols
with open(locals()['var_function-call-3646825604830857458'], 'r') as f:
    l5_data = json.load(f)
level5_set = set(item['symbol'] for item in l5_data)

# Load publication info
with open(locals()['var_function-call-7542188176596272141'], 'r') as f:
    pub_data = json.load(f)

# Process data
records = []
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for entry in pub_data:
    f_date = entry.get('filing_date')
    cpc_str = entry.get('cpc')
    
    if not f_date or not cpc_str:
        continue
        
    # Extract Year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract codes
    found_codes = set()
    for c in cpc_list:
        code_str = c.get('code', '')
        if len(code_str) >= 4:
            sub = code_str[:4]
            if sub in level5_set:
                found_codes.add(sub)
    
    for code in found_codes:
        records.append({'Year': year, 'Code': code})

# Create DataFrame
if not records:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(records)
    # Count per Year-Code
    counts = df.groupby(['Year', 'Code']).size().reset_index(name='Count')
    
    # Pivot
    pivot_df = counts.pivot(index='Year', columns='Code', values='Count').fillna(0)
    
    # Ensure continuous years?
    # Usually pivot includes all years present in data.
    # If there are gaps in years (e.g. 2010, 2012), pivot index will skip 2011? 
    # Yes, if no data for 2011 at all.
    # It's better to reindex to full range.
    all_years = range(pivot_df.index.min(), pivot_df.index.max() + 1)
    pivot_df = pivot_df.reindex(all_years, fill_value=0)
    
    # Calculate EMA
    # alpha = 0.2, adjust=False
    ema_df = pivot_df.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year
    best_years = ema_df.idxmax()
    
    # Filter for 2022
    # Check if 2022 is in the index?
    # If max year < 2022, then it can't be 2022.
    # If max year > 2022, it's possible.
    
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-18438039698466275985': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-11425610840667422492': 'file_storage/function-call-11425610840667422492.json', 'var_function-call-15261515319027993325': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-3988956739634739314': [{'symbol': 'A01H', 'level': '5.0'}], 'var_function-call-16646390810544569620': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3646825604830857458': 'file_storage/function-call-3646825604830857458.json', 'var_function-call-7247946529193589936': [{'COUNT(*)': '277813'}], 'var_function-call-7542188176596272141': 'file_storage/function-call-7542188176596272141.json'}

exec(code, env_args)
