code = """import json, re

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cit = load_json_maybe_path(var_call_8iQgmxQZH8dTEoUu9lvnEql0)
docs = load_json_maybe_path(var_call_zgx8u7CePpLHfPFcFNQvWEQv)

acm_titles=set()
for d in docs:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=(d.get('text') or '')
    if re.search(r'permissions@acm\.org|acm\.org|Association for Computing Machinery|©\s*ACM', text, flags=re.I):
        acm_titles.add(title)

vals=[]
for r in cit:
    if r.get('title') in acm_titles:
        try:
            vals.append(int(r.get('citation_count')))
        except Exception:
            pass

out={"acm_titles":len(acm_titles),"acm_papers_with_2018_citations":len(vals),"average_citation_count_2018": (sum(vals)/len(vals) if vals else None)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8iQgmxQZH8dTEoUu9lvnEql0': 'file_storage/call_8iQgmxQZH8dTEoUu9lvnEql0.json', 'var_call_zgx8u7CePpLHfPFcFNQvWEQv': 'file_storage/call_zgx8u7CePpLHfPFcFNQvWEQv.json', 'var_call_k8dsdLMqOYgh4LSCy5CaoB3x': {'acm_papers_with_2018_citations': 0, 'average_citation_count_2018': None}, 'var_call_Wc7cO5yomJBsEcwmWil82IZP': {'docs_checked': 99, 'pattern_counts': {'©\\s*ACM': 2, '\x08ACM\x08': 0, 'permissions@acm\\.org': 32, 'acm\\.org': 82, 'Association for Computing Machinery': 9}}}

exec(code, env_args)
