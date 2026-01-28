code = """import json
funding_path = var_call_t41ybTqD9rfuGcYnHnPfELh2
civic_docs_path = var_call_RRCtw1M6xV7FbcQ20yHrrUFn
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

def mentions(s):
    if not s:
        return False
    s = s.lower()
    return 'fema' in s or 'emergency' in s or 'outdoor warning' in s

results = []
# check funding table
for r in funding:
    pname = r.get('Project_Name') or ''
    src = r.get('Funding_Source') or ''
    amt = r.get('Amount')
    try:
        amt = int(amt)
    except:
        try:
            amt = int(float(amt))
        except:
            amt = None
    if mentions(pname) or mentions(src):
        results.append({'Project_Name': pname, 'Funding_Source': src, 'Amount': amt, 'Status': None})

# combine civic text
all_text = '\n'.join(d.get('text','') for d in civic_docs)
all_lower = all_text.lower()

# find project titles in docs that mention terms
lines = []
for d in civic_docs:
    for ln in d.get('text','').splitlines():
        ln2 = ln.strip()
        if not ln2:
            continue
        # look for heading indicators after this line
        # simple check: if next words contain 'updates' nearby
        if 'updates:' in d.get('text','').lower():
            # if this line or nearby contains terms, add
            window = ln2.lower()
            if mentions(window) or mentions(all_lower):
                lines.append(ln2)

# add doc-found project names if not already in results
existing = set((r['Project_Name'] or '').strip().lower() for r in results)
for ln in set(lines):
    if ln.strip().lower() not in existing:
        results.append({'Project_Name': ln, 'Funding_Source': None, 'Amount': None, 'Status': None})

# detect status for each result by searching nearby in all_text
for item in results:
    pname = (item.get('Project_Name') or '').split('(')[0].strip()
    if not pname:
        item['Status'] = 'unknown'
        continue
    idx = all_lower.find(pname.lower())
    if idx == -1:
        item['Status'] = 'unknown'
        continue
    start = max(0, idx-200)
    end = min(len(all_lower), idx+200)
    window = all_lower[start:end]
    if 'not started' in window:
        item['Status'] = 'not started'
    elif 'construction was completed' in window or 'notice of completion' in window or 'was completed' in window or 'completed' in window:
        item['Status'] = 'completed'
    elif 'design' in window:
        item['Status'] = 'design'
    else:
        item['Status'] = 'unknown'

# sort and print
results_sorted = sorted(results, key=lambda x: (x['Project_Name'] or '').lower())
print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json', 'var_call_dfvnjNQ8s8EXwWJE9zFV1gmc': {'funding_records': 500, 'civic_docs': 5}}

exec(code, env_args)
