code = """import json
import pandas as pd
import re

# Load Level 5 CPC symbols
with open(locals()['var_function-call-8605716924548816221'], 'r') as f:
    l5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patent Data
with open(locals()['var_function-call-15653579714414806466'], 'r') as f:
    patent_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

years = []
codes_found = set()

for i, entry in enumerate(patent_data):
    if i > 1000: break # Just check first 1000 to see format
    y = extract_year(entry.get('filing_date'))
    if y: years.append(y)
    
    cpc_field = entry.get('cpc')
    if cpc_field:
        try:
            cpc_list = json.loads(cpc_field)
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 4:
                    prefix = code[:4]
                    if prefix in level5_codes:
                        codes_found.add(prefix)
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "sample_years": years[:20],
    "min_year": min(years) if years else None,
    "max_year": max(years) if years else None,
    "codes_found_sample": list(codes_found)[:10],
    "level5_sample": list(level5_codes)[:10]
}))"""

env_args = {'var_function-call-8605716924548816221': 'file_storage/function-call-8605716924548816221.json', 'var_function-call-3390649654093091550': [{'COUNT(*)': '277813'}], 'var_function-call-15653579714414806466': 'file_storage/function-call-15653579714414806466.json', 'var_function-call-3948899147405893627': []}

exec(code, env_args)
