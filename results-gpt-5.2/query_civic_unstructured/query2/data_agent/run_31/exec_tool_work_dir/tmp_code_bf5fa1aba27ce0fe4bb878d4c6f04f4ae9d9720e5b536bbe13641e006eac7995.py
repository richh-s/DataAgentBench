code = """import json, re

# Load docs
src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

# Load funds
fsrc = var_call_wUAIQWHnhpnImBn34Zbk6oW2
if isinstance(fsrc, str):
    with open(fsrc, 'r', encoding='utf-8') as f:
        funds = json.load(f)
else:
    funds = fsrc
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funds}

complete_pat = re.compile('(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\\b[^\\n\\r]{0,80}2022', re.IGNORECASE)

completed_2022_projects = set()
for d in docs:
    text = (d.get('text','') or '')
    if re.search(r'\bpark\b', text, re.IGNORECASE) is None:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.search(r'\bpark\b', ln, re.IGNORECASE) and not re.search(r'^(updates|project schedule|estimated schedule|project description)\b', ln, re.IGNORECASE):
            window = "\n".join(lines[i:i+9])
            if complete_pat.search(window):
                completed_2022_projects.add(re.sub(r'\s+', ' ', ln).strip(' -\t'))

# backtrack
for d in docs:
    lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
    prev = None
    for ln in lines:
        if not ln:
            continue
        if complete_pat.search(ln):
            if prev and re.search(r'\bpark\b', prev, re.IGNORECASE):
                completed_2022_projects.add(re.sub(r'\s+', ' ', prev).strip(' -\t'))
        prev = ln

matched = []
unmatched = []
total = 0
for proj in sorted(completed_2022_projects):
    amt = fund_map.get(proj)
    if amt is None:
        unmatched.append(proj)
    else:
        matched.append({'Project_Name': proj, 'total_amount': amt})
        total += amt

out = {'total_funding_completed_2022_park_projects': total,
       'matched_projects': matched,
       'unmatched_projects': unmatched}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json', 'var_call_fwrAlLIXYuEkd3dLsbunT5gs': {'n_docs': 19, 'first_filename': 'malibucity_agenda_03222023-2060.txt', 'first_text_len': 9796}, 'var_call_Yp5C5xwexk7Gz27AO43Jgc7n': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08'}, 'var_call_dwH69q9JQE7Bb8lXVgihbvm3': {'compiled': True, 'pattern': '(?:construction\\s+was\\s+completed|complete\\s+construction|completed)\x08[^\n\r]{0,80}2022'}}

exec(code, env_args)
