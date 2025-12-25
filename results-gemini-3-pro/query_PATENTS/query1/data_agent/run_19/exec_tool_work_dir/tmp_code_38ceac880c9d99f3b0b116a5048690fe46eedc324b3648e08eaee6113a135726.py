code = """import json
import re
import pandas as pd

# Load level 5 symbols
# var_function-call-12888596123862889220 contains the file path for level 5 symbols
with open(locals()['var_function-call-12888596123862889220'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

# Load patent aggregation data
# var_function-call-7488506461808161305 contains the file path
with open(locals()['var_function-call-7488506461808161305'], 'r') as f:
    patent_data = json.load(f)

# Process data
data = []
for entry in patent_data:
    cpc = entry['cpc4']
    date_str = entry['filing_date']
    cnt = int(entry['cnt'])
    
    if cpc not in level5_symbols:
        continue
        
    # Parse year
    matches = re.findall(r'\b(19\d{2}|20\d{2})\b', date_str)
    if matches:
        # Take the first valid year match
        year = int(matches[0])
        data.append({'cpc': cpc, 'year': year, 'cnt': cnt})

df = pd.DataFrame(data)

if df.empty:
    print("__RESULT__:")
    print("[]")
else:
    # Aggregate by cpc and year (summing counts if multiple entries for same year/cpc)
    df_agg = df.groupby(['cpc', 'year'])['cnt'].sum().reset_index()

    # Define global year range
    min_year = df_agg['year'].min()
    max_year = df_agg['year'].max()
    all_years = list(range(min_year, max_year + 1))
    
    # Create a MultiIndex for all combinations of cpc and year is too big?
    # No, just iterate per CPC and reindex.
    
    results = []
    
    for cpc, group in df_agg.groupby('cpc'):
        # Set index to year
        group = group.set_index('year')
        # Reindex to fill missing years with 0
        # We only care about the trend, so we can probably start from the first year the CPC appears?
        # Or global? If we want to compare "best year", global vs local start matters.
        # If we use local start (first year of CPC), the first value is initial_count.
        # If we use global start (filling 0s from min_year), the EMA ramps up.
        # Let's use global range to be safe and consistent across all CPCs.
        
        group_full = group.reindex(all_years, fill_value=0)
        
        # EMA calculation
        # Pandas ewm(alpha=0.2, adjust=False) uses the recursive formula:
        # y_t = (1-alpha)*y_{t-1} + alpha*x_t
        # Note: pandas uses alpha * x_t + (1 - alpha) * y_{t-1}
        
        group_full['ema'] = group_full['cnt'].ewm(alpha=0.2, adjust=False).mean()
        
        # Find best year
        best_year = group_full['ema'].idxmax()
        # Ensure best_year is the index (year)
        
        results.append({'cpc': cpc, 'best_year': best_year})

    # Filter for best_year == 2022
    final_cpcs = [r['cpc'] for r in results if r['best_year'] == 2022]
    
    print("__RESULT__:")
    print(json.dumps(final_cpcs))"""

env_args = {'var_function-call-17580900439577257718': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-17580900439577255993': 'file_storage/function-call-17580900439577255993.json', 'var_function-call-11879754550989831961': [{'level': '2.0', 'example_symbol': 'A'}, {'level': '4.0', 'example_symbol': 'A01'}, {'level': '5.0', 'example_symbol': 'A01B'}, {'level': '7.0', 'example_symbol': 'A01B1/00'}, {'level': '8.0', 'example_symbol': 'A01B1/02'}, {'level': '9.0', 'example_symbol': 'A01B1/022'}, {'level': '10.0', 'example_symbol': 'A01B1/225'}, {'level': '11.0', 'example_symbol': 'A01B3/421'}, {'level': '12.0', 'example_symbol': 'A01B3/4215'}, {'level': '13.0', 'example_symbol': 'A01D2034/6843'}, {'level': '14.0', 'example_symbol': 'A01D2034/6825'}, {'level': '15.0', 'example_symbol': 'A47J31/4446'}, {'level': '16.0', 'example_symbol': 'A61B17/7028'}, {'level': '17.0', 'example_symbol': 'A61K47/6823'}, {'level': '18.0', 'example_symbol': 'G01N2333/96444'}, {'level': '19.0', 'example_symbol': 'H01L21/32137'}], 'var_function-call-10894433169934078126': [{'len': '4', 'cnt': '677'}], 'var_function-call-15581526158434737241': [{'cnt': '277813'}], 'var_function-call-10805669693324454303': [{'cpc_code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'cpc_code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'cpc_code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'cpc_code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'cpc_code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12888596123862889220': 'file_storage/function-call-12888596123862889220.json', 'var_function-call-4217533507504690285': [{'filing_date': 'dated 5th March 2019', 'year': '2019'}, {'filing_date': 'March the 18th, 2019', 'year': '2019'}, {'filing_date': '29th March 2019', 'year': '2019'}, {'filing_date': 'on March 29th, 2019', 'year': '2019'}, {'filing_date': '2nd April 2019', 'year': '2019'}, {'filing_date': 'on April 8th, 2019', 'year': '2019'}, {'filing_date': '15th April 2019', 'year': '2019'}, {'filing_date': 'April 19th, 2019', 'year': '2019'}, {'filing_date': '2019, April 24th', 'year': '24th'}, {'filing_date': 'April 26th, 2019', 'year': '2019'}], 'var_function-call-7488506461808161305': 'file_storage/function-call-7488506461808161305.json'}

exec(code, env_args)
