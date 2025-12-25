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
year_pattern = re.compile(r'(19|20)\d{2}')

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

if not records:
    print("__RESULT__:")
    print("[]")
else:
    df = pd.DataFrame(records)
    
    # Count per Year-Code
    counts = df.groupby(['Year', 'Code']).size().reset_index(name='Count')
    
    # Pivot
    pivot_df = counts.pivot(index='Year', columns='Code', values='Count').fillna(0)
    
    # Reindex to full year range to ensure EMA continuity
    all_years = range(pivot_df.index.min(), pivot_df.index.max() + 1)
    pivot_df = pivot_df.reindex(all_years, fill_value=0)
    
    # Calculate EMA
    ema_df = pivot_df.ewm(alpha=0.2, adjust=False).mean()
    
    # Find Best Year
    best_years = ema_df.idxmax()
    
    # Filter where Best Year == 2022
    result_codes = best_years[best_years == 2022].index.tolist()
    
    print("__RESULT__:")
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-18438039698466275985': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-11425610840667422492': 'file_storage/function-call-11425610840667422492.json', 'var_function-call-15261515319027993325': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-3988956739634739314': [{'symbol': 'A01H', 'level': '5.0'}], 'var_function-call-16646390810544569620': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3646825604830857458': 'file_storage/function-call-3646825604830857458.json', 'var_function-call-7247946529193589936': [{'COUNT(*)': '277813'}], 'var_function-call-7542188176596272141': 'file_storage/function-call-7542188176596272141.json', 'var_function-call-2924045124924059341': [], 'var_function-call-14784814548662281515': {'error': 'No years found'}, 'var_function-call-7127365575876393656': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-2295869064512019575': [{'date': 'dated 5th March 2019', 'match': None}, {'date': 'March the 18th, 2019', 'match': None}, {'date': '29th March 2019', 'match': None}, {'date': 'on March 29th, 2019', 'match': None}, {'date': '2nd April 2019', 'match': None}, {'date': 'on April 8th, 2019', 'match': None}, {'date': '15th April 2019', 'match': None}, {'date': 'April 19th, 2019', 'match': None}, {'date': '2019, April 24th', 'match': None}, {'date': 'April 26th, 2019', 'match': None}], 'var_function-call-15990137332791724935': [{'date': 'dated 5th March 2019', 'match': '2019'}, {'date': 'March the 18th, 2019', 'match': '2019'}, {'date': '29th March 2019', 'match': '2019'}, {'date': 'on March 29th, 2019', 'match': '2019'}, {'date': '2nd April 2019', 'match': '2019'}, {'date': 'on April 8th, 2019', 'match': '2019'}, {'date': '15th April 2019', 'match': '2019'}, {'date': 'April 19th, 2019', 'match': '2019'}, {'date': '2019, April 24th', 'match': '2019'}, {'date': 'April 26th, 2019', 'match': '2019'}], 'var_function-call-13539911581173680155': {'min': 1900, 'max': 2024}}

exec(code, env_args)
