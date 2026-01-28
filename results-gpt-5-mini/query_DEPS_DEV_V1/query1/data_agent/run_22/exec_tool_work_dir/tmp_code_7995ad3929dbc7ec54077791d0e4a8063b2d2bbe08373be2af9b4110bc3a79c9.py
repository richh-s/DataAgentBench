code = """import json
# Read the package_database latest NPM packages result stored in var_call_cI1IgLplT4t0GR9eLieRluyO
path = var_call_cI1IgLplT4t0GR9eLieRluyO
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Filter for System == 'NPM' and build list of (Name, Version)
pairs = []
for r in records:
    if r.get('System') == 'NPM':
        name = r.get('Name')
        version = r.get('Version')
        if name and version:
            pairs.append((name, version))
# Build SQL WHERE clause: ((Name='n1' AND Version='v1') OR ...)
clauses = []
for name, version in pairs:
    # escape single quotes
    en = name.replace("'", "''")
    ev = version.replace("'", "''")
    clauses.append(f"(ppv.Name = '{en}' AND ppv.Version = '{ev}')")
where_clause = ' OR '.join(clauses) if clauses else '1=0'
# Print result in required format
print("__RESULT__:")
print(json.dumps(where_clause))"""

env_args = {'var_call_cI1IgLplT4t0GR9eLieRluyO': 'file_storage/call_cI1IgLplT4t0GR9eLieRluyO.json'}

exec(code, env_args)
