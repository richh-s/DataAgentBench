code = """import json

# Load data from storage-provided file paths
with open(var_call_VBhtC9hpJRbNT16WmdZtMk4W, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_DFwD6qNOXINdKlJ7slVtPbBE, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# helper to normalize to lowercase alphanumeric words
def normalize_text(s):
    s = s or ''
    chars = []
    for ch in s.lower():
        if ch.isalnum():
            chars.append(ch)
        else:
            chars.append(' ')
    words = [w for w in ''.join(chars).split() if w]
    return ' '.join(words)

# normalize funding records
fundings = []
for r in funding_records:
    amt_raw = r.get('Amount', 0)
    try:
        amt = int(str(amt_raw).replace(',', '').strip())
    except:
        amt = 0
    name = r.get('Project_Name', '').strip()
    fundings.append({'name': name, 'name_norm': normalize_text(name), 'amount': amt})

# extract design project names from civic docs
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    # find end token
    end_pos = len(text)
    # look for other section starts after this start
    tokens = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
    for t in tokens:
        p = text.find(t, start+1)
        if p != -1 and p < end_pos:
            end_pos = p
    section = text[start:end_pos]
    lines = section.splitlines()
    for i, line in enumerate(lines):
        ln = line.strip()
        if not ln:
            continue
        low_lookahead = ' '.join(l.strip().lower() for l in lines[i+1:i+7] if l.strip())
        if 'updates' in low_lookahead or 'project schedule' in low_lookahead or 'project description' in low_lookahead or '(cid:' in low_lookahead or 'project updates' in low_lookahead or 'estimated schedule' in low_lookahead:
            # filter headers
            low = ln.lower()
            if low.startswith('capital improvement') or low.startswith('agenda item') or low.startswith('page') or low.startswith('recommended action'):
                continue
            if 3 < len(ln) < 200:
                design_projects.add(ln)

# fallback: if none found, look for lines containing keywords
if not design_projects:
    keywords = ['project', 'park', 'road', 'median', 'walkway', 'drain', 'storm', 'culvert', 'retaining', 'traffic', 'skate', 'playground', 'water']
    for doc in civic_docs:
        text = doc.get('text', '')
        start = text.find('Capital Improvement Projects (Design)')
        if start == -1:
            continue
        end_pos = len(text)
        tokens = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
        for t in tokens:
            p = text.find(t, start+1)
            if p != -1 and p < end_pos:
                end_pos = p
        section = text[start:end_pos]
        for line in section.splitlines():
            ln = line.strip()
            if not ln:
                continue
            low = ln.lower()
            if any(k in low for k in keywords) and 3 < len(ln) < 120:
                design_projects.add(ln)

# match projects to funding > 50000
matched = []
for proj in sorted(design_projects):
    proj_norm = normalize_text(proj)
    proj_words = set(proj_norm.split())
    if not proj_words:
        continue
    matches = []
    for f in fundings:
        if f['amount'] <= 50000:
            continue
        f_words = set(f['name_norm'].split())
        # match if proj_norm in f_name or f_name in proj_norm or at least 2 shared words
        if proj_norm and (proj_norm == f['name_norm'] or proj_norm in f['name_norm'] or f['name_norm'] in proj_norm):
            matches.append({'funding_name': f['name'], 'amount': f['amount']})
        else:
            if len(proj_words & f_words) >= 2:
                matches.append({'funding_name': f['name'], 'amount': f['amount']})
    if matches:
        matched.append({'project_name': proj, 'funding_matches': matches})

count = len(matched)
result = {'count': count, 'matches': matched, 'design_projects_extracted_count': len(design_projects)}

# print as required
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(result))
print('----END PRINT FORMAT----')"""

env_args = {'var_call_VBhtC9hpJRbNT16WmdZtMk4W': 'file_storage/call_VBhtC9hpJRbNT16WmdZtMk4W.json', 'var_call_DFwD6qNOXINdKlJ7slVtPbBE': 'file_storage/call_DFwD6qNOXINdKlJ7slVtPbBE.json'}

exec(code, env_args)
