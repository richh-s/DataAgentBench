code = """import json
import re

level5_file = locals()['var_function-call-13650408886884758128']
pub_file = locals()['var_function-call-17751803970902191593']

with open(level5_file, 'r') as f:
    level5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_data)

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

year_pattern = re.compile(r'(19|20)\d{2}')

counts = {} # sym -> year -> count

for record in pub_data:
    f_date = record.get('filing_date')
    cpc_str = record.get('cpc')
    
    if not f_date or not cpc_str:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_syms = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                patent_syms.add(prefix)
    
    for sym in patent_syms:
        if sym not in counts:
            counts[sym] = {}
        counts[sym][year] = counts[sym].get(year, 0) + 1

# EMA Calculation
alpha = 0.2
candidates = []

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year = years[-1]
    
    ema = None
    max_ema = -1.0
    best_year = -1
    
    # Calculate EMA through the years
    # Should I extend to 2022 if the last data was before 2022?
    # If the max_year < 2022, then best_year can't be 2022 unless we treat later years as 0 counts?
    # If a symbol has counts in 2020 but 0 in 2021, 2022, the EMA will decay.
    # The max EMA might still be in the past.
    # But if I stop calculation at max_year (e.g. 2020), then best_year will be <= 2020.
    # The query asks "whose best year is 2022".
    # This implies I should consider the timeline up to at least 2022 if possible, or just the inherent max.
    # If I stop at max_year, and max_year < 2022, it won't be 2022.
    # If I extend with zeros up to 2022, the EMA will drop, so the max won't move to 2022.
    # So iterating up to `max(max_year, 2022)` is safer but if count is 0, EMA decreases.
    # Thus, the max EMA will occur at a year with high counts.
    # So iterating up to `max_year` is sufficient to find the peak *within the data range*.
    # If the peak is in 2022, the data must support it (high counts in or around 2022).
    
    for y in range(min_year, max_year + 1):
        count = year_counts.get(y, 0)
        
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
            
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        candidates.append(sym)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-9665950342090287602': 'file_storage/function-call-9665950342090287602.json', 'var_function-call-9665950342090285761': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16928258735931206764': [{'COUNT(*)': '277813'}], 'var_function-call-13650408886884758128': 'file_storage/function-call-13650408886884758128.json', 'var_function-call-17751803970902191593': 'file_storage/function-call-17751803970902191593.json', 'var_function-call-2714896827906959896': [], 'var_function-call-15280219420561285810': {'level5_sample': ['G07D', 'B68C', 'F41C', 'B60F', 'B27D'], 'level5_lengths': [4], 'years_found': [], 'symbols_matched_count': 0}, 'var_function-call-9633243674128522724': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-16820435960730373528': [], 'var_function-call-8660787959445410203': {'error': 'No years found'}, 'var_function-call-6203712476239218394': {'min': 1900, 'max': 2024, 'count_2022': 11966}}

exec(code, env_args)
