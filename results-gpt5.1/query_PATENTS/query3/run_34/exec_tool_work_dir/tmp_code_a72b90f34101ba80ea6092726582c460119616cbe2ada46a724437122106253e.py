code = """import json, re, pandas as pd

# Load full publication results
with open(var_call_POQAuAbk7xUvEptEcyUUrSfH, 'r') as f:
    pub_records = json.load(f)

# Extract UNIV CALIFORNIA publications: need their publication numbers and CPC codes
univ_pubs = []
for r in pub_records:
    info = r.get('Patents_info','') or ''
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    pubnum = m.group(1) if m else None
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        cpc_list = []
    cpc_codes = sorted({e.get('code') for e in cpc_list if isinstance(e, dict) and e.get('code')})
    univ_pubs.append({'pubnum': pubnum, 'cpc_codes': cpc_codes})

# Publication numbers assigned to UNIV CALIFORNIA
univ_pubnums = {p['pubnum'] for p in univ_pubs if p['pubnum']}

# Next, load all publications to find citations TO these pub numbers
# We need Patents_info (for assignee) + cpc and citation
with open(var_call_POQAuAbk7xUvEptEcyUUrSfH, 'r') as f:
    all_pubs = json.load(f)

results = []
for r in all_pubs:
    info = r.get('Patents_info','') or ''
    # Skip UNIV CALIFORNIA assignee
    if 'UNIV CALIFORNIA' in info.upper():
        continue
    # crude assignee extraction: look for ' owned by X' or ' is owned by X' or 'is assigned to X' or 'holds the'
    assignee = None
    m = re.search(r'is owned by ([^.,]+)', info)
    if not m:
        m = re.search(r'is assigned to ([^.,]+)', info)
    if not m:
        m = re.search(r'owned by ([^.,]+)', info)
    if not m:
        m = re.search(r'holds the .* patent filing .* is (?:owned by|assigned to) ([^.,]+)', info)
    if m:
        assignee = m.group(1).strip()
    # citation list
    cit_raw = r.get('citation') or '[]'
    try:
        cits = json.loads(cit_raw)
    except Exception:
        cits = []
    cites_univ = False
    for c in cits:
        if not isinstance(c, dict):
            continue
        pn = c.get('publication_number')
        if pn in univ_pubnums:
            cites_univ = True
            break
    if not cites_univ:
        continue
    # extract CPC codes used in this citing patent
    cpc_raw = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        cpc_list = []
    cpc_codes = sorted({e.get('code') for e in cpc_list if isinstance(e, dict) and e.get('code')})
    if not assignee:
        continue
    results.append({'assignee': assignee, 'cpc_codes': cpc_codes})

# Collect unique CPC codes from citing patents
cpc_set = sorted({code for r in results for code in r['cpc_codes']})

# Load CPC definitions
with open(var_call_UXEjpT8QEMegGDtk99iCrhsl, 'r') as f:
    cpc_defs = json.load(f)

symbol_to_title = {d['symbol']: d['titleFull'] for d in cpc_defs}

# Map CPC to titles (only those available)
code_title = {c: symbol_to_title.get(c) for c in cpc_set if symbol_to_title.get(c)}

# Build final mapping: assignee -> set of CPC titles
assignee_map = {}
for r in results:
    ass = r['assignee']
    titles = {code_title.get(c) for c in r['cpc_codes'] if code_title.get(c)}
    if not titles:
        continue
    assignee_map.setdefault(ass, set()).update(titles)

final_list = []
for ass, titles in assignee_map.items():
    for t in sorted(titles):
        final_list.append({'assignee': ass, 'cpc_titleFull': t})

final_list_sorted = sorted(final_list, key=lambda x: (x['assignee'], x['cpc_titleFull']))

out = json.dumps(final_list_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_POQAuAbk7xUvEptEcyUUrSfH': 'file_storage/call_POQAuAbk7xUvEptEcyUUrSfH.json', 'var_call_UXEjpT8QEMegGDtk99iCrhsl': 'file_storage/call_UXEjpT8QEMegGDtk99iCrhsl.json'}

exec(code, env_args)
