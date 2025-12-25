code = """import json
import re
from collections import defaultdict

# Load level 5 codes
with open(locals()['var_function-call-5663588049585882641'], 'r') as f:
    level5_data = json.load(f)

level5_codes = set(item['symbol'] for item in level5_data)

# Check lengths of level 5 codes
lengths = set(len(s) for s in level5_codes)
print(f"Lengths of Level 5 codes: {lengths}")

# Load publication data
with open(locals()['var_function-call-14468441053053766244'], 'r') as f:
    pub_data = json.load(f)

print(f"Loaded {len(pub_data)} publications.")

# Date parser
def get_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group(0))
    return None

# Aggregation
# counts: {year: {cpc_code: count}}
counts = defaultdict(lambda: defaultdict(int))
years = set()

for row in pub_data:
    y = get_year(row.get('filing_date'))
    if y is None:
        continue
    
    years.add(y)
    
    cpc_json = row.get('cpc')
    if not cpc_json:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique level 5 codes for this patent
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Assuming Level 5 codes are 4 chars as seen in preview. 
        # If lengths vary, this logic needs adjustment.
        # Based on preview, they are 4 chars (Subclass).
        # We will extract first 4 chars.
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                patent_codes.add(prefix)
    
    for c in patent_codes:
        counts[y][c] += 1

if not years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years)
max_year = max(years)
print(f"Year range: {min_year} to {max_year}")

# EMA Calculation
# We need to track EMA for all CPCs that appeared.
all_cpcs = set()
for y in counts:
    all_cpcs.update(counts[y].keys())

print(f"Total unique Level 5 CPCs found: {len(all_cpcs)}")

ema_data = {cpc: {} for cpc in all_cpcs}
alpha = 0.2

for cpc in all_cpcs:
    # Calculate EMA over the full range
    previous_ema = None
    
    # We start from the global min_year to max_year to ensure comparison is fair?
    # Or start from the first year the CPC appears?
    # "highest ... each year" implies in year Y, we compare EMA(CPC_A, Y) vs EMA(CPC_B, Y).
    # If CPC_A started in 1900 and CPC_B in 2020.
    # In 2022, CPC_A has a long history. CPC_B has short.
    # EMA handles this.
    # We should iterate min_year to max_year.
    # Initial value:
    # If a CPC has 0 counts for years, EMA decays towards 0.
    # If we assume 0 before min_year.
    # EMA_min_year = alpha * count_min_year + (1-alpha) * 0 = alpha * count.
    # Wait, usually EMA_0 = value_0.
    # I'll stick to: S_t = alpha*Y_t + (1-alpha)*S_{t-1}.
    # Initialize S_{min_year-1} = 0.
    
    current_ema = 0.0 # seed
    
    for y in range(min_year, max_year + 1):
        count = counts[y].get(cpc, 0)
        
        # Formula
        # If it's the very first year and we define EMA_0 = Y_0.
        # But for comparison, having a uniform formula is better.
        # Let's use S_y = alpha * count + (1-alpha) * S_{y-1}
        # With S_{min_year-1} = 0.
        
        current_ema = alpha * count + (1 - alpha) * current_ema
        ema_data[cpc][y] = current_ema

# Identify "highest ... each year"
# winners_set = set()
# For each year, find the CPC(s) with max EMA.
winners_per_year = {}

for y in range(min_year, max_year + 1):
    # Find max EMA in this year
    max_val = -1.0
    year_winners = []
    
    for cpc in all_cpcs:
        val = ema_data[cpc][y]
        if val > max_val:
            max_val = val
            year_winners = [cpc]
        elif val == max_val:
            year_winners.append(cpc)
            
    winners_per_year[y] = year_winners

# Collect all winners
all_winners = set()
for w_list in winners_per_year.values():
    all_winners.update(w_list)

print(f"Number of annual winners: {len(all_winners)}")

# Filter winners: whose best year is 2022
final_results = []
for cpc in all_winners:
    # Find best year for this CPC
    # Iterate over its EMA history
    best_y = -1
    max_ema_cpc = -1.0
    
    # Check all years in range
    for y in range(min_year, max_year + 1):
        val = ema_data[cpc][y]
        if val > max_ema_cpc:
            max_ema_cpc = val
            best_y = y
        # Tie-breaking? "best year is 2022". If tied, maybe 2022 is one of them?
        # Let's assume strict inequality or latest?
        # Usually "best year" implies the peak. If peak is flat, 2022 matches.
        # I'll check if 2022 has the max value.
        
    if best_y == 2022:
        final_results.append(cpc)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-5663588049585882641': 'file_storage/function-call-5663588049585882641.json', 'var_function-call-15360535260242740816': [{'count(*)': '277813'}], 'var_function-call-14468441053053766244': 'file_storage/function-call-14468441053053766244.json'}

exec(code, env_args)
