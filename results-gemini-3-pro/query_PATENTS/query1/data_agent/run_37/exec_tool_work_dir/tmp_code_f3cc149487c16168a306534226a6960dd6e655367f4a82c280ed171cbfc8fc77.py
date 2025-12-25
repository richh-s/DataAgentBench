code = """import json
import re

# Load publications
try:
    with open('var_function-call-7906511271909197248', 'r') as f:
        pubs = json.load(f)
except:
    pubs = []

years = []
for p in pubs:
    d = p.get('filing_date')
    if d:
        m = re.search(r'\b(19|20)\d{2}\b', d)
        if m:
            years.append(int(m.group(0)))

if years:
    print(f"Min year: {min(years)}")
    print(f"Max year: {max(years)}")
    print(f"Total years parsed: {len(years)}")
else:
    print("No years parsed.")

# Check CPC parsing
sample_cpc = []
l5_symbols = set()
try:
    with open('var_function-call-3410019379130597084', 'r') as f:
        l5_data = json.load(f)
    l5_symbols = set(item['symbol'] for item in l5_data)
except:
    pass

cpc_hits = 0
for p in pubs[:100]:
    cpc_str = p.get('cpc')
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            for item in cpc_list:
                code = item.get('code')
                if code and len(code) >= 4:
                    cand = code[:4]
                    if cand in l5_symbols:
                        cpc_hits += 1
                        if len(sample_cpc) < 10:
                            sample_cpc.append(cand)
        except:
            pass

print(f"Sample matched L5 symbols: {sample_cpc}")
print(f"Total CPC hits in first 100 docs: {cpc_hits}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-3412756028934432070': 'file_storage/function-call-3412756028934432070.json', 'var_function-call-3412756028934430865': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-3410019379130597084': 'file_storage/function-call-3410019379130597084.json', 'var_function-call-10501866726357771340': [{'level': '2.0', 'sample_symbol': 'Y'}, {'level': '4.0', 'sample_symbol': 'Y10'}, {'level': '5.0', 'sample_symbol': 'Y10T'}, {'level': '7.0', 'sample_symbol': 'Y10T83/00'}, {'level': '8.0', 'sample_symbol': 'Y10T83/97'}, {'level': '9.0', 'sample_symbol': 'Y10T83/96'}, {'level': '10.0', 'sample_symbol': 'Y10T83/9498'}, {'level': '11.0', 'sample_symbol': 'Y10T83/949'}, {'level': '12.0', 'sample_symbol': 'Y10T83/9486'}, {'level': '13.0', 'sample_symbol': 'Y10T83/9341'}, {'level': '14.0', 'sample_symbol': 'Y10T83/9338'}, {'level': '15.0', 'sample_symbol': 'Y10T83/656'}, {'level': '16.0', 'sample_symbol': 'Y10T70/7616'}, {'level': '17.0', 'sample_symbol': 'Y10T70/761'}, {'level': '18.0', 'sample_symbol': 'Y10T70/5473'}, {'level': '19.0', 'sample_symbol': 'H01L2224/45984'}], 'var_function-call-7906511271909197248': 'file_storage/function-call-7906511271909197248.json', 'var_function-call-10796942973819325316': []}

exec(code, env_args)
