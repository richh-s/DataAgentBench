code = """import json, re
# Load stored query results
with open(var_call_CkTOw7owItg4Nr1WGfO0TMTR, 'r') as f:
    funding_records = json.load(f)
with open(var_call_Tw7i9VffVvctxE6jTB66qGgv, 'r') as f:
    civic_docs = json.load(f)

# Build combined design sections text
design_phrase = 'capital improvement projects (design)'
construction_phrase = 'capital improvement projects (construction)'
notstarted_phrase = 'capital improvement projects (not started)'
combined_parts = []
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    si = lower.find(design_phrase)
    if si == -1:
        continue
    ei = len(lower)
    ci = lower.find(construction_phrase, si+1)
    if ci != -1 and ci < ei:
        ei = ci
    ni = lower.find(notstarted_phrase, si+1)
    if ni != -1 and ni < ei:
        ei = ni
    part = lower[si:ei]
    combined_parts.append(part)
combined_design_text = '\n'.join(combined_parts)

# Helper normalize
def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    s = ' '.join(s.split())
    return s.strip()

# Filter funding > 50000
fund_over = []
for r in funding_records:
    amt = r.get('Amount')
    try:
        a = int(str(amt))
    except:
        try:
            a = int(float(str(amt)))
        except:
            continue
    if a > 50000:
        fund_over.append({'Project_Name': r.get('Project_Name',''), 'Amount': a})

# Match
matched = []
for rec in fund_over:
    name = rec['Project_Name']
    if not name:
        continue
    nn = normalize(name)
    base = nn.split('(')[0].strip()
    found = False
    if nn and nn in combined_design_text:
        found = True
    elif base and base in combined_design_text:
        found = True
    else:
        tokens = re.findall(r"[a-z0-9]+", base)
        tokens = [t for t in tokens if len(t)>3]
        if tokens:
            if all(tok in combined_design_text for tok in tokens):
                found = True
    if found:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# Deduplicate
unique = {}
for m in matched:
    unique[m['Project_Name']] = m
result = {'count': len(unique), 'projects': list(unique.values())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CkTOw7owItg4Nr1WGfO0TMTR': 'file_storage/call_CkTOw7owItg4Nr1WGfO0TMTR.json', 'var_call_Tw7i9VffVvctxE6jTB66qGgv': 'file_storage/call_Tw7i9VffVvctxE6jTB66qGgv.json', 'var_call_pSS3lDx59fnMuanujypwdapl': {'len_funding': 276, 'len_docs': 19}}

exec(code, env_args)
