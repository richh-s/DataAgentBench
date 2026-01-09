code = """import json, re
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

uc_rows = load_records(var_call_VrvRQiqssVtXSh3gpNtKvN2s)

def extract_pub_number(patents_info:str):
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b', patents_info)
    if not m:
        m = re.search(r'publication number ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b', patents_info)
    if not m:
        m = re.search(r'publication no\. ([A-Z]{2}-[0-9]+[A-Z0-9\-]*-[A-Z0-9]+)\b', patents_info)
    if m:
        return m.group(1)
    return None

uc_pub_nums = sorted({extract_pub_number(r.get('Patents_info','') or '') for r in uc_rows if extract_pub_number(r.get('Patents_info','') or '')})

# gather cited publication_numbers from UC patents
cited_pub_nums = set()
for r in uc_rows:
    cit = r.get('citation')
    if not cit:
        continue
    try:
        arr = json.loads(cit)
    except Exception:
        continue
    for c in arr:
        pn = (c or {}).get('publication_number')
        if pn:
            cited_pub_nums.add(pn)

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pub_nums), 'uc_pub_examples': uc_pub_nums[:10], 'cited_pub_count': len(cited_pub_nums), 'cited_pub_examples': sorted(list(cited_pub_nums))[:20]}))"""

env_args = {'var_call_ddOAz8PfD2fDDJqV0zfHDxg7': ['publicationinfo'], 'var_call_wkNZLGn5gJAtTodjHGp1kZtw': ['cpc_definition'], 'var_call_zI3m4l4umjvRlgbTMTKiwULz': [], 'var_call_FLfVs8tLVEb0QVkhBKPDySh1': 'file_storage/call_FLfVs8tLVEb0QVkhBKPDySh1.json', 'var_call_ndi2SKxJaGEbVMF2HNbiTjIZ': {'uc_publications_count_in_sample': 5, 'sample_uc_patents_info': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.', 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.'], 'has_citations': [4, 145, 0, 38, 3]}, 'var_call_VrvRQiqssVtXSh3gpNtKvN2s': 'file_storage/call_VrvRQiqssVtXSh3gpNtKvN2s.json'}

exec(code, env_args)
