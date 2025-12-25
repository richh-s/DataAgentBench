code = """import json
import re

cpc_defs_path = locals()['var_function-call-8775067390743093543']
patents_path = locals()['var_function-call-17651004867622027777']

with open(cpc_defs_path, 'r') as f:
    cpc_defs = json.load(f)

level_5_codes = set()
for item in cpc_defs:
    try:
        lvl = float(item.get('level', 0))
        if int(lvl) == 5:
            level_5_codes.add(item['symbol'])
    except:
        pass

with open(patents_path, 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

# Global year range tracking
all_years = set()

for p in patents:
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if not match: continue
    year = int(match.group(1))
    all_years.add(year)
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    # Get unique Level 5 codes for this patent
    unique_lvl5 = set()
    for c in cpc_list:
        code = c.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level_5_codes:
                unique_lvl5.add(prefix)
            
    for c in unique_lvl5:
        if c not in counts:
            counts[c] = {}
        counts[c][year] = counts[c].get(year, 0) + 1

# Calculate EMA and find best year
alpha = 0.2
result_codes = []
debug_best_years = {}

# We need to ensure we cover 2022
limit_year = 2022
if all_years:
    limit_year = max(max(all_years), 2022)

for code, year_map in counts.items():
    years = sorted(year_map.keys())
    if not years:
        continue
    start_year = years[0]
    
    ema = year_map[start_year]
    best_ema = ema
    best_year = start_year
    
    # Iterate continuously from start_year + 1 to limit_year
    for y in range(start_year + 1, limit_year + 1):
        val = year_map.get(y, 0)
        ema = (val * alpha) + (ema * (1 - alpha))
        
        if ema > best_ema:
            best_ema = ema
            best_year = y
            
    if best_year == 2022:
        result_codes.append(code)
    
    # Store some debug info
    if len(debug_best_years) < 5:
        debug_best_years[code] = {'best_year': best_year, 'best_ema': best_ema, 'start_year': start_year, 'limit_year': limit_year}

print("__RESULT__:")
print(json.dumps(result_codes))"""

env_args = {'var_function-call-6641923460859800772': 'file_storage/function-call-6641923460859800772.json', 'var_function-call-6641923460859799993': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-4289607868665699138': [{'count': '260808'}], 'var_function-call-4289607868665698023': [{'count(*)': '277813'}], 'var_function-call-8775067390743093543': 'file_storage/function-call-8775067390743093543.json', 'var_function-call-17651004867622027777': 'file_storage/function-call-17651004867622027777.json', 'var_function-call-5059798945412610512': [], 'var_function-call-15245929960655701249': [], 'var_function-call-11939134990751395154': 'DONE', 'var_function-call-7224638551277790076': {'level_5_count': 677, 'codes_with_filings': 0}, 'var_function-call-8938606408172290764': {'sample_patent_codes': ['H01L21/50', 'F25J1/0022', 'B60Y2306/05', 'B65B35/38', 'B32B29/02', 'H01L27/148', 'A61F2/4425', 'H04N5/232', 'H02J7/342', 'A61K31/7052'], 'levels_found_in_patents': ['10.0', '9.0', '8.0', '10.0', '8.0', '11.0', '12.0', '9.0', '10.0', '9.0', '10.0', '8.0', '9.0', '8.0', '8.0', '9.0', '11.0', '11.0', '13.0', '10.0'], 'sample_level_5_from_db': ['A01H', 'A01F', 'A01C', 'A01G', 'A23J', 'A01N', 'A01P', 'A01D', 'A01L', 'A01K']}, 'var_function-call-14311176162521282890': {'codes_found_in_patents': 0}, 'var_function-call-5852688278291348107': {'level_5_count': 677, 'sample_level_5': ['F21H', 'C07C', 'E05D', 'C07F', 'G16Y', 'B60P', 'D10B', 'B24C', 'C12P', 'F24B'], 'lengths': [4], 'H01L_in_level5': True, 'sample_repr': ["'F21H'", "'C07C'", "'E05D'", "'C07F'", "'G16Y'"]}, 'var_function-call-454453905919471500': {'patents_count': 277813, 'found_patent_cpc_str': '[\n  {\n    "code": "H01L27/14685",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L25/0657",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01T7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/02164",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L25/0657",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/144",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L2225/06544",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/1485",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/144",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/02271",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/144",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L31/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14812",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/148",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01T1/242",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01T1/242",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/30625",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L21/265",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14687",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/146",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14812",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14875",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L31/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/3065",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/146",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/1485",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14687",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L29/76891",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L23/481",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14875",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L31/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/146",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/1485",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/02271",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14812",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14687",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/3065",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01T1/242",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L25/0657",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/144",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/146",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/265",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L27/14875",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L31/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L2225/06544",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L23/481",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L21/02164",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L29/76891",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01L21/30625",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01T7/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'parsed_codes': ['H01L27/14685', 'H01L25/0657', 'G01T7/00', 'H01L21/02164', 'H01L25/0657', 'H01L27/144', 'H01L2225/06544', 'H01L27/1485', 'H01L27/144', 'H01L21/02271', 'H01L27/144', 'H01L31/08', 'H01L27/14812', 'H01L27/148', 'G01T1/242', 'G01T1/242', 'H01L21/30625', 'H01L21/265', 'H01L27/14', 'H01L27/14687', 'H01L27/146', 'H01L27/14812', 'H01L27/14875', 'H01L27/14', 'H01L31/08', 'H01L21/3065', 'H01L27/146', 'H01L27/1485', 'H01L27/14687', 'H01L29/76891', 'H01L23/481', 'H01L27/14875', 'H01L27/14685', 'H01L31/08', 'H01L27/146', 'H01L27/1485', 'H01L21/02271', 'H01L27/14812', 'H01L27/14687', 'H01L21/3065', 'G01T1/242', 'H01L25/0657', 'H01L27/144', 'H01L27/146', 'H01L27/14', 'H01L27/14685', 'H01L21/265', 'H01L27/14875', 'H01L31/08', 'H01L2225/06544', 'H01L23/481', 'H01L21/02164', 'H01L29/76891', 'H01L21/30625', 'G01T7/00'], 'matches': ['H01L', 'H01L', 'G01T', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'G01T', 'G01T', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'G01T', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'H01L', 'G01T'], 'is_target_in_set': True}}

exec(code, env_args)
