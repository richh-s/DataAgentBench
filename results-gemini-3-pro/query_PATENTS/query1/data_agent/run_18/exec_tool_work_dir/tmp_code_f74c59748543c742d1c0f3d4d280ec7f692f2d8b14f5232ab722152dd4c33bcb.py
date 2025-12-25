code = """import json
import re

# Load Level 5 symbols
with open(locals()['var_function-call-5087905462925890411'], 'r') as f:
    l5_data = json.load(f)
level5_symbols = set(item['symbol'] for item in l5_data)

# Load Publications
with open(locals()['var_function-call-10591805906603829324'], 'r') as f:
    pubs_data = json.load(f)

# Regex for year: simple 4 digits
year_pattern = re.compile(r'(19|20)\d{2}')

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
    # matches will be a list of strings if no groups, or tuples if groups.
    # The regex (19|20)\d{2} contains a group. 
    # findall returns the captured group? No, if one group, it returns list of strings of that group.
    # Wait, (19|20) is a capturing group.
    # So findall("2019") with r'(19|20)\d{2}' matches "2019". 
    # Group 1 is "20". The whole match is "2019".
    # re.findall returns only captured groups if there are any.
    # So it returns ['20']. That's not the year.
    # I should use non-capturing group (?:19|20) or just match the whole thing.
    
    # Correct regex:
    y_matches = re.findall(r'(?:19|20)\d{2}', f_date)
    if not y_matches:
        continue
    
    year = int(y_matches[-1]) # Use last found year
    
    if year > 2024 or year < 1900: 
        continue

    # Extract CPCs
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_cpcs = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            subclass = code[:4]
            if subclass in level5_symbols:
                patent_cpcs.add(subclass)
    
    for cpc in patent_cpcs:
        if cpc not in counts:
            counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

# Calculate EMA
alpha = 0.2
result_cpcs = []

# Global year range to ensure we cover up to 2022
# Actually, the query says "highest EMA ... each year".
# And "whose best year is 2022".
# This means for a CPC, among all years it has an EMA, 2022 is the max.
# We should calculate EMA for years present in the data?
# Or should we fill missing years?
# If a technology has filings in 2018 and 2020, but 0 in 2019.
# EMA should update for 2019 with 0 count?
# Yes, typically time series analysis requires continuous intervals.
# I will fill missing years between min_year and max(data_year, 2022).

for cpc, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
        
    min_year = years[0]
    max_year_data = years[-1]
    end_year = max(max_year_data, 2022)
    
    ema = year_counts[min_year] # Initialize with first year count
    
    max_ema = ema
    best_year = min_year
    
    # Iterate from min_year + 1 to end_year
    current_ema = ema
    
    for y in range(min_year + 1, end_year + 1):
        count = year_counts.get(y, 0)
        current_ema = alpha * count + (1 - alpha) * current_ema
        
        if current_ema > max_ema:
            max_ema = current_ema
            best_year = y
            
        # Tie-breaking? "Highest" usually implies strictly greater or first?
        # Usually first or last. Let's stick to strict > for now, or >= if we favor later years.
        # But standard `max` finds the first occurrence or specific one.
        # Let's assume strict greater updates the max.
    
    if best_year == 2022:
        result_cpcs.append(cpc)

print("__RESULT__:")
print(json.dumps(result_cpcs))"""

env_args = {'var_function-call-7068108288998237179': [{'filing_date': 'dated 5th March 2019', 'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-7068108288998238214': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-11289752396498631167': [{'level': '2.0', 'symbol': 'A'}, {'level': '2.0', 'symbol': 'B'}, {'level': '2.0', 'symbol': 'C'}, {'level': '2.0', 'symbol': 'D'}, {'level': '2.0', 'symbol': 'E'}, {'level': '2.0', 'symbol': 'F'}, {'level': '2.0', 'symbol': 'G'}, {'level': '2.0', 'symbol': 'H'}, {'level': '2.0', 'symbol': 'Y'}, {'level': '4.0', 'symbol': 'A01'}, {'level': '4.0', 'symbol': 'A21'}, {'level': '4.0', 'symbol': 'A22'}, {'level': '4.0', 'symbol': 'A23'}, {'level': '4.0', 'symbol': 'A24'}, {'level': '4.0', 'symbol': 'A41'}, {'level': '4.0', 'symbol': 'A42'}, {'level': '4.0', 'symbol': 'A43'}, {'level': '4.0', 'symbol': 'A44'}, {'level': '4.0', 'symbol': 'A45'}, {'level': '4.0', 'symbol': 'A46'}], 'var_function-call-3767859603655167710': [{'level': '7.0', 'symbol': 'C13B50/00'}, {'level': '8.0', 'symbol': 'H04Q2213/296'}, {'level': '7.0', 'symbol': 'C13B40/00'}, {'level': '7.0', 'symbol': 'C13B99/00'}, {'level': '7.0', 'symbol': 'C13B45/00'}, {'level': '7.0', 'symbol': 'C21B3/00'}, {'level': '7.0', 'symbol': 'A01B59/00'}, {'level': '8.0', 'symbol': 'H10N89/02'}, {'level': '7.0', 'symbol': 'A01B19/00'}, {'level': '8.0', 'symbol': 'B21D7/04'}], 'var_function-call-5087905462925890411': 'file_storage/function-call-5087905462925890411.json', 'var_function-call-16861969253203945337': [{'COUNT(*)': '277813'}], 'var_function-call-10591805906603829324': 'file_storage/function-call-10591805906603829324.json', 'var_function-call-10128769687173690775': [], 'var_function-call-12914436660827401054': {'total_l5': 677, 'total_pubs': 277813, 'dates_parsed': 0, 'valid_cpcs_occurrences': 0, 'sample_cpc_found': [], 'sample_l5': ['Y02C', 'B24D', 'B41N', 'B65F', 'C08K', 'A63C', 'B67B', 'D06B', 'F16J', 'C09F']}}

exec(code, env_args)
