code = """import json
import pandas as pd
import re

# Load CPC Definitions
cpc_def_path = locals()['var_function-call-5294950170102655327']
with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)
cpc_map = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Load Patents
patents_path = locals()['var_function-call-16435967301398580660']
with open(patents_path, 'r') as f:
    patents = json.load(f)

# Regex for Germany (avoiding \b issues)
# Matches "from DE", "DE patent", "DE-[number]"
# (?:^|\W) matches start of string or non-word char
de_pattern = re.compile(r'(?:^|\W)from DE(?:$|\W)|(?:^|\W)DE-\d+')

count_by_cpc_year = {}

def parse_date(date_str):
    # Remove common suffixes
    clean = re.sub(r'(st|nd|rd|th|on|dated|,|of|the)', '', date_str)
    try:
        return pd.to_datetime(clean).date()
    except:
        return None

for p in patents:
    # 1. Filter by Germany
    if not de_pattern.search(p.get('Patents_info', '')):
        continue
    
    # 2. Filter by Grant Date (H2 2019)
    g_date = parse_date(p.get('grant_date', ''))
    if not g_date:
        continue
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue

    # 3. Get Filing Year
    f_date = parse_date(p.get('filing_date', ''))
    if not f_date:
        continue
    f_year = f_date.year

    # 4. Process CPC
    cpc_raw = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_raw)
    except:
        continue
    
    # Identify unique Level 4 CPCs for this patent
    patent_cpcs = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            l4 = code[:3]
            # Verify it is a valid Level 4 symbol
            if l4 in cpc_map:
                patent_cpcs.add(l4)
    
    # Increment counts
    for cpc in patent_cpcs:
        if cpc not in count_by_cpc_year:
            count_by_cpc_year[cpc] = {}
        count_by_cpc_year[cpc][f_year] = count_by_cpc_year[cpc].get(f_year, 0) + 1

# Calculate EMA and find best year
results = []
alpha = 0.1

for cpc, years_dict in count_by_cpc_year.items():
    if not years_dict:
        continue
    
    min_year = min(years_dict.keys())
    max_year = max(years_dict.keys())
    
    ema = 0
    max_ema = -1
    best_year = -1
    
    # Start from min_year
    # Initialize EMA with the count of the first year
    ema = years_dict.get(min_year, 0)
    if ema > max_ema:
        max_ema = ema
        best_year = min_year
    
    # Iterate through subsequent years
    for y in range(min_year + 1, max_year + 1):
        count = years_dict.get(y, 0)
        ema = alpha * count + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        "full_title": cpc_map[cpc],
        "cpc_group_code": cpc,
        "best_year": best_year,
        "max_ema": max_ema
    })

# Sort by max_ema descending
results.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9027804141299956237': ['publicationinfo'], 'var_function-call-9027804141299956054': ['cpc_definition'], 'var_function-call-13891800015006892835': 'file_storage/function-call-13891800015006892835.json', 'var_function-call-13748478948310889332': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_function-call-6605672204215736455': [{'symbol': 'B', 'level': '2.0'}, {'symbol': 'H', 'level': '2.0'}, {'symbol': 'Y', 'level': '2.0'}, {'symbol': 'D', 'level': '2.0'}, {'symbol': 'F', 'level': '2.0'}, {'symbol': 'E', 'level': '2.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'G', 'level': '2.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_function-call-8398798029853849913': [], 'var_function-call-7499511620997998355': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-3699617742520592814': [{'symbol': 'C01', 'titleFull': 'INORGANIC CHEMISTRY'}], 'var_function-call-16435967301398580660': 'file_storage/function-call-16435967301398580660.json', 'var_function-call-11235697834189481417': [{'symbol': 'A01', 'len': '3'}, {'symbol': 'A21', 'len': '3'}, {'symbol': 'A22', 'len': '3'}, {'symbol': 'A23', 'len': '3'}, {'symbol': 'A24', 'len': '3'}, {'symbol': 'A41', 'len': '3'}, {'symbol': 'A42', 'len': '3'}, {'symbol': 'A43', 'len': '3'}, {'symbol': 'A44', 'len': '3'}, {'symbol': 'A45', 'len': '3'}], 'var_function-call-12448420585321566256': [], 'var_function-call-5294950170102655327': 'file_storage/function-call-5294950170102655327.json', 'var_function-call-4570370100524341779': [], 'var_function-call-3803934444735919657': {'total': 216, 'matches_de': 0, 'parsed_dates_in_subset': 182, 'h2_2019': 89, 'failed_dates': []}, 'var_function-call-5584651003589227180': ['Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'Patent application (number US-201415314902-A) from US, held by HEWLETT PACKARD ENTPR DEV LP, with publication number US-10176043-B2.'], 'var_function-call-6562417655425560090': {'string': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'match': 'None', 'pattern': '\x08from DE\x08|\x08DE-\\d+'}}

exec(code, env_args)
