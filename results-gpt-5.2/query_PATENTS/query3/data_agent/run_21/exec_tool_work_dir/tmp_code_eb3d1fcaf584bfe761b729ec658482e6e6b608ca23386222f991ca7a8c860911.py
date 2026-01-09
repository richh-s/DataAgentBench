code = """import json, re
import pandas as pd

with open(var_call_E6tbXMkCCY50UNQlzqQSeEjh, 'r', encoding='utf-8') as f:
    uc_recs=json.load(f)
with open(var_call_65uPjKCFaiNNd7bRcSfrJwgT, 'r', encoding='utf-8') as f:
    citing_recs=json.load(f)

uc_pub_to_primary_subclass={}
for r in uc_recs:
    pi=r.get('Patents_info') or ''
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi) or re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    pub=m.group(1) if m else None
    primary=None
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
        for e in cpcs:
            if isinstance(e, dict) and e.get('first') is True and e.get('code'):
                primary=e['code']
                break
    except Exception:
        primary=None
    if pub and primary:
        uc_pub_to_primary_subclass[pub]=primary[:4]

pairs=[]
for r in citing_recs:
    pi=r.get('Patents_info') or ''
    am=re.search(r'(?:owned by|assigned to)\s+([^,.]+)', pi) or re.search(r'^([^,]+?)\s+holds', pi)
    assignee=am.group(1).strip() if am else None
    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    try:
        cits=json.loads(r.get('citation') or '[]')
    except Exception:
        continue
    subclasses=set()
    for c in cits:
        pn=(c or {}).get('publication_number')
        if pn in uc_pub_to_primary_subclass:
            subclasses.add(uc_pub_to_primary_subclass[pn])
    for sc in subclasses:
        pairs.append({'citing_assignee':assignee,'cpc_subclass':sc})

out_df=pd.DataFrame(pairs).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
subclasses=sorted(out_df['cpc_subclass'].unique().tolist()) if len(out_df) else []
print('__RESULT__:')
print(json.dumps({'pairs': out_df.to_dict(orient='records'), 'subclasses': subclasses}))"""

env_args = {'var_call_ky9p28bfw6ZzpdkIpcICy6Ul': ['publicationinfo'], 'var_call_9FjvG9K7GEUQ2jOWlZFfSjSr': ['cpc_definition'], 'var_call_FPczLPUeIyYnvaQzIKLNGXAr': [], 'var_call_E6tbXMkCCY50UNQlzqQSeEjh': 'file_storage/call_E6tbXMkCCY50UNQlzqQSeEjh.json', 'var_call_JuEFYCQ1kR51VnVGUHBz75aP': 'file_storage/call_JuEFYCQ1kR51VnVGUHBz75aP.json', 'var_call_4XGmYMbVJ7u6IZ4sJG6aFSf1': [{'name': 'publicationinfo'}], 'var_call_65uPjKCFaiNNd7bRcSfrJwgT': 'file_storage/call_65uPjKCFaiNNd7bRcSfrJwgT.json'}

exec(code, env_args)
