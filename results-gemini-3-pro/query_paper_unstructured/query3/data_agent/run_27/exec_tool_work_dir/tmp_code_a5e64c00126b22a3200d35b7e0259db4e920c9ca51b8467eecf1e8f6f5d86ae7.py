code = """import json
path_papers = locals()['var_function-call-11974208795470481837']
with open(path_papers, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
print(f"Total papers: {len(papers)}")
for i, p in enumerate(papers):
    print(f"--- Paper {i} ---")
    print(f"Filename: {p['filename']}")
    print(f"Header: {p['text'][:200].replace(chr(10), ' ')}")"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json', 'var_function-call-13901182043948570327': [], 'var_function-call-4571711046377204237': {'years_preview': [2015, None, None, None, None], 'total_papers': 5, 'empirical_in_first_20': 2}, 'var_function-call-11974208795470481837': 'file_storage/function-call-11974208795470481837.json'}

exec(code, env_args)
