code = """import json
import re
import pandas as pd

# Load level 5 symbols
with open(locals()['var_function-call-12377978627195880798'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load publication data
with open(locals()['var_function-call-17981272633275780013'], 'r') as f:
    publications = json.load(f)

# Data structure to hold counts: {code: {year: count}}
counts = {}

# Regex: look for 19xx or 20xx anywhere
year_regex = re.compile(r'(19|20)\d{2}')

for pub in publications:
    # Parse year
    filing_date = pub.get('filing_date', '')
    if not isinstance(filing_date, str):
        continue
    match = year_regex.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    
    # Parse CPC
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    unique_codes_for_patent = set()
    
    for entry in cpc_list:
        code = entry.get('code', '')
        # Check matching level 5
        # Assuming level 5 codes are prefixes of length 4
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_codes:
                unique_codes_for_patent.add(prefix)
    
    for c in unique_codes_for_patent:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
result_codes = []

# To ensure we cover up to 2022, we determine the global min and max year
all_years = set()
for c in counts:
    all_years.update(counts[c].keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
else:
    min_year_global = min(all_years)
    max_year_global = max(all_years)
    # Ensure 2022 is in range if meaningful
    end_year = max(max_year_global, 2022)

    for code, year_counts in counts.items():
        # Fill missing years with 0 from first year of activity?
        # Or from global min year?
        # Usually EMA is calculated from the start of the data series for that entity.
        # But to compare "best year", we should probably look at the history.
        
        years = sorted(year_counts.keys())
        start_year = years[0]
        
        ema = 0
        max_ema = -1.0
        best_year = -1
        
        # Iterate from start_year to end_year (at least 2022)
        # We stop at end_year.
        
        first = True
        
        # We need to iterate sequentially
        for y in range(start_year, end_year + 1):
            count = year_counts.get(y, 0)
            if first:
                ema = count
                first = False
            else:
                ema = alpha * count + (1 - alpha) * ema
            
            # Check if this is the max EMA so far?
            # No, we need the max EMA over the whole history.
            # So we just store (year, ema) and find max later?
            # Or update max on the fly.
            
            if ema > max_ema:
                max_ema = ema
                best_year = y
            elif ema == max_ema:
                # If equal, prefer later year? Or multiple?
                # Usually best year is unique or we define a tie-breaker.
                # Let's assume strict greater, or keep the first one. 
                # Or keep the most recent?
                # "best year is 2022" implies 2022 has the highest.
                # Let's update best_year to the latest if tied, or keep. 
                # Since EMA is float, ties are rare.
                pass
                
        if best_year == 2022:
            result_codes.append(code)

    print("__RESULT__:")
    print(json.dumps(result_codes))"""

env_args = {'var_function-call-11743318916466858898': 'file_storage/function-call-11743318916466858898.json', 'var_function-call-16238834244750781196': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-12377978627195880798': 'file_storage/function-call-12377978627195880798.json', 'var_function-call-17981272633275780013': 'file_storage/function-call-17981272633275780013.json', 'var_function-call-7974876835116330076': [], 'var_function-call-8239502842607938833': {'years_found': [], 'total_pubs': 277813, 'code_matches_in_sample': 11180, 'sample_level5': ['F01K', 'B23D', 'B27C', 'B27J', 'B61H']}, 'var_function-call-5759052096816044900': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019']}

exec(code, env_args)
