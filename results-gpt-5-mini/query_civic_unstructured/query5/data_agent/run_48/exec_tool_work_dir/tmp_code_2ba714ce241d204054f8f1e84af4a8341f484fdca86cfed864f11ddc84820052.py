code = """import json, re

# Load funding data
fpath = var_call_yn9UnOwYQKVMmOX7FNz53bYZ
if isinstance(fpath, str) and fpath.endswith('.json'):
    with open(fpath, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fpath

# Load civic docs data
dpath = var_call_hn1g47AlWbPVm7TZBgFNWVGS
if isinstance(dpath, str) and dpath.endswith('.json'):
    with open(dpath, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = dpath

# Helper normalize
def normalize_name(n):
    if n is None:
        return ''
    n = re.sub(r"\s*\(.*?\)\s*", "", n)  # remove parenthetical suffixes
    n = re.sub(r"[^a-z0-9 ]+", " ", n.lower())
    n = re.sub(r"\s+", " ", n).strip()
    return n

markers = ['fema', 'caloes', 'cal o es', 'caljpia', 'disaster', 'fire', 'woolsey', 'calo es', 'calo es', 'cal o es']

total = 0
included = []

# Precompute lower text for docs
docs_texts = []
for doc in civic_docs:
    txt = ''
    if isinstance(doc, dict):
        txt = doc.get('text','') or ''
        filename = doc.get('filename','') or ''
    else:
        txt = str(doc)
        filename = ''
    docs_texts.append({'text': txt.lower(), 'filename': filename.lower()})

for rec in funding:
    pname = rec.get('Project_Name','')
    amt_raw = rec.get('Amount', 0)
    try:
        amount = int(float(amt_raw))
    except:
        try:
            amount = int(''.join(ch for ch in str(amt_raw) if ch.isdigit()))
        except:
            amount = 0

    pname_low = pname.lower()
    base = normalize_name(pname)

    # Determine if disaster-related by name markers
    disaster_by_name = any(m in pname_low for m in ['fema', 'caloes', 'caljpia'])

    # Determine if it started in 2022 by checking name or civic docs
    start2022 = False
    if '2022' in pname:
        start2022 = True

    disaster_by_doc = False

    # Search docs for base or full name
    for d in docs_texts:
        t = d['text']
        idx = -1
        if base and base in t:
            idx = t.find(base)\n        elif pname_low and pname_low in t:
            idx = t.find(pname_low)
        if idx >= 0:
            ctx = t[max(0, idx-300): idx+300]
            if '2022' in ctx:
                start2022 = True
            # check markers in context
            if any(m in ctx for m in markers):
                disaster_by_doc = True
            # also check if near 'disaster recovery'
            if 'disaster recovery' in ctx or 'disaster' in ctx:
                disaster_by_doc = True
            # if we've found relevant info, no need to search more docs (but continue to accumulate markers)
            # do not break to allow other docs to set start2022

    is_disaster = disaster_by_name or disaster_by_doc

    if is_disaster and start2022:
        total += amount
        included.append({'Project_Name': pname, 'Amount': amount})

result = {'total_funding': total, 'included_projects': included}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yn9UnOwYQKVMmOX7FNz53bYZ': 'file_storage/call_yn9UnOwYQKVMmOX7FNz53bYZ.json', 'var_call_hn1g47AlWbPVm7TZBgFNWVGS': 'file_storage/call_hn1g47AlWbPVm7TZBgFNWVGS.json'}

exec(code, env_args)
