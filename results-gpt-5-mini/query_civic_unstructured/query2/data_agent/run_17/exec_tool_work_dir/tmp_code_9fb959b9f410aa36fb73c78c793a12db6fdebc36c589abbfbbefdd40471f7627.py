code = """import json, re

# Load civic docs results
path_civic = var_call_qq5H8yxp6vSjXz8DyOJq4vMt
with open(path_civic, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding results
path_funding = var_call_MRy4mHtwIMauqNFgG2MkW8MK
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to int
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount', 0)))
        except:
            r['Amount'] = 0

# Primary park-related keywords
park_kw = ['park', 'playground', 'bluffs']

# Find funding projects that are clearly park-related by name
park_candidates = []
for r in funding:
    name = r.get('Project_Name','')
    lname = name.lower()
    if any(k in lname for k in park_kw):
        park_candidates.append(r)

matched = []

# Helper to check if project is mentioned as completed in 2022 within civic docs
def project_completed_in_2022(project_name):
    pname = project_name.lower()
    for doc in civic_docs:
        text = doc.get('text','').lower()
        if pname in text:
            # find windows around occurrences
            idx = text.find(pname)
            # search within 400 chars window
            start = max(0, idx-400)
            end = min(len(text), idx+len(pname)+400)
            window = text[start:end]
            if '2022' in window and ('complete' in window or 'completed' in window or 'construction was completed' in window or 'notice of completion' in window):
                return True
    return False

# Check park_candidates
for proj in park_candidates:
    if project_completed_in_2022(proj['Project_Name']):
        matched.append({'Project_Name': proj['Project_Name'], 'Amount': proj['Amount']})

# Additionally, find park mentions in docs that say completed in 2022, extract nearby phrase and match to funding by substring
found_park_phrases = set()
for doc in civic_docs:
    text = doc.get('text','')
    ltext = text.lower()
    if 'park' in ltext and '2022' in ltext and 'completed' in ltext:
        # find all occurrences of 'park'
        for m in re.finditer('park', ltext):
            i = m.start()
            start = max(0, i-60)
            end = min(len(text), i+60)
            snippet = text[start:end]
            # clean snippet to get a candidate name: split on newlines and punctuation
            cand = snippet.strip()
            # remove leading/trailing non-alphanum
            cand = re.sub(r'^[^A-Za-z0-9]+','',cand)
            cand = re.sub(r'[^A-Za-z0-9]+$','',cand)
            if len(cand) > 3:
                found_park_phrases.add(cand)

# Try matching these phrases to funding entries
for phrase in found_park_phrases:
    lphrase = phrase.lower()
    for f in funding:
        if lphrase in f['Project_Name'].lower() or f['Project_Name'].lower() in lphrase:
            if not any(x['Project_Name']==f['Project_Name'] for x in matched):
                matched.append({'Project_Name': f['Project_Name'], 'Amount': f['Amount']})

# As a final safety, consider funding entries whose name suggests park but that may not have been matched; check civic docs for their base name words and 2022 completion
for f in funding:
    lname = f['Project_Name'].lower()
    if any(k in lname for k in park_kw) and not any(x['Project_Name']==f['Project_Name'] for x in matched):
        if project_completed_in_2022(f['Project_Name']):
            matched.append({'Project_Name': f['Project_Name'], 'Amount': f['Amount']})

# Sum amounts
total = sum(item['Amount'] for item in matched)

result = {'total_funding': total, 'matched_projects': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_h13harN4hIdf4SoYdUp1TJC9': ['civic_docs'], 'var_call_cRJrleGz2E7eW0b4Wfh42kvJ': ['Funding'], 'var_call_qq5H8yxp6vSjXz8DyOJq4vMt': 'file_storage/call_qq5H8yxp6vSjXz8DyOJq4vMt.json', 'var_call_MRy4mHtwIMauqNFgG2MkW8MK': 'file_storage/call_MRy4mHtwIMauqNFgG2MkW8MK.json'}

exec(code, env_args)
