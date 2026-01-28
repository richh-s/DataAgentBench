code = """import json
import re

# Load civic docs
civic_path = var_call_ZEagpG3qicTk8xDnkvuXEAoZ
if isinstance(civic_path, str):
    with open(civic_path, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

# Load funding data
funding_path = var_call_zb5hL7XuNPEyB7pXOtEhCvU5
if isinstance(funding_path, str):
    with open(funding_path, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_path

# Normalize funding amounts
for row in funding:
    try:
        row['Amount'] = int(row.get('Amount', 0))
    except Exception:
        s = re.sub(r'[^0-9]', '', str(row.get('Amount', '0')))
        row['Amount'] = int(s) if s else 0

# Extract design project names using heuristics
def extract_design_projects(text):
    names = []
    low = text.lower()
    marker = 'capital improvement projects (design)'
    idx = low.find(marker)
    if idx == -1:
        return names
    start = idx + len(marker)
    # find end markers
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (completed)', '\n\n']
    end_positions = []
    for em in end_markers:
        pos = low.find(em, start)
        if pos != -1:
            end_positions.append(pos)
    end = min(end_positions) if end_positions else None
    section = text[start:end] if end else text[start:]

    # split into blocks by blank lines
    blocks = re.split(r'\n\s*\n', section)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # first line of block
        first_line = block.splitlines()[0].strip()
        if len(first_line) < 4:
            continue
        if first_line.lower().startswith('updates') or first_line.lower().startswith('(cid'):
            continue
        if first_line.lower().startswith('project schedule') or first_line.lower().startswith('project description'):
            continue
        if 'page' in first_line.lower() or 'agenda' in first_line.lower():
            continue
        # filter out lines that look like sentences (contain verbs) by checking for periods
        if first_line.endswith('.') and len(first_line.split()) > 6:
            continue
        # avoid lines that are all caps like headings
        names.append(first_line)
    # dedupe
    seen = set()
    uniq = []
    for n in names:
        key = re.sub(r'\s+', ' ', n).strip().lower()
        if key not in seen:
            seen.add(key)
            uniq.append(n)
    return uniq

# gather design projects from all docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    ps = extract_design_projects(text)
    for p in ps:
        if p not in design_projects:
            design_projects.append(p)

# match funding
results = []
for proj in design_projects:
    proj_l = proj.lower()
    matching_rows = []
    total_amount = 0
    for row in funding:
        fn = str(row.get('Project_Name', '')).lower()
        if not fn:
            continue
        if proj_l == fn or proj_l in fn or fn in proj_l:
            matching_rows.append({'Project_Name': row.get('Project_Name'), 'Amount': row.get('Amount')})
            total_amount += row.get('Amount', 0)
    results.append({'project': proj, 'matched_funding_rows': matching_rows, 'total_amount': total_amount})

count = sum(1 for r in results if r['total_amount'] > 50000)

output = {'count': count, 'details': results}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ZEagpG3qicTk8xDnkvuXEAoZ': 'file_storage/call_ZEagpG3qicTk8xDnkvuXEAoZ.json', 'var_call_zb5hL7XuNPEyB7pXOtEhCvU5': 'file_storage/call_zb5hL7XuNPEyB7pXOtEhCvU5.json'}

exec(code, env_args)
