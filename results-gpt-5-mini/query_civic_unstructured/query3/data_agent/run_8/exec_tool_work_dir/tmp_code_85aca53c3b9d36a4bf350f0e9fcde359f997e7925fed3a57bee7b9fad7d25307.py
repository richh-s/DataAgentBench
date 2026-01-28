code = """import json

funding_path = var_call_U60WqxOGdjsbcqS6PF9PWbjF
docs_path = var_call_8vBnfmWWXT7qozNkwSfsNVHc

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# identify docs with fema or emergency
key_docs = []
for d in docs:
    text = d.get('text','')
    low = text.lower()
    if 'fema' in low or 'emergency' in low:
        key_docs.append(low)

# helper status inference
def infer_status(ctx):
    c = ctx.lower()
    if 'completed' in c or 'notice of completion' in c or 'construction was completed' in c:
        return 'completed'
    if 'begin construction' in c or 'under construction' in c or 'advertise' in c:
        return 'design'
    if 'design' in c or 'plans are being finalized' in c or 'complete design' in c:
        return 'design'
    if 'not started' in c or 'identified' in c or 'awaiting' in c or 'pending' in c:
        return 'not started'
    return 'unknown'

keywords = ['fema', 'emergency', 'outdoor warning', 'sirens']
result = []
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_low = pname.lower()
    related = False
    status = 'unknown'
    # if name contains keyword
    for k in keywords:
        if k in pname_low:
            related = True
            break
    # search in key docs
    if not related:
        for txt in key_docs:
            if pname_low and pname_low in txt:
                related = True
                # infer status from around the first occurrence
                idx = txt.find(pname_low)
                start = idx - 200 if idx>200 else 0
                end = idx + 200 if idx+200 < len(txt) else len(txt)
                ctx = txt[start:end]
                status = infer_status(ctx)
                break
    else:
        # if related because of name, try to find status in key docs if name appears there
        for txt in key_docs:
            if pname_low and pname_low in txt:
                idx = txt.find(pname_low)
                start = idx - 200 if idx>200 else 0
                end = idx + 200 if idx+200 < len(txt) else len(txt)
                ctx = txt[start:end]
                status = infer_status(ctx)
                break
    if related:
        try:
            amt = int(rec.get('Amount',0))
        except:
            try:
                amt = int(float(rec.get('Amount',0)))
            except:
                amt = 0
        result.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source',''), 'Amount': amt, 'Status': status})

# deduplicate by Project_Name
seen = set()
unique = []
for r in result:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique.append(r)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json', 'var_call_LjDjToKzxMRjHcG573Em5PnB': 'file_storage/call_LjDjToKzxMRjHcG573Em5PnB.json'}

exec(code, env_args)
