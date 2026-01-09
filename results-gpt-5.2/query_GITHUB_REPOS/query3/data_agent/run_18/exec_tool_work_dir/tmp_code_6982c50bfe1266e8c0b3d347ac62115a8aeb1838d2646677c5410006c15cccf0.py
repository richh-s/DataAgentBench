code = """import json
from pathlib import Path

p = Path(var_call_5034TdZFF1lP9Yefup6AMEGp)
repos = json.loads(p.read_text())
repo_names = [r['repo_name'] for r in repos]

# chunk to avoid huge IN clause
def esc(s):
    return s.replace("'","''")

chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + esc(r) + "'" for r in chunk])
    chunks.append(f"repo_name IN ({in_list})")

where_repos = '(' + ' OR '.join(chunks) + ')' if chunks else '(1=0)'

query = (
"SELECT COUNT(*) AS cnt\n"
"FROM commits\n"
f"WHERE {where_repos}\n"
"  AND message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(trim(message)) NOT LIKE 'merge%'\n"
"  AND lower(trim(message)) NOT LIKE 'update%'\n"
"  AND lower(trim(message)) NOT LIKE 'test%';"
)

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_5034TdZFF1lP9Yefup6AMEGp': 'file_storage/call_5034TdZFF1lP9Yefup6AMEGp.json', 'var_call_mVIQBwn6iioDm315rXANpozH': [{'cnt': '0'}]}

exec(code, env_args)
