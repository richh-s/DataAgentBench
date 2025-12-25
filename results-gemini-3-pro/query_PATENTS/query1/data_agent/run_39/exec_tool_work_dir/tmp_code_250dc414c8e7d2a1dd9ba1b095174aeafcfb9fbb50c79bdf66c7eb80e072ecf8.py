code = """import json
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-4228191098478002445'], 'r') as f:
    l5_data = json.load(f)
target_cpcs = set(item['symbol'] for item in l5_data)

# Load publication info
with open(locals()['var_function-call-18000460645263660191'], 'r') as f:
    pub_data = json.load(f)

counts = {}
global_years = set()
year_pattern = re.compile(r'(19|20)\d{2}')

for row in pub_data:
    f_date = row.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Filter reasonable years
    if year < 1900 or year > 2025:
        continue
        
    global_years.add(year)
    
    cpc_json = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Per patent, count each relevant subclass once?
    # Or count every occurrence? Usually "filings" means patents filed.
    # If a patent has multiple codes in "A01B", it is still one patent in "A01B".
    # So we use a set per patent.
    seen_in_this_patent = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in target_cpcs:
                seen_in_this_patent.add(prefix)
    
    for cpc in seen_in_this_patent:
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

if not global_years:
    print("__RESULT__:")
    print(json.dumps([]))
else:
    min_year = min(global_years)
    max_year = max(global_years)
    # Ensure we cover up to 2022 if it exists in range or we need to check it
    end_year = max(max_year, 2022)
    
    alpha = 0.2
    results = []
    
    # Debug stats
    debug_max_ema_year_dist = {}
    
    for cpc, year_counts in counts.items():
        # Calculate EMA
        ema = 0
        best_ema = -1.0
        best_year = -1
        
        # We start from the first year this CPC appeared or global start?
        # Usually EMA runs on the whole timeline of the dataset.
        # But if a CPC didn't exist, its count was 0.
        # Let's assume global timeline from min_year to end_year.
        
        first_val = True
        
        # To handle initialization correctly:
        # Standard pandas ewm(alpha=0.2, adjust=False)
        # y0 = x0
        # yt = (1-alpha)*y(t-1) + alpha*xt
        
        # But if we start from global_min_year, and the CPC has no filings for 50 years,
        # EMA stays 0. Then when it appears, it goes up.
        # This seems correct for "technology areas".
        
        current_ema = 0.0
        # Initialize with 0 or first value?
        # If we iterate from min_year, and count is 0, EMA becomes 0.
        # Once we hit the first non-zero, it rises.
        # Exception: if we want to initialize with the first available data point for that series.
        # However, "highest exponential moving average ... each year" implies we compare them in specific years.
        # If we align them all to the calendar year, we should run 2010..2022.
        
        # Let's iterate from min_year to end_year.
        # Initialization: current_ema = 0 initially? 
        # Or should we skip until first data point? 
        # If we skip, the timeline is shifted. Calendar year matters here ("best year is 2022").
        # So we must stick to calendar years.
        # We will assume EMA = 0 before data starts.
        
        # But wait, standard EMA formula: y_t = alpha * x_t + (1-alpha) * y_{t-1}
        # If y_{t-1} is 0 and x_t is 0, y_t is 0.
        # If x_t appears, it starts growing.
        
        # One nuance: The first observation x_0. usually EMA_0 = x_0.
        # If we start at global_min_year, and x=0, then EMA=0.
        # If the series starts later, say 2015, effectively we treat 2000-2014 as 0s.
        # This penalizes new technologies slightly but eventually they catch up.
        # Given "smoothing factor 0.2", it reacts relatively slowly.
        
        # Let's use 0 initialization.
        current_ema = 0.0
        # Wait, if I initialize with 0, and the first count is 100.
        # Year 1: 0.2 * 100 + 0.8 * 0 = 20.
        # If I initialized with first value: Year 1: 100.
        # Pandas `adjust=False` (recursive) does:
        # y0 = x0
        # y1 = alpha*x1 + (1-alpha)*y0
        # I should probably detect the first year with data for THIS cpc to initialize properly,
        # otherwise early years are dragged down artificially.
        
        # Find first year with data for this CPC
        cpc_years = sorted(year_counts.keys())
        if not cpc_years:
            continue
        first_cpc_year = cpc_years[0]
        
        # We iterate from global min_year.
        # Before first_cpc_year, count is 0.
        # Should we initialize at first_cpc_year?
        # If we do, what is the EMA for years before that? Undefined or 0?
        # "Identify ... highest EMA each year".
        # If it's undefined, it can't be the highest.
        # If 0, it is low.
        
        # I will start calculation from global_min_year.
        # But to avoid the startup lag dragging down the peak year if it's early,
        # I will check if it matters.
        # User asks for "best year".
        # I will implement the standard recursive formula starting from global_min_year, initialized at 0.
        # This is safe for comparing across different start times on a fixed timeline.
        
        for y in range(min_year, end_year + 1):
            val = year_counts.get(y, 0)
            if y == min_year:
                # Initialization
                # If we assume infinite history of 0s, then EMA_0 = alpha*val + (1-alpha)*0 = alpha*val.
                # If we assume EMA_0 = val (standard pandas), we do that.
                # Let's do EMA_0 = val.
                current_ema = val
            else:
                current_ema = alpha * val + (1 - alpha) * current_ema
            
            if current_ema > best_ema:
                best_ema = current_ema
                best_year = y
        
        debug_max_ema_year_dist[best_year] = debug_max_ema_year_dist.get(best_year, 0) + 1
        
        if best_year == 2022:
            results.append(cpc)
            
    # Print debug info to result if empty
    if not results:
        debug_info = {
            "msg": "No results",
            "years_range": [min_year, max_year],
            "end_year_used": end_year,
            "best_year_dist": debug_max_ema_year_dist,
            "sample_counts": list(counts.items())[:2]
        }
        print("__RESULT__:")
        print(json.dumps(debug_info)) # Return this so I can read it
    else:
        print("__RESULT__:")
        print(json.dumps(results))"""

env_args = {'var_function-call-4228191098478004752': 'file_storage/function-call-4228191098478004752.json', 'var_function-call-4228191098478002445': 'file_storage/function-call-4228191098478002445.json', 'var_function-call-1200149957190319519': [], 'var_function-call-11228189343625932313': 'Done', 'var_function-call-348325328612645503': {'total_records': 10, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'years_found': [], 'matched_cpcs_count': 0}, 'var_function-call-18000460645263660191': 'file_storage/function-call-18000460645263660191.json'}

exec(code, env_args)
