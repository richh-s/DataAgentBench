code = """import json
path = var_call_hW65jdsv3GmpdCSlUQsl6fxo
with open(path, 'r', encoding='utf-8') as f:
    names = json.load(f)
# Escape single quotes
def esc(s):
    return s.replace("'", "''")
chunk_size = 1000
# Build WHERE Name IN (...) clause
quoted = ["'" + esc(n) + "'" for n in names]
# Split into chunks to avoid extremely long single IN? We'll just create one
in_list = ','.join(quoted)
query = f"SELECT System, Name, Version, ProjectName FROM project_packageversion WHERE System = 'NPM' AND Name IN ({in_list});"
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json'}

exec(code, env_args)
