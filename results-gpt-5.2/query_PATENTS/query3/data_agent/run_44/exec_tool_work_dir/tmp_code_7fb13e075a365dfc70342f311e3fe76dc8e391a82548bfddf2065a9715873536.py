code = """import json, re
import pandas as pd

# load UC-assigned publications
path_or_list = var_call_vYKm1esgoHJCdL9fP4Ctb86Q
if isinstance(path_or_list, str):
    with open(path_or_list, 'r', encoding='utf-8') as f:
        uc_recs = json.load(f)
else:
    uc_recs = path_or_list

# helper: extract publication number from Patents_info
pub_re = re.compile(r'pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', re.I)

def extract_pub(patents_info):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    return m.group(1).upper() if m else None

uc_pubs = set(filter(None, (extract_pub(r.get('Patents_info','')) for r in uc_recs)))

# gather UC primary CPC subclass codes (subclass = first 4 chars like A01B; handle Y02B etc)
# We'll derive subclass as first 4 of code after removing spaces

def primary_subclasses(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return []
    subs = []
    for e in arr:
        if isinstance(e, dict) and e.get('first') is True and e.get('code'):
            code = str(e['code']).strip().replace(' ', '')
            subs.append(code[:4])
    # unique preserve order
    seen=set(); out=[]
    for s in subs:
        if s not in seen:
            seen.add(s); out.append(s)
    return out

uc_pub_to_subs = {}
for r in uc_recs:
    pub = extract_pub(r.get('Patents_info',''))
    if not pub:
        continue
    subs = primary_subclasses(r.get('cpc'))
    if subs:
        uc_pub_to_subs[pub]=subs

# find citing patents by scanning all patents whose citation list includes any UC pub
# do SQL LIKE chunks to reduce size
uc_pubs_list = sorted(list(uc_pubs))
# sample limit for LIKE patterns: use prefixes 'US-' and year? We'll just search for 'US-' etc by chunking publication numbers

# Build patterns for SQL LIKE: citation LIKE '%<pub>%'
# We'll query per chunk and union results
import sqlite3

def run_sql(query):
    # use tool instead? can't inside python. We'll instead prepare output telling needed patterns.
    pass

# We'll output uc_pubs and uc_pub_to_subs for next stage
result = {
    'uc_publication_count': len(uc_pubs),
    'uc_pub_sample': uc_pubs_list[:20],
    'uc_pub_to_subs_sample': {k: uc_pub_to_subs[k] for k in list(uc_pub_to_subs)[:10]},
    'uc_pub_to_subs_count': len(uc_pub_to_subs)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fBZMIILGsx3QduPvpb8RFRXP': ['publicationinfo'], 'var_call_qbhDpu0qYyBfnieGsly3FqwM': ['cpc_definition'], 'var_call_AtPkufOYVCYqriWgJNq0Ojvr': [], 'var_call_hfEcekjFBGW6jNzhROmcnP4e': [], 'var_call_BU7QHAls9nhBnHAvJajrGoNI': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_442d0iDZ3xjqOMOTfHbiebFG': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'Application (no. US-77231501-A) from US, owned by CALIFORNIA INST OF TECHN, with publication no. US-6559125-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'The US application (number US-202016813462-A) is held by CALIFORNIA INST OF TECHN and has publication no. US-11226538-B2.'}, {'Patents_info': 'CALIFORNIA INST OF TECHN holds the US patent application (number US-201815983019-A), with publication number US-10746600-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'In US, the application (number US-201715617385-A) is held by PACIFIC BIOSCIENCES CALIFORNIA INC and has pub. number US-2017343479-A1.'}, {'Patents_info': 'The IL application (number IL-9133089-A) is held by CALIFORNIA BIOTECHNOLOGY INC and has publication number IL-91330-A0.'}, {'Patents_info': 'In AU, the patent application (ID AU-6533598-A) is assigned to CALIFORNIA INST OF TECHN and has publication no. AU-6533598-A.'}, {'Patents_info': 'Application (ID US-7889393-A) from US, held by CALIFORNIA INST OF TECHN, with pub. number US-5414799-A.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US application (ID US-25351088-A) is owned by CALIFORNIA INST OF TECHN and has publication no. US-5023808-A.'}, {'Patents_info': 'In US, the patent filing (app. number US-40249741-A) is assigned to CALIFORNIA CEDAR PROD and has publication no. US-2386828-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'In AU, the patent application (no. AU-3117200-A) is belonging to CALIFORNIA INST OF TECHN and has publication no. AU-767912-B2.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}, {'Patents_info': 'PACIFIC BIOSCIENCES CALIFORNIA INC holds the AU patent filing (app. number AU-2019255987-A), with pub. number AU-2019255987-A1.'}, {'Patents_info': 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.'}, {'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.'}, {'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.'}, {'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.'}, {'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.'}, {'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.'}, {'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'}, {'Patents_info': 'Patent filing (application no. US-20145750-A) from US, owned by CALIFORNIA INST RES FOUND, with pub. number US-2618766-A.'}, {'Patents_info': 'CALIFORNIA RESEARCH CORP holds the US application (no. US-72112758-A), with publication no. US-2900339-A.'}, {'Patents_info': 'CALIFORNIA CORRUGATED CULVERT COMPANY holds the US patent application (ID US-1912713798-A), with pub. number US-1054150-A.'}, {'Patents_info': 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.'}, {'Patents_info': 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.'}, {'Patents_info': 'Application (ID US-201916503894-A) from US, assigned to E INK CALIFORNIA LLC, with pub. number US-2019333454-A1.'}, {'Patents_info': 'CALIFORNIA INST OF TECHN holds the AU application (no. AU-2003294429-A), with publication number AU-2003294429-A1.'}, {'Patents_info': 'PACIFIC BIOSCIENCES CALIFORNIA INC holds the EP patent filing (application number EP-22194814-A), with publication no. EP-4123294-A1.'}, {'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'Patents_info': 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.'}, {'Patents_info': 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.'}, {'Patents_info': 'Patent filing (app. number KR-20047006671-A) from KR, held by CALIFORNIA INST OF TECHN, with publication no. KR-20050043737-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.'}, {'Patents_info': 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.'}], 'var_call_vYKm1esgoHJCdL9fP4Ctb86Q': 'file_storage/call_vYKm1esgoHJCdL9fP4Ctb86Q.json'}

exec(code, env_args)
