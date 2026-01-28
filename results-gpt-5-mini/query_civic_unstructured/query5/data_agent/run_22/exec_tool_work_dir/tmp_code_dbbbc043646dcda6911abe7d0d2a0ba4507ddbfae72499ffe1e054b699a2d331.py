code = """import json
from pathlib import Path

# Load tool results from storage
with open(var_call_aQFf9HFC0I6EHkMxw2lXyTLi, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_NLbmrWzNUTVCenWjcer45Eg2, 'r') as f:
    funding = json.load(f)

# Prepare
civic_texts = [doc.get('text','') for doc in civic_docs]

def contains_2022_near(text, name, window=500):
    name_low = name.lower()
    idx = text.lower().find(name_low)
    if idx == -1:
        return False, ''
    start = max(0, idx-window)
    end = min(len(text), idx+len(name)+window)
    snippet = text[start:end]
    return ('2022' in snippet), snippet

# disaster keywords
disaster_kw = ['fema','caloes','caljpia','disaster','fire','woolsey','emergency','flood']

matched = []
total = 0

for r in funding:
    pname = r.get('Project_Name','')
    amount_raw = r.get('Amount',0)
    try:
        amount = int(amount_raw)
    except:
        try:
            amount = int(float(amount_raw))
        except:
            amount = 0
    found_2022 = False
    snippet_combined = ''
    # search across all civic docs
    for txt in civic_texts:
        f2022, snippet = contains_2022_near(txt, pname)
        if f2022:
            found_2022 = True
            snippet_combined = snippet
            break
    # if not found by full name, try searching by shorter tokens of name (first 5 words)
    if not found_2022:
        tokens = pname.split()
        for L in range(min(5,len(tokens)),0,-1):
            short = ' '.join(tokens[:L])
            for txt in civic_texts:
                f2022, snippet = contains_2022_near(txt, short)
                if f2022:
                    found_2022 = True
                    snippet_combined = snippet
                    break
            if found_2022:
                break
    # determine disaster-related
    pname_low = pname.lower()
    is_disaster = any(kw in pname_low for kw in disaster_kw)
    if not is_disaster and snippet_combined:
        low = snippet_combined.lower()
        is_disaster = any(kw in low for kw in disaster_kw)
    # If project name contains typical suffixes like '(FEMA' or 'FEMA/'
    if not is_disaster:
        if '(fema' in pname_low or 'fema/' in pname_low or '(caloes' in pname_low or '(caljpia' in pname_low:
            is_disaster = True
    # If both conditions met, include
    if found_2022 and is_disaster:
        matched.append({'Project_Name': pname, 'Amount': amount})
        total += amount

result = {'total_funding': total, 'matched_projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_utJOBOc79HvVbEidPJDgTaft': ['civic_docs'], 'var_call_kvmPThKwXI8qM9r7EJwF4nIo': ['Funding'], 'var_call_aQFf9HFC0I6EHkMxw2lXyTLi': 'file_storage/call_aQFf9HFC0I6EHkMxw2lXyTLi.json', 'var_call_NLbmrWzNUTVCenWjcer45Eg2': 'file_storage/call_NLbmrWzNUTVCenWjcer45Eg2.json'}

exec(code, env_args)
