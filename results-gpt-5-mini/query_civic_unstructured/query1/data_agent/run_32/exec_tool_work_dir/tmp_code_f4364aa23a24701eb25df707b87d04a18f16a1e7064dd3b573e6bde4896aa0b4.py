code = """import json

funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build combined design-related text
combined_design_text = ''
for doc in docs:
    txt = doc.get('text','').lower()
    if 'capital improvement projects' in txt and 'design' in txt:
        combined_design_text += '\n' + txt

if not combined_design_text:
    # fallback: include all documents
    combined_design_text = '\n'.join([d.get('text','').lower() for d in docs])

# helper to normalize strings: remove parentheses content and non-alphanumeric
def normalize(s):
    s = s.lower()
    if '(' in s:
        s = s.split('(')[0]
    # keep alnum and spaces
    s2 = ''.join(ch if (ch.isalnum() or ch.isspace()) else ' ' for ch in s)
    s2 = ' '.join(s2.split())
    return s2

# prepare funding records with Amount > 50000
funding_filtered = []
for r in funding:
    amt_raw = r.get('Amount')
    try:
        amt = int(str(amt_raw).replace(',',''))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            amt = 0
    if amt > 50000:
        funding_filtered.append({'Project_Name': r.get('Project_Name',''), 'Amount': amt})

matched = []
for fr in funding_filtered:
    name = fr['Project_Name']
    norm_name = normalize(name)
    if not norm_name:
        continue
    if norm_name in combined_design_text:
        matched.append(name)
        continue
    # check token overlap: require at least 3 tokens present in text
    tokens = [t for t in norm_name.split() if len(t)>2]
    if len(tokens) >= 3:
        found_all = True
        for tok in tokens:
            if tok not in combined_design_text:
                found_all = False
                break
        if found_all:
            matched.append(name)

matched_unique = sorted(list(set(matched)))
result = {'count': len(matched_unique), 'projects': matched_unique}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json', 'var_call_lVtDhaZ9wn4RKCdruIyGSd0p': {'funding_records': 276}}

exec(code, env_args)
