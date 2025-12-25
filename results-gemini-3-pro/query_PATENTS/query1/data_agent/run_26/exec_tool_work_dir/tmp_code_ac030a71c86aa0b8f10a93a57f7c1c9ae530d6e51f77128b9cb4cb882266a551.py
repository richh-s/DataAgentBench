code = """import json
import re

path_level5 = locals()['var_function-call-8552121385304934685']
path_patents = locals()['var_function-call-12122079112080214207']

with open(path_level5, 'r') as f:
    level5_list = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_list)

with open(path_patents, 'r') as f:
    patent_data = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

years_found = set()
patents_with_matches = 0
total_patents = 0

sample_counts = {}

for row in patent_data:
    total_patents += 1
    f_date = row.get('filing_date')
    if not f_date:
        continue
    
    match = year_pattern.search(f_date)
    if not match:
        continue
    year = int(match.group(0))
    years_found.add(year)
    
    cpc_str = row.get('cpc')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
    except:
        continue
    
    matched = False
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 4:
            prefix = code[:4]
            if prefix in level5_symbols:
                matched = True
                if prefix not in sample_counts:
                    sample_counts[prefix] = {}
                sample_counts[prefix][year] = sample_counts[prefix].get(year, 0) + 1
    
    if matched:
        patents_with_matches += 1

print("__RESULT__:")
print(json.dumps({
    "min_year": min(years_found) if years_found else None,
    "max_year": max(years_found) if years_found else None,
    "total_patents": total_patents,
    "patents_with_matches": patents_with_matches,
    "sample_keys": list(sample_counts.keys())[:10],
    "sample_data": {k: sample_counts[k] for k in list(sample_counts.keys())[:2]}
}))"""

env_args = {'var_function-call-1397089811542180174': ['publicationinfo'], 'var_function-call-1397089811542180177': ['cpc_definition'], 'var_function-call-3017323399836205737': 'file_storage/function-call-3017323399836205737.json', 'var_function-call-3017323399836208786': [{'count': '677'}], 'var_function-call-16375230660246420135': [{'count(*)': '277813'}], 'var_function-call-8552121385304934685': 'file_storage/function-call-8552121385304934685.json', 'var_function-call-12122079112080214207': 'file_storage/function-call-12122079112080214207.json', 'var_function-call-16341698527960964951': []}

exec(code, env_args)
