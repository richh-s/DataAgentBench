code = """import json

# Load stored results
with open(var_call_cw1ExblnS6q3arcB6rY11l2F, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_xuXPISfPelohqatkiXoesOCZ, 'r') as f:
    funding_records = json.load(f)

# Helper to get substring index safely

def find_sub(s, sub, start=0):
    try:
        return s.index(sub, start)
    except ValueError:
        return -1

# Extract design project titles without using regex
unique_design_projects = []
seen = set()
for doc in civic_docs:
    text = doc.get('text', '')
    idx = find_sub(text, 'Capital Improvement Projects (Design)')
    if idx == -1:
        continue
    start = idx + len('Capital Improvement Projects (Design)')
    end = len(text)
    for header in ('Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)'):
        h = find_sub(text, header, start)
        if h != -1 and h < end:
            end = h
    section = text[start:end]
    # Build paragraphs by scanning lines
    lines = section.splitlines()
    paras = []
    cur = []
    for line in lines:
        if line.strip() == '':
            if cur:
                paras.append('\n'.join(cur).strip())
                cur = []
        else:
            cur.append(line)
    if cur:
        paras.append('\n'.join(cur).strip())
    # For each paragraph, take first non-empty line as candidate title
    for p in paras:
        first_line = p.split('\n')[0].strip()
        if not first_line:
            continue
        low = first_line.lower()
        if any(k in low for k in ('updates:', 'project schedule', 'estimated schedule', 'project description', 'recommended action', 'discussion', 'page', 'agenda')):
            continue
        if first_line.startswith('(cid'):
            continue
        if len(first_line) < 4:
            continue
        if first_line not in seen:
            seen.add(first_line)
            unique_design_projects.append(first_line)

# Normalization without regex
def normalize(name):
    # remove parenthetical part
    if '(' in name:
        name = name.split('(')[0]
    name = name.lower()
    # replace non-alnum with space
    name = ''.join(ch if (ch.isalnum() or ch.isspace()) else ' ' for ch in name)
    name = ' '.join(name.split())
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

# Match design capital projects to funding > 50000
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
