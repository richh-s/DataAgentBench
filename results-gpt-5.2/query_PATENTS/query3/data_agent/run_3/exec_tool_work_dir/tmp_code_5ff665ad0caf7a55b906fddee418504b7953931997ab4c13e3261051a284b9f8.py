code = """import json, re

# load UC records for pub->subclass
uc_src = var_call_QlDCLePqJogYQ2wyYP5FHfsg
if isinstance(uc_src, str) and uc_src.endswith('.json'):
    with open(uc_src, 'r', encoding='utf-8') as f:
        uc_recs = json.load(f)
else:
    uc_recs = uc_src

uc_pub_to_subclass = {}
for r in uc_recs:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-\d{7,}-[A-Z]\d?)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-\d{7,}-[A-Z]\d?)', pi)
    if not m:
        m = re.search(r'publication no\.\s+([A-Z]{2}-\d{7,}-[A-Z]\d?)', pi)
    pub = m.group(1) if m else None
    cpc_raw = r.get('cpc')
    primary = None
    if cpc_raw:
        try:
            cpcs = json.loads(cpc_raw)
        except Exception:
            cpcs=[]
        for e in cpcs:
            if isinstance(e, dict) and e.get('first') is True:
                code=e.get('code')
                if isinstance(code,str):
                    primary=code.strip(); break
    if pub and primary:
        m2=re.match(r'^([A-HY]\d{2}[A-Z])', primary)
        uc_pub_to_subclass[pub]=m2.group(1) if m2 else primary

# load citing recs where Patents_info includes UNIV CALIFORNIA (may include self)
src = var_call_eVlLZ0Gl8M5PXLTU6utXh2Kr
if isinstance(src, str) and src.endswith('.json'):
    with open(src,'r',encoding='utf-8') as f:
        citing_recs=json.load(f)
else:
    citing_recs=src

assignee=None
pairs=set(); subclasses=set(); assignees=set()
for r in citing_recs:
    pi=(r.get('Patents_info') or '').strip()
    # parse assignee various patterns
    m=re.search(r'^(.+?)\s+holds the\s+', pi, re.I)
    if m:
        assignee=m.group(1).strip()
    else:
        m=re.search(r'is belonging to\s+(.+?)\s+and has', pi, re.I)
        if m:
            assignee=m.group(1).strip()
        else:
            m=re.search(r'is assigned to\s+(.+?)\s+and has', pi, re.I)
            if m:
                assignee=m.group(1).strip()
            else:
                assignee=None
    if not assignee or assignee.upper()=='UNIV CALIFORNIA':
        continue
    cit_raw=r.get('citation')
    if not cit_raw or cit_raw=='[]':
        continue
    try:
        cits=json.loads(cit_raw)
    except Exception:
        continue
    for c in cits:
        pub=c.get('publication_number') if isinstance(c,dict) else None
        if pub in uc_pub_to_subclass:
            sc=uc_pub_to_subclass[pub]
            pairs.add((assignee,sc))
            subclasses.add(sc)
            assignees.add(assignee)

print('__RESULT__:')
print(json.dumps({'pair_count':len(pairs),'assignee_count':len(assignees),'subclass_count':len(subclasses),'pairs_sample':sorted(list(pairs))[:50]}))"""

env_args = {'var_call_WHv1lmPSfKcTdS8wJQw8DFVx': ['publicationinfo'], 'var_call_9FObhEdTKcKZY57NsI47GeTw': ['cpc_definition'], 'var_call_C0tsT6udBqwTfDYCy6wmqC6T': [], 'var_call_QlDCLePqJogYQ2wyYP5FHfsg': 'file_storage/call_QlDCLePqJogYQ2wyYP5FHfsg.json', 'var_call_lAbblgE98YuUeC0cXyKhKWzg': {'uc_pub_count': 108, 'mapped_primary_count': 108, 'sample': [['US-2022074631-A1', 'F25B'], ['TW-201925402-A', 'C09J'], ['US-11421276-B2', 'C12Q'], ['AU-2019275518-B2', 'A61K'], ['US-2017281687-A1', 'A61K']]}, 'var_call_P8ItLF3p8mT20DQ3M3xroKFn': 'file_storage/call_P8ItLF3p8mT20DQ3M3xroKFn.json', 'var_call_SAwmZx9PwapYroFLWsLWzf7x': {'pair_count': 0, 'assignee_count': 0, 'subclass_count': 0, 'pairs_sample': [], 'subclasses': []}, 'var_call_WYkroV8MZg0VU0V4qlpWX9U4': 'file_storage/call_WYkroV8MZg0VU0V4qlpWX9U4.json', 'var_call_eVlLZ0Gl8M5PXLTU6utXh2Kr': 'file_storage/call_eVlLZ0Gl8M5PXLTU6utXh2Kr.json'}

exec(code, env_args)
