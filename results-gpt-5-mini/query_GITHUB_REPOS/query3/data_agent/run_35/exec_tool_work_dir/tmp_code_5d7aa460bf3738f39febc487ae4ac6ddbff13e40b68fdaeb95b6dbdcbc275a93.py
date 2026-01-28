code = """import json
# var_call_COm8Aw8kN260BreJqf2C2xDz is available in this environment as per tool storage
records = var_call_COm8Aw8kN260BreJqf2C2xDz
# Extract repo names, dedupe
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# Escape single quotes in repo names
def sql_quote(s):
    return "'" + s.replace("'","''") + "'"

in_list = ','.join(sql_quote(r) for r in repo_names)
# Build DuckDB SQL query to count matching commit messages
query = (
    'SELECT COUNT(*) AS count FROM commits '
    f"WHERE repo_name IN ({in_list}) "
    "AND message IS NOT NULL "
    "AND message <> '' "
    "AND length(message) < 1000 "
    "AND lower(message) NOT LIKE 'merge%' "
    "AND lower(message) NOT LIKE 'update%' "
    "AND lower(message) NOT LIKE 'test%';"
)
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_COm8Aw8kN260BreJqf2C2xDz': 'file_storage/call_COm8Aw8kN260BreJqf2C2xDz.json'}

exec(code, env_args)
