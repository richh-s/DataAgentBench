code = """import json
# var_call_HEzdcz70IjrP9lRgEgpSAqfY is available in this environment as provided by storage
data_path = var_call_HEzdcz70IjrP9lRgEgpSAqfY
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Build unique (System, Name, Version) tuples
tuples = set()
for r in records:
    tuples.add((r.get('System'), r.get('Name'), r.get('Version')))
# Limit to 2000 tuples to keep SQL manageable
tuples = list(tuples)[:2000]
# Helper to escape single quotes
def esc(s):
    if s is None:
        return ''
    return s.replace("'", "''")
# Build IN clause
in_items = []
for sys,name,ver in tuples:
    in_items.append("('%s','%s','%s')" % (esc(sys), esc(name), esc(ver)))
in_clause = ','.join(in_items)
sql = f"SELECT ppv.System, ppv.Name, ppv.Version, ppv.ProjectName, pi.Project_Information, pi.Licenses FROM project_packageversion ppv LEFT JOIN project_info pi ON pi.Project_Information LIKE '%' || ppv.ProjectName || '%' WHERE (ppv.System, ppv.Name, ppv.Version) IN ({in_clause});"
result = {'sql': sql, 'num_tuples': len(tuples)}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HEzdcz70IjrP9lRgEgpSAqfY': 'file_storage/call_HEzdcz70IjrP9lRgEgpSAqfY.json'}

exec(code, env_args)
