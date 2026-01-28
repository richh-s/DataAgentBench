code = """import json
with open(var_call_CkTOw7owItg4Nr1WGfO0TMTR,'r') as f:
    funding = json.load(f)
with open(var_call_Tw7i9VffVvctxE6jTB66qGgv,'r') as f:
    docs = json.load(f)
# get design sections
designs = []
for d in docs:
    t = d.get('text','')
    tl = t.lower()
    idx = tl.find('capital improvement projects (design)')
    if idx!=-1:
        # take next 3000 chars
        designs.append(tl[idx:idx+3000])
design_text = ' '.join(designs)
# get funding >50k
fund_over = [r for r in funding if (str(r.get('Amount','0')).isdigit() and int(r.get('Amount'))>50000)]
# match by checking if base name (without parenthesis) appears in design_text
matched = []
for r in fund_over:
    name = r.get('Project_Name','')
    if not name:
        continue
    base = name.lower().split('(')[0].strip()
    if base and base in design_text:
        matched.append({'Project_Name': r.get('Project_Name'), 'Amount': int(r.get('Amount'))})
# unique
unique = {m['Project_Name']:m for m in matched}
res = {'count': len(unique), 'projects': list(unique.values())}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_CkTOw7owItg4Nr1WGfO0TMTR': 'file_storage/call_CkTOw7owItg4Nr1WGfO0TMTR.json', 'var_call_Tw7i9VffVvctxE6jTB66qGgv': 'file_storage/call_Tw7i9VffVvctxE6jTB66qGgv.json', 'var_call_pSS3lDx59fnMuanujypwdapl': {'len_funding': 276, 'len_docs': 19}}

exec(code, env_args)
