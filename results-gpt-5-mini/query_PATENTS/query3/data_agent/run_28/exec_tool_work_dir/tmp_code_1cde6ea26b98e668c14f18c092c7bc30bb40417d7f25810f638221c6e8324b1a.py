code = """import json,re
with open(var_call_D4rq9cs4gFNTl4lSdqgfzKOa, 'r', encoding='utf-8') as f:
    unc_rows = json.load(f)

pub_patterns = [r'pub\. number\s*([A-Z0-9\-\._]+)', r'publication number\s*([A-Z0-9\-\._]+)', r'with pub\. number\s*([A-Z0-9\-\._]+)', r'with publication number\s*([A-Z0-9\-\._]+)']
unc_pubnums = set()
map_row_pub = {}
for r in unc_rows:
    info = r.get('Patents_info','')
    found = None
    for p in pub_patterns:
        m = re.search(p, info, flags=re.IGNORECASE)
        if m:
            found = m.group(1).strip()
            break
    if not found:
        m = re.search(r'([A-Z]{1,3}-\d{4,}|US-\d+|WO-\d+|JP-\w+|TW-\d+|FR-\d+|EP-\d+|CN-\d+)', info)
        if m:
            found = m.group(0)
    if found:
        unc_pubnums.add(found)
        map_row_pub[r.get('rowid')] = found

res = {'unc_pubnums': sorted(list(unc_pubnums)), 'map_row_pub': map_row_pub}
import json
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_D4rq9cs4gFNTl4lSdqgfzKOa': 'file_storage/call_D4rq9cs4gFNTl4lSdqgfzKOa.json', 'var_call_IItaqV0SEoPNDJAoMxeGoSEA': 'file_storage/call_IItaqV0SEoPNDJAoMxeGoSEA.json', 'var_call_pSLyigoaH7UAq2q3yo9MVvhl': []}

exec(code, env_args)
