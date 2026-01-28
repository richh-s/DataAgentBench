code = """import json
import re
from pathlib import Path

# Load data from storage keys
# var_call_ctLyqZR8fkaXSHk4KkkSkUGJ contains funding query result (possibly a path)
# var_call_ccBil4OvpM1STg64nB901Qca contains civic docs query result

def load_var(var):
    if isinstance(var, str):
        p = Path(var)
        with p.open('r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

funding = load_var(var_call_ctLyqZR8fkaXSHk4KkkSkUGJ)
docs = load_var(var_call_ccBil4OvpM1STg64nB901Qca)

# Normalize funding amounts and project names
for r in funding:
    # Ensure Amount is int
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except:
        # remove any non-digits
        s = re.sub(r"[^0-9]", "", str(r.get('Amount', '0')))
        r['Amount'] = int(s) if s!='' else 0
    r['Project_Name_norm'] = r.get('Project_Name','').strip().lower()

# Parse civic docs for project headings and completed lines in 2022
completed_projects = set()

for doc in docs:
    text = doc.get('text','')
    if not text:
        continue
    lines = text.splitlines()
    # build list of non-empty trimmed lines to analyze with indices
    n = len(lines)
    i = 0
    current_proj = None
    while i < n:
        line = lines[i].strip()
        # find next non-empty line
        if line:
            # lookahead to next non-empty line
            j = i+1
            next_non = ''
            while j < n:
                if lines[j].strip():
                    next_non = lines[j].strip()
                    break
                j += 1
            # Heuristic for heading: line does not start with '(' and not end with ':' and not all uppercase like 'PAGE 1' and next_non contains 'Updates' or '(cid' or 'Updates:' or next_non starts with '(cid'
            low = line.lower()
            is_heading = False
            if (not line.startswith('(')) and (not line.endswith(':')) and (not re.match(r'^page \d+', low)) and (len(line) < 200):
                if next_non and ('update' in next_non.lower() or next_non.lower().startswith('(cid') or 'updates:' in next_non.lower() or 'updates'==next_non.lower()):
                    is_heading = True
                # also if line contains words like 'park' or 'playground' or 'walkway' or 'playground' assume heading
                if any(w in low for w in ['park', 'playground', 'walkway', 'walk', 'playground']):
                    is_heading = True
            if is_heading:
                current_proj = line
                # look forward few lines to see if completed in 2022
                k = i+1
                found = False
                while k < min(n, i+20):
                    l = lines[k].strip()
                    if not l:
                        k += 1
                        continue
                    lowl = l.lower()
                    # If we hit another heading-like line, break
                    if (not l.startswith('(')) and (not l.endswith(':')) and (len(l) < 200) and (any(w in l.lower() for w in ['park','walk','playground','repairs','project','improvements','repair','walkway'])):
                        # but avoid breaking immediately; allow scanning up to 20 lines
                        pass
                    # check completion
                    if 'completed' in lowl and '2022' in lowl:
                        completed_projects.add(current_proj.strip())
                        break
                    k += 1
        i += 1

# Filter for park-related project names (contain 'park')
park_completed_projects = [p for p in completed_projects if 'park' in p.lower()]

# Now match funding records: match if funding.project_name contains the civic project name or vice versa (case-insensitive), using normalized forms
matched_funding_ids = set()
matched_records = []
for p in park_completed_projects:
    p_norm = p.strip().lower()
    for r in funding:
        fn = r['Project_Name_norm']
        if p_norm and (p_norm in fn or fn in p_norm):
            matched_funding_ids.add(r['Funding_ID'])
            matched_records.append({'Funding_ID': r['Funding_ID'], 'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

# Sum amounts (unique Funding_IDs)
unique_ids = set(matched_funding_ids)
total = 0
for r in funding:
    if r['Funding_ID'] in unique_ids:
        total += r['Amount']

# Prepare result
result = {
    'park_completed_projects_detected': sorted(list(park_completed_projects)),
    'matched_funding_records': matched_records,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ctLyqZR8fkaXSHk4KkkSkUGJ': 'file_storage/call_ctLyqZR8fkaXSHk4KkkSkUGJ.json', 'var_call_QtXnjwntrTMUfGDmFcDaabI9': ['civic_docs'], 'var_call_ccBil4OvpM1STg64nB901Qca': 'file_storage/call_ccBil4OvpM1STg64nB901Qca.json'}

exec(code, env_args)
