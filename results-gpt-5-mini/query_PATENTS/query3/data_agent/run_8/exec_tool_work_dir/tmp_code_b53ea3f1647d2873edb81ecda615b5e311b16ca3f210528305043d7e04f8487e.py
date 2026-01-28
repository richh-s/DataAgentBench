code = """import json, re
path = var_call_uxK6ufKP7sP5MNcbECREGAlY
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)

# We need mapping of cited publication -> assignee (global). We earlier built mapping for Univ California rows only.
# Let's build mapping for all rows we loaded (limited sample) where we can extract pubnum and assignee
pub_to_assignee = {}
for r in rows:
    pinfo = r.get('Patents_info','')
    # extract pubnum
    m = re.search(r'([A-Z]{2}-\d{4,}[A-Z0-9\-]*)', pinfo)
    pub = m.group(1) if m else None
    # extract assignee similar heuristics
    assignee = None
    if ' holds ' in pinfo:
        assignee = pinfo.split(' holds ',1)[0].strip()
    elif ' owned by ' in pinfo:
        assignee = pinfo.split(' owned by ',1)[1].split(' and ')[0].strip()
    elif ' assigned to ' in pinfo:
        assignee = pinfo.split(' assigned to ',1)[1].split(' and ')[0].strip()
    elif ' is owned by ' in pinfo:
        assignee = pinfo.split(' is owned by ',1)[1].split(' and ')[0].strip()
    elif pinfo.upper().startswith('UNIV') or pinfo.upper().startswith('THE REGENTS'):
        assignee = pinfo.split(' ',3)[:3]
        assignee = ' '.join(assignee)
    if pub and assignee:
        pub_to_assignee[pub] = assignee

# Now identify citations where cited pub maps to Univ California
def is_univ(assg):
    if not assg: return False
    s = assg.lower()
    return 'california' in s and ('univ' in s or 'university' in s)

pairs = set()
for r in rows:
    pinfo = r.get('Patents_info','')
    # citing assignee
    citing_assignee = None
    if ' holds ' in pinfo:
        citing_assignee = pinfo.split(' holds ',1)[0].strip()
    elif ' owned by ' in pinfo:
        citing_assignee = pinfo.split(' owned by ',1)[1].split(' and ')[0].strip()
    elif ' assigned to ' in pinfo:
        citing_assignee = pinfo.split(' assigned to ',1)[1].split(' and ')[0].strip()
    else:
        # maybe first token
        citing_assignee = pinfo.split('(',1)[0].strip()
    if not citing_assignee:
        continue
    if is_univ(citing_assignee):
        continue
    # primary subclass from cpc
    primary = None
    cpc_field = r.get('cpc')
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list) and len(cpcs)>0:
                code = cpcs[0].get('code')
                if code:
                    primary = re.sub(r'\s+','',code)[:4]
        except Exception:
            pass
    # parse citations
    cit_field = r.get('citation')
    if not cit_field:
        continue
    try:
        cit_list = json.loads(cit_field)
    except Exception:
        continue
    for c in cit_list:
        if not isinstance(c, dict):
            continue
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        assg = pub_to_assignee.get(cited_pub)
        if assg and is_univ(assg):
            pairs.add((citing_assignee, primary))

res = [{'citing_assignee': a, 'primary_subclass': s} for a,s in sorted(pairs)]
subs = sorted({x['primary_subclass'] for x in res if x['primary_subclass']})
print('__RESULT__:')
print(json.dumps({'pairs': res, 'subclasses': subs, 'pub_to_assignee_count': len(pub_to_assignee)}))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json', 'var_call_uhZPtxfUJEEwobfhVN8uLJfv': {'pairs': [], 'subclasses': []}, 'var_call_B8JJOFd47fc03V6045GS9Gbw': 'file_storage/call_B8JJOFd47fc03V6045GS9Gbw.json', 'var_call_iSikYemGpJjCyiuMbOeMopAo': {'count': 113, 'sample': {'US-202117472182-A': 'UNIV CALIFORNIA', 'TW-107142982-A': 'UNIV CALIFORNIA', 'US-201916454755-A': 'UNIV CALIFORNIA', 'AU-2019275518-A': 'UNIV CALIFORNIA', 'US-201515313510-A': 'UNIV CALIFORNIA', 'JP-13313985-A': 'UNIV CALIFORNIA', 'US-201715625819-A': 'UNIV CALIFORNIA', 'EP-00992018-A': 'UNIV CALIFORNIA', 'EP-21763795-A': 'THE REGENTS OF UNIV OF CALIFORNIA', 'US-55161904-A': 'UNIV CALIFORNIA'}}, 'var_call_uxK6ufKP7sP5MNcbECREGAlY': 'file_storage/call_uxK6ufKP7sP5MNcbECREGAlY.json'}

exec(code, env_args)
