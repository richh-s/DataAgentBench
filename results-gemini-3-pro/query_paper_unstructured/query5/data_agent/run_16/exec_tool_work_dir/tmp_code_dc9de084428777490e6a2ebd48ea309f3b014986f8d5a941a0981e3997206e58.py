code = """import json

# Load citations data
path_citations = locals().get('var_function-call-7498192109235549923')
with open(path_citations, 'r') as f:
    citations_data = json.load(f)
cited_titles = set(c['title'] for c in citations_data)

# Load paper docs
path_docs = locals().get('var_function-call-7995451070674360072')
with open(path_docs, 'r') as f:
    docs = json.load(f)

matched_docs = [d for d in docs if d['filename'].replace('.txt', '') in cited_titles]

headers = []
for d in matched_docs[:10]:
    headers.append({
        "filename": d['filename'],
        "header": d['text'][:300]
    })

print("__RESULT__:")
print(json.dumps(headers))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188, 'var_function-call-15965521281973898392': 'file_storage/function-call-15965521281973898392.json', 'var_function-call-6154840779900112772': 'file_storage/function-call-6154840779900112772.json', 'var_function-call-4693824508147823644': 'file_storage/function-call-4693824508147823644.json', 'var_function-call-9895404596539580614': 16, 'var_function-call-7995451070674360072': 'file_storage/function-call-7995451070674360072.json', 'var_function-call-5270707642555143575': 0}

exec(code, env_args)
