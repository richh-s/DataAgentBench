code = """import json
import re

with open(locals()['var_function-call-7168665038669852193'], 'r') as f:
    definitions = json.load(f)
valid_cpcs = set(d['symbol'] for d in definitions)

with open(locals()['var_function-call-12636907471574372890'], 'r') as f:
    patents = json.load(f)

counts = {}
year_pattern = re.compile(r'\b(19|20)\d{2}\b')
all_years = set()

for p in patents:
    cpc = p.get('cpc_l5')
    date_str = p.get('filing_date')
    if not cpc or not date_str: continue
    if cpc not in valid_cpcs: continue
    match = year_pattern.search(date_str)
    if match:
        year = int(match.group(0))
        all_years.add(year)
        if cpc not in counts: counts[cpc] = {}
        counts[cpc][year] = counts[cpc].get(year, 0) + 1

print("__RESULT__:")
print(json.dumps({
    "min_year": min(all_years) if all_years else None,
    "max_year": max(all_years) if all_years else None,
    "sample_counts": list(counts.items())[:5]
}))"""

env_args = {'var_function-call-7168665038669852193': 'file_storage/function-call-7168665038669852193.json', 'var_function-call-10792060600082410393': 'file_storage/function-call-10792060600082410393.json', 'var_function-call-17520737272150592810': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C', 'level': '2.0'}, {'symbol': 'C01', 'level': '4.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-1418283475394270998': [{'count(*)': '277813'}], 'var_function-call-6985419727303954916': [{'code': 'C01B33/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01B35/00', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0565', 'filing_date': 'dated 5th March 2019'}, {'code': 'H01M10/0562', 'filing_date': 'dated 5th March 2019'}, {'code': 'C01G45/006', 'filing_date': 'dated 5th March 2019'}], 'var_function-call-12636907471574372890': 'file_storage/function-call-12636907471574372890.json', 'var_function-call-6477679623935836888': []}

exec(code, env_args)
