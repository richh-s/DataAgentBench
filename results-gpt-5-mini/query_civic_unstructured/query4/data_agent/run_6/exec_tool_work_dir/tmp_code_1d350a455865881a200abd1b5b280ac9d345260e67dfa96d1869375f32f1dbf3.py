code = """import json,re
# Load civic docs
path_docs = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path_docs,'r',encoding='utf-8') as f:
    docs = json.load(f)
# Load funding records
path_fund = var_call_CFKJoBPrTGwuRxwH2jrhFHYg
with open(path_fund,'r',encoding='utf-8') as f:
    funds = json.load(f)

def normalize(name):
    if not name:
        return ''
    s = name.lower().strip()
    # remove parenthetical tags
    s = re.sub(r"\([^)]*\)","",s)
    s = re.sub(r"[^a-z0-9 ]+"," ",s)
    s = re.sub(r"\s+"," ",s).strip()
    return s

candidates = set()
for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    # find 'spring' occurrences
    for m in re.finditer('spring', lower):
        i = m.start()
        window_start = max(0, i-200)
        window_end = min(len(lower), i+200)
        window = lower[window_start:window_end]
        if '2022' in window:
            # find preceding line
            prev = text[window_start:i]
            lines = prev.strip().splitlines()
            if lines:
                cand = lines[-1].strip()
                if 3 < len(cand) < 200:
                    candidates.add(cand)
    # months
    for month in ('march','april','may'):
        for m in re.finditer(month, lower):
            i = m.start()
            window_start = max(0, i-200)
            window_end = min(len(lower), i+200)
            window = lower[window_start:window_end]
            if '2022' in window:
                prev = text[window_start:i]
                lines = prev.strip().splitlines()
                if lines:
                    cand = lines[-1].strip()
                    if 3 < len(cand) < 200:
                        candidates.add(cand)
    # look for patterns like 'Complete Construction: April 2022' or 'Begin Construction: April 2022'
    for m in re.finditer(r'(complete construction|begin construction|advertise|project schedule|estimated schedule)[^\n]{0,80}(2022)', text, flags=re.I):
        i = m.start()
        window_start = max(0, i-200)
        prev = text[window_start:i]
        lines = prev.strip().splitlines()
        if lines:
            cand = lines[-1].strip()
            if 3 < len(cand) < 200:
                candidates.add(cand)

# Normalize candidates
norm_cands = {normalize(c):c for c in candidates if normalize(c)}

# Prepare funding records normalized map
fundings = []
for r in funds:
    pname = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_i = int(amt)
    except:
        try:
            amt_i = int(float(amt))
        except:
            amt_i = 0
    fundings.append({'orig':pname,'norm':normalize(pname),'amount':amt_i})

matched_fund_projects = set()
# For each candidate try to match funding projects by normalized containment
for nc, orig_cand in norm_cands.items():
    for f in fundings:
        fn = f['norm']
        if not fn:
            continue
        if nc and (nc in fn or fn in nc):
            matched_fund_projects.add(f['orig'])
# As a fallback, if candidate exact matches any funding orig
for nc, orig_cand in norm_cands.items():
    for f in fundings:
        if orig_cand.lower() == f['orig'].lower():
            matched_fund_projects.add(f['orig'])

# Sum amounts for matched funding projects
total = 0
for f in fundings:
    if f['orig'] in matched_fund_projects:
        total += f['amount']

result = {'count': len(matched_fund_projects), 'total_funding': total, 'matched_projects': sorted(list(matched_fund_projects))}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json', 'var_call_CFKJoBPrTGwuRxwH2jrhFHYg': 'file_storage/call_CFKJoBPrTGwuRxwH2jrhFHYg.json'}

exec(code, env_args)
