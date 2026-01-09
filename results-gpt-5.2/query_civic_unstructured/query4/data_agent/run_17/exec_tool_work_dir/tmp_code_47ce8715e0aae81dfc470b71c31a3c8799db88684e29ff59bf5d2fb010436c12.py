code = """import json, re

with open(var_call_5FRoyKoaGE92xUhwFnjuJHFV, 'r', encoding='utf-8') as f:
    docs = json.load(f)

texts = [d.get('text','') for d in docs]
text_all = "\n".join(texts)

pat = re.compile(r'(?i)Spring\s+2022')
spans = [m.start() for m in pat.finditer(text_all)]

contexts = []
for pos in spans[:20]:
    contexts.append(text_all[max(0, pos-120):pos+120])

out = {'occurrences': int(len(spans)), 'sample_contexts': contexts}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5FRoyKoaGE92xUhwFnjuJHFV': 'file_storage/call_5FRoyKoaGE92xUhwFnjuJHFV.json', 'var_call_B8i9KzeWghvmclogSXmtIm7J': 'file_storage/call_B8i9KzeWghvmclogSXmtIm7J.json', 'var_call_C0VOOFKGG33dRWa4HHxU2gC1': {'count': 0, 'total_funding_usd': 0, 'projects': []}}

exec(code, env_args)
