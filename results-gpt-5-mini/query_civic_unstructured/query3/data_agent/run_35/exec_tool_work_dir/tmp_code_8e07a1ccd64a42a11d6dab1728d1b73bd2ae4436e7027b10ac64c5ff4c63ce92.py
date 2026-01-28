code = """import json

funding_path = var_call_t41ybTqD9rfuGcYnHnPfELh2
civic_docs_path = var_call_RRCtw1M6xV7FbcQ20yHrrUFn

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# helper
def mentions_terms(s):
    if not s:
        return False
    s = s.lower()
    terms = ['fema', 'emergency', 'outdoor warning', 'emergency warning']
    return any(t in s for t in terms)

# Normalize funding entries and filter those mentioning fema/emergency
filtered = []
for r in funding:
    pname = r.get('Project_Name') or ''
    fsrc = r.get('Funding_Source') or ''
    amt = r.get('Amount')
    try:
        amt = int(amt)
    except:
        try:
            amt = int(float(amt))
        except:
            amt = None
    if mentions_terms(pname) or mentions_terms(fsrc):
        filtered.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt})

# Extract potential project names from civic docs that are project headings
proj_names_from_docs = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for i, ln in enumerate(lines):
        nxt = lines[i+1] if i+1 < len(lines) else ''
        if any(k in nxt.lower() for k in ['updates:', 'project schedule', 'project description']):
            # check nearby context for terms
            context = ' '.join(lines[max(0,i-3):i+4]).lower()
            if mentions_terms(ln) or mentions_terms(context):
                proj_names_from_docs.add(ln)

# Add doc-found projects that are not in funding
existing = set((r['Project_Name'] or '').strip().lower() for r in filtered)
for name in proj_names_from_docs:
    if name.strip().lower() not in existing:
        filtered.append({'Project_Name': name, 'Funding_Source': None, 'Amount': None})

# Combine all civic text for status search
all_text = '\n'.join(doc.get('text','') for doc in civic_docs).lower()

# status detection
def detect_status(pname):
    if not pname:
        return 'unknown'
    base = pname.split('(')[0].strip().lower()
    idx = all_text.find(base)
    if idx == -1:
        idx = all_text.find(pname.lower())
    if idx == -1:
        return 'unknown'
    start = max(0, idx-200)
    end = min(len(all_text), idx+200)
    window = all_text[start:end]
    if 'not started' in window:
        return 'not started'
    if 'construction was completed' in window or 'notice of completion' in window or 'was completed' in window or 'completed' in window:
        return 'completed'
    if 'design' in window or 'preliminary design' in window or 'complete design' in window or 'final design' in window or 'design phase' in window:
        return 'design'
    return 'unknown'

# Build textual answer
lines = []
seen = set()
for r in filtered:
    pname = r.get('Project_Name') or 'Unknown Project'
    fsrc = r.get('Funding_Source') or 'N/A'
    amt = r.get('Amount')
    amt_str = ("$%s" % amt) if isinstance(amt, int) else 'N/A'
    status = detect_status(pname)
    key = (pname.strip().lower(), fsrc.strip().lower() if fsrc else '', amt_str, status)
    if key in seen:
        continue
    seen.add(key)
    lines.append(f"Project: {pname} | Funding Source: {fsrc} | Amount: {amt_str} | Status: {status}")

if not lines:
    answer_text = 'No projects related to FEMA or emergency were found.'
else:
    answer_text = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json', 'var_call_dfvnjNQ8s8EXwWJE9zFV1gmc': {'funding_records': 500, 'civic_docs': 5}}

exec(code, env_args)
