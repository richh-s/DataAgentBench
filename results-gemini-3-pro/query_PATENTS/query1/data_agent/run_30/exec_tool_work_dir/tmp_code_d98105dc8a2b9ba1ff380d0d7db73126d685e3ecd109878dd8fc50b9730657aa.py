code = """import json
import re

# Load Level 5 symbols
with open(locals()['var_function-call-9506971857936168120'], 'r') as f:
    level5_data = json.load(f)
valid_level5 = set(item['symbol'] for item in level5_data)

# Load Publication Data
with open(locals()['var_function-call-16148835938051840028'], 'r') as f:
    pub_data = json.load(f)

# Count
cpc_counts = {}
all_years = set()
year_pattern = re.compile(r'\d{4}')

for record in pub_data:
    f_date = record.get('filing_date', '')
    if not f_date:
        continue
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    # Basic sanity check on year (e.g. 1900-2030)
    if year < 1900 or year > 2030:
        continue
    
    all_years.add(year)
    
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Identify unique valid level 5 CPCs in this patent
    record_cpcs = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_level5:
                record_cpcs.add(subclass)
            # What if the valid level 5 symbol is longer than 4 chars?
            # From previous check, they seem to be 4 chars.
            # If I want to be safe, I could iterate through valid_level5 and check startswith, but that's slow.
            # Given the preview showed 4 chars, I'll stick to that.
            
    for cpc in record_cpcs:
        if cpc not in cpc_counts:
            cpc_counts[cpc] = {}
        cpc_counts[cpc][year] = cpc_counts[cpc].get(year, 0) + 1

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year = min(all_years)
    max_year = max(all_years)
    sorted_years = sorted(list(all_years))
    
    alpha = 0.2
    target_cpcs = []
    
    for cpc, year_counts in cpc_counts.items():
        ema = 0
        best_ema = -1.0
        best_year = None
        
        # Iterate over all years in the range
        # Initialization: For the first year in the dataset, EMA = Count.
        # This is a common way to initialize if no prior history.
        
        first_y = sorted_years[0]
        count = year_counts.get(first_y, 0)
        ema = count
        
        if ema > best_ema:
            best_ema = ema
            best_year = first_y
            
        for y in sorted_years[1:]:
            count = year_counts.get(y, 0)
            ema = alpha * count + (1 - alpha) * ema
            
            # Using >= to prefer later years? Or strict >?
            # "whose best year is 2022"
            # If equal, usually keep first or last.
            # I will use strict >.
            if ema > best_ema:
                best_ema = ema
                best_year = y
        
        if best_year == 2022:
            target_cpcs.append(cpc)
            
    print("__RESULT__:")
    print(json.dumps(target_cpcs))"""

env_args = {'var_function-call-9506971857936168120': 'file_storage/function-call-9506971857936168120.json', 'var_function-call-16148835938051840028': 'file_storage/function-call-16148835938051840028.json', 'var_function-call-17364678478425837483': [], 'var_function-call-2451587056434014575': {'years': []}, 'var_function-call-941017270970426086': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-10617383023866283671': [None, None, None], 'var_function-call-7057600685381119556': ['2019', '2019', '2019']}

exec(code, env_args)
