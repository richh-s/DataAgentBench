code = """import json, re
# var_call_gDrSP1Sva9xFHcnb3CZWe5Hy is available from previous query_db
path = var_call_gDrSP1Sva9xFHcnb3CZWe5Hy
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubnums = set()
pattern = re.compile(r"[A-Z]{2}-[0-9A-Z\-]+")
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern.findall(pi):
        pubnums.add(m.strip())
# Also try to extract publication numbers from the 'citation' field where present
for rec in data:
    cit = rec.get('citation','')
    # citation may be JSON string or list; try to parse
    try:
        cit_list = json.loads(cit)
        for c in cit_list:
            pn = c.get('publication_number')
            if pn:
                pubnums.add(pn.strip())
    except Exception:
        # fallback: regex
        for m in pattern.findall(cit):
            pubnums.add(m.strip())
pubnums = sorted([p for p in pubnums if len(p)>0])
result = {'publication_numbers': pubnums}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gDrSP1Sva9xFHcnb3CZWe5Hy': 'file_storage/call_gDrSP1Sva9xFHcnb3CZWe5Hy.json'}

exec(code, env_args)
