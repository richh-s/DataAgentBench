code = """import json
import re

# Load level 5 symbols
with open(locals()['var_function-call-7269545379291600604'], 'r') as f:
    level5_data = json.load(f)
level5_symbols = [item['symbol'] for item in level5_data]

# Check lengths
lengths = list(set(len(s) for s in level5_symbols))
sample_symbols = level5_symbols[:10]

# Load publications
with open(locals()['var_function-call-7269545379291602853'], 'r') as f:
    publications = json.load(f)

# Check years
year_pattern = re.compile(r'\b(19|20)\d{2}\b')
years = []
for pub in publications[:1000]: # Check first 1000
    fdate = pub.get('filing_date', '')
    match = year_pattern.search(fdate)
    if match:
        years.append(int(match.group(0)))

max_year_sample = max(years) if years else None

# Check matching
match_count = 0
level5_set = set(level5_symbols)
for pub in publications[:100]:
    cpc_str = pub.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    found = False
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4 and code[:4] in level5_set:
            found = True
            break
    if found:
        match_count += 1

result = {
    "lengths": lengths,
    "sample_symbols": sample_symbols,
    "sample_years": years[:10],
    "max_year_sample": max_year_sample,
    "match_count_first_100": match_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2156360617671993543': 'file_storage/function-call-2156360617671993543.json', 'var_function-call-2156360617671993474': [{'symbol': 'A01K2227/108', 'level': '9.0'}, {'symbol': 'A01K2227/105', 'level': '9.0'}, {'symbol': 'A01K2227/101', 'level': '9.0'}, {'symbol': 'A01K2227/107', 'level': '9.0'}, {'symbol': 'A01K2227/103', 'level': '9.0'}], 'var_function-call-13197801515955793315': [{'count(*)': '277813'}], 'var_function-call-13197801515955789834': [{'count': '677'}], 'var_function-call-7269545379291600604': 'file_storage/function-call-7269545379291600604.json', 'var_function-call-7269545379291602853': 'file_storage/function-call-7269545379291602853.json', 'var_function-call-5018208914705499515': []}

exec(code, env_args)
