code = """import json, re

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_zgx8u7CePpLHfPFcFNQvWEQv)

patterns = [r'©\s*ACM', r'\bACM\b', r'permissions@acm\.org', r'acm\.org', r'Association for Computing Machinery']
counts={p:0 for p in patterns}
# check first 200 docs for speed
for d in docs[:200]:
    t=d.get('text','') or ''
    for p in patterns:
        if re.search(p,t):
            counts[p]+=1
out={"docs_checked":min(200,len(docs)),"pattern_counts":counts}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8iQgmxQZH8dTEoUu9lvnEql0': 'file_storage/call_8iQgmxQZH8dTEoUu9lvnEql0.json', 'var_call_zgx8u7CePpLHfPFcFNQvWEQv': 'file_storage/call_zgx8u7CePpLHfPFcFNQvWEQv.json', 'var_call_k8dsdLMqOYgh4LSCy5CaoB3x': {'acm_papers_with_2018_citations': 0, 'average_citation_count_2018': None}}

exec(code, env_args)
