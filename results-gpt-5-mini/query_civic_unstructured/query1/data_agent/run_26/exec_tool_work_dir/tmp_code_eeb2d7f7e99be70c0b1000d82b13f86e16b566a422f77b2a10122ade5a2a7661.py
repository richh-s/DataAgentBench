code = """import json
import re

# Load stored results
with open(var_call_cw1ExblnS6q3arcB6rY11l2F, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_xuXPISfPelohqatkiXoesOCZ, 'r') as f:
    funding_records = json.load(f)

# Extract design project titles using simple string searches
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    idx = text.find('Capital Improvement Projects (Design)')
    if idx == -1:
        continue
    start = idx + len('Capital Improvement Projects (Design)')
    # find next headers
    next_idx = len(text)
    for header in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        h = text.find(header, start)
        if h != -1 and h < next_idx:
            next_idx = h
    block = text[start:next_idx]
    # split by two or more newlines
    segments = re.split('\n\s*\n', block)
    for seg in segments:
        s = seg.strip()
        if not s:
            continue
        first_line = s.split('\n')[0].strip()
        if not first_line:
            continue
        low = first_line.lower()
        if any(k in low for k in ['updates:', 'project schedule', 'estimated schedule', 'project description', 'recommended action', 'discussion', 'page', 'agenda']):
            continue
        if first_line.startswith('(cid'):
            continue
        if len(first_line) < 4:
            continue
        design_projects.append(first_line)

# Deduplicate preserving order
seen = set()
unique_design_projects = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        unique_design_projects.append(p)

# Normalize function
def normalize(name):
    # remove parenthetical suffixes
    name = name.split('(')[0]
    name = name.lower()
    name = re.sub('[^a-z0-9 ]', ' ', name)
    name = re.sub('\s+', ' ', name).strip()
    return name

funding_list = []
for r in funding_records:
    pname = r.get('Project_Name', '')
    amt = r.get('Amount', 0)
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    funding_list.append({'orig': pname, 'norm': normalize(pname), 'amount': amt_int})

# Match
matched = []
for p in unique_design_projects:
    p_norm = normalize(p)
    if len(p_norm) < 3:
        continue
    for f in funding_list:
        if f['amount'] <= 50000:
            continue
        fn = f['norm']
        if p_norm == fn or p_norm in fn or fn in p_norm:
            matched.append(p)
            break

result = {'count': len(matched), 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7N3Y42AyKSQv4OAbqJJcpBzF': ['civic_docs'], 'var_call_cw1ExblnS6q3arcB6rY11l2F': 'file_storage/call_cw1ExblnS6q3arcB6rY11l2F.json', 'var_call_xuXPISfPelohqatkiXoesOCZ': 'file_storage/call_xuXPISfPelohqatkiXoesOCZ.json'}

exec(code, env_args)
