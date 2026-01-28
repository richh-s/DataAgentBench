code = """import json, re

# load full table
path = var_call_vVVmQ2VpsYjPkYThYNl2X0H7
with open(path,'r',encoding='utf-8') as f:
    all_recs=json.load(f)

# UC publication numbers set
uc_path = var_call_D8KOFXg6SsoYmdwmDXj91rd5
with open(uc_path,'r',encoding='utf-8') as f:
    uc_recs=json.load(f)

uc_pub=set()
for r in uc_recs:
    pi=r.get('Patents_info','')
    m=re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\.', pi)
    if m:
        uc_pub.add(m.group(1))

# helper to extract assignee name from Patents_info
pat_assignee_re = re.compile(r'^(.*?)\s+holds|^In\s+\w+,\s+the\s+(?:application|patent filing|patent application)\s*\(.*?\)\s+is\s+(?:owned by|assigned to)\s+([^\n]+?)\s+and\s+has', re.IGNORECASE)

def extract_assignee(pi:str):
    m=pat_assignee_re.search(pi)
    if not m:
        # fallback: 'is owned by X and has'
        m2=re.search(r'is\s+(?:owned by|assigned to)\s+(.+?)\s+and\s+has', pi, re.IGNORECASE)
        if m2:
            return m2.group(1).strip()
        m3=re.search(r'^(.+?)\s+holds\s+the', pi, re.IGNORECASE)
        if m3:
            return m3.group(1).strip()
        return None
    # groups: if starts with name holds, group1 else group2
    return (m.group(1) or m.group(2)).strip()

citing_rows=[]
for r in all_recs:
    cit=r.get('citation')
    if not cit or cit=='[]':
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    hit=False
    for c in cit_list:
        pn=c.get('publication_number')
        if pn in uc_pub:
            hit=True
            break
    if not hit:
        continue
    ass=extract_assignee(r.get('Patents_info','') or '')
    if not ass:
        continue
    # exclude UC itself
    if 'UNIV CALIFORNIA' in ass.upper() or 'UNIVERSITY OF CALIFORNIA' in ass.upper() or 'REGENTS OF THE UNIVERSITY OF CALIFORNIA' in ass.upper():
        continue
    # primary CPC subclasses: take entries in cpc with first==true; take subclass = code up to '/'
    cpc=r.get('cpc')
    subclasses=set()
    if cpc:
        try:
            cpc_list=json.loads(cpc)
            for e in cpc_list:
                if e.get('first') is True:
                    code=e.get('code')
                    if code:
                        subclasses.add(code.split('/')[0])
        except Exception:
            pass
    for sc in (subclasses or []):
        citing_rows.append({'citing_assignee': ass, 'cpc_subclass': sc})

# unique pairs
pairs=sorted({(d['citing_assignee'], d['cpc_subclass']) for d in citing_rows})
subclasses=sorted({sc for _,sc in pairs})

print('__RESULT__:')
print(json.dumps({'pair_count': len(pairs), 'subclass_count': len(subclasses), 'subclasses': subclasses[:50], 'pairs_preview': pairs[:20]}))"""

env_args = {'var_call_6r9kRKlWpAnxGL0RQggEq1u2': ['publicationinfo'], 'var_call_E96U2H3Ln095YkOv6QIGX04g': ['cpc_definition'], 'var_call_tPdPyr8N8C3FwSeXzne8Nu8v': [], 'var_call_d2oOELDTbDWpa9VNRi39QqwN': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_D8KOFXg6SsoYmdwmDXj91rd5': 'file_storage/call_D8KOFXg6SsoYmdwmDXj91rd5.json', 'var_call_8KqE4sLa73ab8P4tWMqgU4h7': {'uc_pub_count': 58}, 'var_call_vVVmQ2VpsYjPkYThYNl2X0H7': 'file_storage/call_vVVmQ2VpsYjPkYThYNl2X0H7.json'}

exec(code, env_args)
