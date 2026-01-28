code = """import json
import re

# Load data
with open(var_call_VBhtC9hpJRbNT16WmdZtMk4W, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_DFwD6qNOXINdKlJ7slVtPbBE, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records
fundings = []
for r in funding_records:
    amt_raw = r.get('Amount', 0)
    try:
        amt = int(str(amt_raw).replace(',', '').strip())
    except:
        amt = 0
    name = r.get('Project_Name', '').strip()
    fundings.append({'name': name, 'name_l': re.sub(r"[\W_]+", ' ', name).strip().lower(), 'amount': amt})

# Extract design project names from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    # find end of this Design section
    end_candidates = []
    for token in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Design)']:
        pos = text.find(token, start + 1)
        if pos != -1:
            end_candidates.append(pos)
    end = min(end_candidates) if end_candidates else len(text)
    section = text[start:end]
    lines = section.splitlines()
    for i, line in enumerate(lines):
        ln = line.strip()
        if not ln:
            continue
        lower_ln = ln.lower()
        # skip obvious headers/footers
        if lower_ln.startswith('capital improvement') or lower_ln.startswith('agenda item') or lower_ln.startswith('page') or lower_ln.startswith('recommended action'):
            continue
        # look ahead for indicators that this line is a project title
        lookahead_lines = lines[i+1:i+7]
        la = ' '.join(l.strip().lower() for l in lookahead_lines if l.strip())
        if any(k in la for k in ['updates', 'project schedule', 'project description', 'estimated schedule', '(cid:', 'project updates', 'estimated schedule']):
            # clean title
            title = re.sub(r"[:\t\n\r]+$", '', ln).strip()
            if 3 < len(title) < 200:
                design_projects.add(title)

# Fallback: also capture lines in the section that look like Title Case and contain the word 'Project' or 'Park' or 'Road' or 'Median' or 'Walkway' or 'Storm' etc.
if not design_projects:
    keywords = ['project', 'park', 'road', 'median', 'walkway', 'drain', 'storm', 'culvert', 'retaining', 'traffic', 'skate', 'playground', 'water']
    for doc in civic_docs:
        text = doc.get('text', '')
        start = text.find('Capital Improvement Projects (Design)')
        if start == -1:
            continue
        end_candidates = []
        for token in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Design)']:
            pos = text.find(token, start + 1)
            if pos != -1:
                end_candidates.append(pos)
        end = min(end_candidates) if end_candidates else len(text)
        section = text[start:end]
        for line in section.splitlines():
            ln = line.strip()
            if not ln:
                continue
            if any(k in ln.lower() for k in keywords) and 3 < len(ln) < 120:
                design_projects.add(ln)

# Match design projects to funding records with amount > 50000
matched = []
for proj in sorted(design_projects):
    proj_norm = re.sub(r"[\W_]+", ' ', proj).strip().lower()
    matches = []
    for f in fundings:
        if f['amount'] <= 50000:
            continue
        fn = f['name_l']
        # match if normalized names overlap significantly: check if proj_norm in fn or fn in proj_norm or share >=2 words
        if proj_norm and (proj_norm in fn or fn in proj_norm):
            matches.append({'funding_name': f['name'], 'amount': f['amount']})
        else:
            # shared words
            proj_words = set(proj_norm.split())
            fn_words = set(fn.split())
            if len(proj_words & fn_words) >= 2:
                matches.append({'funding_name': f['name'], 'amount': f['amount']})
    if matches:
        matched.append({'project_name': proj, 'funding_matches': matches})

count = len(matched)

result = {'count': count, 'matches': matched, 'design_projects_extracted_count': len(design_projects)}

# Print in required format
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(result))
print('----END PRINT FORMAT----')"""

env_args = {'var_call_VBhtC9hpJRbNT16WmdZtMk4W': 'file_storage/call_VBhtC9hpJRbNT16WmdZtMk4W.json', 'var_call_DFwD6qNOXINdKlJ7slVtPbBE': 'file_storage/call_DFwD6qNOXINdKlJ7slVtPbBE.json'}

exec(code, env_args)
