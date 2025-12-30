code = """import json, re
from statistics import mean

# Load full citations result
path_cit = var_call_7wjlPr53Ty8MuYQKURIv8Ldl
with open(path_cit, 'r') as f:
    citations = json.load(f)

# Load full papers result
path_pap = var_call_JEHeoZVLlJ2pbs3elGXzSldq
with open(path_pap, 'r') as f:
    papers = json.load(f)

# Build map from title to source using heuristic: look for 'Copyright YYYY © ACM' or 'ACM' near copyright
acm_titles = set()
for doc in papers:
    text = doc.get('text','')
    lower = text.lower()
    # Heuristic: look for 'copyright' line containing 'acm'
    if 'acm' in lower:
        # stronger: copyright ... acm or 'permission to make digital or hard copies' and later 'acm'
        if 'permission  to  make  digital  or  hard  copies' in lower or 'copyright' in lower:
            # treat as ACM source
            title = doc.get('filename','').replace('.txt','')
            if title:
                acm_titles.add(title)

# Collect citation counts for ACM papers cited in 2018
vals = []
for rec in citations:
    title = rec['title']
    if title in acm_titles:
        try:
            vals.append(int(rec['citation_count']))
        except:
            pass

avg = mean(vals) if vals else None

import json as j
result = j.dumps({'average_citation_count_acm_2018': avg, 'num_papers': len(vals)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_7wjlPr53Ty8MuYQKURIv8Ldl': 'file_storage/call_7wjlPr53Ty8MuYQKURIv8Ldl.json', 'var_call_JEHeoZVLlJ2pbs3elGXzSldq': 'file_storage/call_JEHeoZVLlJ2pbs3elGXzSldq.json'}

exec(code, env_args)
