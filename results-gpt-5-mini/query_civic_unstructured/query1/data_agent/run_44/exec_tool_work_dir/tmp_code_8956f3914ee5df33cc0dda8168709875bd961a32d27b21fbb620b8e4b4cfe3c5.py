code = """import json
# Load stored query results
with open(var_call_CkTOw7owItg4Nr1WGfO0TMTR,'r') as f:
    funding = json.load(f)
with open(var_call_Tw7i9VffVvctxE6jTB66qGgv,'r') as f:
    docs = json.load(f)
# build combined design text
design_phrase = 'capital improvement projects (design)'
combined = ''
for d in docs:
    t = d.get('text','')
    tl = t.lower()
    i = tl.find(design_phrase)
    if i!=-1:
        # take up to 5000 chars after phrase
        combined += ' ' + tl[i:i+5000]
combined_text = combined
# helper
def to_int(x):
    try:
        return int(str(x))
    except:
        try:
            return int(float(str(x)))
        except:
            return None
# filter funding > 50000
fund_over = []
for r in funding:
    a = to_int(r.get('Amount'))
    if a and a>50000:
        fund_over.append({'Project_Name': r.get('Project_Name',''), 'Amount': a})
# match
matched = []
for rec in fund_over:
    name = rec['Project_Name']
    if not name:
        continue
    nn = name.lower().strip()
    base = nn.split('(')[0].strip()
    if base and base in combined_text:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
        continue
    # token check
    words = [w for w in base.replace('\n',' ').split(' ') if len(w)>3]
    if words and all(w in combined_text for w in words):
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})
# dedupe
unique = {}
for m in matched:
    unique[m['Project_Name']] = m
result = {'count': len(unique), 'projects': list(unique.values())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CkTOw7owItg4Nr1WGfO0TMTR': 'file_storage/call_CkTOw7owItg4Nr1WGfO0TMTR.json', 'var_call_Tw7i9VffVvctxE6jTB66qGgv': 'file_storage/call_Tw7i9VffVvctxE6jTB66qGgv.json', 'var_call_pSS3lDx59fnMuanujypwdapl': {'len_funding': 276, 'len_docs': 19}}

exec(code, env_args)
