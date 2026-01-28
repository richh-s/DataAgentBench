code = """import json
p = var_call_COm8Aw8kN260BreJqf2C2xDz
with open(p, 'r') as f:
    records = json.load(f)
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})

def sql_quote(s):
    return "'" + s.replace("'", "''") + "'"

in_list = ','.join(sql_quote(r) for r in repo_names)
query = (
    'SELECT COUNT(*) AS count FROM commits '
    f"WHERE repo_name IN ({in_list}) "
    "AND message IS NOT NULL "
    "AND message <> '' "
    "AND length(message) < 1000 "
    "AND ltrim(lower(message)) NOT LIKE 'merge%' "
    "AND ltrim(lower(message)) NOT LIKE 'update%' "
    "AND ltrim(lower(message)) NOT LIKE 'test%';"
)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_COm8Aw8kN260BreJqf2C2xDz': 'file_storage/call_COm8Aw8kN260BreJqf2C2xDz.json', 'var_call_cmi9iKVzjejooAD4B3gfpXVU': "SELECT COUNT(*) AS count FROM commits WHERE repo_name IN () AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';"}

exec(code, env_args)
