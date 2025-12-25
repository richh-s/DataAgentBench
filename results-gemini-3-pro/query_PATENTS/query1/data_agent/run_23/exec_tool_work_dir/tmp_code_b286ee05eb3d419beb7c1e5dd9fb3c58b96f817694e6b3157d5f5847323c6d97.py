code = """import json
import re
import pandas as pd

# Load level 5 symbols
with open(locals()['var_function-call-12377978627195880798'], 'r') as f:
    level5_data = json.load(f)
level5_codes = set(item['symbol'] for item in level5_data)

# Load publication data
with open(locals()['var_function-call-17981272633275780013'], 'r') as f:
    publications = json.load(f)

# Debug counters
year_counts_global = {}
code_match_count = 0
total_pubs = len(publications)

year_regex = re.compile(r'\b(19|20)\d{2}\b')

for pub in publications[:1000]: # Check first 1000
    filing_date = pub.get('filing_date', '')
    match = year_regex.search(filing_date)
    if match:
        year = int(match.group(0))
        year_counts_global[year] = year_counts_global.get(year, 0) + 1
    
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        for entry in cpc_list:
            code = entry.get('code', '')
            if len(code) >= 4:
                prefix = code[:4]
                if prefix in level5_codes:
                    code_match_count += 1
    except:
        pass

print("__RESULT__:")
print(json.dumps({
    "years_found": sorted(year_counts_global.keys()), 
    "total_pubs": total_pubs,
    "code_matches_in_sample": code_match_count,
    "sample_level5": list(level5_codes)[:5]
}))"""

env_args = {'var_function-call-11743318916466858898': 'file_storage/function-call-11743318916466858898.json', 'var_function-call-16238834244750781196': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-12377978627195880798': 'file_storage/function-call-12377978627195880798.json', 'var_function-call-17981272633275780013': 'file_storage/function-call-17981272633275780013.json', 'var_function-call-7974876835116330076': []}

exec(code, env_args)
