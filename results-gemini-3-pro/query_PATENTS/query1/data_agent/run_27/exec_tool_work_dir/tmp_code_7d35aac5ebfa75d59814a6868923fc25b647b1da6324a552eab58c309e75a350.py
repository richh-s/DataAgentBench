code = """import json
import re
import pandas as pd

# Load Level 5 codes
with open(locals()['var_function-call-12790738948294253475'], 'r') as f:
    level5_data = json.load(f)
valid_level5_codes = set(item['symbol'] for item in level5_data)

# Load Publication data
with open(locals()['var_function-call-2189748292734170066'], 'r') as f:
    pub_data = json.load(f)

counts = {} # year -> code -> count

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for record in pub_data:
    date_str = record.get('filing_date', '')
    if not date_str:
        continue
        
    # Extract year
    matches = year_pattern.findall(date_str)
    if not matches:
        continue
    # Assuming the last match is the year if multiple, but usually one. 
    # Or just picking the first one that looks like a year.
    # The regex \b(19|20)\d{2}\b matches the full year string.
    # The findall returns the group if grouped, or the match.
    # Wait, (19|20) is a capturing group. findall will return just "19" or "20".
    # I should use non-capturing group or search differently.
    
    # Better regex logic
    full_matches = re.findall(r'\b(?:19|20)\d{2}\b', date_str)
    if not full_matches:
        continue
    year = int(full_matches[0]) # Take the first valid year found.

    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract unique valid level 5 codes for this patent
    # A patent can have multiple codes. Should we count each?
    # Usually "patent filings" implies counting the patent once per category.
    # So if a patent has C01B and H01M, it counts for both.
    # If it has multiple C01B codes (e.g. C01B 33/00 and C01B 35/00), it counts once for C01B.
    
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_level5_codes:
                patent_codes.add(subclass)
    
    for code in patent_codes:
        if year not in counts:
            counts[year] = {}
        counts[year][code] = counts[year].get(code, 0) + 1

# Convert counts to DataFrame for easier handling
# Rows: Years, Cols: Codes
# But it's sparse.
# Let's pivot: DataFrame with index=Year, columns=Codes
data_list = []
for year, code_counts in counts.items():
    for code, count in code_counts.items():
        data_list.append({'Year': year, 'Code': code, 'Count': count})

df = pd.DataFrame(data_list)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Pivot to fill missing years with 0
    df_pivot = df.pivot(index='Year', columns='Code', values='Count').fillna(0).sort_index()
    
    # Ensure all years in range are present?
    # The prompt implies "each year". Continuous time series is best for EMA.
    min_year = df_pivot.index.min()
    max_year = df_pivot.index.max()
    full_range = range(min_year, max_year + 1)
    df_pivot = df_pivot.reindex(full_range, fill_value=0)
    
    # Calculate EMA
    alpha = 0.2
    # ewm(alpha=0.2, adjust=False) implements: y_t = alpha * x_t + (1 - alpha) * y_{t-1}
    # adjust=False is important for the recursive definition.
    ema_df = df_pivot.ewm(alpha=alpha, adjust=False).mean()
    
    # Find best year for each code
    best_years = ema_df.idxmax()
    
    # Filter for best year == 2022
    target_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(target_codes))"""

env_args = {'var_function-call-10820619102234232879': 'file_storage/function-call-10820619102234232879.json', 'var_function-call-13188904574193367056': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-13958987405040638588': [{'level': '2.0', 'sample_symbol': 'A'}, {'level': '4.0', 'sample_symbol': 'A01'}, {'level': '5.0', 'sample_symbol': 'A01B'}, {'level': '7.0', 'sample_symbol': 'A01B1/00'}, {'level': '8.0', 'sample_symbol': 'A01B1/02'}, {'level': '9.0', 'sample_symbol': 'A01B1/022'}, {'level': '10.0', 'sample_symbol': 'A01B1/225'}, {'level': '11.0', 'sample_symbol': 'A01B3/421'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137'}], 'var_function-call-12790738948294253475': 'file_storage/function-call-12790738948294253475.json', 'var_function-call-17223264580135065158': [{'count(*)': '277813'}], 'var_function-call-2189748292734170066': 'file_storage/function-call-2189748292734170066.json'}

exec(code, env_args)
