code = """import json, re
from pathlib import Path

# Load storage-provided JSON files
with open(var_call_VAIIgByZSdgcjr25PevQ2kkY, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_GS48k3w0jE3Dso9vMsDQ40Z4, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Prepare funding project names and amounts
funding_projects = []
for r in funding:
    name = r.get('Project_Name')
    try:
        amt = int(r.get('Amount'))
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            amt = 0
    funding_projects.append({'name': name, 'amount': amt})

# Helper to find if project has a start in Spring 2022 in civic docs
spring_months = ['march', 'mar', 'april', 'apr', 'may']

matched_projects = {}

for fp in funding_projects:
    pname = fp['name']
    pname_lower = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','').lower()
        # search for exact name or partial significant words
        if pname_lower in text:
            # find occurrences
            for m in re.finditer(re.escape(pname_lower), text):
                start = m.start()
                window = text[start:start+1000]  # look ahead in 1000 chars
                # Check for 'spring' within window and '2022' near it
                if 'spring' in window and '2022' in window:
                    found = True
                    break
                # Check for spring months with 2022 within a small distance
                for mon in spring_months:
                    if mon in window and '2022' in window:
                        found = True
                        break
                if found:
                    break
        if found:
            matched_projects[pname] = matched_projects.get(pname, 0) + fp['amount']
            break

# Additionally, some projects might be in civic docs but funding table has slightly different names.
# To capture more, search civic docs for any project-like lines containing 'Begin Construction' or 'Begin Construction:' or 'Construction was completed' with 'spring' and '2022', then try to match nearby project titles from funding list using substring matching.

# Build a set of candidate project titles from civic docs by scanning for lines that look like project headings
candidates = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Heuristic: project headings often are Title Case and not very long
        if line.strip() and len(line.strip()) < 100 and any(c.isalpha() for c in line):
            # Look ahead for schedule info in next 6 lines
            lookahead = " ".join(lines[i:i+12]).lower()
            if ('spring' in lookahead or any(mon in lookahead for mon in spring_months)) and '2022' in lookahead:
                candidates.append(line.strip())

# Try to match candidates to funding project names by fuzzy substring
for cand in candidates:
    cl = cand.lower()
    for fp in funding_projects:
        pname = fp['name']
        if pname.lower() in cl or cl in pname.lower() or any(word in pname.lower() for word in cl.split() if len(word)>5):
            if pname not in matched_projects:
                matched_projects[pname] = matched_projects.get(pname, 0) + fp['amount']

# Prepare final results
unique_projects = sorted(list(matched_projects.keys()))
total_funding = sum(matched_projects.values())
count = len(unique_projects)

result = {'count': count, 'total_funding': total_funding, 'projects': unique_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VAIIgByZSdgcjr25PevQ2kkY': 'file_storage/call_VAIIgByZSdgcjr25PevQ2kkY.json', 'var_call_GS48k3w0jE3Dso9vMsDQ40Z4': 'file_storage/call_GS48k3w0jE3Dso9vMsDQ40Z4.json'}

exec(code, env_args)
