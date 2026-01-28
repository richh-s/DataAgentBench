code = """import json
import re

# Load mongo query results file
path_docs = var_call_dziWdH68wzWWoRRglXmdYLQx
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding table results file
path_fund = var_call_VqvuxlAzlcifj1bcMkrjIDVw
with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)

keywords = ['fema', 'emergency']

# Helper to normalize names
def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())

# Extract project titles and nearby text containing keywords
projects = {}  # norm_name -> {'name': original, 'status': inferred}

for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in keywords):
            # find title up to 6 lines above
            title = None
            for j in range(max(0, i-6), i)[::-1]:
                cand = lines[j].strip()
                if not cand:
                    continue
                lowc = cand.lower()
                bad_tokens = ['updates', 'project description', 'project schedule', 'agenda', 'item', 'page', 'meeting date', 'to:', 'prepared by', 'approved by']
                if any(bt in lowc for bt in bad_tokens):
                    continue
                if len(cand) > 300:
                    continue
                # prefer lines that look like a project title (contain Project or Repairs or Improvements or Sirens or Park or Road or Bridge or Drain)
                good_tokens = ['project', 'repairs', 'improvements', 'sirens', 'park', 'road', 'bridge', 'drain', 'culvert', 'slope', 'water', 'treatment', 'storm']
                if any(gt in lowc for gt in good_tokens) or (len(cand) < 100):
                    title = cand
                    break
            if not title:
                # fallback: use a merged snippet around line
                title = (lines[max(0,i-2):i+1])
                title = ' '.join([l.strip() for l in title if l.strip()])
            n = norm(title)
            # infer status by scanning nearby lines (from title to +12 lines)
            status = None
            window = '\n'.join(lines[max(0, i-6): min(len(lines), i+12)])
            wlow = window.lower()
            if re.search(r'complete construction|construction was completed|complete design|complete(d)?\b', wlow):
                status = 'completed'
            if status is None and re.search(r'currently under construction|begin construction|begin construction:|construction', wlow):
                status = 'construction'
            if status is None and re.search(r'preliminary design|in the preliminary design phase|design|final design|complete design', wlow):
                status = 'design'
            if status is None and re.search(r'not started|identified but not begun|not begun|not started', wlow):
                status = 'not started'
            # map certain phrases
            if status == 'construction':
                status = 'in construction'
            # store
            if n not in projects:
                projects[n] = {'name': title, 'status': status}

# Now match funding records related to FEMA or emergency or matching project names
results = []
for rec in funds:
    pname = rec.get('Project_Name','')
    pname_norm = norm(pname)
    include = False
    # include if funding project name mentions FEMA or emergency
    if 'fema' in pname_norm or 'emergency' in pname_norm:
        include = True
    else:
        # check if pname_norm contains any extracted project normalized name or vice versa
        for pnorm, info in projects.items():
            if pnorm and (pnorm in pname_norm or pname_norm in pnorm):
                include = True
                break
    if include:
        # get status if possible
        status = None
        # try direct match
        for pnorm, info in projects.items():
            if pnorm and (pnorm in pname_norm or pname_norm in pnorm):
                status = info.get('status')
                break
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': int(rec.get('Amount')) if rec.get('Amount') not in (None, '') else None,
            'Status': status
        })

# Also include extracted projects that didn't have funding records but mentioned FEMA/emergency
for pnorm, info in projects.items():
    # check if any funding record already included
    already = any(norm(r['Project_Name']) == pnorm for r in results)
    if not already:
        # include if project name or its context included 'fema' or 'emergency' -- we only extracted those that did
        results.append({
            'Project_Name': info['name'],
            'Funding_Source': None,
            'Amount': None,
            'Status': info.get('status')
        })

# Deduplicate results by normalized Project_Name preserving order
seen = set()
unique_results = []
for r in results:
    k = norm(r['Project_Name'])
    if k not in seen:
        seen.add(k)
        unique_results.append(r)

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_jWONQnnlxfAddtKc97l9A619': ['civic_docs'], 'var_call_kS6pRvnaONEfsjsY5YLZIDQR': ['Funding'], 'var_call_dziWdH68wzWWoRRglXmdYLQx': 'file_storage/call_dziWdH68wzWWoRRglXmdYLQx.json', 'var_call_VqvuxlAzlcifj1bcMkrjIDVw': 'file_storage/call_VqvuxlAzlcifj1bcMkrjIDVw.json'}

exec(code, env_args)
