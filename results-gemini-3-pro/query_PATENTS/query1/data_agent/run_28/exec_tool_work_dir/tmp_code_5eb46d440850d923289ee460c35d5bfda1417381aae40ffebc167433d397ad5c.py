code = """import json
import re

# Get file paths from local variables
level5_file = locals()['var_function-call-11934561377780751846']
patent_file = locals()['var_function-call-17024007861906348069']

# Load Level 5 symbols
with open(level5_file, "r") as f:
    level5_data = json.load(f)
# Ensure we stripping whitespace if any
level5_codes = set(item['symbol'].strip() for item in level5_data)

# Load Patent data
with open(patent_file, "r") as f:
    patent_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    # Look for 4 digits
    match = re.search(r'\d{4}', date_str)
    if match:
        return int(match.group(0))
    return None

# Process data
# Count: {cpc_code: {year: count}}
counts = {}

for row in patent_data:
    year = extract_year(row.get('filing_date'))
    if year is None:
        continue
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Extract unique Level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '').strip()
        # Try to match Level 5 codes
        # Iterate lengths 4
        if len(code) >= 4:
            candidate = code[:4]
            if candidate in level5_codes:
                patent_codes.add(candidate)
    
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
result_codes = []

# Determine global max year to ensure we cover 2022
all_years = set()
for code_counts in counts.values():
    all_years.update(code_counts.keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

max_year_global = max(all_years)
target_year_limit = max(max_year_global, 2022)

for code, yearly_counts in counts.items():
    sorted_years_available = sorted(yearly_counts.keys())
    if not sorted_years_available:
        continue
        
    start_y = sorted_years_available[0]
    
    # We must calculate EMA up to at least 2022 if start_y <= 2022
    # If the series ends before 2022, we continue calculating with 0 counts.
    # If the series starts after 2022, max year can't be 2022 unless it's the start year and it's 2022.
    
    # We define the range of interest.
    # We should simulate year by year from start_y until at least 2022 (if possible) or the end of data.
    # Ideally, we should simulate until 2022 to see if it peaks then.
    
    # Let's iterate from start_y to target_year_limit
    
    current_ema = 0
    max_ema_val = -1
    max_ema_year = -1
    
    for y in range(start_y, target_year_limit + 1):
        val = yearly_counts.get(y, 0)
        
        if y == start_y:
            current_ema = val
        else:
            current_ema = alpha * val + (1 - alpha) * current_ema
        
        # Track max
        if current_ema > max_ema_val:
            max_ema_val = current_ema
            max_ema_year = y
        # If equal, we might prefer later year or earlier? usually strict > to find first peak or >= for last?
        # "best year is 2022". If it peaks in 2021 with 100 and 2022 with 100, is best year 2022?
        # Let's assume strict greater for update, so first peak is kept. Or >= for last peak.
        # "Best year" implies the single year with the highest value. Ties are edge cases.
        # Let's use strict > so we keep the first occurrence of the max.
        # If I use >=, I keep the last.
        # Let's verify if there are ties.
        
    if max_ema_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-569863329969676081': 'file_storage/function-call-569863329969676081.json', 'var_function-call-569863329969676028': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-569863329969675975': [{'cnt': '277813'}], 'var_function-call-11075431982575898925': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}], 'var_function-call-16171950182153960249': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-16171950182153959852': [{'symbol': 'A62B'}, {'symbol': 'A63G'}, {'symbol': 'A63K'}, {'symbol': 'A63B'}, {'symbol': 'A63J'}], 'var_function-call-16171950182153959455': [], 'var_function-call-2347784331555982775': [{'symbol': 'C13B50/00'}, {'symbol': 'C13B40/00'}, {'symbol': 'C13B99/00'}, {'symbol': 'C13B45/00'}, {'symbol': 'C21B3/00'}], 'var_function-call-11934561377780751846': 'file_storage/function-call-11934561377780751846.json', 'var_function-call-17024007861906348069': 'file_storage/function-call-17024007861906348069.json'}

exec(code, env_args)
