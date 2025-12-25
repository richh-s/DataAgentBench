code = """import json
import re
from collections import defaultdict

# Load level 5 symbols
# Use the actual keys provided in previous turns
level5_file = locals()['var_function-call-4744927068419664464']
pub_file = locals()['var_function-call-4744927068419665303']

with open(level5_file, 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

counts = defaultdict(lambda: defaultdict(int))
global_years = set()

# Regex to find years like 1999, 2020
year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')

for row in pub_data:
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    # Extract year
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    # Take the last match as the year (e.g. "March 20, 2019" -> 2019)
    try:
        year = int(matches[-1])
    except ValueError:
        continue
        
    # Extract CPCs
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except json.JSONDecodeError:
        continue
        
    # Identify unique level 5 codes in this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Map code to level 5 symbol
        # Strategy: Match the symbol length. Level 5 symbols seen were 4 chars.
        # Check if the first 4 chars are in level5_codes.
        # Some level 5 codes might be longer or shorter?
        # Based on preview (A01H, B01J), they are 4 chars.
        # But to be safe, we can try to match the longest prefix that is in level5_codes.
        # Or just assume 4 chars as standard for Subclass (which seems to be level 5 here).
        # Let's try 4 chars.
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
    
    # We want to check if the BEST year is 2022.
    # We should calculate EMA up to max_year.
    
    alpha = 0.2
    result_codes = []
    
    for code, year_counts in counts.items():
        ema = 0
        best_ema_val = -1
        best_year = -1
        
        # Initialize with first year data?
        # Let's iterate from min_year to max_year.
        # Init: ema = count[min_year]
        
        # However, to be robust, let's treat it as a sequence.
        # ema_t = alpha * x_t + (1-alpha) * ema_{t-1}
        
        ema = year_counts.get(min_year, 0)
        if ema > best_ema_val:
            best_ema_val = ema
            best_year = min_year
            
        for y in range(min_year + 1, max_year + 1):
            val = year_counts.get(y, 0)
            ema = alpha * val + (1 - alpha) * ema
            
            # Update best year
            # Note: If EMAs are equal, keep the first one? Or last?
            # "whose best year is 2022". Usually strict inequality or implies specific interest.
            # Let's update if ema > best_ema_val.
            if ema > best_ema_val:
                best_ema_val = ema
                best_year = y
                
        if best_year == 2022:
            result_codes.append(code)
            
    # Sort for consistent output
    result_codes.sort()
    
    print('__RESULT__:')
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-18281922881261155290': ['publicationinfo'], 'var_function-call-18281922881261156991': ['cpc_definition'], 'var_function-call-3853867713196752715': 'file_storage/function-call-3853867713196752715.json', 'var_function-call-3853867713196752716': [{'count': '277813'}], 'var_function-call-3853867713196752717': [{'count': '677'}], 'var_function-call-4744927068419664464': 'file_storage/function-call-4744927068419664464.json', 'var_function-call-4744927068419665303': 'file_storage/function-call-4744927068419665303.json'}

exec(code, env_args)
