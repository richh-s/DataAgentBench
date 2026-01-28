code = """import json
from pathlib import Path

# Load tool result files
funding_path = Path(var_call_6sPeBNDTHNtwmBHnnW5cL0Lo)
civic_path = Path(var_call_uIW8AEKnifZF8TLcNMhOHUny)
funding = json.load(open(funding_path, 'r'))
civic_docs = json.load(open(civic_path, 'r'))

# helper to normalize names
def normalize(s):
    if s is None:
        return ''
    return ''.join(ch.lower() if ch.isalnum() or ch.isspace() else ' ' for ch in s).strip()

# Build list of funding records (already filtered Amount>50000 by earlier query)
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = 0
    r['norm_name'] = normalize(r.get('Project_Name',''))

# For each funding record, check if any civic doc contains 'capital improvement projects (design)' and the project name
matched = []
for r in funding:
    pname = r.get('Project_Name','')
    norm = r['norm_name']
    found_design = False
    for doc in civic_docs:
        text = doc.get('text','')
        low = text.lower()
        if 'capital improvement projects (design)' in low:
            # if project name appears in document
            if norm and normalize(low).find(norm) != -1:
                found_design = True
                break
            # also try without parentheses content
            # create a simple short name
            short = pname.split('(')[0].strip().lower()
            if short and short in low:
                found_design = True
                break
        else:
            # if header not present, look for pattern where project name and the word 'design' occur nearby
            ln = low
            if pname.lower() in ln:
                idx = ln.find(pname.lower())
                start = max(0, idx-200)
                end = min(len(ln), idx+200)
                window = ln[start:end]
                if 'design' in window:
                    # also check 'capital' somewhere in doc
                    if 'capital improvement' in low or 'capital improvement projects' in low:
                        found_design = True
                        break
    if found_design:
        matched.append(pname)

# Unique count
unique_matched = sorted(list(set(matched)))
count = len(unique_matched)

out = {'count': count, 'projects': unique_matched}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6sPeBNDTHNtwmBHnnW5cL0Lo': 'file_storage/call_6sPeBNDTHNtwmBHnnW5cL0Lo.json', 'var_call_uIW8AEKnifZF8TLcNMhOHUny': 'file_storage/call_uIW8AEKnifZF8TLcNMhOHUny.json'}

exec(code, env_args)
