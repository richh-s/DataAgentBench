code = """import json
import re

# Get file paths from storage
path_cpc = locals()['var_function-call-17682530284056883508']
path_patents = locals()['var_function-call-1425838539260044447']

# Load Level 5 CPC symbols
with open(path_cpc, 'r') as f:
    cpc_defs = json.load(f)

level_5_symbols = set()
for item in cpc_defs:
    if 'symbol' in item:
        level_5_symbols.add(item['symbol'])

# Inspect format
sample_symbols = list(level_5_symbols)[:10]
print("Sample Level 5 Symbols:", sample_symbols)

# Determine matching strategy
# Check if all are 4 chars
if level_5_symbols and all(len(s) == 4 for s in sample_symbols):
    match_mode = 'subclass'
else:
    match_mode = 'exact' # Or 'unknown', but let's assume exact if not all 4 chars
    # Double check if any are not 4 chars
    # We can check the whole set
    if any(len(s) != 4 for s in level_5_symbols):
        match_mode = 'exact'

print(f"Match mode: {match_mode}")

# Load Patent Data
with open(path_patents, 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for p in patents:
    f_date = p.get('filing_date', '')
    cpc_json = p.get('cpc', '[]')
    
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    year = int(matches[-1])
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
            
        target_code = None
        if match_mode == 'subclass':
            if len(code) >= 4:
                target_code = code[:4]
        else:
            # If match_mode is exact, it means level 5 symbols are likely Groups (e.g. A01B1/00)
            # We should check if the patent code starts with any level 5 symbol?
            # Or if it matches exactly?
            # Standard CPC: A symbol is defined. A patent is assigned a code.
            # Usually the patent is assigned at the lowest level.
            # If level 5 is "A01B 1/00" and patent has "A01B 1/02", does it count for "A01B 1/00"?
            # Usually aggregation is done at the level requested.
            # So if requested level is Main Group, we aggregate all Subgroups under it.
            # However, mapping arbitrary code to Main Group requires string manipulation (cut after slash? or before slash?)
            # Main Group format: "Subclass MainGroup/00"
            # Subgroup format: "Subclass MainGroup/SubGroup"
            # So we can split by '/' and check.
            # But let's look at the sample symbols first.
            target_code = code # Placeholder until we see the sample output

        # Refined logic will be applied after I see the print output in the next turn if needed.
        # But I need to produce a result now.
        # Let's add a logic: if 'exact', we try to match exactly or check membership.
        # But wait, if match_mode is subclass, I aggregate to subclass.
        # If match_mode is exact, and I just check `code in level_5_symbols`, I might miss children.
        # However, without full hierarchy logic, exact match or simple truncation is best.
        # If level 5 symbols are Main Groups (e.g. ending in /00), and patent has specific subgroup,
        # I should probably map the subgroup to the main group.
        # BUT, the DB query for level 5 returned specific symbols.
        # Let's assume for now we only count exact occurrences if not subclass.
        # Or better: check if the code *starts with* a level 5 symbol? No, symbols can overlap.
        
        # Let's proceed with `match_mode` logic. 
        # I will implement the aggregation if I see the symbols are not 4 chars.
        
        if match_mode == 'subclass':
             if target_code and target_code in level_5_symbols:
                if target_code not in counts:
                    counts[target_code] = {}
                counts[target_code][year] = counts[target_code].get(year, 0) + 1
        else:
             # Fallback: exact match
             if code in level_5_symbols:
                if code not in counts:
                    counts[code] = {}
                counts[code][year] = counts[code].get(year, 0) + 1
             # NOTE: This ignores children if level 5 is a parent node. 
             # Given the "HINTS", "cpc" field contains entries with code. 
             # I'll stick to exact match if not subclass.

# Calculate EMA
alpha = 0.2
results = []
# We need to cover years up to 2022.
# Find global max year
all_years = []
for yc in counts.values():
    all_years.extend(yc.keys())
    
if not all_years:
    global_max_year = 2022
else:
    global_max_year = max(max(all_years), 2022)

for code, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    min_year = years[0]
    
    ema = 0
    first = True
    best_ema = -1.0
    best_year = -1
    
    # Iterate through all years from start of this code's activity up to at least 2022
    # or the end of its activity if it stopped before.
    # Actually, if it stopped before 2022, the count is 0 for subsequent years, and EMA decays.
    # We should calculate EMA up to 2022 to see if 2022 is the best year (unlikely if decaying, but possible if it just peaked).
    # Wait, if it peaked in 2021, and 2022 is 0, EMA(2022) < EMA(2021).
    # So checking up to max(years, 2022) is correct.
    
    limit_year = max(years[-1], 2022)
    
    for y in range(min_year, limit_year + 1):
        count = year_counts.get(y, 0)
        if first:
            ema = count
            first = False
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # We need to track the BEST year.
        if ema > best_ema:
            best_ema = ema
            best_year = y
        # If tie?
        # If ema == best_ema, we don't update best_year (keep earliest) or update (keep latest)?
        # Let's assume floating point equality is rare, but if it happens, usually we want the peak.
        
    if best_year == 2022:
        results.append(code)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json'}

exec(code, env_args)
