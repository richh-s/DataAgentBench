code = """import json, re

# Load data from storage-provided file paths
with open(var_call_ZFmfTDFvIzrFfg8wWNS449Ve, 'r') as f:
    funding = json.load(f)
with open(var_call_D7V2fpC8OJzXCjuYVCZUz81c, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and prepare list
for rec in funding:
    try:
        rec['Amount'] = int(rec.get('Amount') or 0)
    except:
        # Remove non-digits
        s = re.sub(r"[^0-9]", "", str(rec.get('Amount') or "0"))
        rec['Amount'] = int(s) if s else 0

# Candidate keyword list for park-related projects
keywords = ['park', 'walkway', 'playground', 'bench', 'paver', 'shade', 'play']

# Function to determine if a project is marked completed in 2022 within civic docs
def is_completed_in_2022(project_name, docs):
    pname = project_name.lower()
    # tokens from project name to help fuzzy matching
    tokens = [t for t in re.findall(r"\w+", pname) if len(t) > 3]
    # Always include 'park' and 'walkway' as context tokens
    tokens += ['park', 'walkway', 'playground']
    tokens = list(set(tokens))

    for doc in docs:
        text = (doc.get('text') or '').lower()
        if not text:
            continue
        # Direct project name occurrences
        starts = []
        idx = text.find(pname)
        while idx != -1:
            starts.append(idx)
            idx = text.find(pname, idx + 1)
        # Also search for token occurrences
        for t in tokens:
            idx = text.find(t)
            while idx != -1:
                starts.append(idx)
                idx = text.find(t, idx + 1)
        # Check windows around occurrences for 'completed' and '2022'
        for pos in starts:
            window = text[max(0, pos-300): pos+300]
            if 'completed' in window and '2022' in window:
                return True
        # Check specific phrasing patterns
        # e.g., 'construction was completed ... 2022' or 'completed, November 2022'
        if re.search(r'construction[^.]{0,200}completed[^.]{0,200}2022', text):
            # ensure project token nearby that match exists within 300 chars of the phrase
            for m in re.finditer(r'construction[^.]{0,200}completed[^.]{0,200}2022', text):
                span = m.span()
                window = text[max(0, span[0]-300): min(len(text), span[1]+300)]
                if any(t in window for t in tokens):
                    return True
        # generic 'completed' and '2022' in same sentence
        for m in re.finditer(r'([^.]*completed[^.]*2022[^.]*)', text):
            sentence = m.group(1)
            if any(t in sentence for t in tokens):
                return True
    return False

# Gather candidate funding records that look park-related
candidates = [r for r in funding if any(k in (r.get('Project_Name') or '').lower() for k in keywords)]

matched = []
for rec in candidates:
    pname = rec.get('Project_Name','')
    if is_completed_in_2022(pname, civic_docs):
        matched.append({'Project_Name': pname, 'Amount': rec['Amount']})

total = sum(r['Amount'] for r in matched)

result = {'total_funding': total, 'matched_projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZFmfTDFvIzrFfg8wWNS449Ve': 'file_storage/call_ZFmfTDFvIzrFfg8wWNS449Ve.json', 'var_call_D7V2fpC8OJzXCjuYVCZUz81c': 'file_storage/call_D7V2fpC8OJzXCjuYVCZUz81c.json'}

exec(code, env_args)
