code = """import json, re

# load citing records
src = var_call_P8ItLF3p8mT20DQ3M3xroKFn
if isinstance(src, str) and src.endswith('.json'):
    with open(src, 'r', encoding='utf-8') as f:
        citing_recs = json.load(f)
else:
    citing_recs = src

# load uc pub->primary subclass mapping (recompute from earlier file)
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
    pub = m.group(1) if m else None
    cpc_raw = r.get('cpc')
    primary = None
    if cpc_raw:
        try:
            cpcs = json.loads(cpc_raw)
        except Exception:
            cpcs = []
        for e in cpcs:
            if isinstance(e, dict) and e.get('first') is True:
                code = e.get('code')
                if isinstance(code, str):
                    primary = code.strip()
                    break
    if pub and primary:
        m2 = re.match(r'^([A-HY]\d{2}[A-Z])', primary)
        subclass = m2.group(1) if m2 else primary
        uc_pub_to_subclass[pub]=subclass

# parse citing assignee from Patents_info
assignee_re = re.compile(r'^(.+?)\s+holds the\s+(?:US|EP|WO|CN|JP|KR|AU|CA|DE|FR|GB|TW|IN|BR|RU|IL|MX|ZA|SE|NL|ES|IT|CH|SG)\s+patent', re.I)
assignee_re2 = re.compile(r'^In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+assigned\s+to\s+(.+?)\s+and\s+has\s+(?:pub\.|publication)', re.I)
assignee_re3 = re.compile(r'^(.+?)\s+owns the\s+', re.I)

pairs=set()
subclasses=set()
for r in citing_recs:
    pi = (r.get('Patents_info') or '').strip()
    assignee=None
    m=assignee_re.search(pi)
    if m:
        assignee=m.group(1).strip()
    else:
        m=assignee_re2.search(pi)
        if m:
            assignee=m.group(1).strip()
        else:
            m=assignee_re3.search(pi)
            if m:
                assignee=m.group(1).strip()
    if not assignee:
        continue
    if assignee.upper()=='UNIV CALIFORNIA':
        continue
    cit_raw=r.get('citation')
    if not cit_raw or cit_raw=='[]':
        continue
    try:
        cits=json.loads(cit_raw)
    except Exception:
        continue
    for c in cits:
        if not isinstance(c, dict):
            continue
        pub=c.get('publication_number')
        if pub in uc_pub_to_subclass:
            sc=uc_pub_to_subclass[pub]
            pairs.add((assignee, sc))
            subclasses.add(sc)

print('__RESULT__:')
print(json.dumps({'pair_count': len(pairs), 'assignee_count': len(set(a for a,_ in pairs)), 'subclass_count': len(subclasses), 'pairs_sample': sorted(list(pairs))[:20], 'subclasses': sorted(list(subclasses))}))"""

env_args = {'var_call_WHv1lmPSfKcTdS8wJQw8DFVx': ['publicationinfo'], 'var_call_9FObhEdTKcKZY57NsI47GeTw': ['cpc_definition'], 'var_call_C0tsT6udBqwTfDYCy6wmqC6T': [], 'var_call_QlDCLePqJogYQ2wyYP5FHfsg': 'file_storage/call_QlDCLePqJogYQ2wyYP5FHfsg.json', 'var_call_lAbblgE98YuUeC0cXyKhKWzg': {'uc_pub_count': 108, 'mapped_primary_count': 108, 'sample': [['US-2022074631-A1', 'F25B'], ['TW-201925402-A', 'C09J'], ['US-11421276-B2', 'C12Q'], ['AU-2019275518-B2', 'A61K'], ['US-2017281687-A1', 'A61K']]}, 'var_call_P8ItLF3p8mT20DQ3M3xroKFn': 'file_storage/call_P8ItLF3p8mT20DQ3M3xroKFn.json'}

exec(code, env_args)
