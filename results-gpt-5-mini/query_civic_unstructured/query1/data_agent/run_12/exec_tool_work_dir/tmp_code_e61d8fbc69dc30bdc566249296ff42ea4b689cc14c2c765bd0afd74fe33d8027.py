code = """import json
import re

# Load civic docs
civic_path = var_call_ZEagpG3qicTk8xDnkvuXEAoZ
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = var_call_zb5hL7XuNPEyB7pXOtEhCvU5
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to integers
for row in funding:
    amt = row.get('Amount', 0)
    try:
        row['Amount'] = int(amt)
    except Exception:
        s = re.sub('[^0-9]', '', str(amt))
        row['Amount'] = int(s) if s else 0

# Heuristic extraction of projects under Design
def extract_design_projects(text):
    names = []
    low = text.lower()
    marker = 'capital improvement projects (design)'
    idx = low.find(marker)
    if idx == -1:
        return names
    start = idx + len(marker)
    # find next occurrence of 'capital improvement projects (' after start
    next_idx = low.find('capital improvement projects (', start)
    end = next_idx if next_idx != -1 else None
    section = text[start:end] if end else text[start:]

    # split into blocks by double newlines
    blocks = section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # take first non-empty line
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        first = lines[0]
        if len(first) < 4:
            continue
        fl = first.lower()
        if fl.startswith('updates') or fl.startswith('(cid') or fl.startswith('project schedule') or fl.startswith('project description'):
            continue
        if 'page' in fl or 'agenda' in fl:
            continue
        # avoid sentences
        if first.endswith('.') and len(first.split()) > 6:
            continue
        names.append(first)
    # dedupe
    seen = set()
    uniq = []
    for n in names:
        key = re.sub('\s+', ' ', n).strip().lower()
        if key not in seen:
            seen.add(key)
            uniq.append(n)
    return uniq

# collect design projects from all documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    ps = extract_design_projects(text)
    for p in ps:
        if p not in design_projects:
            design_projects.append(p)

# match funding and compute totals
results = []
for proj in design_projects:
    proj_l = proj.lower()
    matched = []
    total = 0
    for row in funding:
        fn = str(row.get('Project_Name', '')).lower()
        if not fn:
            continue
        if proj_l == fn or proj_l in fn or fn in proj_l:
            matched.append({'Project_Name': row.get('Project_Name'), 'Amount': row.get('Amount')})
            total += row.get('Amount', 0)
    results.append({'project': proj, 'matched_funding_rows': matched, 'total_amount': total})

count = sum(1 for r in results if r['total_amount'] > 50000)

output = {'count': count, 'details': results}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ZEagpG3qicTk8xDnkvuXEAoZ': 'file_storage/call_ZEagpG3qicTk8xDnkvuXEAoZ.json', 'var_call_zb5hL7XuNPEyB7pXOtEhCvU5': 'file_storage/call_zb5hL7XuNPEyB7pXOtEhCvU5.json'}

exec(code, env_args)
