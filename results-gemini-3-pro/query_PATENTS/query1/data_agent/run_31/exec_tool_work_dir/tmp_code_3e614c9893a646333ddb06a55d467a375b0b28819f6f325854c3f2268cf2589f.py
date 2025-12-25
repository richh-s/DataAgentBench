code = """import json
import pandas as pd
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-8605716924548816221'], 'r') as f:
    l5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-15653579714414806466'], 'r') as f:
    patent_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits starting with 19 or 20
    # Removed \b to be safer, assume 4 digits in range is year
    match = re.search(r'(19|20)\d{2}', str(date_str))
    if match:
        return int(match.group(0))
    return None

# Process data
counts = {} # Key: (cpc_code, year), Value: count
years_seen = set()

for entry in patent_data:
    year = extract_year(entry.get('filing_date'))
    if year is None:
        continue
    years_seen.add(year)
    
    cpc_field = entry.get('cpc')
    if not cpc_field:
        continue
    
    try:
        cpc_list = json.loads(cpc_field)
    except:
        continue
        
    # Extract unique Level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    for pc in patent_codes:
        key = (pc, year)
        counts[key] = counts.get(key, 0) + 1

if not counts:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    # Convert to DataFrame
    df = pd.DataFrame([{'cpc': k[0], 'year': k[1], 'count': v} for k, v in counts.items()])
    
    # Fill missing years
    # We should cover the range of years present in the data
    min_year = df['year'].min()
    max_year = df['year'].max()
    all_years = range(min_year, max_year + 1)
    
    # Pivot: Index=Year, Columns=CPC
    df_pivot = df.pivot(index='year', columns='cpc', values='count').reindex(all_years).fillna(0)
    
    # Calculate EMA
    # alpha=0.2
    ema_df = df_pivot.ewm(alpha=0.2, adjust=False).mean()
    
    # Find best year for each CPC
    # idxmax returns the index (year) of the max value
    best_years = ema_df.idxmax()
    
    # Filter where best year is 2022
    target_cpcs = best_years[best_years == 2022].index.tolist()
    
    print('__RESULT__:')
    print(json.dumps(target_cpcs))"""

env_args = {'var_function-call-8605716924548816221': 'file_storage/function-call-8605716924548816221.json', 'var_function-call-3390649654093091550': [{'COUNT(*)': '277813'}], 'var_function-call-15653579714414806466': 'file_storage/function-call-15653579714414806466.json', 'var_function-call-3948899147405893627': [], 'var_function-call-6555282486067486608': {'sample_years': [], 'min_year': None, 'max_year': None, 'codes_found_sample': ['F41H', 'H02J', 'D06B', 'B25D', 'Y02E', 'F28D', 'G05D', 'G11B', 'F41C', 'G04F'], 'level5_sample': ['F41H', 'H02J', 'D06B', 'B25D', 'F22D', 'Y02E', 'F28D', 'C08H', 'G05D', 'G11B']}, 'var_function-call-17022073147038242497': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-17189268383737464155': [None, None, None], 'var_function-call-11122473221756250122': ["'dated 5th March 2019'", "'March the 18th, 2019'"]}

exec(code, env_args)
