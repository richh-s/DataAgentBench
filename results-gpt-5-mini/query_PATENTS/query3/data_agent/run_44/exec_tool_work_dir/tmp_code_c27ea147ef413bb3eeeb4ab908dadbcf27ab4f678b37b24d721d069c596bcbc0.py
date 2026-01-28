code = """import json, re
data_var = var_call_cc68Z6aX2MXH8DgcWXYV034B
if isinstance(data_var, str):
    with open(data_var, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = data_var

pubnums = set()
# regex for publication numbers like US-123456-A1, EP-1224461-B1, WO-..., JP-S6163700-A, TW-201925402-A etc.
regex = re.compile(r"\b[A-Z]{2,3}-\d{4,}[A-Z0-9-]*\b")
for r in records:
    pi = r.get('Patents_info','') or ''
    for m in regex.findall(pi):
        pubnums.add(m)
# also check citation arrays within these records for publication_number fields
import ast
for r in records:
    cit = r.get('citation','') or ''
    try:
        arr = json.loads(cit)
    except Exception:
        try:
            arr = ast.literal_eval(cit)
        except Exception:
            arr = []
    if isinstance(arr, list):
        for it in arr:
            pn = it.get('publication_number') if isinstance(it, dict) else None
            if pn:
                # normalize
                pn = pn.strip()
                if pn:
                    pubnums.add(pn)

pub_list = sorted(pubnums)
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_cc68Z6aX2MXH8DgcWXYV034B': 'file_storage/call_cc68Z6aX2MXH8DgcWXYV034B.json', 'var_call_r1rLlChnwgV9fpjtfBZ4FUB9': [], 'var_call_gpK3xriqZczE4HtoLAE6feqr': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.']}

exec(code, env_args)
