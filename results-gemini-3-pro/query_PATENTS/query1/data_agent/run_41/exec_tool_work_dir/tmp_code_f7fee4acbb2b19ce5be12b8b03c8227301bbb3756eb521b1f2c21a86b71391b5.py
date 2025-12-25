code = """import json
import re
from collections import defaultdict

# Load Level 5 codes
with open(locals()['var_function_call_14088919373237144211'], 'r') as f:
    level5_data = json.load(f)
    valid_level5 = set(item['symbol'] for item in level5_data)

# Load Patent Data
with open(locals()['var_function_call_14088919373237143530'], 'r') as f:
    patent_data = json.load(f)

filings = defaultdict(lambda: defaultdict(int))
all_years = set()

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for row in patent_data:
    # Extract Year
    fdate = row.get('filing_date', '')
    match = year_pattern.search(fdate)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    
    # Extract Codes
    cpc_str = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique Level 5 codes for this patent
    patent_codes = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in valid_level5:
                patent_codes.add(subclass)
    
    # Aggregate
    for code in patent_codes:
        filings[code][year] += 1

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
alpha = 0.2

result_codes = []

for code in filings:
    counts = filings[code]
    
    # Calculate EMA
    # Initialize EMA with the count of the first year (min_year)
    # Using simple EMA: EMA_t = alpha * x_t + (1-alpha) * EMA_t-1
    # For t=0 (min_year), EMA_0 = x_0
    
    current_ema = float(counts[min_year])
    max_ema = current_ema
    best_year = min_year
    
    for y in range(min_year + 1, max_year + 1):
        count = counts[y]
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
        elif current_ema == max_ema:
            # Tie-breaking? Usually later year or earlier. 
            # If equal, it doesn't strictly matter unless it's 2022.
            # If tie with 2022, we can say best year includes 2022.
            best_year = y # Update to latest year
            
    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-12010284986386434738': 'file_storage/function-call-12010284986386434738.json', 'var_function-call-12010284986386434717': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-7040256387500827623': [{'count(*)': '277813'}], 'var_function-call-5357179191043032962': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-2320558758355266598': [{'len': '4', 'count': '677'}], 'var_function-call-14088919373237144211': 'file_storage/function-call-14088919373237144211.json', 'var_function-call-14088919373237143530': 'file_storage/function-call-14088919373237143530.json'}

exec(code, env_args)
