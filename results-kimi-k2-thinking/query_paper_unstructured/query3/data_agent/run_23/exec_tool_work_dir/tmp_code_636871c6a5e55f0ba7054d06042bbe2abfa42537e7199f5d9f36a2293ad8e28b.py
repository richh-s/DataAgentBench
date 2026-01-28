code = """import json, re
file_path = locals()['var_functions.query_db:2']
papers = json.load(open(file_path))
result = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    txt = p['text']
    year_match = re.search(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(\d{4})', txt)
    year = int(year_match.group(2)) if year_match else 0
    has_empirical = 'empirical' in txt.lower() and 'contribution' in txt.lower()
    if has_empirical and year > 2016:
        result.append({'title': title, 'year': year})
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
