code = """import json, re
with open(var_call_i7pIUn02ScRKLaKBgJHjsfpF, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_yGOk2ofuIXBkXuO9xfTzY1aP, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

def norm(s):
    return re.sub(r'\s+', ' ', s.lower().strip())

# Extract design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    key = 'Capital Improvement Projects (Design)'
    idx = text.find(key)
    if idx == -1:
        idx = text.lower().find(key.lower())
        if idx == -1:
            continue
    start = idx + len(key)
    end = len(text)
    next_heads = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
    for nh in next_heads:
        j = text.find(nh, start)
        if j != -1 and j < end:
            end = j
    block = text[start:end]
    lines = [ln.strip() for ln in block.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        if ':' in ln:
            continue
        if low.startswith('updates') or low.startswith('(cid') or low.startswith('page') or low.startswith('agenda'):
            continue
        if 'project schedule' in low or 'project description' in low or 'estimated schedule' in low or 'project updates' in low:
            continue
        if low.startswith('recommended action') or low.startswith('discussion'):
            continue
        if len(ln) < 6:
            continue
        if ln.endswith('.'):
            continue
        design_projects.add(ln)

# Normalize maps
design_norm = {norm(s): s for s in design_projects}

# Funding set (from previously queried rows which had Amount > 50000)
fund_set = set()
for r in funding_rows:
    pname = r.get('Project_Name') or ''
    try:
        amt = int(float(r.get('Amount', 0)))
    except:
        try:
            amt = int(str(r.get('Amount', '0')).replace(',', ''))
        except:
            amt = 0
    if amt > 50000:
        fund_set.add(pname)
fund_norm = {norm(s): s for s in fund_set}

# Match
matched = set()
for dnorm, dorig in design_norm.items():
    for fnorm, forig in fund_norm.items():
        if dnorm == fnorm or dnorm in fnorm or fnorm in dnorm:
            matched.add(dorig)
            break

result = {'count': len(matched), 'matched_projects': sorted(list(matched))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_niYonW9IOdRbZkwnICOKFidL': ['civic_docs'], 'var_call_RDD7R3XhMlU6f4fAerIDHaAH': ['Funding'], 'var_call_yGOk2ofuIXBkXuO9xfTzY1aP': 'file_storage/call_yGOk2ofuIXBkXuO9xfTzY1aP.json', 'var_call_i7pIUn02ScRKLaKBgJHjsfpF': 'file_storage/call_i7pIUn02ScRKLaKBgJHjsfpF.json'}

exec(code, env_args)
