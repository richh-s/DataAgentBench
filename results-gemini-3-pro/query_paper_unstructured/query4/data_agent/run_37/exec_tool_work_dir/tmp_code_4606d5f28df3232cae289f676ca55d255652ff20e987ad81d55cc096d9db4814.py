code = """import json

file_path = locals()['var_function-call-7710092852733637321']
with open(file_path, 'r') as f:
    papers = json.load(f)

total = len(papers)
year_2016_count = 0
domain_pa_count = 0
both_count = 0

headers_sample = []

for i, p in enumerate(papers):
    text = p.get('text', '')
    header = text[:500]
    if i < 3:
        headers_sample.append(header)
    
    if '2016' in header:
        year_2016_count += 1
    
    if 'physical activity' in text.lower():
        domain_pa_count += 1
        
    if '2016' in header and 'physical activity' in text.lower():
        both_count += 1

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "year_2016_count": year_2016_count,
    "domain_pa_count": domain_pa_count,
    "both_count": both_count,
    "headers_sample": headers_sample
}))"""

env_args = {'var_function-call-8028739805573563198': ['paper_docs'], 'var_function-call-8028739805573566195': ['Citations', 'sqlite_sequence'], 'var_function-call-12468047497345130248': 'file_storage/function-call-12468047497345130248.json', 'var_function-call-7710092852733637321': 'file_storage/function-call-7710092852733637321.json', 'var_function-call-2111382860012225725': []}

exec(code, env_args)
