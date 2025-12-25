code = """import json
import pandas as pd
import re

# Load level 5 symbols
with open(locals()['var_function-call-5220002852052879670'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load publication info
with open(locals()['var_function-call-3342335174744796923'], 'r') as f:
    pub_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

# Process data
records = []
for entry in pub_data:
    date_str = entry.get('filing_date')
    cpc_str = entry.get('cpc')
    
    if not date_str or not cpc_str:
        continue
        
    year = extract_year(date_str)
    if year is None:
        continue
        
    try:
        cpc_list = json.loads(cpc_str)
    except json.JSONDecodeError:
        continue
        
    # Extract unique level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Check against level 5 symbols
        # Try exact match or prefix
        # Based on previous analysis, level 5 symbols are like "A01B" (4 chars)
        # So we take the first 4 chars of the code.
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_symbols:
                patent_codes.add(subclass)
    
    for code in patent_codes:
        records.append({'year': year, 'code': code})

df = pd.DataFrame(records)

# Aggregation
if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    counts = df.groupby(['year', 'code']).size().reset_index(name='count')
    pivot = counts.pivot(index='year', columns='code', values='count').fillna(0)
    
    # Fill missing years in the range
    full_idx = range(pivot.index.min(), pivot.index.max() + 1)
    pivot = pivot.reindex(full_idx, fill_value=0)
    
    # Calculate EMA
    # alpha = 0.2
    ema = pivot.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year
    best_years = ema.idxmax()
    
    # Filter for best year == 2022
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-6966994197956776721': 'file_storage/function-call-6966994197956776721.json', 'var_function-call-6966994197956777598': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-7852690627219261662': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-14140994627699433809': [{'count(*)': '277813'}], 'var_function-call-5220002852052879670': 'file_storage/function-call-5220002852052879670.json', 'var_function-call-3342335174744796923': 'file_storage/function-call-3342335174744796923.json'}

exec(code, env_args)
