code = """import json
import re

# Load level 5 symbols
# var_function-call-8552121385304934685 is the file path
with open('var_function-call-8552121385304934685', 'r') as f:
    level5_list = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_list)

# Check lengths
lengths = set(len(s) for s in level5_symbols)
# We handle matching by checking if code starts with symbol.
# To optimize, if all are length 4, we use slicing.
# If mixed, we might need a different approach.
# We'll see. For now, general approach:
# Create a set of valid prefixes?
# If lengths are small (e.g. only 4), slicing is best.

# Load patent data
with open('var_function-call-12122079112080214207', 'r') as f:
    patent_data = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

counts = {} # {symbol: {year: count}}

for row in patent_data:
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Identify unique Level 5 symbols for this patent
    # To be efficient:
    # Iterate cpc codes. For each code, check if it belongs to a level 5 symbol.
    # If level 5 symbols are subclasses (4 chars), check first 4 chars.
    
    current_patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                current_patent_symbols.add(prefix)
            # If there are symbols of different lengths, we need to check those too.
            # But based on the preview, they look like 4.
            # We can double check if 'lengths' contains anything other than 4.
            
    for s in current_patent_symbols:
        if s not in counts:
            counts[s] = {}
        counts[s][year] = counts[s].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
selected_symbols = []

for sym, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    start_year = years[0]
    end_year = years[-1]
    
    # If the series ends before 2022, it can't be the best year? 
    # Or maybe it peaked earlier.
    # But if it ends in 2020, 2022 doesn't exist.
    # However, if we assume 0 for future years, EMA will decay.
    # To be safe, we should extend to 2022 if the data goes that far in general?
    # Let's check the global max year in the dataset.
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    current_ema = None
    
    # We iterate through the range. 
    # Logic: EMA_t depends on EMA_{t-1}.
    
    # Note: If best year is 2022, we must have data up to 2022 (or implied 0s).
    # If a technology stopped in 2010, its EMA would decay. 
    # If we stop calculation at 2010, we'd say best year was somewhere in 2010 range.
    # If we extend to 2022 with 0s, the EMA would drop.
    # So we should extend the calculation up to at least 2022 for all series to fairly compare "best year".
    # But wait, if we extend to 2022 with 0s, the EMA will likely decrease, so the peak won't be 2022.
    # Unless there are filings in 2022.
    # So effectively, we just need to iterate up to max(year_counts.keys()) provided it is >= 2022?
    # Or should we find the global max year across all patents?
    
    # Let's find the max year for this specific symbol.
    # If max_year < 2022, then for years > max_year, count is 0, EMA decays.
    # So the max EMA will occur at or before max_year.
    # So if max_year < 2022, the best year cannot be 2022.
    # So we only care if max_year >= 2022.
    
    if end_year < 2022:
        continue
        
    for y in range(start_year, end_year + 1):
        c = year_counts.get(y, 0)
        if current_ema is None:
            current_ema = c
        else:
            current_ema = alpha * c + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
    if best_year == 2022:
        selected_symbols.append(sym)

print("__RESULT__:")
print(json.dumps(selected_symbols))"""

env_args = {'var_function-call-1397089811542180174': ['publicationinfo'], 'var_function-call-1397089811542180177': ['cpc_definition'], 'var_function-call-3017323399836205737': 'file_storage/function-call-3017323399836205737.json', 'var_function-call-3017323399836208786': [{'count': '677'}], 'var_function-call-16375230660246420135': [{'count(*)': '277813'}], 'var_function-call-8552121385304934685': 'file_storage/function-call-8552121385304934685.json', 'var_function-call-12122079112080214207': 'file_storage/function-call-12122079112080214207.json'}

exec(code, env_args)
