code = """import json
import re

# Load data from storage paths
with open(var_call_twkje1XB9wItR2bODeZFtWzA, 'r') as f:
    funding = json.load(f)
with open(var_call_mmDfgxQsjfGR7MR2se4d5CBB, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts to int
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except Exception:
        r['Amount'] = 0

# Filter funding records that are park-related by name
park_funding = [r for r in funding if 'park' in r.get('Project_Name','').lower() or 'playground' in r.get('Project_Name','').lower()]

# Find civic document sentences that mention park and completed in 2022
park_completed_sentences = []
for doc in civic_docs:
    text = doc.get('text','')
    # split into lines to reduce complexity
    for line in text.split('\n'):
        l = line.strip()
        ll = l.lower()
        if 'park' in ll and 'completed' in ll and '2022' in ll:
            park_completed_sentences.append(l)

# Match funding projects to those sentences by token overlap
matched = {}

def tokens(s):
    s2 = s.lower()
    # split on non-alphanumeric
    toks = [t for t in re.split('[^a-z0-9]+', s2) if t]
    return set(toks)

for sent in park_completed_sentences:
    sent_toks = tokens(sent)
    for pf in park_funding:
        pname = pf.get('Project_Name','')
        pname_toks = tokens(pname)
        # require at least 2 token overlap
        if len(sent_toks & pname_toks) >= 2:
            matched[pname] = matched.get(pname, 0) + pf.get('Amount', 0)

# Additionally, explicitly check for exact mention of project name near 'completed' and '2022' in civic docs
for pf in park_funding:
    pname = pf.get('Project_Name','')
    pname_low = pname.lower()
    for doc in civic_docs:
        t = doc.get('text','').lower()
        if pname_low in t:
            # check if 'completed' and '2022' occur within 600 characters of project name occurrence
            idx = t.find(pname_low)
            if idx != -1:
                seg = t[max(0, idx-600): idx+600]
                if 'completed' in seg and '2022' in seg:
                    matched[pname] = matched.get(pname, 0) + pf.get('Amount', 0)
                    break

# Prepare matched list
matched_list = [{'Project_Name': k, 'Amount': v} for k,v in matched.items()]
total = sum(matched.values())

out = {'matched_projects': matched_list, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mmDfgxQsjfGR7MR2se4d5CBB': 'file_storage/call_mmDfgxQsjfGR7MR2se4d5CBB.json', 'var_call_twkje1XB9wItR2bODeZFtWzA': 'file_storage/call_twkje1XB9wItR2bODeZFtWzA.json'}

exec(code, env_args)
