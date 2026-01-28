code = """import json
p = var_call_uVzqr6w3MBdD5uKse2Gi8DUU
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# data is list of records with keys System, Name, Version
triples = set()
for r in data:
    triples.add((r['System'], r['Name'], r['Version']))
# build IN list, but limit to reasonable number if extremely large
triples = sorted(triples)
# To be safe, if too many, we'll include all (hope it's ok)
def esc(s):
    return s.replace("'", "''")
vals = []
for sys,name,ver in triples:
    vals.append("('" + esc(sys) + "','" + esc(name) + "','" + esc(ver) + "')")
in_list = ",".join(vals)
query = "SELECT ProjectName, System, Name, Version FROM project_packageversion WHERE (System, Name, Version) IN (" + in_list + ");"
import json
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_uVzqr6w3MBdD5uKse2Gi8DUU': 'file_storage/call_uVzqr6w3MBdD5uKse2Gi8DUU.json'}

exec(code, env_args)
