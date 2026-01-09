code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_WmvCBm49m9oGdB5RA0jNkePG)
cpc_recs = load_records(var_call_gre8zOZFtjVX1yWIPtvZ3cm7)

cpc_title = {r['symbol']: r.get('titleFull') for r in cpc_recs}

# helper: parse assignee from Patents_info
assignee_pat = re.compile(r"owned by ([^.;]+)|assigned to ([^.;]+)|holds the [A-Z]{2} patent filing .*? owned by ([^.;]+)")

def get_assignee(pi):
    m = assignee_pat.search(pi or '')
    if not m:
        # fallback common phrasing
        m2 = re.search(r"is (?:owned by|assigned to) ([^.;]+)", pi or '')
        if m2:
            return m2.group(1).strip()
        return None
    for g in m.groups():
        if g:
            return g.strip()
    return None

# build UC publication numbers set
uc_pubnums=set()
rows=[]
for r in pub_recs:
    pi=r.get('Patents_info')
    ass=get_assignee(pi)
    if not ass or 'UNIV CALIFORNIA' not in ass.upper():
        continue
    m=re.search(r"pub\. number\s+([A-Z]{2}-[0-9A-Za-z-]+)", pi or '')
    if m:
        uc_pubnums.add(m.group(1).strip())
    else:
        m=re.search(r"publication number\s+([A-Z]{2}-[0-9A-Za-z-]+)", pi or '')
        if m:
            uc_pubnums.add(m.group(1).strip())

# map publication_number -> primary CPC subclass title
primary_subclass_title_by_pub={}
for r in pub_recs:
    pi=r.get('Patents_info')
    pubm=re.search(r"pub\. number\s+([A-Z]{2}-[0-9A-Za-z-]+)", pi or '') or re.search(r"publication number\s+([A-Z]{2}-[0-9A-Za-z-]+)", pi or '')
    if not pubm:
        continue
    pubnum=pubm.group(1).strip()
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs=[]
    primary_code=None
    for e in cpcs:
        if isinstance(e, dict) and e.get('first') is True:
            primary_code=e.get('code')
            break
    if not primary_code and cpcs:
        # fallback first code
        if isinstance(cpcs[0], dict):
            primary_code=cpcs[0].get('code')
        elif isinstance(cpcs[0], str):
            primary_code=cpcs[0]
    if not primary_code:
        continue
    # subclass = first 4 chars of code (e.g., F25B)
    subclass=primary_code.replace(' ', '')[:4]
    title=cpc_title.get(subclass)
    if title:
        primary_subclass_title_by_pub[pubnum]=title

# find citing assignees: patents whose citations include any UC pubnum
result=set()
for r in pub_recs:
    pi=r.get('Patents_info')
    citing_assignee=get_assignee(pi)
    if not citing_assignee:
        continue
    if 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    try:
        cites=json.loads(r.get('citation') or '[]')
    except Exception:
        cites=[]
    cited_pubnums=[c.get('publication_number') for c in cites if isinstance(c, dict)]
    for cp in cited_pubnums:
        if cp in uc_pubnums:
            title=primary_subclass_title_by_pub.get(cp)
            if title:
                result.add((citing_assignee, title))

out=[{'citing_assignee':a, 'cpc_subclass_title':t} for a,t in sorted(result)]
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_WmvCBm49m9oGdB5RA0jNkePG': 'file_storage/call_WmvCBm49m9oGdB5RA0jNkePG.json', 'var_call_gre8zOZFtjVX1yWIPtvZ3cm7': 'file_storage/call_gre8zOZFtjVX1yWIPtvZ3cm7.json'}

exec(code, env_args)
