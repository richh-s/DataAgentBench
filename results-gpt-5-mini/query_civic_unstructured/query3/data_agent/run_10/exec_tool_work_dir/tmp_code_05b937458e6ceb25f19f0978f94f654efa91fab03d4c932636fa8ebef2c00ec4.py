code = """import json

with open(var_call_lzuql9XO4mip4vcz5jSfIR6d, 'r') as f:
    funding = json.load(f)
with open(var_call_OTWLMZF2U2vjKkDgiSiAfRbv, 'r') as f:
    docs = json.load(f)

doc_texts = [d.get('text','').lower() for d in docs]
combined = "\n".join(doc_texts)

keywords = ['fema','emergency','outdoor warning','sirens','backup power','disaster']

results = []
seen = set()
for row in funding:
    pname = row.get('Project_Name','')
    pname_low = pname.lower()
    pname_norm = pname_low.split('(')[0].strip()

    related = False
    for k in keywords:
        if k in pname_low:
            related = True
            break
    if not related and pname_norm:
        for t in doc_texts:
            if pname_norm in t:
                related = True
                break
    if not related:
        continue

    # amount
    amt = None
    try:
        amt = int(row.get('Amount'))
    except:
        try:
            amt = int(float(row.get('Amount')))
        except:
            amt = None

    # status
    status = None
    for t in doc_texts:
        if pname_norm in t or pname_low in t:
            if 'construction was completed' in t or 'notice of completion' in t or 'complete construction' in t or 'completed' in t:
                status = 'completed'
                break
            if 'design' in t or 'complete design' in t or 'preliminary design' in t or 'working with the consultant' in t or 'awaiting' in t or 'begin construction' in t:
                status = 'design'
                break
            if 'not started' in t or 'identified' in t or 'waiting for the agreement' in t:
                status = 'not started'
                break
    if status is None:
        if 'fema' in pname_low or 'emergency' in pname_low:
            status = 'design'

    if pname not in seen:
        seen.add(pname)
        results.append({'Project_Name': pname, 'Funding_Source': row.get('Funding_Source'), 'Amount': amt, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json', 'var_call_kpbSuqMp0pn6b3LPb8E1hlgz': {'var1_type': 'str', 'var2_type': 'str'}, 'var_call_IYe14sR0kxs7mSnFvSfNNoBv': {'funding_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
