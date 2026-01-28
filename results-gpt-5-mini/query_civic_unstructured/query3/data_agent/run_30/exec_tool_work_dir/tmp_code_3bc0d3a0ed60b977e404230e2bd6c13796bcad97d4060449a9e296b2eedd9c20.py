code = """import json

# Load files from storage
path_docs = var_call_dziWdH68wzWWoRRglXmdYLQx
path_fund = var_call_VqvuxlAzlcifj1bcMkrjIDVw

with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)

def norm(s):
    return ' '.join(s.split()).strip().lower()

keywords = ['fema', 'emergency']
projects = {}

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in keywords):
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
                good_tokens = ['project', 'repairs', 'improvements', 'sirens', 'park', 'road', 'bridge', 'drain', 'culvert', 'slope', 'water', 'treatment', 'storm']
                if any(gt in lowc for gt in good_tokens) or len(cand) < 100:
                    title = cand
                    break
            if not title:
                # fallback: use small snippet around the line
                snippet_lines = lines[max(0,i-2):i+1]
                title = ' '.join([l.strip() for l in snippet_lines if l.strip()])
            n = norm(title)
            # infer status from surrounding text
            window = '\n'.join(lines[max(0, i-6): min(len(lines), i+12)])
            wlow = window.lower()
            status = None
            if 'completed' in wlow or 'construction was completed' in wlow or 'complete construction' in wlow or 'complete design' in wlow:
                status = 'completed'
            elif 'under construction' in wlow or 'begin construction' in wlow or 'begin construction:' in wlow or 'begin construction' in wlow:
                status = 'in construction'
            elif 'preliminary design' in wlow or 'in the preliminary design phase' in wlow or 'design' in wlow or 'final design' in wlow:
                status = 'design'
            elif 'not started' in wlow or 'not begun' in wlow:
                status = 'not started'
            if n not in projects:
                projects[n] = {'name': title, 'status': status}

# Match funding records
results = []
for rec in funds:
    pname = rec.get('Project_Name','')
    pname_norm = norm(pname)
    include = False
    if 'fema' in pname_norm or 'emergency' in pname_norm:
        include = True
    else:
        for pnorm in projects.keys():
            if pnorm and (pnorm in pname_norm or pname_norm in pnorm):
                include = True
                break
    if include:
        try:
            amt = int(rec.get('Amount'))
        except Exception:
            amt = None
        # find status if possible
        status = None
        for pnorm, info in projects.items():
            if pnorm and (pnorm in pname_norm or pname_norm in pnorm):
                status = info.get('status')
                break
        results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amt, 'Status': status})

# add extracted projects without funding
for pnorm, info in projects.items():
    already = any(norm(r['Project_Name']) == pnorm for r in results)
    if not already:
        results.append({'Project_Name': info['name'], 'Funding_Source': None, 'Amount': None, 'Status': info.get('status')})

# deduplicate by normalized name preserving order
seen = set()
unique = []
for r in results:
    k = norm(r['Project_Name'])
    if k not in seen:
        seen.add(k)
        unique.append(r)

import json
print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_jWONQnnlxfAddtKc97l9A619': ['civic_docs'], 'var_call_kS6pRvnaONEfsjsY5YLZIDQR': ['Funding'], 'var_call_dziWdH68wzWWoRRglXmdYLQx': 'file_storage/call_dziWdH68wzWWoRRglXmdYLQx.json', 'var_call_VqvuxlAzlcifj1bcMkrjIDVw': 'file_storage/call_VqvuxlAzlcifj1bcMkrjIDVw.json'}

exec(code, env_args)
