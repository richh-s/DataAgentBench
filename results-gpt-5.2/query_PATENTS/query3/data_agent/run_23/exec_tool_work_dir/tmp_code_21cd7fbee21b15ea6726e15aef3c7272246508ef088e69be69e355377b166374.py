code = """import json, re

# load UC patents rows and build pub number set
with open(var_call_xNu75D1MsakbKFD0Cw620bkj,'r',encoding='utf-8') as f:
    uc_rows = json.load(f)
uc_pub_nums=set()
for r in uc_rows:
    pi=r.get('Patents_info','') or ''
    m=re.search(r'pub\.? number\s+([A-Z]{2,}-[^\s\.,]+)',pi,flags=re.I)
    if m:
        uc_pub_nums.add(m.group(1).upper())

# load all citing candidates (with citations)
with open(var_call_yPQXULut7RwXm1JJmsji0g0Z,'r',encoding='utf-8') as f:
    all_rows=json.load(f)

pairs=set()  # (assignee, primary_subclass)
for r in all_rows:
    cit=r.get('citation')
    if not cit or cit=='[]':
        continue
    try:
        cits=json.loads(cit)
    except Exception:
        continue
    cited_any=False
    for c in cits:
        pn=(c.get('publication_number') or '').upper()
        if pn in uc_pub_nums:
            cited_any=True
            break
    if not cited_any:
        continue
    pi=r.get('Patents_info','') or ''
    if 'UNIV CALIFORNIA' in pi.upper():
        continue
    # extract assignee name
    ass=None
    m=re.match(r'(.+?)\s+holds\b',pi)
    if m:
        ass=m.group(1).strip()
    else:
        m=re.search(r'owned by\s+([^\.,]+?)\s+and\s+has',pi,flags=re.I)
        if m:
            ass=m.group(1).strip()
        else:
            m=re.search(r'assigned to\s+([^\.,]+?)\s+and\s+has',pi,flags=re.I)
            if m:
                ass=m.group(1).strip()
    if not ass:
        continue
    if ass.upper().strip()== 'UNIV CALIFORNIA':
        continue
    # parse primary CPC code(s) where first==true
    primary_codes=[]
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
        for e in cpcs:
            if e.get('first') is True and e.get('code'):
                code=str(e['code']).strip().upper()
                # subclass: remove digits and anything after slash
                base=code.split('/')[0]
                subclass=re.sub(r'\d+$','',base)
                if subclass:
                    primary_codes.append(subclass)
    except Exception:
        primary_codes=[]
    for sc in set(primary_codes):
        pairs.add((ass, sc))

print('__RESULT__:')
print(json.dumps({'pair_count': len(pairs), 'sample': list(sorted(list(pairs)))[:20]}))"""

env_args = {'var_call_bn8TU9VmVk7pN006TU4zWS7v': ['publicationinfo'], 'var_call_4JOLYly9fdp0lGpLaOI60GYA': ['cpc_definition'], 'var_call_8mi1In3NOVkCaut8K4dmMMBZ': [], 'var_call_DQHDx6XuPUEqnb6zdY4YYVtE': [], 'var_call_hexwFqpBOYPl5UnOP4IVCFVL': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_xNu75D1MsakbKFD0Cw620bkj': 'file_storage/call_xNu75D1MsakbKFD0Cw620bkj.json', 'var_call_ONamGQwhRaqkRKoZST5o9ogf': {'uc_pub_count': 64, 'sample': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2009234210-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6492396-A', 'AU-6535890-A', 'CA-2298540-A1']}, 'var_call_yPQXULut7RwXm1JJmsji0g0Z': 'file_storage/call_yPQXULut7RwXm1JJmsji0g0Z.json'}

exec(code, env_args)
