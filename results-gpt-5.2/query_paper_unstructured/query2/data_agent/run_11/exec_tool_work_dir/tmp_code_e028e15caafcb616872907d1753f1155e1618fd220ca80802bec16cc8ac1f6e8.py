code = """import json, pandas as pd

# Load citations 2018
path_cit = var_call_L9tkCvRR33ldgwPVkgzG2sgN
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# Load paper docs
path_docs = var_call_Yj7BwiBGFSVpAE3v2hCDBqHk
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    txt = (d.get('text') or '').lower()
    # heuristic: look for ACM copyright/classification markers
    if 'acm' in txt and ('permission to make digital or hard copies' in txt or 'acm classification' in txt or 'copyright' in txt):
        acm_titles.add(title)

vals = []
for r in cit:
    t = r.get('title')
    if t in acm_titles:
        try:
            vals.append(float(r.get('citation_count')))
        except Exception:
            pass

avg = sum(vals)/len(vals) if vals else None
out = {
    "average_citation_count_2018_for_acm_papers": avg,
    "num_acm_papers_with_2018_citations": len(vals)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eriewBUAc1G3k7BQ1MwGjAau': [{'name': 'Citations'}, {'name': 'sqlite_sequence'}], 'var_call_L9tkCvRR33ldgwPVkgzG2sgN': 'file_storage/call_L9tkCvRR33ldgwPVkgzG2sgN.json', 'var_call_Yj7BwiBGFSVpAE3v2hCDBqHk': 'file_storage/call_Yj7BwiBGFSVpAE3v2hCDBqHk.json'}

exec(code, env_args)
