code = """import json
from pathlib import Path

# Load the results from previous tool calls (file paths are provided)
with open(var_call_LlZ7mhYIkhEkeUOzYWP7cLpZ, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_E8lpLXkKNAAsMBozhAcI8V6z, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Normalize funding rows: convert Amount to int
for r in funding_rows:
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except:
            r['Amount'] = 0

# Target date tokens indicating Spring 2022
tokens = ["spring 2022", "2022-spring", "2022 spring", "march 2022", "mar 2022", "april 2022", "may 2022", "03/2022", "04/2022", "05/2022", "2022-03", "2022-04", "2022-05"]

found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # split into lines
    lines = text.splitlines()
    for i, line in enumerate(lines):
        l = line.lower()
        if any(tok in l for tok in tokens):
            # search backwards up to 10 lines for a project name candidate
            candidate = None
            for j in range(max(0, i-10), i)[::-1]:
                s = lines[j].strip()
                sl = s.lower()
                if not s:
                    continue
                # skip known non-title lines
                if any(k in sl for k in ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'meeting date', 'subject', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion']):
                    continue
                if ':' in s:
                    continue
                if s.startswith('(') or s.startswith('-'):
                    continue
                # likely project title (avoid very short lines)
                if len(s) < 5:
                    continue
                candidate = s
                break
            if candidate:
                # normalize whitespace
                nm = ' '.join(candidate.split())
                if nm not in found_projects:
                    found_projects.append(nm)

# For safety, also look for lines that explicitly say 'Begin Construction: Spring 2022' or 'Advertise: Spring 2022'
extra_targets = ['begin construction', 'advertise', 'complete design', 'begin construction:']
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        ll = line.lower()
        if any(tok in ll for tok in tokens) and any(et in ll for et in ['begin construction','advertise','complete design','begin construction:','begin construction :']):
            # find project name backwards
            candidate = None
            for j in range(max(0, i-12), i)[::-1]:
                s = lines[j].strip()
                sl = s.lower()
                if not s:
                    continue
                if any(k in sl for k in ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'meeting date', 'subject']):
                    continue
                if ':' in s:
                    continue
                if len(s) < 5:
                    continue
                candidate = s
                break
            if candidate:
                nm = ' '.join(candidate.split())
                if nm not in found_projects:
                    found_projects.append(nm)

# Now match found_projects to funding rows
projects_info = []

def match_funding(name):
    lname = name.lower()
    matches = []
    for r in funding_rows:
        pname = (r.get('Project_Name') or '').lower()
        if not pname:
            continue
        if lname == pname:
            matches.append(r)
        elif lname in pname:
            matches.append(r)
        elif pname in lname:
            matches.append(r)
    return matches

total_funding = 0
for p in found_projects:
    matches = match_funding(p)
    amt = sum(m['Amount'] for m in matches)
    total_funding += amt
    projects_info.append({'name': p, 'funding': amt, 'matched_funding_records': len(matches)})

result = {
    'count': len(found_projects),
    'total_funding': total_funding,
    'projects': projects_info
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_c2EGlBtSoAW0fGTcqwQDZFvK': ['civic_docs'], 'var_call_ehXlmY6tjqkVM78tdGQKjQjX': ['Funding'], 'var_call_LlZ7mhYIkhEkeUOzYWP7cLpZ': 'file_storage/call_LlZ7mhYIkhEkeUOzYWP7cLpZ.json', 'var_call_E8lpLXkKNAAsMBozhAcI8V6z': 'file_storage/call_E8lpLXkKNAAsMBozhAcI8V6z.json'}

exec(code, env_args)
