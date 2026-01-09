code = """import json, re
path = var_call_59lcvJsIjZ1vcLpPvQ8cFHob
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_pubnum(info):
    m = re.search(r'pub\. number\s+([A-Z]{2}-\d+-[A-Z0-9]+)', info)
    if m:
        return m.group(1)
    m = re.search(r'publication number\s+([A-Z]{2}-\d+-[A-Z0-9]+)', info)
    if m:
        return m.group(1)
    return None

pubs=[]
for r in recs[:2000]:
    p=extract_pubnum(r.get('Patents_info','') or '')
    if p:
        pubs.append(p)

print('__RESULT__:')
print(json.dumps({'found':len(pubs), 'sample':pubs[:10]}))"""

env_args = {'var_call_iHXHysJC3duFCWWnJW64v10h': ['publicationinfo'], 'var_call_jlHGhsPdB6yLdpu78t6zwQ84': ['cpc_definition'], 'var_call_59lcvJsIjZ1vcLpPvQ8cFHob': 'file_storage/call_59lcvJsIjZ1vcLpPvQ8cFHob.json', 'var_call_cHnpmjdlTkbewpaKyoAQJmfn': {'uc_pubnums_count': 0, 'uc_pubnums_sample': []}, 'var_call_sUHm40o9xxZWOiW1ZcJe76dg': {'example': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}}

exec(code, env_args)
