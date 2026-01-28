code = """import json

funding_path = var_call_VzgihgZ7OwHfelcmF5z1sI2X
docs_path = var_call_zyKqzSQAopIHC3ukf8gNzESM

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a single big lowercase text for each document
doc_texts = [d.get('text','').lower() for d in docs]

matched = []
for r in funding:
    # parse amount
    amt_raw = r.get('Amount')
    try:
        amt = int(str(amt_raw).replace(',',''))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            amt = 0
    if amt <= 50000:
        continue
    name = r.get('Project_Name','')
    if not name:
        continue
    name_norm = name.lower()
    name_norm = name_norm.split('(')[0].strip()
    name_norm = name_norm.replace('.', ' ')
    name_norm = name_norm.replace('/', ' ')
    name_norm = name_norm.replace('-', ' ')
    # simple token check
    tokens = [t for t in name_norm.split() if len(t)>2]
    if not tokens:
        continue
    # check each document for presence of name tokens in order
    found_design = False
    for txt in doc_texts:
        if tokens[0] in txt:
            # check if all tokens are present
            all_present = True
            for tk in tokens:
                if tk not in txt:
                    all_present = False
                    break
            if not all_present:
                continue
            # find position of first token
            pos = txt.find(tokens[0])
            # get context window
            start = pos - 200 if pos - 200 > 0 else 0
            end = pos + 200
            ctx = txt[start:end]
            if 'design' in ctx:
                found_design = True
                break
            # also check whole doc for 'capital improvement projects' and 'design'
            if 'capital improvement projects' in txt and 'design' in txt:
                # and project name appears anywhere
                if all(tk in txt for tk in tokens):
                    found_design = True
                    break
    if found_design:
        matched.append(name)

matched_unique = sorted(list(set(matched)))
result = {'count': len(matched_unique), 'projects': matched_unique}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w6mzZJWh1Qf1WequniXaReqc': ['civic_docs'], 'var_call_8FNlL82nAuBCB7zgbjsxnppT': ['Funding'], 'var_call_VzgihgZ7OwHfelcmF5z1sI2X': 'file_storage/call_VzgihgZ7OwHfelcmF5z1sI2X.json', 'var_call_zyKqzSQAopIHC3ukf8gNzESM': 'file_storage/call_zyKqzSQAopIHC3ukf8gNzESM.json', 'var_call_lVtDhaZ9wn4RKCdruIyGSd0p': {'funding_records': 276}}

exec(code, env_args)
