code = """import json, re

# load sample citing records
src = var_call_vaof8GzCBaPtnCK5smrbRTQo
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        citing_recs = json.load(f)
else:
    citing_recs = src

# load UC records (for target list)
src2 = var_call_GYAWO6qr1r7qnkcH97SYl3D4
if isinstance(src2, str):
    with open(src2, 'r', encoding='utf-8') as f:
        uc_recs = json.load(f)
else:
    uc_recs = src2

PUBNO_RE = re.compile(r"pub\.? number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")
PUBNO_RE2 = re.compile(r"publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")

def extract_pubno(patents_info:str):
    for r in (PUBNO_RE, PUBNO_RE2):
        m = r.search(patents_info or '')
        if m:
            return m.group(1).strip()
    return None

def parse_json_field(s):
    if not s:
        return []
    if isinstance(s, list):
        return s
    ss = s.strip()
    try:
        return json.loads(ss)
    except Exception:
        return []

uc_pubnos = {extract_pubno(r.get('Patents_info','')) for r in uc_recs}
uc_pubnos.discard(None)

# check intersection with citations
hits = []
for rec in citing_recs:
    cits = parse_json_field(rec.get('citation'))
    cited_pubnos = [c.get('publication_number') for c in cits if isinstance(c, dict)]
    common = sorted(set(cited_pubnos).intersection(uc_pubnos))
    if common:
        hits.append({'patents_info': rec.get('Patents_info','')[:120], 'common': common[:5]})

print('__RESULT__:')
print(json.dumps({'uc_pubno_count': len(uc_pubnos), 'hit_count': len(hits), 'sample_hits': hits[:5]}))"""

env_args = {'var_call_ZSyNIgN7aBSNAiZM7qedGzE1': ['publicationinfo'], 'var_call_Gj7WHr85gETDG1tp4fJxUlUA': ['cpc_definition'], 'var_call_GYAWO6qr1r7qnkcH97SYl3D4': 'file_storage/call_GYAWO6qr1r7qnkcH97SYl3D4.json', 'var_call_T2PonMvVGmPKx2jPVROHdtUf': {'pairs': [], 'subclasses': []}, 'var_call_vaof8GzCBaPtnCK5smrbRTQo': 'file_storage/call_vaof8GzCBaPtnCK5smrbRTQo.json'}

exec(code, env_args)
