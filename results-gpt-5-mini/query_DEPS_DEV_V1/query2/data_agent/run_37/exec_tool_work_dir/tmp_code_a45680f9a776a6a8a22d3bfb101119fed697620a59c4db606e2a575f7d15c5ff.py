code = """import json
# load the package list from the previous query stored in var_call_xoiRbYVhG6oB3Nh77ykHM5fW
fp = var_call_xoiRbYVhG6oB3Nh77ykHM5fW
with open(fp, 'r') as f:
    records = json.load(f)
# deduplicate tuples
seen = set()
pairs = []
for r in records:
    t = (r['Name'], r['Version'])
    if t not in seen:
        seen.add(t)
        pairs.append(t)
# build SQL where clause as a series of OR conditions with proper escaping
def esc(s):
    return s.replace("'","''")
conds = []
for name, ver in pairs:
    conds.append(f"(\"Name\" = '{esc(name)}' AND \"Version\" = '{esc(ver)}')")
where_clause = ' OR '.join(conds)
where_clause = '(' + where_clause + ')'
# prepare output
out = {
    'num_pairs': len(pairs),
    'where_clause': where_clause
}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_GFjoBvPPCjrqO1febE5dj3UX': ['packageinfo'], 'var_call_GEHAWCkzbkVYIGaW9lhUPqPS': ['project_info', 'project_packageversion'], 'var_call_xoiRbYVhG6oB3Nh77ykHM5fW': 'file_storage/call_xoiRbYVhG6oB3Nh77ykHM5fW.json'}

exec(code, env_args)
