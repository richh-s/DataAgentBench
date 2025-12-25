code = """import json
import re

# Load data
cpc_file_path = locals()['var_function-call-15748739634169971950']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

level5_symbols = set()
for item in cpc_data:
    if item.get('symbol'):
        level5_symbols.add(item['symbol'])

pub_file_path = locals()['var_function-call-14833157841070883006']
with open(pub_file_path, 'r') as f:
    pub_data = json.load(f)

counts = {} # counts[symbol][year] = count
year_pattern = re.compile(r'\d{4}')

for row in pub_data:
    f_date = row.get('filing_date', '')
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    
    # Try to find a valid year from matches (prefer last one)
    year = -1
    for m in reversed(matches):
        y = int(m)
        if 1900 <= y <= 2025:
            year = y
            break
    if year == -1:
        continue
        
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
        seen_syms = set()
        for entry in cpc_list:
            code = entry.get('code', '')
            if len(code) >= 4:
                prefix = code[:4]
                if prefix in level5_symbols:
                    seen_syms.add(prefix)
        
        for s in seen_syms:
            if s not in counts:
                counts[s] = {}
            counts[s][year] = counts[s].get(year, 0) + 1
    except:
        continue

# Calculate EMA and find best year
alpha = 0.2
results = []

# Find global min year to ensure consistent start?
# Or start from the first year of each symbol?
# "exponential moving average ... each year"
# Usually EMA starts at the first data point.
# But if we compare "best year", we should probably consider the series up to 2022.

for sym, year_counts in counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    start_year = years[0]
    end_year = 2022 
    # If the data goes beyond 2022, we should include it? 
    # The question asks for "best year is 2022". If the peak is in 2023, then it's not 2022.
    # So we should consider all available years.
    # But usually patent data has lag.
    # Let's use the max year from data or 2022, whichever is higher?
    # I'll use max(years[-1], 2022).
    
    max_y = max(years[-1], 2022)
    
    ema = None
    max_ema_val = -1.0
    best_year = -1
    
    # Iterate from start_year to max_y
    for y in range(start_year, max_y + 1):
        count = year_counts.get(y, 0)
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
            
        if ema > max_ema_val:
            max_ema_val = ema
            best_year = y
            
    if best_year == 2022:
        results.append(sym)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15748739634169971950': 'file_storage/function-call-15748739634169971950.json', 'var_function-call-15365107857304262203': 'file_storage/function-call-15365107857304262203.json', 'var_function-call-14487137383779015423': [{'COUNT(*)': '277813'}], 'var_function-call-14833157841070883006': 'file_storage/function-call-14833157841070883006.json', 'var_function-call-9103271946905956666': [], 'var_function-call-18064361241579381342': 'Done', 'var_function-call-16200861530441648505': {'num_level5': 677, 'sample_level5': ['B61K', 'E05Y', 'G16Y', 'A01H', 'B01F', 'B66C', 'B60F', 'B44B', 'A44D', 'B60V'], 'num_records': 277813, 'matched_years': 0, 'matched_cpcs_patents': 0, 'sample_counts_keys': []}, 'var_function-call-2057085515518975045': [{'date': 'dated 5th March 2019', 'matches': ['2019']}, {'date': 'March the 18th, 2019', 'matches': ['2019']}, {'date': '29th March 2019', 'matches': ['2019']}, {'date': 'on March 29th, 2019', 'matches': ['2019']}, {'date': '2nd April 2019', 'matches': ['2019']}, {'date': 'on April 8th, 2019', 'matches': ['2019']}, {'date': '15th April 2019', 'matches': ['2019']}, {'date': 'April 19th, 2019', 'matches': ['2019']}, {'date': '2019, April 24th', 'matches': ['2019']}, {'date': 'April 26th, 2019', 'matches': ['2019']}]}

exec(code, env_args)
