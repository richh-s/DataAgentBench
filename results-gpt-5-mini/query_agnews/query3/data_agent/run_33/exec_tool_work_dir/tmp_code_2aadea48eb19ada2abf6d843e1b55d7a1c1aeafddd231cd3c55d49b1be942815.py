code = """import json
# load the metadata query result file path from storage variable
fp = var_call_XvectxODeRSqQPEq7oNorDKh
with open(fp, 'r') as f:
    data = json.load(f)
# extract article_ids as ints
ids = []
for r in data:
    try:
        ids.append(int(r.get('article_id')))
    except:
        pass
ids = sorted(list(set(ids)))
out = json.dumps(ids)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XvectxODeRSqQPEq7oNorDKh': 'file_storage/call_XvectxODeRSqQPEq7oNorDKh.json'}

exec(code, env_args)
