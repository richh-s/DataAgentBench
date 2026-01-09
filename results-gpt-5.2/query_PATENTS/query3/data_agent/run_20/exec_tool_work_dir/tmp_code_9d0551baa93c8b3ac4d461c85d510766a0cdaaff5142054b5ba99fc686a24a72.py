code = """import json, re
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

rows = load_records(var_call_pjGAMTLVhdopabRffb8gaZI8)

def extract_assignee(pi:str):
    m = re.search(r'assigned to (.+?) and has pub\.', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'owned by (.+?) and has pub\.', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'owned by (.+?), with publication no\.', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'assigned to (.+?), with publication no\.', pi)
    if m:
        return m.group(1).strip()
    return None

def extract_pub_number(pi:str):
    for pat in [r'pub\. number ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b', r'publication number ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b', r'publication no\. ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b']:
        m=re.search(pat, pi)
        if m:
            return m.group(1)
    return None

# cited UC publication numbers list from previous computation? recompute from uc rows file
uc_rows = load_records(var_call_VrvRQiqssVtXSh3gpNtKvN2s)
cited_uc_set=set()
for r in uc_rows:
    try:
        arr=json.loads(r.get('citation') or '[]')
    except Exception:
        arr=[]
    for c in arr:
        pn=(c or {}).get('publication_number')
        if pn:
            cited_uc_set.add(pn)

hits=[]
for r in rows:
    pi=r.get('Patents_info','') or ''
    ass=extract_assignee(pi)
    pub=extract_pub_number(pi)
    if ass and pub and pub in cited_uc_set and 'UNIV CALIFORNIA' not in ass:
        hits.append({'citing_assignee':ass,'citing_pub':pub,'cpc':r.get('cpc')})

print('__RESULT__:')
print(json.dumps({'matches':len(hits),'examples':hits[:20]}))"""

env_args = {'var_call_ddOAz8PfD2fDDJqV0zfHDxg7': ['publicationinfo'], 'var_call_wkNZLGn5gJAtTodjHGp1kZtw': ['cpc_definition'], 'var_call_zI3m4l4umjvRlgbTMTKiwULz': [], 'var_call_FLfVs8tLVEb0QVkhBKPDySh1': 'file_storage/call_FLfVs8tLVEb0QVkhBKPDySh1.json', 'var_call_ndi2SKxJaGEbVMF2HNbiTjIZ': {'uc_publications_count_in_sample': 5, 'sample_uc_patents_info': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.', 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.'], 'has_citations': [4, 145, 0, 38, 3]}, 'var_call_VrvRQiqssVtXSh3gpNtKvN2s': 'file_storage/call_VrvRQiqssVtXSh3gpNtKvN2s.json', 'var_call_kEHSamkCiX0e5KZVV3SX6cvE': {'uc_pub_count': 0, 'uc_pub_examples': [], 'cited_pub_count': 99, 'cited_pub_examples': ['CN-1237247-A', 'CN-85101623-A', 'EP-1122806-A1', 'EP-1939202-A1', 'FR-3105380-A1', 'JP-2001024221-A', 'JP-H11261169-A', 'KR-960004436-A', 'US-10046057-B2', 'US-10151649-B2', 'US-11466906-B2', 'US-2003113740-A1', 'US-2003143388-A1', 'US-2003143688-A1', 'US-2003155679-A1', 'US-2005079574-A1', 'US-2005176135-A1', 'US-2006052403-A1', 'US-2006234112-A1', 'US-2007118916-A1']}, 'var_call_pjGAMTLVhdopabRffb8gaZI8': 'file_storage/call_pjGAMTLVhdopabRffb8gaZI8.json'}

exec(code, env_args)
