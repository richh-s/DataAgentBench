code = """import json
import re
from collections import defaultdict

level5_file = locals()['var_function-call-4744927068419664464']
pub_file = locals()['var_function-call-4744927068419665303']

with open(level5_file, 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

counts = defaultdict(lambda: defaultdict(int))
global_years = set()

# Use \d{4} as it proved reliable
year_pattern = re.compile(r'\d{4}')

for row in pub_data:
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    
    # Filter for valid years
    valid_years = []
    for m in matches:
        y = int(m)
        if 1900 <= y <= 2030:
            valid_years.append(y)
            
    if not valid_years:
        continue
        
    # Take the last valid year
    year = valid_years[-1]
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    if patent_codes:
        global_years.add(year)
        for c in patent_codes:
            counts[c][year] += 1

if not global_years:
    print('__RESULT__:')
    print("[]")
else:
    min_year = min(global_years)
    max_year = max(global_years)
    
    # Ensure we cover up to 2022 if data allows, or stops at 2022 if data goes further?
    # "whose best year is 2022".
    # I should calculate EMA for all years available.
    # If max_year < 2022, then 2022 can't be the best year (no data).
    # If max_year > 2022, and best is 2023, then it's not 2022.
    
    alpha = 0.2
    result_codes = []
    
    for code in counts:
        ema = counts[code].get(min_year, 0)
        
        best_ema = ema
        best_year = min_year
        
        # Iterate years
        # If the series has gaps, counts are 0.
        for y in range(min_year + 1, max_year + 1):
            val = counts[code].get(y, 0)
            ema = alpha * val + (1 - alpha) * ema
            
            # Update best
            # Use strict inequality? Or >=?
            # Usually "best year" implies the peak.
            # If equal, usually the first or last?
            # Let's assume strict inequality for updates, keeping the earliest year of peak?
            # Or latest?
            # Given "trend", latest is often more relevant.
            # But let's stick to simple comparison.
            if ema > best_ema:
                best_ema = ema
                best_year = y
        
        if best_year == 2022:
            result_codes.append(code)
            
    result_codes.sort()
    print('__RESULT__:')
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-18281922881261155290': ['publicationinfo'], 'var_function-call-18281922881261156991': ['cpc_definition'], 'var_function-call-3853867713196752715': 'file_storage/function-call-3853867713196752715.json', 'var_function-call-3853867713196752716': [{'count': '277813'}], 'var_function-call-3853867713196752717': [{'count': '677'}], 'var_function-call-4744927068419664464': 'file_storage/function-call-4744927068419664464.json', 'var_function-call-4744927068419665303': 'file_storage/function-call-4744927068419665303.json', 'var_function-call-4885472280726247165': [], 'var_function-call-11578580308570018388': {'min_year': None, 'max_year': None, 'total_records': 277813, 'records_with_date_match': 0, 'unique_cpcs_found': 0, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'sample_cpcs': [], 'sample_level5': ['C22F', 'C09K', 'C09B', 'B81B', 'F16F', 'B62B', 'F27D', 'B02B', 'A61Q', 'F41G'], 'sample_counts': {}}, 'var_function-call-1564629367961302156': {'dated 5th March 2019': ['2019'], 'March the 18th, 2019': ['2019'], '29th March 2019': ['2019'], 'on March 29th, 2019': ['2019'], '2nd April 2019': ['2019']}}

exec(code, env_args)
