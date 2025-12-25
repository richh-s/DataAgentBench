code = """import json
import re
from collections import Counter

# Load Level 5 CPC symbols
with open(locals()['var_function-call-11899126964537840596'], 'r') as f:
    cpc_defs = json.load(f)
level_5_symbols = set(item['symbol'] for item in cpc_defs)

# Load Patent Data
with open(locals()['var_function-call-2886696176158669052'], 'r') as f:
    patents = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

years_found = []
symbols_matched = 0
total_patents = 0

for p in patents[:10000]: # Check first 10000
    total_patents += 1
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        years_found.append(int(match.group(0)))
    
    cpc_str = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level_5_symbols:
                symbols_matched += 1

print("__RESULT__:")
print(json.dumps({
    "years_sample": list(set(years_found))[:20],
    "min_year": min(years_found) if years_found else None,
    "max_year": max(years_found) if years_found else None,
    "symbols_matched_count": symbols_matched,
    "total_patents_checked": total_patents
}))"""

env_args = {'var_function-call-11899126964537840596': 'file_storage/function-call-11899126964537840596.json', 'var_function-call-13245455590723009020': [{'count(*)': '277813'}], 'var_function-call-2886696176158669052': 'file_storage/function-call-2886696176158669052.json', 'var_function-call-5697690738001880409': []}

exec(code, env_args)
