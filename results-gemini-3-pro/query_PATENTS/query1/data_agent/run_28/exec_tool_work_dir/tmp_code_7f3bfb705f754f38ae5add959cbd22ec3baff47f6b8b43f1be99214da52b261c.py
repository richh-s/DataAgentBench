code = """import json
import re

# Load Level 5 symbols
with open("var_function-call-11934561377780751846.json", "r") as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load Patent data
with open("var_function-call-17024007861906348069.json", "r") as f:
    patent_data = json.load(f)

print(f"Loaded {len(level5_codes)} Level 5 codes.")
print(f"Loaded {len(patent_data)} patent records.")

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
        code = item.get('code', '')
        # Try to match Level 5 codes
        # Most Level 5 codes seem to be 4 chars (e.g. A01B).
        # Patent codes are like C01B33/00.
        # We try to see if the prefix matches a known Level 5 code.
        # Since Level 5 codes can vary in length (though most are 4), checking against the set is best.
        # We can iterate through lengths 3, 4, 5... but that's slow.
        # Standard CPC Subclass is 4 chars.
        # Let's assume 4 chars for now as primary candidate.
        if len(code) >= 4:
            candidate = code[:4]
            if candidate in level5_codes:
                patent_codes.add(candidate)
            else:
                # Some might be shorter or longer?
                # Check 3 chars? unlikely for subclass.
                # Check 5 chars?
                pass
    
    for code in patent_codes:
        if code not in counts:
            counts[code] = {}
        counts[code][year] = counts[code].get(year, 0) + 1

# Calculate EMA
# Filter codes where best year is 2022
alpha = 0.2
result_codes = []

# Get range of years to iterate properly?
# EMA is time-series. We should iterate sorted years.
# What is the global min and max year?
all_years = set()
for code_counts in counts.values():
    all_years.update(code_counts.keys())

if not all_years:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(all_years)
max_year = max(all_years)
years = sorted(list(all_years))

for code, yearly_counts in counts.items():
    # Construct time series
    # Logic: EMA_t = alpha * Val_t + (1-alpha) * EMA_{t-1}
    # Initialize EMA with the first available value? Or 0?
    # Usually first available.
    
    sorted_years_available = sorted(yearly_counts.keys())
    if not sorted_years_available:
        continue
        
    ema = None
    best_ema = -1
    best_year = -1
    
    # Iterate through all years from first available for this code to max_year?
    # Or just the years available?
    # Standard EMA updates at every time step. If count is 0, EMA decays.
    # So we should iterate from min_year_for_code to max_year_overall? 
    # Or min_year_global to max_year_global?
    # "Identify the CPC technology areas with the highest exponential moving average of patent filings each year"
    # This implies we track the EMA over time.
    # Assuming annual time steps.
    
    # Let's iterate from the first year this code appears until the global max year (or 2022 if higher/lower).
    # Actually, the user says "whose best year is 2022". So we need EMA for 2022.
    # So we must compute up to at least 2022.
    
    start_y = sorted_years_available[0]
    # end_y = max(max_year, 2022) # Ensure we cover 2022
    end_y = max_year
    
    current_ema = 0
    # Initialization
    # EMA_0 = Value_0 (at start_y)
    
    # We need to store best year.
    max_ema_val = -1
    max_ema_year = -1
    
    # Iterate year by year
    for y in range(start_y, end_y + 1):
        val = yearly_counts.get(y, 0)
        if y == start_y:
            current_ema = val
        else:
            current_ema = alpha * val + (1 - alpha) * current_ema
        
        if current_ema > max_ema_val:
            max_ema_val = current_ema
            max_ema_year = y
            
    if max_ema_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-569863329969676081': 'file_storage/function-call-569863329969676081.json', 'var_function-call-569863329969676028': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}], 'var_function-call-569863329969675975': [{'cnt': '277813'}], 'var_function-call-11075431982575898925': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}], 'var_function-call-16171950182153960249': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-16171950182153959852': [{'symbol': 'A62B'}, {'symbol': 'A63G'}, {'symbol': 'A63K'}, {'symbol': 'A63B'}, {'symbol': 'A63J'}], 'var_function-call-16171950182153959455': [], 'var_function-call-2347784331555982775': [{'symbol': 'C13B50/00'}, {'symbol': 'C13B40/00'}, {'symbol': 'C13B99/00'}, {'symbol': 'C13B45/00'}, {'symbol': 'C21B3/00'}], 'var_function-call-11934561377780751846': 'file_storage/function-call-11934561377780751846.json', 'var_function-call-17024007861906348069': 'file_storage/function-call-17024007861906348069.json'}

exec(code, env_args)
