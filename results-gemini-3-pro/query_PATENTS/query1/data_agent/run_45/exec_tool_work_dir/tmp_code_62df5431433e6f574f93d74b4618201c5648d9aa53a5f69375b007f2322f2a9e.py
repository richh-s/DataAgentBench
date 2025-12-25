code = """import json
import re

# Load level 5 symbols
with open(locals()['var_function-call-554775488917991620'], 'r') as f:
    cpc_def_data = json.load(f)
    
valid_level5 = set()
for item in cpc_def_data:
    if 'symbol' in item:
        valid_level5.add(item['symbol'])

# Load patent data
with open(locals()['var_function-call-4578472368250917218'], 'r') as f:
    patents = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Aggregation
# counts[code][year] = count
counts = {}
all_years = set()

for p in patents:
    # Extract Year
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    # Extract CPC
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique level 5 codes for this patent
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        # Map to level 5 (first 4 chars usually)
        # Check lengths. Level 5 symbols in valid_level5 are mostly 4 chars (e.g., A01B)
        # But we should verify against valid_level5 set.
        # We can try prefixes.
        # A code like "C01B33/00" starts with "C01B" which is in valid_level5.
        # A code like "H01M10/0565" starts with "H01M" which is in valid_level5.
        # We try to match the longest prefix that is in valid_level5.
        # Since level 5 seems to be Subclass (4 chars), we can try taking first 4 chars.
        
        candidate = code[:4]
        if candidate in valid_level5:
            patent_codes.add(candidate)
        else:
            # Fallback or check if level 5 can be longer/shorter?
            # Based on previous analysis, level 5 is Subclass (4 chars).
            # There might be exceptions?
            pass
            
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    global_max_year = max(all_years)
    global_min_year = min(all_years)
    
    # Filtered results
    result_codes = []
    
    for code, year_counts in counts.items():
        # Determine start year for this code
        years = sorted(year_counts.keys())
        start_year = years[0]
        
        ema = 0
        best_ema = -1.0
        best_year = -1
        
        # Initialize EMA with the first year's count
        ema = year_counts[start_year]
        best_ema = ema
        best_year = start_year
        
        # Iterate through years
        # We go up to global_max_year or just the last year of the code?
        # The query asks for "best year is 2022". 
        # If the code has no filings after 2020, its EMA will decay.
        # We should iterate up to max(global_max_year, 2022) to be safe, or just global_max_year.
        # Let's use global_max_year.
        
        current_year = start_year + 1
        while current_year <= global_max_year:
            count = year_counts.get(current_year, 0)
            ema = 0.2 * count + 0.8 * ema
            
            if ema > best_ema:
                best_ema = ema
                best_year = current_year
            # If equal, we keep the earlier one? Or later? 
            # Usually "best year" implies strict peak. If it stays flat, the first year is the peak.
            # But with decay, it changes.
            
            current_year += 1
            
        if best_year == 2022:
            result_codes.append(code)
            
    print("__RESULT__:")
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-5429124950122687575': 'file_storage/function-call-5429124950122687575.json', 'var_function-call-5429124950122687372': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-2491700961690963414': [{'symbol': 'A01B59/00', 'level': '7.0'}, {'symbol': 'A01B19/00', 'level': '7.0'}, {'symbol': 'A01B35/00', 'level': '7.0'}, {'symbol': 'A01B13/00', 'level': '7.0'}, {'symbol': 'A01B67/00', 'level': '7.0'}, {'symbol': 'A01B76/00', 'level': '7.0'}, {'symbol': 'A01B37/00', 'level': '7.0'}, {'symbol': 'A01B47/00', 'level': '7.0'}, {'symbol': 'A01B79/00', 'level': '7.0'}, {'symbol': 'A01B23/00', 'level': '7.0'}], 'var_function-call-2505457230602989857': [{'level': '2.0', 'sample_symbol': 'A'}, {'level': '4.0', 'sample_symbol': 'A01'}, {'level': '5.0', 'sample_symbol': 'A01B'}, {'level': '7.0', 'sample_symbol': 'A01B1/00'}, {'level': '8.0', 'sample_symbol': 'A01B1/02'}, {'level': '9.0', 'sample_symbol': 'A01B1/022'}, {'level': '10.0', 'sample_symbol': 'A01B1/225'}, {'level': '11.0', 'sample_symbol': 'A01B3/421'}, {'level': '12.0', 'sample_symbol': 'A01B3/4215'}, {'level': '13.0', 'sample_symbol': 'A01D2034/6843'}, {'level': '14.0', 'sample_symbol': 'A01D2034/6825'}, {'level': '15.0', 'sample_symbol': 'A47J31/4446'}, {'level': '16.0', 'sample_symbol': 'A61B17/7028'}, {'level': '17.0', 'sample_symbol': 'A61K47/6823'}, {'level': '18.0', 'sample_symbol': 'G01N2333/96444'}, {'level': '19.0', 'sample_symbol': 'H01L21/32137'}], 'var_function-call-850820474688023751': [{'COUNT(*)': '277813'}], 'var_function-call-554775488917991620': 'file_storage/function-call-554775488917991620.json', 'var_function-call-4578472368250917218': 'file_storage/function-call-4578472368250917218.json'}

exec(code, env_args)
