code = """import json, re, pandas as pd

# load docs
path_docs = var_call_WAMNJ61f5486JcBabZKxFr05
with open(path_docs,'r',encoding='utf-8') as f:
    docs = json.load(f)

# load funding projects with total_amount > 50000
path_fund = var_call_OzDBGocdOD2fMDtup9EMDpm1
with open(path_fund,'r',encoding='utf-8') as f:
    fund = json.load(f)

fund_names = {r['Project_Name'] for r in fund}

# extract capital projects under "Capital Improvement Projects (Design)" sections
proj_status = {}
for d in docs:
    text = d.get('text','') or ''
    # normalize line endings
    lines = [ln.strip() for ln in text.splitlines()]
    # find design section start indices
    for i,ln in enumerate(lines):
        if re.search(r'^Capital Improvement Projects \(Design\)', ln, re.IGNORECASE):
            # parse subsequent lines until next section header
            j=i+1
            while j < len(lines):
                l = lines[j]
                if not l:
                    j+=1; continue
                if re.search(r'^Capital Improvement Projects \(Construction\)', l, re.IGNORECASE) or \
                   re.search(r'^Capital Improvement Projects \(Not Started\)', l, re.IGNORECASE) or \
                   re.search(r'^Disaster Recovery Projects', l, re.IGNORECASE):
                    break
                # project name heuristic: a line without bullets/colon and not common words
                if ('Updates' in l) or ('Project Schedule' in l) or ('Estimated Schedule' in l) or ('Project Description' in l):
                    j+=1; continue
                if l.startswith(('(', 'cid', '•', '·', '-', '–')):
                    j+=1; continue
                if re.match(r'^Page \d+', l) or re.match(r'^Agenda Item', l, re.IGNORECASE):
                    j+=1; continue
                # if line looks like a title (not too long, mostly letters/numbers/&/-, and no period at end)
                if len(l) <= 120 and not l.endswith('.'):
                    name = re.sub(r'\s+', ' ', l).strip()
                    # exclude obvious non-project headers
                    if name.lower() in {'capital improvement projects (design)'}:
                        j+=1; continue
                    # record status design
                    proj_status[name] = 'design'
                j+=1

# count projects that are capital (design section implies capital) and have funding>50000
count = sum(1 for n,s in proj_status.items() if s=='design' and n in fund_names)

print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': sorted([n for n in proj_status if n in fund_names])}))"""

env_args = {'var_call_GQQRAR4Br5hBvc3Rkjibl2AI': [{'cnt': '276'}], 'var_call_WAMNJ61f5486JcBabZKxFr05': 'file_storage/call_WAMNJ61f5486JcBabZKxFr05.json', 'var_call_OzDBGocdOD2fMDtup9EMDpm1': 'file_storage/call_OzDBGocdOD2fMDtup9EMDpm1.json', 'var_call_deBjpp3TjgMxZurAUpOdbbmB': 'file_storage/call_deBjpp3TjgMxZurAUpOdbbmB.json', 'var_call_iv9KLC9P0WAxW6oQvxSksTco': ['Funding']}

exec(code, env_args)
