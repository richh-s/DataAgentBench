code = """import json, re

docs_src = var_call_JfAXMaifEjUuzNF65e2KwdVd
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

beg2022 = re.compile('\\b(Begin|Start)\\b[^\\n]{0,120}2022', re.IGNORECASE)
count=0
examples=[]
for d in docs:
    text=d.get('text') or ''
    m=beg2022.search(text)
    if m:
        count += 1
        if len(examples)<5:
            s=max(0,m.start()-80); e=min(len(text), m.end()+80)
            examples.append(text[s:e])

print('__RESULT__:')
print(json.dumps({'docs_with_begin_start_2022': count, 'examples': examples}))"""

env_args = {'var_call_DxZXrgir7bSPofq0krrauG1m': 'file_storage/call_DxZXrgir7bSPofq0krrauG1m.json', 'var_call_JfAXMaifEjUuzNF65e2KwdVd': 'file_storage/call_JfAXMaifEjUuzNF65e2KwdVd.json', 'var_call_TCTs3cGEi5kICAZ0yDI5sy91': ['civic_docs'], 'var_call_umEJ4GpybYpolnXPUAjvCwXZ': ['Funding'], 'var_call_31KAvYQlBKpc4NWlA31swVWY': {'ok': True}, 'var_call_SJnV9u6cAf5Qujvm4JKQkVV2': {'compiled': True}, 'var_call_XoRyC4xNZGy1G0tpGAUQ45o2': {'total_funding': 0, 'n_projects': 0}, 'var_call_qBzJ3Wb2tUgDQC2Q1m8yzDFJ': {'total_funding': 0, 'n_projects': 0, 'projects': []}}

exec(code, env_args)
