code = """import json
import re
from collections import defaultdict

# Correct keys
key1 = 'var_function-call-14088919373237144211'
key2 = 'var_function-call-14088919373237143530'

# Load Level 5 codes
with open(locals()[key1], 'r') as f:
    level5_data = json.load(f)
    valid_level5 = set(item['symbol'] for item in level5_data)

# Load Patent Data
with open(locals()[key2], 'r') as f:
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
    # Filter reasonable years to avoid noise
    if year < 1900 or year > 2024:
        continue
        
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
    current_ema = float(counts[min_year])
    max_ema = current_ema
    best_year = min_year
    
    for y in range(min_year + 1, max_year + 1):
        count = counts[y]
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
        # If strict inequality, earlier year wins ties. If >=, later year wins.
        # "Best year is 2022" implies 2022 is the peak.
        # Let's assume strict greater to update max, so earlier year is preferred in tie?
        # Or usually recent is better?
        # Let's stick to strict >. If 2022 ties with 2021, and max was set in 2021, best is 2021.
        # If I want 2022 to be the best, it must be strictly better or I should update on >=.
        # Given "Identify... whose best year is 2022", if 2022 is equal to 2021, is it the best?
        # I'll use >= to allow 2022 to claim "best" if it ties.
        if current_ema >= max_ema:
             max_ema = current_ema
             best_year = y

    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-12010284986386434738': 'file_storage/function-call-12010284986386434738.json', 'var_function-call-12010284986386434717': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-7040256387500827623': [{'count(*)': '277813'}], 'var_function-call-5357179191043032962': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}, {'symbol': 'H01M10/0565', 'level': '11.0', 'titleFull': 'Polymeric materials, e.g. gel-type or solid-type'}, {'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}], 'var_function-call-2320558758355266598': [{'len': '4', 'count': '677'}], 'var_function-call-14088919373237144211': 'file_storage/function-call-14088919373237144211.json', 'var_function-call-14088919373237143530': 'file_storage/function-call-14088919373237143530.json'}

exec(code, env_args)
