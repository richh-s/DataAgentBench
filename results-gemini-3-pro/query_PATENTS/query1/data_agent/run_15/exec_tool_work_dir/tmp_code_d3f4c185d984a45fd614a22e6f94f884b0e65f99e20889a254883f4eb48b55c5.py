code = """import json
import re

path_symbols = locals()['var_function-call-4195696039592522231']
path_patents = locals()['var_function-call-4195696039592525610']

with open(path_symbols, 'r') as f:
    symbols_data = json.load(f)
valid_symbols = set(item['symbol'] for item in symbols_data)

with open(path_patents, 'r') as f:
    patents_data = json.load(f)

counts = {s: {} for s in valid_symbols}
all_years = set()
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

matched_patents = 0
total_patents = 0

for row in patents_data:
    filing_date = row.get('filing_date', '')
    match = year_pattern.search(filing_date)
    if not match:
        continue
    year = int(match.group(0))
    all_years.add(year)
    total_patents += 1
    
    cpc_str = row.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
        
    patent_symbols = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            sub = code[:4]
            if sub in valid_symbols:
                patent_symbols.add(sub)
    
    if patent_symbols:
        matched_patents += 1
    
    for s in patent_symbols:
        counts[s][year] = counts[s].get(year, 0) + 1

info = {
    "min_year": min(all_years) if all_years else None,
    "max_year": max(all_years) if all_years else None,
    "total_patents_with_year": total_patents,
    "matched_patents": matched_patents,
    "sample_counts": {k: counts[k] for k in list(counts.keys())[:5]}
}

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-1606092503254054957': ['cpc_definition'], 'var_function-call-1606092503254055080': ['publicationinfo'], 'var_function-call-49990340508428720': [{'count': '677'}], 'var_function-call-49990340508428761': 'file_storage/function-call-49990340508428761.json', 'var_function-call-11885506798250293123': [{'count(*)': '277813'}], 'var_function-call-4195696039592522231': 'file_storage/function-call-4195696039592522231.json', 'var_function-call-4195696039592525610': 'file_storage/function-call-4195696039592525610.json', 'var_function-call-937466644733390942': []}

exec(code, env_args)
