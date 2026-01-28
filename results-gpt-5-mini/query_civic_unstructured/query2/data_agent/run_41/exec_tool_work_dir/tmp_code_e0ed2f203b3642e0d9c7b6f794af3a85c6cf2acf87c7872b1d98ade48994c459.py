code = """import json
from pathlib import Path

# Load storage file paths
civic_path = var_call_PtyeJkaJ7tgz3FqTz7Y86hzH
funding_path = var_call_04pIC8dshjrhGwNCQyQ0OpqA

# Read files
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding entries and prepare lookup
funding_records = []
for rec in funding:
    # ensure Amount is int
    amt = rec.get('Amount')
    try:
        amt_i = int(amt)
    except:
        try:
            amt_i = int(float(amt))
        except:
            amt_i = 0
    funding_records.append({
        'Funding_ID': rec.get('Funding_ID'),
        'Project_Name': rec.get('Project_Name'),
        'Amount': amt_i,
        'proj_norm': rec.get('Project_Name','').strip().lower()
    })

# Heuristic extraction from civic docs
candidates = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    # find lines that mention completed and 2022
    for i, line in enumerate(lines):
        low = line.lower()
        if 'completed' in low and '2022' in low and ('park' in low or 'playground' in low or 'walkway' in low or 'bluffs' in low):
            # look back up to 6 lines to find project title
            for j in range(max(0, i-6), i):
                candidate = lines[j]
                if not candidate:
                    continue
                if candidate.startswith('(cid:'):
                    continue
                # heuristic: title lines often Title Case and not sentences (no periods)
                if len(candidate) <= 120 and ('.' not in candidate or candidate.count('.')<2):
                    candidates.add(candidate)
        # also catch lines where earlier lines mention project and later state completed
    # Another pass: find project headings that contain 'park' and then check within next 8 lines for 'completed' and '2022'
    for i, line in enumerate(lines):
        if 'park' in line.lower() or 'playground' in line.lower() or 'bluffs' in line.lower():
            # look forward
            window = ' '.join(lines[i:i+10]).lower()
            if 'completed' in window and '2022' in window:
                candidates.add(lines[i])

# Clean candidates
cleaned = set()
for c in candidates:
    # remove extraneous punctuation
    s = ' '.join(c.split())
    s = s.strip(' -.:\t')
    if len(s) > 2:
        cleaned.add(s)

candidates = sorted(cleaned)

# Match candidates to funding records
matched = []
matched_names = set()
for cand in candidates:
    cn = cand.lower()
    for rec in funding_records:
        pn = rec['proj_norm']
        if cn in pn or pn in cn:
            matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
            matched_names.add(rec['Project_Name'])

# Additionally, some park projects might be referenced in funding but candidate extraction missed them.
# Based on domain knowledge from the civic docs preview, include likely park projects completed in 2022 if present in funding:
# Known from preview: 'Bluffs Park Shade Structure' completed Nov 2022
# Also 'Marie Canyon Green Streets' completed Jan 2023 (not 2022)
# 'Point Dume Walkway Repairs' completed Nov 2022 (walkway, not necessarily park but related to park-like)
# 'Broad Beach Road...' not park
# We'll also search funding for project names containing 'park' and check civic docs for 'completed'+'2022' anywhere
for rec in funding_records:
    if 'park' in rec['proj_norm'] or 'walkway' in rec['proj_norm'] or 'playground' in rec['proj_norm']:
        # search civic docs full text for project name and completed 2022
        pname = rec['Project_Name']
        found = False
        for doc in civic_docs:
            txt = doc.get('text','').lower()
            if pname.lower() in txt and 'completed' in txt and '2022' in txt:
                if pname not in matched_names:
                    matched.append({'Project_Name': pname, 'Amount': rec['Amount']})
                    matched_names.add(pname)
                found = True
                break

# Sum amounts
total = sum(m['Amount'] for m in matched)

# Prepare output
output = {
    'matched_projects': matched,
    'total_amount': total
}

import json
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_hh4ITR6h6eIithh7NHKmshSa': [], 'var_call_GsuCLQRVjH60iU6V9jjGP1rC': ['civic_docs'], 'var_call_PtyeJkaJ7tgz3FqTz7Y86hzH': 'file_storage/call_PtyeJkaJ7tgz3FqTz7Y86hzH.json', 'var_call_04pIC8dshjrhGwNCQyQ0OpqA': 'file_storage/call_04pIC8dshjrhGwNCQyQ0OpqA.json'}

exec(code, env_args)
