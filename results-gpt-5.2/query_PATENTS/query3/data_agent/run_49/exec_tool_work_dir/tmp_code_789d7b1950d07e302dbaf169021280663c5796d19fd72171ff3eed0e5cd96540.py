code = """import json, re

uniq = var_call_Br8KdGELjaXWiJZqdHI9Cv99['uniq_sample']
# but uniq_sample only sample; need full uniq list by recomputing quickly from stored file
import json as _json
with open(var_call_OaoPEXpflIJ6vct6rGPk3PN9,'r',encoding='utf-8') as f:
    cite_recs=_json.load(f)
with open(var_call_59lcvJsIjZ1vcLpPvQ8cFHob,'r',encoding='utf-8') as f:
    uc_recs=_json.load(f)

def extract_pubnum(info):
    for pat in [r'pub\. number\s+([A-Z]{2}-\d+-[A-Z0-9]+)', r'publication number\s+([A-Z]{2}-\d+-[A-Z0-9]+)']:
        m=re.search(pat, info)
        if m:
            return m.group(1)
    return None
uc_pubnums=set(filter(None,[extract_pubnum(r.get('Patents_info','') or '') for r in uc_recs]))

def get_assignee(info):
    m=re.match(r'^(.*?)\s+holds\b', info)
    if m:
        return m.group(1).strip()
    for pat in [r'is owned by\s+(.*?)\s+and has', r'is assigned to\s+(.*?)\s+and has', r'is assigned to\s+(.*?),\s+with publication']:
        m=re.search(pat, info)
        if m:
            return m.group(1).strip()
    return None

def subclass(code):
    m=re.match(r'^([A-HY]\d\d[A-Z])', code)
    return m.group(1) if m else None

uniq_set=set()
for r in cite_recs:
    cit=r.get('citation')
    if not cit or cit=='[]':
        continue
    try:
        cit_list=_json.loads(cit)
    except Exception:
        continue
    if not any((c.get('publication_number') in uc_pubnums) for c in cit_list):
        continue
    info=r.get('Patents_info','') or ''
    assignee=get_assignee(info)
    if not assignee or assignee=='UNIV CALIFORNIA':
        continue
    primary=[]
    try:
        cpc_list=_json.loads(r.get('cpc') or '[]')
        primary=[ce.get('code') for ce in cpc_list if ce.get('first') is True and ce.get('code')]
    except Exception:
        primary=[]
    for code in set(primary):
        sc=subclass(code)
        if sc:
            uniq_set.add((assignee, sc))

uniq_list=sorted(uniq_set)
# map titles
sym2title={d['symbol']: d['titleFull'] for d in var_call_d5lMVvMPzGoCIFXKDkTj30BJ}
lines=[]
for ass, sc in uniq_list:
    lines.append(f"{ass}\t{sym2title.get(sc,'')}")

print('__RESULT__:')
print(json.dumps({'lines': lines}))"""

env_args = {'var_call_iHXHysJC3duFCWWnJW64v10h': ['publicationinfo'], 'var_call_jlHGhsPdB6yLdpu78t6zwQ84': ['cpc_definition'], 'var_call_59lcvJsIjZ1vcLpPvQ8cFHob': 'file_storage/call_59lcvJsIjZ1vcLpPvQ8cFHob.json', 'var_call_cHnpmjdlTkbewpaKyoAQJmfn': {'uc_pubnums_count': 0, 'uc_pubnums_sample': []}, 'var_call_sUHm40o9xxZWOiW1ZcJe76dg': {'example': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_call_6CbOtwWCqCuS4wKv3E6q79vg': {'found': 112, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2']}, 'var_call_OaoPEXpflIJ6vct6rGPk3PN9': 'file_storage/call_OaoPEXpflIJ6vct6rGPk3PN9.json', 'var_call_Br8KdGELjaXWiJZqdHI9Cv99': {'n_pairs': 5, 'n_uniq': 3, 'uniq_sample': [['CALIFORNIA INST OF TECHN', 'G01V'], ['CRYSTAL IS INC', 'C30B'], ['SCHOWALTER LEO J', 'H01L']]}, 'var_call_d5lMVvMPzGoCIFXKDkTj30BJ': [{'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}, {'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}, {'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}]}

exec(code, env_args)
