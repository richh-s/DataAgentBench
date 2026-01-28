code = """import json, re
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

all_recs = load_records(var_call_fk0UdT4razctPDoOG1RcPIOY)
uc_pubs = set(var_call_9mTDf4ARFweehibPe4TuGX4j['uc_publications'])

citing = []
for r in all_recs:
    cit_raw = r.get('citation')
    try:
        cits = json.loads(cit_raw) if isinstance(cit_raw,str) else (cit_raw or [])
    except Exception:
        continue
    cited_pubs = set()
    for c in cits:
        if isinstance(c, dict):
            pn = c.get('publication_number')
            if pn:
                cited_pubs.add(pn)
    inter = cited_pubs & uc_pubs
    if not inter:
        continue
    pi = r.get('Patents_info','')
    m = re.search(r'owned by ([^,]+),', pi)
    if not m:
        m = re.search(r'is owned by ([^,]+) and', pi)
    assignee = m.group(1).strip() if m else None
    if assignee and assignee != 'UNIV CALIFORNIA':
        # get first CPC codes for citing patent
        try:
            cpcs = json.loads(r.get('cpc')) if isinstance(r.get('cpc'), str) else (r.get('cpc') or [])
        except Exception:
            cpcs = []
        first_codes = sorted({c.get('code') for c in cpcs if isinstance(c, dict) and c.get('first') and c.get('code')})
        citing.append({'assignee': assignee, 'cited_uc_pubs': sorted(inter), 'first_cpc_codes': first_codes})

print('__RESULT__:')
print(json.dumps({'matches': citing, 'count': len(citing)}))"""

env_args = {'var_call_WARIrU51ufJzDVMTDu8cN1w8': ['publicationinfo'], 'var_call_QAjMpZ4jD9mwBk4EPKJJhVgl': ['cpc_definition'], 'var_call_zMJEHsIZ0ZXz0lMpwKnP91oh': [], 'var_call_eG8N1uSJihukRzkbf4xtTtS1': 'file_storage/call_eG8N1uSJihukRzkbf4xtTtS1.json', 'var_call_29sZxqw6esmyTqRimgRWD5oe': 'file_storage/call_29sZxqw6esmyTqRimgRWD5oe.json', 'var_call_9mTDf4ARFweehibPe4TuGX4j': {'uc_publications': ['AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'CA-2283629-C', 'CA-3161617-A1', 'CN-100339724-C', 'EP-2210307-A4', 'HK-1052178-A1', 'ID-23426-A', 'IL-274176-A', 'JP-2009260386-A', 'KR-20160119166-A', 'US-11072681-B2', 'US-11667770-B2', 'US-2006292670-A1', 'US-2018243924-A1', 'US-2019209590-A1', 'US-2021002329-A1', 'US-2021181673-A1', 'US-2022074631-A1', 'US-5304932-A', 'WO-2014152660-A1', 'WO-2018067976-A1'], 'count': 23}, 'var_call_fk0UdT4razctPDoOG1RcPIOY': 'file_storage/call_fk0UdT4razctPDoOG1RcPIOY.json'}

exec(code, env_args)
