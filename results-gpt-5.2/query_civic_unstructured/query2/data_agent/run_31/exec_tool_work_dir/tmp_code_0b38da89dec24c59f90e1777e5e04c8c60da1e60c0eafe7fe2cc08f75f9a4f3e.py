code = """import json

# Load docs
src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(src, str):
    docs = json.load(open(src, 'r', encoding='utf-8'))
else:
    docs = src

# Load funds
fsrc = var_call_wUAIQWHnhpnImBn34Zbk6oW2
if isinstance(fsrc, str):
    funds = json.load(open(fsrc, 'r', encoding='utf-8'))
else:
    funds = fsrc
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funds}

# Extract park project names with completion in 2022 by simple scanning
projects=set()
for d in docs:
    lines = d.get('text','').splitlines()
    for i,ln in enumerate(lines):
        lnl = ln.lower()
        if '2022' in lnl and ('completed' in lnl or 'complete construction' in lnl or 'construction was completed' in lnl):
            # find nearest previous line containing 'park'
            for j in range(i-1, max(-1, i-15), -1):
                prev = lines[j].strip()
                if not prev:
                    continue
                if 'park' in prev.lower() and not prev.lower().startswith(('updates','project schedule','estimated schedule','(cid')):
                    projects.add(' '.join(prev.split()))
                    break

matched=[]
unmatched=[]
total=0
for p in sorted(projects):
    amt=fund_map.get(p)
    if amt is None:
        unmatched.append(p)
    else:
        matched.append({'Project_Name': p, 'total_amount': amt})
        total += amt

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'matched': matched, 'unmatched': unmatched, 'total': total}))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json', 'var_call_fwrAlLIXYuEkd3dLsbunT5gs': {'n_docs': 19, 'first_filename': 'malibucity_agenda_03222023-2060.txt', 'first_text_len': 9796}, 'var_call_Yp5C5xwexk7Gz27AO43Jgc7n': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08'}, 'var_call_dwH69q9JQE7Bb8lXVgihbvm3': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08[^\n\r]{0,80}2022'}, 'var_call_IyumGNNGkdSHOH6Jig40FcbA': {'n_hits': 3, 'hits': ['Bluffs Park Shade Structure |  | (cid:190) Updates: Construction was completed November 2022. Notice of completion |  | filed January 2023', '(cid:190) Updates: |  | (cid:131) Construction was completed, November 2022 | (cid:131) Notice of completion filed January 2023 | ', '(cid:190) Updates: |  | (cid:131) Construction was completed, November 2022 | (cid:131) Notice of completion filed January 2023 | ']}}

exec(code, env_args)
