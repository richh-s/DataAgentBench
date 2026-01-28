code = """import json, re

# Load results from storage file paths
with open(var_call_n5EDbvSrpnzsPvtxxsRDXaHn, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_UCtFkeFPukflMVSuRjAX2ATl, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding list with cleaned names and amounts
funding_list = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_i = int(amt)
    except:
        try:
            amt_i = int(float(amt))
        except:
            amt_i = 0
    funding_list.append({'name': name, 'lname': name.strip().lower(), 'amount': amt_i})

# Helper to clean candidate project title
def clean_title(s):
    s = s.strip()
    # remove leading bullets or weird markers
    s = re.sub(r'^[\W_]+', '', s)
    # remove internal multiple spaces
    s = re.sub(r'\s+', ' ', s)
    return s

projects_found = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        # look for spring and 2022 in the same line
        if 'spring' in low and '2022' in low:
            # look back for a probable project title
            title = None
            for j in range(i-1, max(i-12, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                lc = cand.lower()
                # skip lines that are labels or obviously not titles
                if lc.startswith('(cid:') or 'updates' in lc or 'project schedule' in lc or lc.startswith('page') or lc.startswith('agenda') or lc.startswith('item') or lc.startswith('subject') or lc.startswith('discussion'):
                    continue
                # also skip lines that are short like single words 'to:' or 'approved by:'
                if len(cand.split()) <= 1:
                    continue
                # Found candidate
                title = clean_title(cand)
                break
            if title:
                projects_found.append(title)

# deduplicate preserving order
seen = set(); projects = []
for p in projects_found:
    key = p.lower()
    if key not in seen:
        seen.add(key); projects.append(p)

# For each extracted project, find matching funding rows (by substring or reverse)
results = []
for p in projects:
    lp = p.lower()
    matched = []
    total_amt = 0
    for fr in funding_list:
        fn = fr['lname']
        if lp == fn or lp in fn or fn in lp:
            matched.append(fr['name'])
            total_amt += fr['amount']
    results.append({'name': p, 'matched_funding_names': matched, 'total_funding': total_amt})

# Compute overall count and sum across projects
project_count = len(results)
total_funding = sum(r['total_funding'] for r in results)

out = {'projects': results, 'project_count': project_count, 'total_funding': total_funding}

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9zlpGDOz1APG3efSPgSJaT9T': ['civic_docs'], 'var_call_rpSQujyLh04LiaP6jDHIocTv': ['Funding'], 'var_call_n5EDbvSrpnzsPvtxxsRDXaHn': 'file_storage/call_n5EDbvSrpnzsPvtxxsRDXaHn.json', 'var_call_UCtFkeFPukflMVSuRjAX2ATl': 'file_storage/call_UCtFkeFPukflMVSuRjAX2ATl.json'}

exec(code, env_args)
