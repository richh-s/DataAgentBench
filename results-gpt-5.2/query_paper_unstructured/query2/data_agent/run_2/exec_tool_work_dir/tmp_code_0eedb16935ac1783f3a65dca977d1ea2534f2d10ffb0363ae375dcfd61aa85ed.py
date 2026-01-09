code = """import json, pandas as pd
from pathlib import Path

# load citations 2018
p_cit = Path(var_call_sVvX2k0h9tZaTpMAD5sxxGOL)
with p_cit.open('r', encoding='utf-8') as f:
    cit = json.load(f)

# load paper filenames
p_papers = Path(var_call_zmweJaBt3hrh57jl8jd37xbU)
with p_papers.open('r', encoding='utf-8') as f:
    papers = json.load(f)

paper_titles = set()
for r in papers:
    fn = r.get('filename')
    if isinstance(fn, str) and fn.endswith('.txt'):
        paper_titles.add(fn[:-4])

# filter to titles present in paper_docs, then compute mean citation_count
vals = []
for r in cit:
    t = r.get('title')
    if t in paper_titles:
        try:
            vals.append(int(r.get('citation_count')))
        except Exception:
            pass

avg = sum(vals)/len(vals) if vals else None
out = {
    "citation_year": 2018,
    "avg_citation_count": avg,
    "num_papers_matched": len(vals)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sVvX2k0h9tZaTpMAD5sxxGOL': 'file_storage/call_sVvX2k0h9tZaTpMAD5sxxGOL.json', 'var_call_zmweJaBt3hrh57jl8jd37xbU': 'file_storage/call_zmweJaBt3hrh57jl8jd37xbU.json'}

exec(code, env_args)
