code = """import json
from pathlib import Path

p_cit = Path(var_call_sVvX2k0h9tZaTpMAD5sxxGOL)
with p_cit.open('r', encoding='utf-8') as f:
    cit = json.load(f)

p_acm = Path(var_call_bC7NwjgIYvbkQRRjQb8ssizl)
with p_acm.open('r', encoding='utf-8') as f:
    acm = json.load(f)

acm_titles = set(r['filename'][:-4] for r in acm if isinstance(r.get('filename'), str) and r['filename'].endswith('.txt'))

vals = []
for r in cit:
    if r.get('title') in acm_titles:
        try:
            vals.append(int(r.get('citation_count')))
        except Exception:
            pass

avg = sum(vals)/len(vals) if vals else None
out = {"citation_year": 2018, "avg_citation_count": avg, "num_acm_papers_matched": len(vals)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sVvX2k0h9tZaTpMAD5sxxGOL': 'file_storage/call_sVvX2k0h9tZaTpMAD5sxxGOL.json', 'var_call_zmweJaBt3hrh57jl8jd37xbU': 'file_storage/call_zmweJaBt3hrh57jl8jd37xbU.json', 'var_call_Qx7J5BeHMbKTXglzlDULR9kH': {'citation_year': 2018, 'avg_citation_count': 59.36363636363637, 'num_papers_matched': 55}, 'var_call_bC7NwjgIYvbkQRRjQb8ssizl': 'file_storage/call_bC7NwjgIYvbkQRRjQb8ssizl.json'}

exec(code, env_args)
