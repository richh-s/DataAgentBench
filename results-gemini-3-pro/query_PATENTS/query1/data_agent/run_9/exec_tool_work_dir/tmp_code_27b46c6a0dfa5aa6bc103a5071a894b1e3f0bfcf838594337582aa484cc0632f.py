code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-4209797250346039568'], 'r') as f:
    l5_data = json.load(f)
    # l5_data is a list of dicts: [{"symbol": "A01H"}, ...]
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patents
with open(locals()['var_function-call-333056328050436468'], 'r') as f:
    patents = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Aggregation: Counts per (Code, Year)
counts = {} # (code, year) -> count

for p in patents:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Extract CPC codes
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Identify unique Level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            l5 = code[:4]
            if l5 in level5_codes:
                patent_codes.add(l5)
    
    # Increment counts
    for code in patent_codes:
        key = (code, year)
        counts[key] = counts.get(key, 0) + 1

# Convert to DataFrame
data = []
for (code, year), count in counts.items():
    data.append({'code': code, 'year': year, 'count': count})

if not data:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(data)

    # Global min and max year
    min_year = df['year'].min()
    max_year = df['year'].max()

    # We need to calculate EMA for each code over the full range of years
    # to handle years with 0 filings correctly.
    # However, EMA starting point matters. 
    # Standard practice: Start EMA at the first year the code appears? 
    # Or start at global min_year?
    # Usually, if a technology didn't exist, its EMA is 0.
    # I'll create a DataFrame with all years for each code.
    
    codes = df['code'].unique()
    years = range(min_year, max_year + 1)
    
    # Create MultiIndex (code, year)
    idx = pd.MultiIndex.from_product([codes, years], names=['code', 'year'])
    
    # Reindex and fill missing with 0
    df_full = df.set_index(['code', 'year']).reindex(idx, fill_value=0).reset_index()
    
    # Calculate EMA
    # Group by code and sort by year
    # Apply EMA
    # Pandas ewm: alpha=0.2, adjust=False (recursive formula: y_t = alpha*x_t + (1-alpha)*y_{t-1})
    
    def calc_ema(group):
        # We need to ensure it's sorted by year
        g = group.sort_values('year')
        g['ema'] = g['count'].ewm(alpha=0.2, adjust=False).mean()
        return g

    df_ema = df_full.groupby('code', group_keys=False).apply(calc_ema)
    
    # Find Best Year
    # For each code, find the year with max EMA
    # If multiple years have same max, take the latest? Or all?
    # "whose best year is 2022"
    
    # Get rows with max EMA per code
    # idxmax() returns index of first occurrence of maximum.
    # We want to check if 2022 is the best year.
    # Let's get the max EMA value for each code, then check if 2022 has that value.
    
    max_ema = df_ema.groupby('code')['ema'].max().reset_index().rename(columns={'ema': 'max_ema'})
    df_merged = pd.merge(df_ema, max_ema, on='code')
    
    # Filter where ema == max_ema
    best_years = df_merged[df_merged['ema'] == df_merged['max_ema']]
    
    # Filter for year == 2022
    target_codes = best_years[best_years['year'] == 2022]['code'].unique().tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-3066016024932945511': ['cpc_definition'], 'var_function-call-3066016024932944250': ['publicationinfo'], 'var_function-call-12953216539531807597': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-12953216539531806840': 'file_storage/function-call-12953216539531806840.json', 'var_function-call-3195997769448221607': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-14113235830138341004': [], 'var_function-call-239168183394975619': [{'count(*)': '277813'}], 'var_function-call-4209797250346039568': 'file_storage/function-call-4209797250346039568.json', 'var_function-call-333056328050436468': 'file_storage/function-call-333056328050436468.json'}

exec(code, env_args)
