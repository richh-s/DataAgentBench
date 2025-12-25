code = """import json
import pandas as pd
from dateutil import parser
import re

# Get file paths from local variables
path_l4 = locals()['var_function-call-13370481740577550177']
path_patents = locals()['var_function-call-15045618065598234676']

# Load Level 4 definitions
with open(path_l4, 'r') as f:
    level4_data = json.load(f)

level4_defs = {item['symbol']: item['titleFull'] for item in level4_data}
level4_symbols = set(level4_defs.keys())

# Check symbol lengths
lengths = {len(s) for s in level4_symbols}
# print(f"Level 4 symbol lengths: {lengths}")

# Load Patent Data
with open(path_patents, 'r') as f:
    patents = json.load(f)

# print(f"Total patents loaded: {len(patents)}")

def clean_date(d_str):
    if not d_str:
        return None
    d_str = str(d_str).lower().replace('dated', '').replace('on', '').replace('of', '').strip()
    return d_str

def parse_date(d_str):
    clean = clean_date(d_str)
    if not clean: return None
    try:
        return parser.parse(clean, fuzzy=True)
    except:
        return None

target_groups = set()
yearly_counts = {} # {group: {year: count}}
max_len = max(lengths) if lengths else 3

def get_level4_code(full_code):
    for l in sorted(lengths, reverse=True):
        if len(full_code) >= l:
            prefix = full_code[:l]
            if prefix in level4_symbols:
                return prefix
    return None

H2_2019_START = pd.Timestamp("2019-07-01")
H2_2019_END = pd.Timestamp("2019-12-31")

for p in patents:
    p_info = p.get('Patents_info', '')
    if "DE-" not in p_info and "Germany" not in p_info:
        continue

    g_date = parse_date(p.get('grant_date'))
    f_date = parse_date(p.get('filing_date'))
    
    if not f_date:
        continue
    f_year = f_date.year
    
    try:
        cpc_list = json.loads(p.get('cpc', '[]'))
    except:
        continue
        
    p_groups = set()
    for entry in cpc_list:
        code = entry.get('code', '')
        l4 = get_level4_code(code)
        if l4:
            p_groups.add(l4)
    
    if g_date and H2_2019_START <= g_date <= H2_2019_END:
        target_groups.update(p_groups)
        
    for g in p_groups:
        if g not in yearly_counts:
            yearly_counts[g] = {}
        yearly_counts[g][f_year] = yearly_counts[g].get(f_year, 0) + 1

results = []
alpha = 0.1

for g in target_groups:
    counts = yearly_counts.get(g, {})
    if not counts:
        continue
    
    years = sorted(counts.keys())
    if not years:
        continue
        
    start_year = years[0]
    end_year = years[-1]
    
    ema = None
    max_ema = -1
    best_year = None
    
    # Iterate from start year to latest filing year in the dataset for this group
    full_years = range(start_year, end_year + 1)
    
    for y in full_years:
        cnt = counts.get(y, 0)
        if ema is None:
            ema = cnt
        else:
            ema = alpha * cnt + (1 - alpha) * ema
        
        if ema > max_ema:
            max_ema = ema
            best_year = y
            
    results.append({
        "full_title": level4_defs[g],
        "cpc_group_code": g,
        "best_year": int(best_year),
        "max_ema": float(max_ema)
    })

results.sort(key=lambda x: x['max_ema'], reverse=True)

print("__RESULT__:")
print(json.dumps(results)) # Return all"""

env_args = {'var_function-call-17972723781578325660': 'file_storage/function-call-17972723781578325660.json', 'var_function-call-15002815932378172329': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-548673809424394196': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-3614271535354761552': [{'symbol': 'B04', 'level': '4.0'}, {'symbol': 'B23', 'level': '4.0'}, {'symbol': 'B30', 'level': '4.0'}, {'symbol': 'B21', 'level': '4.0'}, {'symbol': 'B25', 'level': '4.0'}], 'var_function-call-8260154943745211595': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-3584803094576377962': [{'count(*)': '277813'}], 'var_function-call-10164500035505625648': [{'count(*)': '11644'}], 'var_function-call-13370481740577550177': 'file_storage/function-call-13370481740577550177.json', 'var_function-call-15045618065598234676': 'file_storage/function-call-15045618065598234676.json'}

exec(code, env_args)
