code = """import json
fp = var_call_odEChWwbyx3ZSKtoFlIj7SPR
with open(fp) as f:
    data = json.load(f)
pairs = set()
for r in data:
    name = r.get('Name')
    version = r.get('Version')
    if name and version:
        pairs.add((name, version))
vals = []
for name, version in sorted(pairs):
    n = name.replace("'", "''")
    v = version.replace("'", "''")
    vals.append("('{}','{}')".format(n, v))
vals_sql = ", ".join(vals)
sql = "WITH latest(name, version) AS (VALUES {} ) SELECT p.System, p.Name, p.Version, p.ProjectName FROM project_packageversion p JOIN latest l ON p.Name = l.name AND p.Version = l.version WHERE p.System='NPM';".format(vals_sql)
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_odEChWwbyx3ZSKtoFlIj7SPR': 'file_storage/call_odEChWwbyx3ZSKtoFlIj7SPR.json'}

exec(code, env_args)
