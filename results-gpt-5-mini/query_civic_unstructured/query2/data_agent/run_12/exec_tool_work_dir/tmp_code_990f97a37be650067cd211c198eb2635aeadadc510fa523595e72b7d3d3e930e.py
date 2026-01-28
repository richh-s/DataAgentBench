code = """import json, re

# Load data
with open(var_call_s3s9kMHqzePGSEzEZp7cikyi, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_y31CKagxiG5kZ38LxNmcdJ1z, 'r') as f:
    funding = json.load(f)

# Normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount',0))
    except:
        r['Amount'] = 0

# Keywords for park-related
keywords = ['park','playground','walkway','bluffs','trail']

# Find funding entries whose Project_Name contains any keyword
matched = []
for r in funding:
    name = r.get('Project_Name','').lower()
    if any(k in name for k in keywords):
        matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

# Extract project snippets from civic docs mentioning 'park' and 'completed' and '2022'
extracted = set()
for doc in civic_docs:
    text = doc.get('text','')
    # case-insensitive search for 'park' occurrences
    for m in re.finditer('park', text, flags=re.IGNORECASE):
        start = max(0, m.start()-50)
        end = min(len(text), m.end()+200)
        window = text[start:end].lower()
        if 'completed' in window and '2022' in window:
            # attempt to capture a title-ish substring before 'park'
            left = text[max(0, m.start()-80):m.start()]
            candidate = (left + text[m.start():m.end()+40]).strip()
            candidate = re.sub('\s+',' ', candidate)
            extracted.add(candidate.lower())

# Try to match extracted snippets to funding rows by substring
for ep in extracted:
    for r in funding:
        fname = r.get('Project_Name','').lower()
        if fname in ep or ep in fname:
            # add if not already
            if not any(m['Project_Name']==r['Project_Name'] for m in matched):
                matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

# Compute total
total = sum(m['Amount'] for m in matched)

result = {'matched_projects': matched, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_s3s9kMHqzePGSEzEZp7cikyi': 'file_storage/call_s3s9kMHqzePGSEzEZp7cikyi.json', 'var_call_y31CKagxiG5kZ38LxNmcdJ1z': 'file_storage/call_y31CKagxiG5kZ38LxNmcdJ1z.json'}

exec(code, env_args)
