code = """import json, pandas as pd

# load citations 2018
path = var_call_8IpMJcDeCmdetu4VYicTuO5n
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# load ACM-ish docs list (filtered by text contains ACM)
path2 = var_call_dJWf7fkOJaC9S6e9KTQT0UJL
with open(path2, 'r', encoding='utf-8') as f:
    acm_docs = json.load(f)

acm_titles = set([d['filename'][:-4] if d.get('filename','').endswith('.txt') else d.get('filename') for d in acm_docs])

vals = []
for r in citations:
    if r['title'] in acm_titles:
        try:
            vals.append(int(r['citation_count']))
        except:
            pass

avg = (sum(vals)/len(vals)) if vals else None
out = {
    'average_citation_count_2018_for_ACM_papers': avg,
    'num_papers_matched': len(vals)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_D2yviFBG2adyEV7IsfxNOINS': [{'avg_citation_count': 'None'}], 'var_call_8IpMJcDeCmdetu4VYicTuO5n': 'file_storage/call_8IpMJcDeCmdetu4VYicTuO5n.json', 'var_call_LMREUfiL7bDDERquHncWrAh3': 'file_storage/call_LMREUfiL7bDDERquHncWrAh3.json', 'var_call_dJWf7fkOJaC9S6e9KTQT0UJL': 'file_storage/call_dJWf7fkOJaC9S6e9KTQT0UJL.json'}

exec(code, env_args)
