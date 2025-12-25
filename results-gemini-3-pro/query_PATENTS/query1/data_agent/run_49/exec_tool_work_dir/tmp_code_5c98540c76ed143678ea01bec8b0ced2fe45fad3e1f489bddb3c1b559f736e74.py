code = """import json
import re
import pandas as pd
import numpy as np

# Get file paths
l5_file = locals()['var_function-call-5635872423012651359']
patents_file = locals()['var_function-call-3527882799012816558']

# Load Level 5 Codes
with open(l5_file, 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load Patent Data
with open(patents_file, 'r') as f:
    patents = json.load(f)

# Process Data
data = []
year_pattern = re.compile(r'\d{4}')

for p in patents:
    f_date = p.get('filing_date', '')
    if not f_date:
        continue
    
    # Extract Year
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    if year < 1900 or year > 2024:
        continue
    
    # Extract CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique Level 5 codes for this patent
    p_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                p_codes.add(prefix)
    
    for code in p_codes:
        data.append({'year': year, 'code': code})

if not data:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(data)

    # Aggregate counts
    df_counts = df.groupby(['code', 'year']).size().reset_index(name='count')

    # Calculate EMA and find best year
    results = []
    codes = df_counts['code'].unique()
    
    # Debug: print years range
    # print("Years range:", df_counts['year'].min(), df_counts['year'].max())

    for code in codes:
        sub = df_counts[df_counts['code'] == code].sort_values('year')
        min_year = sub['year'].min()
        max_year = sub['year'].max()
        
        # We need to cover up to 2022 to verify if it's the best year.
        # If max_year of data is < 2022, we must extend with zeros.
        # If max_year > 2022, we keep data up to max_year but only check if max EMA is in 2022?
        # The query says "whose best year is 2022".
        # This implies comparing 2022 against all other years.
        
        # Construct timeline
        end_year = max(2022, max_year)
        full_idx = pd.RangeIndex(start=min_year, stop=end_year + 1, step=1)
        
        sub = sub.set_index('year').reindex(full_idx, fill_value=0).rename_axis('year').reset_index()
        
        # Calculate EMA
        # alpha = 0.2
        # Initialization: First value is the count itself?
        # Pandas ewm(adjust=False) uses y_0 = x_0. This is standard.
        sub['ema'] = sub['count'].ewm(alpha=0.2, adjust=False).mean()
        
        # Find Best Year
        best_year_idx = sub['ema'].idxmax()
        best_year = sub.loc[best_year_idx, 'year']
        
        if best_year == 2022:
            results.append(code)

    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-11333700863713924145': 'file_storage/function-call-11333700863713924145.json', 'var_function-call-11333700863713924824': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-5635872423012651359': 'file_storage/function-call-5635872423012651359.json', 'var_function-call-4292733715298409796': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-18005061453345551091': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'A41D', 'level': '5.0', 'titleFull': 'OUTERWEAR; PROTECTIVE GARMENTS; ACCESSORIES'}], 'var_function-call-5617066391461986581': [], 'var_function-call-2737902941994605580': [{'count(*)': '277813'}], 'var_function-call-3527882799012816558': 'file_storage/function-call-3527882799012816558.json', 'var_function-call-17578414695543921447': [], 'var_function-call-16013171469503040606': {'total_patents': 277813, 'parsed_years_count': 0, 'min_year': None, 'max_year': None, 'patents_with_level5_match': 277813, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019']}, 'var_function-call-2082607280903482232': {'dated 5th March 2019': 'No match', 'March the 18th, 2019': 'No match', '29th March 2019': 'No match', 'on March 29th, 2019': 'No match', '2nd April 2019': 'No match', 'on April 8th, 2019': 'No match', '15th April 2019': 'No match', 'April 19th, 2019': 'No match', '2019, April 24th': 'No match', 'April 26th, 2019': 'No match'}, 'var_function-call-12791687787020294757': {'dated 5th March 2019': '2019', 'March the 18th, 2019': '2019'}}

exec(code, env_args)
