code = """import json
from pathlib import Path

# Load stored results
civic_path = Path(var_call_2Fp1bAHB7PBvCeTmjbFiiz04)
funding_path = Path(var_call_Z7OVvUBbhExXMcwpCPQkBe4N)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with funding_path.open('r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Normalize funding
funding = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt_raw = r.get('Amount')
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(float(amt_raw))
        except:
            amt = 0
    funding.append({'Project_Name': name or '', 'Amount': amt})

# Matching function
def match_funding(project_name):
    pn = (project_name or '').strip().lower()
    total = 0
    matched = False
    for fr in funding:
        fn = (fr['Project_Name'] or '').strip().lower()
        if not fn:
            continue
        if fn == pn:
            total += fr['Amount']; matched = True; continue
        if pn in fn or fn in pn:
            total += fr['Amount']; matched = True; continue
        # remove parenthetical suffix from fn
        if '(' in fn:
            fn_nop = fn.split('(')[0].strip()
            if fn_nop == pn or pn in fn_nop or fn_nop in pn:
                total += fr['Amount']; matched = True; continue
    return total, matched

# Find project titles that have a line mentioning Spring and 2022 near a 'begin' or 'begin construction' phrase
projects = []
for doc in civic_docs:
    text = doc.get('text') or ''
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'spring' in low and '2022' in low and ('begin' in low or 'advertise' in low or 'complete design' in low or 'begin construction' in low):
            # search backwards for a likely title
            title = None
            for j in range(idx-1, max(-1, idx-15), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                cl = cand.lower()
                if cl.startswith('(cid') or cl.startswith('page ') or 'updates' in cl or 'project schedule' in cl or 'agenda' in cl or 'item' in cl:
                    continue
                if len(cand) < 5:
                    continue
                # skip if cand looks like a schedule line containing months/dates
                if any(m in cl for m in ['spring', 'summer', 'fall', 'winter', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
                    continue
                title = cand
                break
            if title:
                projects.append(title)

# Deduplicate preserving order
seen = set(); unique = []
for p in projects:
    key = p.strip()
    lk = key.lower()
    if lk not in seen:
        seen.add(lk); unique.append(key)

# For each project, find funding
proj_infos = []
total_funding = 0
for p in unique:
    amt, matched = match_funding(p)
    proj_infos.append({'name': p, 'funding': amt, 'matched_funding_record': matched})
    total_funding += amt

result = {'count': len(unique), 'total_funding': total_funding, 'projects': proj_infos}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2Fp1bAHB7PBvCeTmjbFiiz04': 'file_storage/call_2Fp1bAHB7PBvCeTmjbFiiz04.json', 'var_call_Z7OVvUBbhExXMcwpCPQkBe4N': 'file_storage/call_Z7OVvUBbhExXMcwpCPQkBe4N.json'}

exec(code, env_args)
