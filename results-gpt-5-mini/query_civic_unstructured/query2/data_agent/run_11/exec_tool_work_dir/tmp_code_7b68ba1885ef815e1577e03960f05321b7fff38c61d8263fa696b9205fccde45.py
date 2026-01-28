code = """import json, re

# Load data from storage-provided file paths
with open(var_call_FA7KkPgziK2Q90TPgVoTXk32, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_mka5UEs3QWagkOJUBTVZMduK, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding entries
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except Exception:
        amt = str(r.get('Amount','0')).replace(',','').strip()
        try:
            r['Amount'] = int(amt)
        except Exception:
            r['Amount'] = 0
    r['Project_Name_norm'] = str(r.get('Project_Name','')).strip()

# Define park-related keywords
park_keywords = ['park', 'playground', 'walkway', 'bench', 'benches', 'shade structure', 'playground', 'play area', 'walkway', 'bluffs']

# Helper to check if a context indicates completion in 2022
def context_indicates_completed_2022(text):
    t = text.lower()
    return ('completed' in t and '2022' in t) or ('construction was completed' in t and '2022' in t) or (re.search(r'complete( d|d)?\b', t) and '2022' in t)

matched = []

# First pass: match funding project names directly in docs and check nearby context
for rec in funding:
    pname = rec['Project_Name_norm']
    pname_l = pname.lower()
    # Only consider park-related funding records
    if not any(kw in pname_l for kw in park_keywords):
        continue
    found = False
    for doc in docs:
        text = doc.get('text','')
        text_l = text.lower()
        if pname_l in text_l:
            # get index and context window
            idx = text_l.find(pname_l)
            start = max(0, idx-500)
            end = min(len(text_l), idx+500)
            context = text_l[start:end]
            if context_indicates_completed_2022(context):
                matched.append({'Project_Name': pname, 'Amount': rec['Amount'], 'Match_Method': 'direct_name_match'})
                found = True
                break
            else:
                # As fallback, check the whole document
                if context_indicates_completed_2022(text_l):
                    matched.append({'Project_Name': pname, 'Amount': rec['Amount'], 'Match_Method': 'direct_name_match_doc_level'})
                    found = True
                    break
    # no match -> continue

# Second pass: find doc lines that mention park and completed 2022, then try to associate with funding records by token overlap
for doc in docs:
    text = doc.get('text','')
    text_l = text.lower()
    if 'park' in text_l and '2022' in text_l and 'completed' in text_l:
        # find all substrings where completed and 2022 occur and extract surrounding lines
        lines = text.splitlines()
        for i,line in enumerate(lines):
            window = '\n'.join(lines[max(0,i-3):min(len(lines), i+4)])
            if 'park' in window.lower() and context_indicates_completed_2022(window):
                # try to match funding records by token overlap
                for rec in funding:
                    pname = rec['Project_Name_norm']
                    pname_l = pname.lower()
                    if not any(kw in pname_l for kw in park_keywords):
                        continue
                    # compute token overlap: any token of length>4 in common
                    tokens = [t for t in re.split(r'[^a-z0-9]', pname_l) if len(t)>4]
                    if any(tok in window.lower() for tok in tokens):
                        # avoid duplicates
                        if not any(m['Project_Name']==pname for m in matched):
                            matched.append({'Project_Name': pname, 'Amount': rec['Amount'], 'Match_Method': 'doc_window_token_match'})

# Deduplicate and sum amounts
agg = {}
for m in matched:
    name = m['Project_Name']
    agg[name] = agg.get(name, 0) + int(m['Amount'])

matched_list = [{'Project_Name': k, 'Amount': v} for k,v in agg.items()]
total = sum(v for v in agg.values())

result = {'total_funding': total, 'matched_projects': matched_list, 'matched_count': len(matched_list)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FA7KkPgziK2Q90TPgVoTXk32': 'file_storage/call_FA7KkPgziK2Q90TPgVoTXk32.json', 'var_call_mka5UEs3QWagkOJUBTVZMduK': 'file_storage/call_mka5UEs3QWagkOJUBTVZMduK.json'}

exec(code, env_args)
