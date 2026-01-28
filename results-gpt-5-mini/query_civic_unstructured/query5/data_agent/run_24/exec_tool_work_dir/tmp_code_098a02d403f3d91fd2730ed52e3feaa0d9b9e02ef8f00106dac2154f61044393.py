code = """import json
from pathlib import Path

# Load stored results
funding_path = Path(var_call_4wM5k3GTyzdYzrzkX7moL6ZN)
docs_path = Path(var_call_rAaA0qkh81fh2IyO6Se144fH)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# normalize amounts to int
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except Exception:
        s = ''.join(ch for ch in str(r.get('Amount','0')) if ch.isdigit())
        r['Amount'] = int(s) if s else 0

# prepare doc texts
all_texts = [d.get('text','') for d in docs]
all_texts_low = [t.lower() for t in all_texts]

# helper to strip parenthetical suffix
def base_name(name):
    # remove any parentheses and content
    res = ''
    skip = 0
    for ch in name:
        if ch == '(':
            skip += 1
        elif ch == ')' and skip>0:
            skip -= 1
        elif skip==0:
            res += ch
    return res.strip()

disaster_keywords = ['fema', 'caloes', 'cal o es', 'disaster', 'fire', 'woolsey', 'emergency']
start_phrases = ['begin construction', 'construction started', 'start construction', 'beginning construction']

matches = []
for r in funding:
    pname = r.get('Project_Name','')
    pname_low = pname.lower()
    bname = base_name(pname).lower()
    contexts = []
    # find occurrences of project name or base name in documents
    for txt_low in all_texts_low:
        idx = txt_low.find(pname_low)
        if idx == -1 and bname:
            idx = txt_low.find(bname)
        if idx != -1:
            start = max(0, idx-200)
            end = min(len(txt_low), idx+200)
            contexts.append(txt_low[start:end])
    if not contexts:
        # not found in docs
        continue
    # determine if disaster
    is_disaster = False
    for kw in disaster_keywords:
        if kw in pname_low:
            is_disaster = True
            break
    if not is_disaster:
        for c in contexts:
            for kw in disaster_keywords:
                if kw in c:
                    is_disaster = True
                    break
            if is_disaster:
                break
    # determine if started in 2022: look for '2022' and start phrases within the same context
    started_2022 = False
    for c in contexts:
        if '2022' in c:
            for sp in start_phrases:
                if sp in c:
                    started_2022 = True
                    break
        # also check if 'begin construction' appears in doc and nearby (within 200 chars) '2022'
        for sp in start_phrases:
            i = c.find(sp)
            if i != -1:
                # check 200 chars around phrase for 2022
                seg_start = max(0, i-200)
                seg_end = min(len(c), i+200)
                if '2022' in c[seg_start:seg_end]:
                    started_2022 = True
                    break
        if started_2022:
            break
    matches.append({
        'Project_Name': pname,
        'Amount': r['Amount'],
        'is_disaster': is_disaster,
        'started_2022': started_2022,
        'contexts_count': len(contexts)
    })

total = sum(m['Amount'] for m in matches if m['is_disaster'] and m['started_2022'])
selected = [m for m in matches if m['is_disaster'] and m['started_2022']]

result = {'total_funding_for_disaster_projects_started_in_2022': total, 'matched_projects': selected}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ppCisfN2tRpTi42dyxTwHA6j': ['civic_docs'], 'var_call_nCM4EklzTtjpxEpVDK5Li7Kx': ['Funding'], 'var_call_4wM5k3GTyzdYzrzkX7moL6ZN': 'file_storage/call_4wM5k3GTyzdYzrzkX7moL6ZN.json', 'var_call_rAaA0qkh81fh2IyO6Se144fH': 'file_storage/call_rAaA0qkh81fh2IyO6Se144fH.json'}

exec(code, env_args)
