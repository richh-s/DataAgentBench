code = """import json
import re
from collections import defaultdict

# Load Level 5 Symbols
with open(locals()['var_function-call-4372299924973492362'], 'r') as f:
    l5_data = json.load(f)
    # l5_data is a list of dicts: [{"symbol": "A01H"}, ...]
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-3133902688408324092'], 'r') as f:
    patent_data = json.load(f)

# Data Structures
# counts[code][year] = int
counts = defaultdict(lambda: defaultdict(int))
years_seen = set()

# Regex for year
year_pattern = re.compile(r'(19|20)\d{2}')

for row in patent_data:
    cpc_json = row.get('cpc')
    filing_date = row.get('filing_date')
    
    if not cpc_json or not filing_date:
        continue
        
    # Extract Year
    match = year_pattern.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    years_seen.add(year)
    
    # Parse CPC
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
        
    # Extract unique level 5 codes for this patent
    patent_codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_codes:
                patent_codes.add(subclass)
    
    # Update counts
    for code in patent_codes:
        counts[code][year] += 1

if not years_seen:
    print("__RESULT__:")
    print("[]")
    exit()

min_year = min(years_seen)
max_year = max(years_seen)

# Calculate EMA and find best year
alpha = 0.2
result_codes = []

for code, year_counts in counts.items():
    ema = 0
    max_ema = -1
    best_year = -1
    
    # We iterate from min_year to max_year to handle years with 0 counts correctly
    # However, if a code appeared late, should we start from min_year?
    # "EMA of patent filings each year" implies a time series.
    # If we assume 0 for years before the first appearance, the EMA will be low.
    # Standard practice for such analysis is usually over the whole period or starting from first activity.
    # Given "technology areas with highest ... each year", it implies comparing them.
    # If I start from the first year the code appears, the EMA might be artificially high initially if the count is high.
    # But if I start from global min_year (e.g. 1900), and the tech appears in 2020, the EMA will be 0 for a long time.
    # However, since the question asks for "best year is 2022", we care about the peak.
    # Let's use the global range min_year to max_year.
    # Initialize EMA with the count of the first year (min_year).
    
    ema = year_counts.get(min_year, 0)
    
    # Track best year
    # If multiple years have same max EMA? The problem implies a single best year or "is 2022".
    # I'll update best_year if current EMA > max_ema.
    
    if ema > max_ema:
        max_ema = ema
        best_year = min_year
    
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_codes.append(code)

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-13849679105331818549': 'file_storage/function-call-13849679105331818549.json', 'var_function-call-15105805855473499623': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-2181629081178203609': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}], 'var_function-call-1527102725415645429': [{'symbol': 'B04', 'level': '4.0'}, {'symbol': 'B23', 'level': '4.0'}, {'symbol': 'B30', 'level': '4.0'}, {'symbol': 'B21', 'level': '4.0'}, {'symbol': 'B25', 'level': '4.0'}, {'symbol': 'B99', 'level': '4.0'}, {'symbol': 'B29', 'level': '4.0'}, {'symbol': 'B33', 'level': '4.0'}, {'symbol': 'C22', 'level': '4.0'}, {'symbol': 'D99', 'level': '4.0'}], 'var_function-call-5303452088955298926': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}, {'symbol': 'A01M'}, {'symbol': 'A01J'}, {'symbol': 'A01B'}, {'symbol': 'A21D'}, {'symbol': 'A21C'}, {'symbol': 'A21B'}, {'symbol': 'A22B'}, {'symbol': 'A22C'}, {'symbol': 'A23P'}, {'symbol': 'A23C'}], 'var_function-call-4372299924973492362': 'file_storage/function-call-4372299924973492362.json', 'var_function-call-2493449812321384534': [{'COUNT(*)': '277813'}], 'var_function-call-10397705070662511033': [{'filing_date': 'dated 5th March 2019'}, {'filing_date': 'March the 18th, 2019'}, {'filing_date': '29th March 2019'}, {'filing_date': 'on March 29th, 2019'}, {'filing_date': '2nd April 2019'}, {'filing_date': 'on April 8th, 2019'}, {'filing_date': '15th April 2019'}, {'filing_date': 'April 19th, 2019'}, {'filing_date': '2019, April 24th'}, {'filing_date': 'April 26th, 2019'}, {'filing_date': 'on April 30th, 2019'}, {'filing_date': 'dated 1st May 2019'}, {'filing_date': '2019, May 15th'}, {'filing_date': 'May 15th, 2019'}, {'filing_date': 'June the 6th, 2019'}, {'filing_date': 'on June 7th, 2019'}, {'filing_date': '14th of June, 2019'}, {'filing_date': '2019 on Jun 14th'}, {'filing_date': 'dated 18th June 2019'}, {'filing_date': 'June the 19th, 2019'}], 'var_function-call-3133902688408324092': 'file_storage/function-call-3133902688408324092.json'}

exec(code, env_args)
