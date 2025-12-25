code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-5087905462925890411'], 'r') as f:
    l5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in l5_data)

# Load Publications
with open(locals()['var_function-call-10591805906603829324'], 'r') as f:
    pubs_data = json.load(f)

# Regex for year
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

# Counting
counts = {} # {cpc: {year: count}}

for pub in pubs_data:
    f_date = pub.get('filing_date')
    cpc_str = pub.get('cpc')
    
    if not f_date or not cpc_str:
        continue
        
    # Extract Year
    matches = year_pattern.findall(f_date)
    if not matches:
        continue
    # Take the last match as the year (most likely)
    # The regex returns the group, but we want the full match.
    # Wait, (19|20)\d{2} has a group. findall returns list of groups?
    # Let's use search or iterate.
    # Actually, the group (19|20) captures the century.
    # Let's change regex to capture the whole year.
    
    # Simpler regex finding 4 digits
    y_matches = re.findall(r'\b((?:19|20)\d{2})\b', f_date)
    if not y_matches:
        continue
    year = int(y_matches[-1]) # Use last year found in string
    
    if year > 2024 or year < 1900: # Sanity check
        continue

    # Extract CPCs
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    # Get unique level 5 codes for this patent
    patent_cpcs = set()
    for item in cpc_list:
        code = item.get('code', '')
        # Truncate to 4 chars (Subclass)
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_symbols:
                patent_cpcs.add(subclass)
    
    # Update counts
    for cpc in patent_cpcs:
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA and find best year
# Alpha = 0.2
alpha = 0.2
result_cpcs = []

for cpc, year_counts in counts.items():
    if not year_counts:
        continue
        
    years = sorted(year_counts.keys())
    min_year = years[0]
    # We need to calculate up to 2022 at least.
    # But if data goes beyond 2022, we should consider it?
    # "whose best year is 2022". This implies we compare 2022 EMA against all other years.
    # So we should go up to max(years) or 2022, whichever is larger.
    max_year = max(years[-1], 2022)
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    # Initialize EMA with the first year's count
    # But technically, EMA starts accumulating.
    # Standard: EMA_t = alpha * x_t + (1-alpha) * EMA_t-1
    # For first point, EMA_0 = x_0.
    
    ema = year_counts.get(min_year, 0)
    
    if min_year == best_year: # initialization logic
        pass 
        
    # Store EMAs to find max
    # We need to track the max_ema and best_year during the loop
    
    # Check first year
    current_max_ema = ema
    current_best_year = min_year
    
    # Iterate from min_year + 1 to max_year
    for y in range(min_year + 1, max_year + 1):
        count = year_counts.get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        
        if ema > current_max_ema:
            current_max_ema = ema
            current_best_year = y
            
    if current_best_year == 2022:
        result_cpcs.append(cpc)

print("__RESULT__:")
print(json.dumps(result_cpcs))"""

env_args = {'var_function-call-7068108288998237179': [{'filing_date': 'dated 5th March 2019', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-7068108288998238214': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-11289752396498631167': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}], 'var_function-call-3767859603655167710': [{'level': '7.0', 'symbol': 'C13B50/00'}, {'level': '8.0', 'symbol': 'H04Q2213/296'}, {'level': '7.0', 'symbol': 'C13B40/00'}, {'level': '7.0', 'symbol': 'C13B99/00'}, {'level': '7.0', 'symbol': 'C13B45/00'}, {'level': '7.0', 'symbol': 'C21B3/00'}, {'level': '7.0', 'symbol': 'A01B59/00'}, {'level': '8.0', 'symbol': 'H10N89/02'}, {'level': '7.0', 'symbol': 'A01B19/00'}, {'level': '8.0', 'symbol': 'B21D7/04'}], 'var_function-call-5087905462925890411': 'file_storage/function-call-5087905462925890411.json', 'var_function-call-16861969253203945337': [{'COUNT(*)': '277813'}], 'var_function-call-10591805906603829324': 'file_storage/function-call-10591805906603829324.json'}

exec(code, env_args)
