code = """import json
import re
import collections

file_path = locals()['var_function-call-17338179346736761681']
with open(file_path, 'r') as f:
    data = json.load(f)

counts = collections.defaultdict(lambda: collections.defaultdict(int))
all_years = set()
year_pattern = re.compile(r'(19|20)\d{2}')

for row in data:
    f_date = str(row.get('filing_date', ''))
    cpc_str = row.get('cpc', '')
    
    match = year_pattern.search(f_date)
    if match:
        year = int(match.group(0))
        if 1900 <= year <= 2025:
            all_years.add(year)
        else:
            continue
    else:
        continue
        
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    subclasses = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclasses.add(code[:4])
            
    for sc in subclasses:
        counts[sc][year] += 1

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)

# Debug print
# print(f"Years range: {min_year} - {max_year}")

alpha = 0.2
candidates = []

for sc, year_counts in counts.items():
    ema = 0
    # Initialize EMA.
    # Approach: Iterate from min_year to max_year.
    # EMA_t = alpha * Val_t + (1-alpha) * EMA_{t-1}
    # Initial EMA: Can assume 0 before min_year.
    # Then EMA_{min_year} = alpha * Val_{min_year} + 0
    # OR start with first value? 
    # Usually EMA starts with the first observation.
    # But for comparing years, we should be consistent.
    # Let's iterate min_year to max_year.
    
    current_ema = 0 # Assume 0 prior to data
    max_ema_val = -1
    best_year = -1
    
    # We must iterate up to 2022 if it exists.
    # If max_year < 2022, then it's impossible.
    limit_year = max(max_year, 2022) # Just in case data stops early but we want to project? No, "patent filings each year". If no data, filings are 0.
    
    # Use actual max_year from data. If 2022 is not in data, then no 2022 best year.
    
    for y in range(min_year, max_year + 1):
        val = year_counts.get(y, 0)
        
        # Standard EMA update
        if y == min_year:
            # First point initialization
            # Often set to val, or 0. Let's set to val for quick adaptation, or 0 if assuming history of 0s.
            # "Smoothing factor 0.2".
            # If we assume history of 0, EMA_0 = 0.2 * val + 0.8 * 0 = 0.2 * val.
            # If we assume EMA starts at val: EMA_0 = val.
            # Let's use EMA_0 = val.
            current_ema = val
        else:
            current_ema = (val * alpha) + (current_ema * (1 - alpha))
            
        if current_ema > max_ema_val:
            max_ema_val = current_ema
            best_year = y
        elif current_ema == max_ema_val:
            # Tie-breaking? Prefer later year? Prefer earlier?
            # Usually strict inequality for "highest".
            pass
            
    if best_year == 2022:
        candidates.append(sc)

candidates.sort()
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-18328823556170727936': 'file_storage/function-call-18328823556170727936.json', 'var_function-call-1448611933655007552': [{'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-12333554857187488258': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-520411694824460309': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-8582293101607143888': [{'len': '4', 'count': '677'}], 'var_function-call-17338179346736761681': 'file_storage/function-call-17338179346736761681.json', 'var_function-call-6216724140096565940': [], 'var_function-call-11337062287616366428': {'min_year': None, 'max_year': None, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'num_records': 277813}, 'var_function-call-14976001841077050799': [{'index': 0, 'date': 'dated 5th March 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "C'}, {'index': 1, 'date': 'March the 18th, 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "F'}, {'index': 2, 'date': '29th March 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "B'}, {'index': 3, 'date': 'on March 29th, 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "A'}, {'index': 4, 'date': '2nd April 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "H'}, {'index': 5, 'date': 'on April 8th, 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "A'}, {'index': 6, 'date': '15th April 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "H'}, {'index': 7, 'date': 'April 19th, 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "A'}, {'index': 8, 'date': '2019, April 24th', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "G'}, {'index': 9, 'date': 'April 26th, 2019', 'year_extracted': '2019', 'cpc_preview': '[\n  {\n    "code": "F'}]}

exec(code, env_args)
